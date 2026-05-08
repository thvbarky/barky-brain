#!/usr/bin/env python3
"""
Pousse le SEO + Open Graph sur la landing Barky Daily (page Shopify uniquement,
ne touche PAS à la fiche produit) :
  1. Met à jour le template Liquid avec OG/Twitter Cards + image personnalisée
  2. Met à jour la page (seo.title, seo.description, title admin propre)
  3. Vérifie le rendu via curl avec cache-bust
"""
from __future__ import annotations
import json, re, time, urllib.request
from pathlib import Path

REPO = Path("/Users/thv12/Documents/github/barky-brain")

# ─── Charge .env.local ──────────────────────────────────────────────────────
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

THEME_ID = "gid://shopify/OnlineStoreTheme/201764340061"  # Shrine Pro 1.3.3.1
PAGE_ID  = "gid://shopify/Page/713609544029"              # Barky Daily landing
OG_IMAGE = "https://cdn.shopify.com/s/files/1/1068/0146/3645/files/unboxing-box-pot-balle-tagline.png?v=1777296388"

# ─── Copy SEO validé (option A/A) ───────────────────────────────────────────
ADMIN_TITLE   = "Barky Daily — Le multivitaminé quotidien du chien"
SEO_TITLE     = "Barky Daily — Multivitaminé quotidien chien, formulé par 4 vétos"
SEO_DESCR     = "Sept flacons de compléments dans le placard ? Barky Daily les remplace par une seule bouchée. Formulé par 4 vétérinaires français. 28€/mois, garantie 60 jours."

def gql(q: str, v: dict) -> dict:
    req = urllib.request.Request(
        GRAPHQL, method="POST", headers=HEADERS,
        data=json.dumps({"query": q, "variables": v}).encode()
    )
    with urllib.request.urlopen(req) as r:
        return json.load(r)

# ─── Étape 1 : Récupérer le @font-face block existant pour le re-injecter ──
print("→ Lecture du @font-face Recoleta depuis la source…")
src = (REPO / "06-store/landing-pages/multivitamin-v2-shopify.html").read_text()
font_block_match = re.search(
    r'<style>(\s*/\*[^*]*RECOLETA[^*]*\*/.*?)</style>', src, re.DOTALL
)
if not font_block_match:
    # Fallback : trouver le 1er <style> contenant @font-face
    for m in re.finditer(r'<style[^>]*>(.*?)</style>', src, re.DOTALL):
        if "@font-face" in m.group(1):
            font_face_css = m.group(1).strip()
            break
    else:
        raise SystemExit("❌ @font-face block introuvable dans la source")
else:
    font_face_css = font_block_match.group(1).strip()
print(f"  ✓ {font_face_css.count('@font-face')} @font-face declarations extraites")

# ─── Étape 2 : Construire le nouveau template Liquid avec OG/Twitter ───────
print("\n→ Mise à jour du template page.barky-landing.liquid…")
TEMPLATE = """{% layout none %}<!doctype html>
<html lang="{{ request.locale.iso_code | default: 'fr' }}" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="theme-color" content="#FAFAF7">
  <link rel="canonical" href="{{ canonical_url }}">

  {%- assign seo_title = page.metafields.global.title_tag | default: page.title -%}
  {%- assign seo_descr = page.metafields.global.description_tag | default: page.content | strip_html | truncate: 160 -%}
  {%- assign og_image  = '""" + OG_IMAGE + """' -%}

  <title>{{ seo_title }}</title>
  <meta name="description" content="{{ seo_descr | escape }}">

  {{ content_for_header }}

  <!-- Open Graph (override Shopify defaults — image + locale + site_name) -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{{ seo_title | escape }}">
  <meta property="og:description" content="{{ seo_descr | escape }}">
  <meta property="og:url" content="{{ canonical_url }}">
  <meta property="og:image" content="{{ og_image }}">
  <meta property="og:image:alt" content="L'unboxing Barky Daily : pot brun, balle bleue brandée, message Santé Canine au Plus Haut Standard">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:site_name" content="Barky">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{{ seo_title | escape }}">
  <meta name="twitter:description" content="{{ seo_descr | escape }}">
  <meta name="twitter:image" content="{{ og_image }}">
  <meta name="twitter:image:alt" content="L'unboxing Barky Daily">

  <!-- Recoleta self-hosted from Shopify Files -->
  <style>
""" + font_face_css + """
  </style>
</head>
<body class="page-barky-landing">
{{ page.content }}
</body>
</html>
"""

