# 16-veille / briefs

Briefs quotidiens de veille concurrentielle générés automatiquement par la tâche programmée Cowork sur claude.ai.

## Format

`YYYY-MM-DD-veille.md` — un fichier par jour.

## Source

- **Pipeline** : tâche programmée Cowork (claude.ai) → MCP TrendTrack → écriture directe sur ce repo via plugin GitHub
- **Prisme d'analyse** : [`../contexte-veille.md`](../contexte-veille.md) (chargé en tête de prompt à chaque run)
- **Cadence** : quotidienne (déclenchée par `mcp__scheduled-tasks__create_scheduled_task`)

## Ce qu'on cherche dans un brief

Une créa concurrente n'est ni bonne ni mauvaise dans l'absolu — elle est **utile à Barky ou pas**. Le brief filtre via le prisme du `contexte-veille.md` : pertinence pour P1/P2, angles activables, allégations reprenables.

## Historique

Voir liste des fichiers ci-dessous (Git log = chronologie complète).
