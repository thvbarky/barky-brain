#!/usr/bin/env python3
"""
Upload des 5 créas manuelles Barky du 14/05/2026 vers Shopify Files CDN.
Réutilise les helpers de shopify_upload_assets.py.
Sortie : JSON {filename: cdn_url} pour push dans Notion (champ Visual).
"""
from __future__ import annotations
import json, sys
from pathlib import Path

# Réutilise les helpers du script principal
sys.path.insert(0, str(Path(__file__).parent))
from shopify_upload_assets import upload, REPO

FILES = [
    "08-ads/meta/creatives/barky_p1_pas-vieux-il-manque_lifestyle_v1.png",
    "08-ads/meta/creatives/barky_p1_signes-mobilite_proof_v1.png",
    "08-ads/meta/creatives/barky_p2_liste-complete-actifs_producthero_v1.png",
    "08-ads/meta/creatives/barky_p1_cest-lage_lifestyle_v1.png",
    "08-ads/meta/creatives/barky_p1_signes-mobilite_producthero_v1.png",
]

print(f"=== Upload de {len(FILES)} créas manuelles vers Shopify Files ===\n")
results = [upload(f) for f in FILES]

out = REPO / "08-ads/meta/creatives/_shopify-cdn-map.json"
out.write_text(json.dumps(results, indent=2, ensure_ascii=False))

ok = sum(1 for r in results if r.get("url"))
fail = sum(1 for r in results if r.get("error"))
print(f"\n=== TERMINÉ : {ok} OK, {fail} échec(s) ===")
print(f"Mapping sauvegardé dans : {out.relative_to(REPO)}")
