# Machines — Barky OS

Agents automatisés qui travaillent pour Barky 24h/24. À développer avec Claude Code.

---

## 📡 Stack MCP — Claude orchestrateur

> **Source de vérité opérationnelle** : [`mcp-stack.md`](./mcp-stack.md)

Trois couches branchées (ou à brancher) à Claude Code :

- **Trendtrack MCP** ✅ — data marché (250M+ pubs, 5M+ shops). Playbook : [`02-marche/intel-veille-trendtrack.md`](../02-marche/intel-veille-trendtrack.md)
- **Meta Ads MCP** ⏳ — own data (à brancher post-J7 de spend, M1+)
- **Higgsfield MCP** ⏳ — production créa (post-scaling M2-M3, **packshots/moodboards uniquement, pas de chien IA**)

Workflow créatif complet : [`08-ads/workflow-creative-mcp.md`](../08-ads/workflow-creative-mcp.md)

---

## Machines prévues

### M01 — Veille concurrentielle
- Scrape : nouveaux produits Zoomalia, Amazon, reviews
- Fréquence : hebdomadaire
- Output : `02-marche/concurrents.md` mis à jour

### M02 — Générateur de contenu
- Input : cerveau Barky + signaux actualité
- Output : drafts posts Instagram/TikTok dans `07-content/`
- Fréquence : quotidienne

### M03 — Weekly Review automatique
- Agrège : KPIs Shopify + Meta + Klaviyo
- Output : rapport dans `12-operations/weekly-reviews/`
- Fréquence : chaque lundi matin

### M04 — Brief UGC
- Génère des briefs créateurs basés sur les meilleurs angles ads
- Output : `07-content/ugc/`

### M05 — Email generator
- Génère les drafts d'emails Klaviyo à valider
- Output : `09-email-sms/sequences/`

---

## Stack technique

- Claude Code / Claude CLI (0€ via abonnement Max)
- Node.js / Python selon la machine
- Cron ou GitHub Actions pour la planification
- VPS si besoin de tourner 24h/24 (Hostinger ~5€/mois)

---

## Comment développer une machine

1. Définir : input, output, fréquence
2. Ouvrir Claude Code dans barky-brain
3. Décrire la machine en langage naturel
4. Claude code la machine
5. Tester en local
6. Déployer
