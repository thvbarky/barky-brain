"""
Composition V3 — SET 1 Lifestyle P1 "C'est l'âge"
Source : v3-lifestyle-p1-cest-lage-nanobanana-1856x2304.png
Sortie : final/final-v3-lifestyle-p1-cest-lage-1080x1350.png

V2 (corrigée) :
- sub-headline opacité 100% pour lisibilité
- flèche CTA dessinée en primitives (Recoleta sans glyph →)
- logo SVG Barky composé en bas (rendu via cairosvg si dispo, sinon fallback texte)
"""
from PIL import Image, ImageDraw, ImageFont
import os

# ─────────── CONSTANTES BARKY ───────────
TARGET_W, TARGET_H = 1080, 1350
HEX_AMBER = (70, 52, 50)         # #463432
HEX_CREAM = (245, 240, 235)      # #F5F0EB
HEX_BLUE = (202, 220, 228)       # #CADCE4

# ─────────── CHEMINS ───────────
BASE_DIR = "/Users/thv12/Documents/github/barky-brain"
SRC = f"{BASE_DIR}/08-ads/statics/2026-05-05/v3-lifestyle-p1-cest-lage-nanobanana-1856x2304.png"
DST = f"{BASE_DIR}/08-ads/statics/2026-05-05/final/final-v3-lifestyle-p1-cest-lage-1080x1350.png"
RECOLETA = f"{BASE_DIR}/01-identite/assets/Recoleta"
LOGO_SVG = f"{BASE_DIR}/01-identite/assets/logo/Barky marron sans fond.svg"

# ─────────── 1. LOAD + CROP/RESIZE 4:5 ───────────
img = Image.open(SRC).convert("RGB")
sw, sh = img.size
print(f"Source: {sw}x{sh}, ratio {sw/sh:.4f}")

scale = TARGET_H / sh
new_w = int(round(sw * scale))
img_resized = img.resize((new_w, TARGET_H), Image.Resampling.LANCZOS)

left = (new_w - TARGET_W) // 2
img_4_5 = img_resized.crop((left, 0, left + TARGET_W, TARGET_H))
print(f"Cropped: {img_4_5.size}")

