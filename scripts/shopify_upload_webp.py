#!/usr/bin/env python3
"""
Upload les WebP générés (depuis les PNG converties) vers Shopify Files.
Idempotent : skip ce qui est déjà dans _shopify-asset-map.json.
"""
from __future__ import annotations
import json, mimetypes, time, urllib.request
from pathlib import Path

REPO = Path("/Users/thv12/Documents/github/barky-brain")
MAP_FILE = REPO / "06-store/landing-pages/_shopify-asset-map.json"

# ─── Charge .env.local ───────────────────────────────────────────────────────
env: dict[str, str] = {}
for line in (REPO / ".env.local").read_text().splitlines():
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1)
        env[k] = v.strip().strip('"')

SHOP = env["SHOPIFY_SHOP"]
TOKEN = env["SHOPIFY_ACCESS_TOKEN"]
API = env["SHOPIFY_API_VERSION"]
GRAPHQL = f"https://{SHOP}/admin/api/{API}/graphql.json"
HEADERS = {"Content-Type": "application/json", "X-Shopify-Access-Token": TOKEN}

# ─── Helpers GraphQL identiques au script principal ─────────────────────────
def gql(query: str, variables: dict) -> dict:
    req = urllib.request.Request(
        GRAPHQL, method="POST", headers=HEADERS,
        data=json.dumps({"query": query, "variables": variables}).encode()
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)

def staged_upload_target(local: Path) -> dict:
    mut = """
    mutation stagedUploadsCreate($input: [StagedUploadInput!]!) {
      stagedUploadsCreate(input: $input) {
        stagedTargets { url resourceUrl parameters { name value } }
        userErrors { field message }
      }
    }
    """
    variables = {"input": [{
        "filename": local.name,
        "mimeType": "image/webp",
        "httpMethod": "POST",
        "resource": "IMAGE",
        "fileSize": str(local.stat().st_size),
    }]}
    res = gql(mut, variables)
    errs = res.get("data", {}).get("stagedUploadsCreate", {}).get("userErrors", [])
    if errs or res.get("errors"):
        raise RuntimeError(f"stagedUploadsCreate failed for {local.name}: {errs or res.get('errors')}")
    return res["data"]["stagedUploadsCreate"]["stagedTargets"][0]

def post_to_s3(target: dict, local: Path) -> None:
    boundary = "----barky-upload-boundary-7c4f2"
    payload = bytearray()
    for p in target["parameters"]:
        payload += f"--{boundary}\r\n".encode()
        payload += f'Content-Disposition: form-data; name="{p["name"]}"\r\n\r\n'.encode()
        payload += p["value"].encode() + b"\r\n"
    payload += f"--{boundary}\r\n".encode()
    payload += f'Content-Disposition: form-data; name="file"; filename="{local.name}"\r\n'.encode()
    payload += b"Content-Type: image/webp\r\n\r\n"
    payload += local.read_bytes() + b"\r\n"
    payload += f"--{boundary}--\r\n".encode()

    req = urllib.request.Request(
        target["url"], method="POST",
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        data=bytes(payload)
    )
    with urllib.request.urlopen(req) as resp:
        if resp.status >= 300:
            raise RuntimeError(f"S3 upload {local.name} failed: HTTP {resp.status}")

def file_create(local: Path, resource_url: str) -> dict:
    mut = """
    mutation fileCreate($files: [FileCreateInput!]!) {
      fileCreate(files: $files) {
        files {
          id fileStatus alt
          ... on MediaImage { image { url } mimeType }
        }
        userErrors { field code message }
      }
    }
    """
    alt = local.stem.replace("-", " ").replace("_", " ").capitalize()
    variables = {"files": [{
        "alt": alt,
        "contentType": "IMAGE",
        "originalSource": resource_url,
    }]}
    res = gql(mut, variables)
    errs = res.get("data", {}).get("fileCreate", {}).get("userErrors", [])
    if errs or res.get("errors"):
        raise RuntimeError(f"fileCreate failed for {local.name}: {errs or res.get('errors')}")
    return res["data"]["fileCreate"]["files"][0]

def fetch_url(file_id: str, max_tries: int = 12) -> str | None:
    q = """
    query FileById($id: ID!) {
      node(id: $id) {
        ... on MediaImage { image { url } fileStatus }
      }
    }
    """
    url = None
    for i in range(max_tries):
        res = gql(q, {"id": file_id})
        node = res.get("data", {}).get("node") or {}
        status = node.get("fileStatus")
        url = (node.get("image") or {}).get("url") or url
        if url and status == "READY":
            return url
        time.sleep(0.7 * (i + 1))
    return url

def upload(local_path: str) -> dict:
    local = REPO / local_path
    if not local.exists():
        return {"local": local_path, "error": "FILE NOT FOUND"}
    print(f"  ↑ {local_path} ({local.stat().st_size//1024} KB) …", end=" ", flush=True)
    try:
        target = staged_upload_target(local)
        post_to_s3(target, local)
        file = file_create(local, target["resourceUrl"])
        url = fetch_url(file["id"])
        print(f"OK → {url}")
        return {"local": local_path, "id": file["id"], "url": url, "status": file.get("fileStatus")}
    except Exception as e:
        print(f"FAIL: {e}")
        return {"local": local_path, "error": str(e)}

# ─── Pipeline ────────────────────────────────────────────────────────────────
existing = json.loads(MAP_FILE.read_text()) if MAP_FILE.exists() else []
already_done = {entry["local"] for entry in existing if entry.get("url")}

webps = sorted(p for p in (REPO / "01-identite/assets/photos").rglob("*.webp"))
to_upload = [p.relative_to(REPO).as_posix() for p in webps if p.relative_to(REPO).as_posix() not in already_done]

if not to_upload:
    print("Tous les WebP sont déjà uploadés. Rien à faire.")
    raise SystemExit(0)

print(f"=== Upload de {len(to_upload)} WebP vers Shopify Files ===\n")
results = [upload(a) for a in to_upload]

# Append au mapping existant
merged = existing + results
MAP_FILE.write_text(json.dumps(merged, indent=2, ensure_ascii=False))

ok = sum(1 for r in results if r.get("url"))
fail = sum(1 for r in results if r.get("error"))
print(f"\n=== TERMINÉ : {ok} OK, {fail} échec(s) ===")
print(f"Mapping mis à jour : {MAP_FILE.relative_to(REPO)}")
