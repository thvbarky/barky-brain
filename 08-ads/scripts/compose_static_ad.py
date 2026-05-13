#!/usr/bin/env python3
"""
Compose une statique Meta-ready Barky à partir d'un visuel Higgsfield généré.

Workflow :
1. Charge l'image source (visuel généré avec packshot Barky centré + zones top/bottom vides)
2. Resize/crop en 1080×1080
3. Ajoute le hook FR en haut (Recoleta Black 2 lignes, avec un mot encadré "VRAIMENT" pour emphasis — clone Exode problem-solution-01)
4. Ajoute 3 colonnes bénéfices en bas (icône cercle simple + label Recoleta SemiBold uppercase)
5. Sauvegarde le PNG final

Usage :
    python3 compose_static_ad.py --input <visual.png> --output <final.png>
"""

import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path(__file__).resolve().parents[2]
FONTS_DIR = REPO_ROOT / "01-identite" / "assets" / "Recoleta"

# Palette Barky stricte
BLEU_PASTEL = (202, 220, 228)        # #CADCE4
BRUN_AMBRE = (70, 52, 50)            # #463432
CREAM = (245, 240, 235)              # #F5F0EB
NOIR_PROFOND = (26, 20, 18)          # #1A1412

OUT_SIZE = 1080


def load_font(weight: str, size: int) -> ImageFont.FreeTypeFont:
    mapping = {
        "black": "Recoleta Alt Black.otf",
        "bold": "Recoleta Bold.otf",
        "semibold": "Recoleta SemiBold.otf",
        "regular": "Recoleta Regular.otf",
        "light": "Recoleta Light.otf",
    }
    path = FONTS_DIR / mapping[weight]
    return ImageFont.truetype(str(path), size)


def fit_to_square(img: Image.Image, size: int) -> Image.Image:
    """Resize + crop center pour sortir un carré size×size."""
    w, h = img.size
    short = min(w, h)
    left = (w - short) // 2
    top = (h - short) // 2
    img = img.crop((left, top, left + short, top + short))
    return img.resize((size, size), Image.LANCZOS)


def draw_text_centered(draw: ImageDraw.ImageDraw, text: str, y: int, font: ImageFont.FreeTypeFont, fill, canvas_w: int):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (canvas_w - tw) // 2 - bbox[0]
    draw.text((x, y - bbox[1]), text, font=font, fill=fill)
    return tw


def draw_word_with_box(draw: ImageDraw.ImageDraw, words_before: str, boxed_word: str, words_after: str,
                       y: int, font: ImageFont.FreeTypeFont, canvas_w: int,
                       text_color, box_fill_color, box_text_color):
    """Dessine 'words_before [boxed_word] words_after' sur une ligne centrée, avec le mot encadré (clone Exode 'NATUREL')."""
    pad_x = 16
    pad_y = 8

    parts = [(words_before, text_color), (boxed_word, box_text_color), (words_after, text_color)]
    widths = []
    for txt, _ in parts:
        bbox = draw.textbbox((0, 0), txt, font=font)
        widths.append((bbox[2] - bbox[0], bbox[1], bbox[3]))

    total_w = widths[0][0] + (widths[1][0] + 2 * pad_x) + widths[2][0]
    x = (canvas_w - total_w) // 2

    # words_before
    if words_before:
        draw.text((x, y - widths[0][1]), words_before, font=font, fill=text_color)
        x += widths[0][0]

    # boxed_word : fond
    box_top = y - pad_y
    box_bottom = y + (widths[1][2] - widths[1][1]) + pad_y
    box_left = x
    box_right = x + widths[1][0] + 2 * pad_x
    draw.rounded_rectangle([box_left, box_top, box_right, box_bottom], radius=6, fill=box_fill_color)
    draw.text((x + pad_x, y - widths[1][1]), boxed_word, font=font, fill=box_text_color)
    x = box_right

    # words_after
    if words_after:
        draw.text((x, y - widths[2][1]), words_after, font=font, fill=text_color)