# ─────────── 2. OVERLAY GRADIENT TOP + BANDEAU CREAM BOTTOM ───────────
overlay = Image.new("RGBA", (TARGET_W, TARGET_H), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# gradient plus profond pour lisibilité sub-headline (520px, alpha max 200)
for y in range(520):
    alpha = int(200 * (1 - y / 520) ** 1.4)
    draw.rectangle([(0, y), (TARGET_W, y + 1)], fill=(0, 0, 0, alpha))

# bandeau cream bottom 320px
BAND_H = 320
band_y = TARGET_H - BAND_H
draw.rectangle(
    [(0, band_y), (TARGET_W, TARGET_H)],
    fill=(*HEX_CREAM, 255)
)

img_4_5_rgba = img_4_5.convert("RGBA")
composed = Image.alpha_composite(img_4_5_rgba, overlay)
draw = ImageDraw.Draw(composed)

# ─────────── 3. TYPO ───────────
font_headline = ImageFont.truetype(f"{RECOLETA}/Recoleta Bold.otf", 96)
font_sub      = ImageFont.truetype(f"{RECOLETA}/Recoleta Light.otf", 36)
font_body     = ImageFont.truetype(f"{RECOLETA}/Recoleta Medium.otf", 28)
font_cta      = ImageFont.truetype(f"{RECOLETA}/Recoleta SemiBold.otf", 30)
font_logo     = ImageFont.truetype(f"{RECOLETA}/Recoleta Bold.otf", 44)
font_baseline = ImageFont.truetype(f"{RECOLETA}/Recoleta Light.otf", 18)

def center_text(text, font, y, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text(((TARGET_W - w) // 2, y), text, font=font, fill=fill)
    return bbox[3] - bbox[1]

# HEADLINE : « C'est l'âge. »
center_text("« C'est l'âge. »", font_headline, 110, HEX_CREAM)

# SUB-HEADLINE — opacité 100%
center_text("— ce que tu te dis depuis 6 mois.", font_sub, 240, HEX_CREAM)

# BODY (2 lignes) dans le bandeau cream
center_text("Et si ce n'était pas le déclin —", font_body, band_y + 38, HEX_AMBER)
center_text("mais une carence ?", font_body, band_y + 78, HEX_AMBER)

# Séparateur ornement
sep_y = band_y + 140
draw.line(
    [(TARGET_W // 2 - 24, sep_y), (TARGET_W // 2 + 24, sep_y)],
    fill=HEX_AMBER,
    width=2
)

# ─────────── 4. CTA BUTTON avec flèche dessinée ───────────
cta_text = "Découvrir Barky"
cta_bbox = draw.textbbox((0, 0), cta_text, font=font_cta)
cta_w = cta_bbox[2] - cta_bbox[0]
cta_h = cta_bbox[3] - cta_bbox[1]

# Bouton dimensions
btn_pad_x = 36
btn_pad_y = 16
arrow_space = 30  # espace pour la flèche dessinée
btn_w = cta_w + 2 * btn_pad_x + arrow_space
btn_h = cta_h + 2 * btn_pad_y + 10
btn_x = (TARGET_W - btn_w) // 2
btn_y = sep_y + 28

# bouton arrondi brun
draw.rounded_rectangle(
    [(btn_x, btn_y), (btn_x + btn_w, btn_y + btn_h)],
    radius=6,
    fill=HEX_AMBER
)

# texte CTA cream
text_x = btn_x + btn_pad_x
text_y = btn_y + btn_pad_y
draw.text((text_x, text_y), cta_text, font=font_cta, fill=HEX_CREAM)

# flèche dessinée (chevron + ligne)
arrow_x = text_x + cta_w + 12
arrow_y_center = btn_y + btn_h // 2
draw.line([(arrow_x, arrow_y_center), (arrow_x + 18, arrow_y_center)], fill=HEX_CREAM, width=2)
draw.line([(arrow_x + 12, arrow_y_center - 6), (arrow_x + 18, arrow_y_center)], fill=HEX_CREAM, width=2)
draw.line([(arrow_x + 12, arrow_y_center + 6), (arrow_x + 18, arrow_y_center)], fill=HEX_CREAM, width=2)

# ─────────── 5. LOGO BARKY (depuis SVG si possible) ───────────
logo_y = TARGET_H - 70
logo_rendered = False
try:
    import cairosvg
    import io
    png_bytes = cairosvg.svg2png(url=LOGO_SVG, output_width=180)
    logo_img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
    lw, lh = logo_img.size
    composed.paste(logo_img, ((TARGET_W - lw) // 2, logo_y - lh + 10), logo_img)
    print(f"✅ Logo SVG composé ({lw}×{lh})")
    logo_rendered = True
except (ImportError, OSError) as e:
    print(f"⚠️ SVG indispo ({type(e).__name__}) — fallback texte 'Barky' Recoleta Bold")

if not logo_rendered:
    bbox = draw.textbbox((0, 0), "Barky", font=font_logo)
    w = bbox[2] - bbox[0]
    draw.text(((TARGET_W - w) // 2, logo_y - 8), "Barky", font=font_logo, fill=HEX_AMBER)

# Tagline / baseline sous logo
tagline = "Nourri comme il le mérite."
tag_bbox = draw.textbbox((0, 0), tagline, font=font_baseline)
tag_w = tag_bbox[2] - tag_bbox[0]
draw.text(((TARGET_W - tag_w) // 2, TARGET_H - 26), tagline, font=font_baseline, fill=HEX_AMBER)

# ─────────── 6. EXPORT ───────────
final = composed.convert("RGB")
final.save(DST, "PNG", optimize=True)
print(f"✅ Sauvegardé : {DST}")
print(f"Taille : {os.path.getsize(DST) / 1024:.0f} KB")
