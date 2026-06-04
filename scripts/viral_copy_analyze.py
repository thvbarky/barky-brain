#!/usr/bin/env python3
"""
viral_copy_analyze.py — Phase 1 step 3.4 du skill /viral-copy

Upload une vidéo MP4 à Gemini Files API, attend l'état ACTIVE, génère un
rapport d'analyse 5 sections en français, écrit dans {output_dir}/report.md.

Usage:
    python3 scripts/viral_copy_analyze.py <video_path> <output_dir>

Output stdout (JSON):
    {"status": "ok", "report_path": "...", "model_used": "...", "char_count": N}

Env requis (depuis .env.local à la racine du repo):
    GEMINI_API_KEY=...

Modèles essayés dans l'ordre:
    1. gemini-2.5-pro   (stable, default)
    2. gemini-2.5-flash (fallback moins riche mais ~5× moins cher)

Note: gemini-3.1-pro-preview pourra être ajouté en tête de liste quand dispo.
"""

import json
import os
import sys
import time
from pathlib import Path

try:
    from dotenv import load_dotenv
    from google import genai
except ImportError as e:
    print(f"ERROR: dépendance manquante ({e}). Installe avec:", file=sys.stderr)
    print("  pip3 install --user google-genai python-dotenv", file=sys.stderr)
    sys.exit(1)


MODELS_TO_TRY = ["gemini-2.5-pro", "gemini-2.5-flash"]
UPLOAD_TIMEOUT_S = 120
POLL_INTERVAL_S = 5

PROMPT = """Tu es un expert en analyse de vidéos publicitaires TikTok virales. Analyse la vidéo fournie et produis un rapport structuré en français, organisé en 5 sections strictes :

**1. Structure narrative** — Liste chaque plan avec timestamp début-fin (mm:ss) + description du contenu visuel + ce qui est dit (transcription voix off ou dialogue) + texte overlay s'il y en a.

**2. Esthétique** — Style visuel (3D Pixar / live action / mixed media / motion design), palette dominante (noms de couleurs précis), grain/qualité d'image, typographie des overlays (couleurs, taille, animation), composition et cadrage.

**3. Sound design** — Voix off (genre, âge approximatif, ton, débit, accent), musique (style, intensité, moments clés), SFX (whoosh, impacts, transitions), silences éventuels et leur fonction dramatique.

**4. Structure dramatique** — Hook (premiers 0-2s : qu'est-ce qui retient le scroll ?), arc narratif (problème → péripétie → résolution), payoff (les 2-3 dernières secondes : punchline ? CTA ? cliffhanger ?), point de bascule émotionnel.

**5. Pattern reproductible** — La FORMULE virale en 1-2 phrases (ex: "POV + personnification du problème + résolution produit"), pourquoi ça marche (levier psychologique), quels éléments sont transférables à une autre marque, quels éléments sont spécifiques à cette marque (à ne pas copier tels quels).

Sois précis, factuel, exhaustif. Pas de bullshit marketing. Pas d'éloges gratuits. Format Markdown propre avec des titres `##` pour chaque section."""


def log(msg: str) -> None:
    """Print to stderr (stdout is reserved for the final JSON status)."""
    print(msg, file=sys.stderr, flush=True)


def main() -> int:
    if len(sys.argv) != 3:
        log("Usage: viral_copy_analyze.py <video_path> <output_dir>")
        return 2

    video_path = Path(sys.argv[1]).resolve()
    output_dir = Path(sys.argv[2]).resolve()

    if not video_path.exists():
        log(f"ERROR: video file not found: {video_path}")
        return 1

    if video_path.stat().st_size < 100_000:
        log(f"ERROR: video file suspiciously small ({video_path.stat().st_size} bytes) — likely a download failure")
        return 1

    # Load env from repo root .env.local
    repo_root = Path(__file__).resolve().parent.parent
    env_file = repo_root / ".env.local"
    if env_file.exists():
        load_dotenv(env_file)
    else:
        log(f"WARN: {env_file} not found, relying on shell env")

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        log("ERROR: GEMINI_API_KEY not set (check .env.local)")
        return 1

    client = genai.Client(api_key=api_key)

    # 1. Upload video to Files API
    log(f"Uploading {video_path.name} ({video_path.stat().st_size / 1e6:.1f} MB) to Gemini Files API…")
    try:
        uploaded = client.files.upload(file=str(video_path))
    except Exception as e:
        log(f"ERROR: upload failed: {e}")
        return 1

    log(f"Uploaded as {uploaded.name}, polling until ACTIVE…")

    # 2. Wait for ACTIVE state
    deadline = time.time() + UPLOAD_TIMEOUT_S
    while True:
        try:
            current = client.files.get(name=uploaded.name)
        except Exception as e:
            log(f"WARN: poll error: {e}, retrying…")
            time.sleep(POLL_INTERVAL_S)
            continue

        state_name = current.state.name if hasattr(current.state, "name") else str(current.state)
        if state_name == "ACTIVE":
            log(f"File ACTIVE: {current.name}")
            uploaded = current
            break
        if state_name == "FAILED":
            log("ERROR: Gemini Files API state FAILED")
            return 1
        if time.time() > deadline:
            log(f"ERROR: timeout after {UPLOAD_TIMEOUT_S}s, file still {state_name}")
            return 1
        time.sleep(POLL_INTERVAL_S)

    # 3. Generate content — try models in order
    response = None
    model_used = None
    last_error = None
    for model in MODELS_TO_TRY:
        log(f"Calling generateContent with model {model}…")
        try:
            response = client.models.generate_content(
                model=model,
                contents=[uploaded, PROMPT],
            )
            model_used = model
            break
        except Exception as e:
            log(f"WARN: {model} failed: {e}")
            last_error = e
            continue

    if response is None:
        log(f"ERROR: all models failed, last error: {last_error}")
        # Cleanup before exiting
        try:
            client.files.delete(name=uploaded.name)
        except Exception:
            pass
        return 1

    # 4. Write report
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "report.md"
    report_text = response.text or ""
    report_path.write_text(report_text, encoding="utf-8")

    # 5. Cleanup uploaded file (Gemini free tier file storage is limited)
    try:
        client.files.delete(name=uploaded.name)
        log(f"Cleaned up uploaded file: {uploaded.name}")
    except Exception as e:
        log(f"WARN: cleanup failed (non-fatal): {e}")

    # 6. Print JSON status to stdout
    summary = {
        "status": "ok",
        "report_path": str(report_path),
        "model_used": model_used,
        "char_count": len(report_text),
    }
    log(f"OK — report.md written ({len(report_text)} chars) using {model_used}")
    print(json.dumps(summary))
    return 0


if __name__ == "__main__":
    sys.exit(main())
