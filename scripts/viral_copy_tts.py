#!/usr/bin/env python3
"""
viral_copy_tts.py — Phase 2 step 4.2c du skill /viral-copy-run

Lit les plans YAML d'un script validé, génère la voix off FR pour chaque plan
via ElevenLabs Multilingual v2, écrit les mp3 dans {output_dir}/audio/.

Usage:
    .venv/bin/python3 scripts/viral_copy_tts.py <output_dir> <voice_id> [stability] [similarity_boost] [style]

Args:
    output_dir : Le dossier contenant plans/plan_*.yaml (ex: 08-ads/viral-copy/2026-05-15-1614_test-exode-skeleton)
    voice_id   : L'ID ElevenLabs de la voix à utiliser (récupéré depuis voice-library.md)
    stability, similarity_boost, style : optionnels (défauts 0.4, 0.75, 0.5)

Output (stdout JSON):
    {"status": "ok", "audio_files": [{"plan": 1, "path": "...", "char_count": N}, ...], "total_chars": N, "cost_estimate_eur": X}

Env requis (depuis .env.local à la racine du repo):
    ELEVENLABS_API_KEY=sk_...
"""

import json
import os
import re
import sys
from pathlib import Path

try:
    import requests
    from dotenv import load_dotenv
except ImportError as e:
    print(f"ERROR: dépendance manquante ({e}). Installe via: .venv/bin/pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)


ELEVENLABS_TTS_URL = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
MODEL_ID = "eleven_multilingual_v2"
OUTPUT_FORMAT = "mp3_44100_128"
# Tarif ElevenLabs Multilingual v2 ≈ 0,30 €/min de speech (varie selon plan)
# Estimation char→sec : ~15 chars/sec pour la voix FR (rough)
CHARS_PER_SECOND = 15
EUR_PER_MINUTE = 0.30


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def extract_dialogue_fr(yaml_text: str) -> str:
    """Parse simple : extrait la valeur de dialogue_fr d'un YAML plan.

    On évite d'introduire pyyaml comme dépendance pour un parse trivial.
    Format attendu :
        dialogue_fr: "« Voilà... »"
    Le texte peut être sur une seule ligne (chaîne JSON-style avec quotes).
    """
    for line in yaml_text.splitlines():
        line = line.strip()
        if line.startswith("dialogue_fr:"):
            value = line[len("dialogue_fr:"):].strip()
            # Strip les quotes extérieures si présentes
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            # Strip les guillemets français extérieurs si présents
            value = value.strip("« »").strip()
            return value
    raise ValueError("Champ `dialogue_fr` non trouvé dans le YAML")


def main() -> int:
    if len(sys.argv) < 3:
        log("Usage: viral_copy_tts.py <output_dir> <voice_id> [stability] [similarity_boost] [style]")
        return 2

    output_dir = Path(sys.argv[1]).resolve()
    voice_id = sys.argv[2].strip()
    stability = float(sys.argv[3]) if len(sys.argv) > 3 else 0.4
    similarity_boost = float(sys.argv[4]) if len(sys.argv) > 4 else 0.75
    style = float(sys.argv[5]) if len(sys.argv) > 5 else 0.5

    if voice_id.upper() == "TBD" or not voice_id:
        log("ERROR: voice_id manquant ou TBD. Remplis-le dans .claude/skills/viral-copy/voice-library.md")
        return 1

    plans_dir = output_dir / "plans"
    if not plans_dir.exists():
        log(f"ERROR: dossier plans introuvable: {plans_dir}")
        return 1

    plan_files = sorted(plans_dir.glob("plan_*.yaml"))
    if not plan_files:
        log(f"ERROR: aucun fichier plans/plan_*.yaml dans {plans_dir}")
        return 1

    # Load env
    repo_root = Path(__file__).resolve().parent.parent
    env_file = repo_root / ".env.local"
    if env_file.exists():
        load_dotenv(env_file)

    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        log("ERROR: ELEVENLABS_API_KEY not set in .env.local")
        return 1

    audio_dir = output_dir / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    audio_files = []
    total_chars = 0
    headers = {"xi-api-key": api_key, "Content-Type": "application/json"}
    url = ELEVENLABS_TTS_URL.format(voice_id=voice_id)

    for plan_file in plan_files:
        # Extract plan number from filename (plan_1.yaml → 1)
        match = re.match(r"plan_(\d+)\.yaml$", plan_file.name)
        if not match:
            log(f"WARN: nom de fichier non standard, skip: {plan_file.name}")
            continue
        plan_num = int(match.group(1))

        try:
            yaml_text = plan_file.read_text(encoding="utf-8")
            dialogue = extract_dialogue_fr(yaml_text)
        except Exception as e:
            log(f"ERROR: impossible de lire dialogue_fr depuis {plan_file.name}: {e}")
            return 1

        char_count = len(dialogue)
        total_chars += char_count
        log(f"Plan {plan_num}: {char_count} chars — « {dialogue[:80]}{'…' if len(dialogue) > 80 else ''} »")

        body = {
            "text": dialogue,
            "model_id": MODEL_ID,
            "output_format": OUTPUT_FORMAT,
            "voice_settings": {
                "stability": stability,
                "similarity_boost": similarity_boost,
                "style": style,
            },
        }

        resp = requests.post(url, headers=headers, json=body, timeout=60)
        if resp.status_code != 200:
            log(f"ERROR: ElevenLabs API {resp.status_code} for plan {plan_num}: {resp.text[:500]}")
            return 1

        out_path = audio_dir / f"plan_{plan_num}.mp3"
        out_path.write_bytes(resp.content)
        size_kb = out_path.stat().st_size / 1024
        log(f"  → {out_path.name} ({size_kb:.1f} KB)")

        audio_files.append({
            "plan": plan_num,
            "path": str(out_path),
            "char_count": char_count,
            "size_kb": round(size_kb, 1),
        })

    # Cost estimate
    estimated_seconds = total_chars / CHARS_PER_SECOND
    estimated_minutes = max(1, int((estimated_seconds + 59) / 60))  # ceil
    cost_estimate = round(estimated_minutes * EUR_PER_MINUTE, 3)

    summary = {
        "status": "ok",
        "voice_id": voice_id,
        "n_plans": len(audio_files),
        "audio_files": audio_files,
        "total_chars": total_chars,
        "estimated_speech_seconds": round(estimated_seconds, 1),
        "cost_estimate_eur": cost_estimate,
    }
    log(f"OK — {len(audio_files)} mp3 générés, {total_chars} chars, ~{estimated_seconds:.0f}s speech, ~{cost_estimate} €")
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
