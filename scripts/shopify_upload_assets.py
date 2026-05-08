#!/usr/bin/env python3
"""
Upload tous les assets Barky (logos, fontes Recoleta, photos) sur Shopify Files.
Sauve un mapping local-path → URL CDN dans 06-store/landing-pages/_shopify-asset-map.json
"""
from __future__ import annotations
import json, mimetypes, os, sys, time, urllib.request
from pathlib import Path

REPO = Path("/Users/thv12/Documents/github/barky-brain")

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

# ─── Liste des assets ────────────────────────────────────────────────────────
ASSETS = [
    # Logos (SVG → IMAGE)
    "01-identite/assets/logo/Barky.svg",
    "01-identite/assets/logo/Barky marron sans fond.svg",
    "01-identite/assets/logo/Barky fond marron.svg",
    # Fontes Recoleta (woff2 → FILE)
    "01-identite/assets/Recoleta/Recoleta Light.woff2",
    "01-identite/assets/Recoleta/Recoleta Regular.woff2",
    "01-identite/assets/Recoleta/Recoleta Medium.woff2",
    "01-identite/assets/Recoleta/Recoleta SemiBold.woff2",
    "01-identite/assets/Recoleta/Recoleta Bold.woff2",
    "01-identite/assets/Recoleta/Recoleta Black.woff2",
    # Photos packshot (PNG → IMAGE)
    "01-identite/assets/photos/packshot/packshot-bouchees-3-nuages.png",
    "01-identite/assets/photos/packshot/packshot-bouchees-vue-dessus.png",
    "01-identite/assets/photos/packshot/packshot-pot-dos-ingredients.png",
    "01-identite/assets/photos/packshot/packshot-pot-ferme-bleu-pastel.png",
    "01-identite/assets/photos/packshot/packshot-pot-nuages.png",
    # Photos lifestyle (PNG → IMAGE)
    "01-identite/assets/photos/lifestyle/lifestyle-beagle-cuisine-bouchee.png",
    "01-identite/assets/photos/lifestyle/lifestyle-bichon-cuisine-dos.png",
    "01-identite/assets/photos/lifestyle/lifestyle-bouledogue-francais-tapis.png",
    "01-identite/assets/photos/lifestyle/lifestyle-cane-corso-foulard.png",
    "01-identite/assets/photos/lifestyle/lifestyle-corgi-gazon.png",
    "01-identite/assets/photos/lifestyle/lifestyle-couple-petit-chien.png",
    "01-identite/assets/photos/lifestyle/lifestyle-goldendoodle-herbe.png",
    "01-identite/assets/photos/lifestyle/lifestyle-jack-russell-canape.png",
    # Unboxing (PNG → IMAGE)
    "01-identite/assets/photos/unboxing/unboxing-box-pot-balle-tagline.png",
    # Editorial (PNG → IMAGE)
    "01-identite/assets/photos/editorial/editorial-composition-aliments-actifs.png",
]

# ─── Helpers ─────────────────────────────────────────────────────────────────
def gql(query: str, variables: dict) -> dict:
    req = urllib.request.Request(
        GRAPHQL, method="POST", headers=HEADERS,
        data=json.dumps({"query": query, "variables": variables}).encode()
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)

def mime_for(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".svg":   return "image/svg+xml"
    if suffix == ".woff2": return "font/woff2"
    if suffix == ".png":   return "image/png"
    if suffix in {".jpg", ".jpeg"}: return "image/jpeg"
    return mimetypes.guess_type(str(path))[0] or "application/octet-stream"

def is_image(path: Path) -> bool:
    return path.suffix.lower() in {".svg", ".png", ".jpg", ".jpeg", ".webp", ".gif"}

# ─── Étape 1 — stagedUploadsCreate ───────────────────────────────────────────
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
        "mimeType": mime_for(local),
        "httpMethod": "POST",
        "resource": "IMAGE" if is_image(local) else "FILE",
        "fileSize": str(local.stat().st_size),
    }]}
    res = gql(mut, variables)
    errs = res.get("data", {}).get("stagedUploadsCreate", {}).get("userErrors", [])
    if errs or res.get("errors"):
        raise RuntimeError(f"stagedUploadsCreate failed for {local.name}: {errs or res.get('errors')}")
    return res["data"]["stagedUploadsCreate"]["stagedTargets"][0]

# ─── Étape 2 — POST multipart vers S3 ────────────────────────────────────────
def post_to_s3(target: dict, local: Path) -> None:
    boundary = "----barky-upload-boundary-7c4f2"
    payload = bytearray()
    # Add S3 form params
    for p in target["parameters"]:
        payload += f"--{boundary}\r\n".encode()
        payload += f'Content-Disposition: form-data; name="{p["name"]}"\r\n\r\n'.encode()
        payload += p["value"].encode() + b"\r\n"
    # Add the file (must be LAST in S3 multipart)
    payload += f"--{boundary}\r\n".encode()
    payload += f'Content-Disposition: form-data; name="file"; filename="{local.name}"\r\n'.encode()
    payload += f"Content-Type: {mime_for(local)}\r\n\r\n".encode()
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

# ─── Étape 3 — fileCreate ────────────────────────────────────────────────────
def file_create(local: Path, resource_url: str) -> dict:
    mut = """
    mutation fileCreate($files: [FileCreateInput!]!) {
      fileCreate(files: $files) {
        files {
          id
          fileStatus
          alt
          ... on MediaImage { image { url } mimeType }
          ... on GenericFile { url mimeType }
        }
        userErrors { field code message }
      }
    }
    """
    alt = local.stem.replace("-", " ").replace("_", " ").capitalize()
    variables = {"files": [{
        "alt": alt,
        "contentType": "IMAGE" if is_image(local) else "FILE",
        "originalSource": resource_url,
    }]}
    res = gql(mut, variables)
    errs = res.get("data", {}).get("fileCreate", {}).get("userErrors", [])
    if errs or res.get("errors"):
        raise RuntimeError(f"fileCreate failed for {local.name}: {errs or res.get('errors')}")
    return res["data"]["fileCreate"]["files"][0]

# ─── Étape 4 — Re-query pour récupérer l'URL finale (asynchrone) ─────────────
def fetch_url(file_id: str, max_tries: int = 10) -> str | None:
    q = """
    query FileById($id: ID!) {
      node(id: $id) {
        ... on MediaImage { image { url } fileStatus }
        ... on GenericFile { url fileStatus }
      }
    }
    """
    for i in range(max_tries):
        res = gql(q, {"id": file_id})
        node = res.get("data", {}).get("node") or {}
        status = node.get("fileStatus")
        url = (node.get("image") or {}).get("url") or node.get("url")
        if url and status == "READY":
            return url
        time.sleep(0.6 * (i + 1))
    return url  # fallback même si pas READY

# ─── Pipeline ────────────────────────────────────────────────────────────────
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

print(f"=== Upload de {len(ASSETS)} assets vers Shopify Files ===\n")
results = [upload(a) for a in ASSETS]

# ─── Sauve le mapping ────────────────────────────────────────────────────────
out = REPO / "06-store/landing-pages/_shopify-asset-map.json"
out.write_text(json.dumps(results, indent=2, ensure_ascii=False))

ok = sum(1 for r in results if r.get("url"))
fail = sum(1 for r in results if r.get("error"))
print(f"\n=== TERMINÉ : {ok} OK, {fail} échec(s) ===")
print(f"Mapping sauvegardé dans : {out.relative_to(REPO)}")
