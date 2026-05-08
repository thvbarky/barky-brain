#!/usr/bin/env python3
"""
Génère la version Shopify-ready de multivitamin-v2.html (chemins → URLs CDN)
puis crée la page sur Shopify avec le template page.barky-landing.

Ne supprime rien, n'écrase rien. Crée juste une nouvelle page.
"""
from __future__ import annotations
import json, re, sys, urllib.request
from pathlib import Path

REPO = Path("/Users/thv12/Documents/github/barky-brain")
LANDING = REPO / "06-store/landing-pages/multivitamin-v2.html"
ASSET_MAP = REPO / "06-store/landing-pages/_shopify-asset-map.json"
SHOPIFY_READY = REPO / "06-store/landing-pages/multivitamin-v2-shopify.html"

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
PUBLIC_DOMAIN = env["SHOPIFY_PUBLIC_DOMAIN"]
GRAPHQL = f"https://{SHOP}/admin/api/{API}/graphql.json"
HEADERS = {"Content-Type": "application/json", "X-Shopify-Access-Token": TOKEN}

def gql(query: str, variables: dict) -> dict:
    req = urllib.request.Request(
        GRAPHQL, method="POST", headers=HEADERS,
        data=json.dumps({"query": query, "variables": variables}).encode()
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)

# ─── Étape 1 — Substitue les chemins locaux par les URLs CDN ────────────────
print("→ Substitution des chemins locaux vers URLs CDN…")
html = LANDING.read_text()
asset_map = json.loads(ASSET_MAP.read_text())

substitutions = 0
for entry in asset_map:
    if not entry.get("url"):
        continue
    relative = "../../" + entry["local"]
    relative_encoded = relative.replace(" ", "%20")
    cdn_url = entry["url"]
    # Replace both URL-encoded and raw variants
    for pattern in (relative_encoded, relative):
        if pattern in html:
            html = html.replace(pattern, cdn_url)
            substitutions += 1

print(f"  {substitutions} substitution(s) faites")

# Sauve la version Shopify-ready en local pour audit
SHOPIFY_READY.write_text(html)
print(f"  Sauvegardé : {SHOPIFY_READY.relative_to(REPO)}")

# ─── Étape 2 — Extrait le fragment entre BARKY_LANDING_START / END ──────────
print("\n→ Extraction du fragment entre BARKY_LANDING_START / END…")
match = re.search(
    r"<!-- BARKY_LANDING_START -->(.*?)<!-- BARKY_LANDING_END -->",
    html, re.DOTALL
)
if not match:
    sys.exit("❌ Markers BARKY_LANDING_START/END introuvables")
fragment = match.group(1).strip()
print(f"  Fragment de {len(fragment):,} chars extrait")

# Sanity check : aucun chemin local relatif ne doit survivre dans le fragment
remaining = re.findall(r"\.\./\.\./01-identite/[^\"')\s]+", fragment)
if remaining:
    print(f"  ⚠️  Chemins locaux résiduels (non substitués) :")
    for r in remaining[:10]:
        print(f"      {r}")
    sys.exit("❌ Substitution incomplète — abort.")
print("  ✓ Aucun chemin local résiduel — substitution complète")

# ─── Étape 3 — Crée la page sur Shopify ─────────────────────────────────────
print("\n→ Création de la page Shopify…")

PAGE_TITLE = "Barky Daily — Test landing v2 (preview)"
PAGE_HANDLE = "barky-daily-journal"

# Vérifie si une page avec ce handle existe déjà (au cas où on relance le script)
check = gql(
    'query($q: String!) { pages(first: 1, query: $q) { edges { node { id title handle } } } }',
    {"q": f"handle:{PAGE_HANDLE}"}
)
edges = check.get("data", {}).get("pages", {}).get("edges", [])
existing = edges[0]["node"] if edges else None
if existing:
    print(f"  ⚠️  Page existante détectée : {existing['title']}")
    print(f"      → mise à jour via pageUpdate au lieu de pageCreate")
    mut = """
    mutation pageUpdate($id: ID!, $page: PageUpdateInput!) {
      pageUpdate(id: $id, page: $page) {
        page { id title handle templateSuffix isPublished }
        userErrors { field code message }
      }
    }
    """
    variables = {
        "id": existing["id"],
        "page": {
            "title": PAGE_TITLE,
            "body": fragment,
            "templateSuffix": "barky-landing",
            "isPublished": True,
        }
    }
    op_name = "pageUpdate"
else:
    mut = """
    mutation pageCreate($page: PageCreateInput!) {
      pageCreate(page: $page) {
        page { id title handle templateSuffix isPublished }
        userErrors { field code message }
      }
    }
    """
    variables = {
        "page": {
            "title": PAGE_TITLE,
            "handle": PAGE_HANDLE,
            "body": fragment,
            "templateSuffix": "barky-landing",
            "isPublished": True,
        }
    }
    op_name = "pageCreate"

res = gql(mut, variables)
if res.get("errors"):
    print(json.dumps(res, indent=2))
    sys.exit("❌ Erreur GraphQL")

payload = res["data"][op_name]
errs = payload.get("userErrors", [])
if errs:
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    sys.exit(f"❌ userErrors : {errs}")

page = payload["page"]
print(f"  ✓ {op_name} OK")
print(f"     id           : {page['id']}")
print(f"     title        : {page['title']}")
print(f"     handle       : {page['handle']}")
print(f"     template     : {page['templateSuffix']}")
print(f"     published    : {page['isPublished']}")
# ─── URL publique pour preview ──────────────────────────────────────────────
public_url = f"https://{PUBLIC_DOMAIN}/pages/{page['handle']}"
print(f"\n🌐 URL publique : {public_url}")