mut_theme = """
mutation themeFilesUpsert($files: [OnlineStoreThemeFilesUpsertFileInput!]!, $themeId: ID!) {
  themeFilesUpsert(files: $files, themeId: $themeId) {
    upsertedThemeFiles { filename }
    userErrors { field code message }
  }
}
"""
res = gql(mut_theme, {
    "themeId": THEME_ID,
    "files": [{
        "filename": "templates/page.barky-landing.liquid",
        "body": {"type": "TEXT", "value": TEMPLATE}
    }]
})
errs = res.get("data", {}).get("themeFilesUpsert", {}).get("userErrors", [])
if errs:
    print(json.dumps(res, indent=2, ensure_ascii=False))
    raise SystemExit(f"❌ themeFilesUpsert errors: {errs}")
print("  ✓ Template mis à jour")

# ─── Étape 3 : Mettre à jour la page avec SEO ──────────────────────────────
print("\n→ Mise à jour de la page (admin title + seo.title + seo.description)…")
mut_page = """
mutation pageUpdate($id: ID!, $page: PageUpdateInput!) {
  pageUpdate(id: $id, page: $page) {
    page {
      id title handle templateSuffix isPublished
      title_tag: metafield(namespace: "global", key: "title_tag") { value }
      description_tag: metafield(namespace: "global", key: "description_tag") { value }
    }
    userErrors { field code message }
  }
}
"""
res = gql(mut_page, {
    "id": PAGE_ID,
    "page": {
        "title": ADMIN_TITLE,
        "metafields": [
            {"namespace": "global", "key": "title_tag",
             "value": SEO_TITLE, "type": "single_line_text_field"},
            {"namespace": "global", "key": "description_tag",
             "value": SEO_DESCR, "type": "multi_line_text_field"},
        ],
    }
})
errs = res.get("data", {}).get("pageUpdate", {}).get("userErrors", [])
if errs or res.get("errors"):
    print(json.dumps(res, indent=2, ensure_ascii=False))
    raise SystemExit(f"❌ pageUpdate errors: {errs or res.get('errors')}")
page = res["data"]["pageUpdate"]["page"]
print(f"  ✓ Admin title  : {page['title']}")
print(f"  ✓ title_tag    : {(page.get('title_tag') or {}).get('value')}")
descr = (page.get('description_tag') or {}).get('value', '')
print(f"  ✓ descr_tag    : {descr[:80]}…" if descr else "  ✓ descr_tag    : (vide?)")

# ─── Étape 4 : Verif ───────────────────────────────────────────────────────
print("\n→ Attente 5s puis vérif via curl…")
time.sleep(5)
url = f"https://{PUBLIC_DOMAIN}/pages/{page['handle']}?bust={int(time.time())}"
req = urllib.request.Request(url, headers={"Cache-Control": "no-cache"})
html = urllib.request.urlopen(req).read().decode()

checks = {
    "<title> contient SEO_TITLE": SEO_TITLE in html,
    "<meta description> contient hook 'Sept flacons'": "Sept flacons" in html,
    "og:image personnalisé (unboxing)": OG_IMAGE in html,
    "og:locale fr_FR": "og:locale" in html and "fr_FR" in html,
    "twitter:card summary_large_image": "summary_large_image" in html,
    "@font-face Recoleta servies": html.count("@font-face") >= 6,
    "CTAs vers cf-01 produit": html.count("/products/cf-01") >= 4,
}
print()
for label, ok in checks.items():
    icon = "✓" if ok else "✗"
    print(f"  {icon} {label}")
ok_count = sum(checks.values())
total = len(checks)
print(f"\n  {ok_count}/{total} checks OK")

if ok_count == total:
    print(f"\n🎉 SEO + OG + Twitter déployés. URL : https://{PUBLIC_DOMAIN}/pages/{page['handle']}")
else:
    print(f"\n⚠️  Quelques checks manqués — peut-être effet cache CDN, retest dans 30s.")