def draw_benefit_column(draw: ImageDraw.ImageDraw, center_x: int, top_y: int,
                        circle_label: str, line1: str, line2: str,
                        label_font: ImageFont.FreeTypeFont, line_font: ImageFont.FreeTypeFont,
                        accent: tuple, text_color: tuple):
    # Cercle outline
    radius = 36
    cx, cy = center_x, top_y + radius
    draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], outline=accent, width=4)
    # Symbole au centre du cercle
    bbox = draw.textbbox((0, 0), circle_label, font=label_font)
    sw = bbox[2] - bbox[0]
    sh = bbox[3] - bbox[1]
    draw.text((cx - sw // 2 - bbox[0], cy - sh // 2 - bbox[1]), circle_label, font=label_font, fill=accent)
    # Lignes texte sous le cercle
    y = cy + radius + 18
    for line in [line1, line2]:
        bbox = draw.textbbox((0, 0), line, font=line_font)
        tw = bbox[2] - bbox[0]
        draw.text((cx - tw // 2 - bbox[0], y - bbox[1]), line, font=line_font, fill=text_color)
        y += (bbox[3] - bbox[1]) + 4


def compose(input_path: Path, output_path: Path,
            headline_line1: str,
            headline_box_before: str, headline_box_word: str, headline_box_after: str,
            benefits: list[tuple[str, str, str]]):
    base = Image.open(input_path).convert("RGB")
    base = fit_to_square(base, OUT_SIZE)
    canvas = base.copy()
    draw = ImageDraw.Draw(canvas, "RGBA")

    # --- TOP : voile cream semi-transparent pour faire ressortir la typo ---
    top_h = int(OUT_SIZE * 0.28)
    overlay_top = Image.new("RGBA", (OUT_SIZE, top_h), CREAM + (210,))
    canvas.paste(overlay_top, (0, 0), overlay_top)
    draw = ImageDraw.Draw(canvas, "RGBA")

    # --- HEADLINE ligne 1 : "Un complément qui marche" (sans box) ---
    headline_font = load_font("black", 56)
    line1_y = 56
    draw_text_centered(draw, headline_line1, line1_y, headline_font, BRUN_AMBRE, OUT_SIZE)

    # --- HEADLINE ligne 2 : "[VRAIMENT], ça existe ?" (avec box autour de VRAIMENT) ---
    line2_y = line1_y + 80
    draw_word_with_box(
        draw,
        headline_box_before, headline_box_word, headline_box_after,
        y=line2_y, font=headline_font, canvas_w=OUT_SIZE,
        text_color=BRUN_AMBRE, box_fill_color=BRUN_AMBRE, box_text_color=CREAM,
    )

    # --- BOTTOM : voile cream semi-transparent pour les 3 bénéfices ---
    bottom_h = int(OUT_SIZE * 0.26)
    overlay_bottom = Image.new("RGBA", (OUT_SIZE, bottom_h), CREAM + (210,))
    canvas.paste(overlay_bottom, (0, OUT_SIZE - bottom_h), overlay_bottom)
    draw = ImageDraw.Draw(canvas, "RGBA")

    # --- 3 BÉNÉFICES (cercles + labels) ---
    label_font = load_font("black", 30)        # symbole dans le cercle
    line_font = load_font("semibold", 22)      # labels sous le cercle
    column_centers = [OUT_SIZE // 6, OUT_SIZE // 2, OUT_SIZE - OUT_SIZE // 6]
    column_top = OUT_SIZE - bottom_h + 28
    for cx, (symbol, l1, l2) in zip(column_centers, benefits):
        draw_benefit_column(
            draw, cx, column_top,
            circle_label=symbol, line1=l1, line2=l2,
            label_font=label_font, line_font=line_font,
            accent=BRUN_AMBRE, text_color=BRUN_AMBRE,
        )

    canvas.save(output_path, "PNG", optimize=True)
    print(f"OK → {output_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    # Brief P1 angle "C'est l'âge" cloné sur Exode problem-solution-01
    compose(
        input_path=args.input,
        output_path=args.output,
        headline_line1="Un complément qui marche",
        headline_box_before="",
        headline_box_word="VRAIMENT",
        headline_box_after=", ça existe ?",
        benefits=[
            ("FR", "MADE IN", "FRANCE"),
            ("4", "FORMULÉ PAR", "4 VÉTÉRINAIRES"),
            ("1", "1 BOUCHÉE", "PAR JOUR"),
        ],
    )


if __name__ == "__main__":
    main()
