#!/usr/bin/env bash
# Hook SessionEnd Claude Code — auto-sync barky-brain sur GitHub.
# Déclenché à la fin de chaque session Claude.
# - Si HEAD = main et modifs non-pushées → auto-commit + push
# - Si HEAD ≠ main → notif info, pas d'auto-push
# - Notif macOS (banner) + notif ntfy.sh (iPhone) si NTFY_TOPIC dispo

set -uo pipefail

REPO_PATH="/Users/thv12/Documents/github/barky-brain"
LOG_FILE="$REPO_PATH/.claude/hooks/sync.log"
mkdir -p "$(dirname "$LOG_FILE")"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG_FILE"; }

# Charge .env.local pour récupérer NTFY_TOPIC s'il existe
if [ -f "$REPO_PATH/.env.local" ]; then
  set -a
  # shellcheck disable=SC1091
  source "$REPO_PATH/.env.local"
  set +a
fi

NTFY_TOPIC="${NTFY_TOPIC:-}"

notify() {
  local title="$1"
  local message="$2"
  local priority="${3:-default}"

  # Notification macOS (banner local)
  osascript -e "display notification \"$message\" with title \"$title\"" 2>/dev/null || true

  # Notification ntfy.sh (iPhone) si topic configuré
  if [ -n "$NTFY_TOPIC" ]; then
    curl -fsSL \
      -H "Title: $title" \
      -H "Priority: $priority" \
      -H "Tags: package" \
      -d "$message" \
      "https://ntfy.sh/$NTFY_TOPIC" >/dev/null 2>&1 || log "ntfy push failed"
  fi
}

cd "$REPO_PATH" || { log "REPO_PATH introuvable: $REPO_PATH"; exit 0; }

BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "?")
log "session ended on branch=$BRANCH"

# Compte les modifs (modified + deleted + untracked non-ignored)
CHANGES=$(git status --porcelain | wc -l | tr -d ' ')

if [ "$CHANGES" -eq 0 ]; then
  log "rien à sync"
  exit 0
fi

# Si on n'est pas sur main, on ne push pas auto — juste notif
if [ "$BRANCH" != "main" ]; then
  notify "🌿 Barky — branche $BRANCH" "$CHANGES fichier(s) modifié(s) non poussé(s). Auto-push désactivé hors main."
  log "skip: pas sur main"
  exit 0
fi

# Snapshot de ce qui change pour le résumé
SUMMARY=$(git status --porcelain | head -5 | sed 's/^.. //' | tr '\n' ',' | sed 's/,$//')
[ "$CHANGES" -gt 5 ] && SUMMARY="$SUMMARY (+$((CHANGES-5)) autres)"

# Auto-commit + push
git add -A >> "$LOG_FILE" 2>&1
COMMIT_MSG="auto-sync: $CHANGES fichier(s) — $(date '+%Y-%m-%d %H:%M')

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"

if git commit -m "$COMMIT_MSG" >> "$LOG_FILE" 2>&1; then
  log "commit OK"
  if git push origin main >> "$LOG_FILE" 2>&1; then
    log "push OK"
    notify "✅ Barky synchronisé" "$CHANGES fichier(s) pushé(s) sur GitHub. $SUMMARY"
  else
    log "push FAIL"
    notify "⚠️ Barky push échoué" "Commit fait localement mais push KO. Voir .claude/hooks/sync.log" "high"
  fi
else
  log "commit FAIL ou rien à committer"
  notify "ℹ️ Barky" "Commit non fait (peut-être pré-commit hook). Voir .claude/hooks/sync.log"
fi

exit 0
