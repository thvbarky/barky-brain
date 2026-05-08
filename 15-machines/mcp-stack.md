# Stack MCP Barky — Claude orchestrateur

> Source : analyse tweet @Lezardoloris (2026-05-01) + état réel des outils MCP connectés à Claude Code Barky.
> **Principe** : Claude n'est pas un assistant. C'est l'orchestrateur d'une stack outil branchée sur le marché, sur notre compte, et sur la production créa.

---

## Vue d'ensemble — les 3 couches

```
┌──────────────────────────────────────────────┐
│  CLAUDE CODE (Opus 4.7) — orchestrateur      │
│  Lit le cerveau, enchaîne les MCP, livre     │
└──────────┬───────────────────┬───────────────┘
           │                   │
   ┌───────▼────────┐   ┌──────▼──────────┐   ┌───────────────┐
   │ DATA MARCHÉ    │   │ DATA OWN ACCOUNT│   │ PRODUCTION    │
   │ Trendtrack MCP │   │ Meta Ads MCP    │   │ Higgsfield MCP│
   │ ✅ branché      │   │ ⏳ à brancher    │   │ ⏳ à brancher  │
   │ (data: marché) │   │ (data: notre CA)│   │ (créa: visuels)│
   └────────────────┘   └─────────────────┘   └───────────────┘
```

| Couche | MCP | Statut | Phase d'utilité Barky |
|---|---|---|---|
| **Marché** | Trendtrack | ✅ branché | **Maintenant** — spy concurrents, pré-validation |
| **Own data** | Meta Ads (officiel) | ⏳ à brancher post-M1 | Quand on aura des campagnes live (≥ 30j de spend) |
| **Production créa** | Higgsfield | ⏳ à brancher post-validation | Phase scaling, sur packshots/mood (pas chiens réels) |
| **Stack tech Shopify** | `@shopify/dev-mcp` | ✅ branché | Dev landing pages, validation GraphQL |
| **Computer use / Chrome** | natifs Claude | ✅ dispo | QA visuel des landing pages |

---

## 1. Trendtrack MCP — la couche marché ✅

### Ce que c'est

250M+ pubs trackées · 5M+ boutiques Shopify · mises à jour quotidiennes · scope monde avec filtres pays/langue/prix/durée d'ad/spend EU/UK.

### Sub-skills disponibles dans Claude Code

```
mcp__trendtrack__search_advertisers       ← cherche annonceurs (boutique → pubs)
mcp__trendtrack__search_ads                ← cherche pubs avec filtres
mcp__trendtrack__search_shops              ← cherche boutiques Shopify
mcp__trendtrack__find_winning_products     ← winners de la semaine par niche
mcp__trendtrack__find_similar_shops        ← clones d'une boutique cible
mcp__trendtrack__brief_competitor          ← fiche complète d'une boutique
mcp__trendtrack__analyze_tracked_brand     ← deep dive sur brand suivie
mcp__trendtrack__analyze_brand_changes     ← changements 30j (pubs, LPs, emails)
mcp__trendtrack__daily_radar               ← changements quotidiens des brands trackées
mcp__trendtrack__creative_inspiration_pack ← top hooks/angles d'une niche
mcp__trendtrack__scan_ad                   ← décortique une pub spécifique (Pro)
mcp__trendtrack__search_emails             ← cadence email d'une marque (Pro)
mcp__trendtrack__analyze_shop_emails       ← stratégie email complète (Pro)
mcp__trendtrack__list_tracked_brands       ← brands actuellement suivies
mcp__trendtrack__check_credits             ← vérifier consommation API
```

### Cas d'usage prioritaires Barky → voir [`02-marche/intel-veille-trendtrack.md`](../02-marche/intel-veille-trendtrack.md)

---

## 2. Meta Ads MCP — la couche own data ⏳

### À brancher quand

- Premier euro dépensé en Meta Ads (post-test S3 ou M1 si GO)
- Au moins **7 jours de data** sinon les insights sont du bruit

### Source à utiliser

MCP officiel `@meta/business-mcp` (à confirmer au moment du branchement) ou via Supermetrics MCP qui aggrège déjà Meta Ads (présent dans la liste skills : `mcp__plugin_marketing_supermetrics__*`).

### Cas d'usage spécifiques Barky

```
"Sur les 7 derniers jours, quel angle a le meilleur CPM ? CTR ? CPP ?"
"Découpe la dépense par audience FR 25-34 vs 35-44 sur le SKU multivit hero."
"Liste les 3 créas qui ont brûlé > 50 € avec un CTR < 1% — à killer."
"Compare le payback CAC observé vs cible (< 3 mois)."
```

### Couplage avec Trendtrack

```
"Compare nos hooks vs les top hooks Trendtrack sur la niche pet wellness FR cette semaine."
"Notre CPM sur l'angle pelage est X — donne-moi le médian Trendtrack pet supplements EU."
```

---

## 3. Higgsfield MCP — la couche production créa ⏳

### À brancher

- **Quand** : phase post-validation, avant scaling M2-M3
- **Pour quoi** : packshots, moodboards, environnements, scènes lifestyle abstraites
- **Pas pour** : chien réel mangeant une bouchée, before/after pelage, UGC propriétaire-chien

### Pourquoi cette restriction est non-négociable

Le pet space a un **filtre uncanny valley plus serré** que la cosmétique humaine. Un chien IA même excellent est repéré en 2 secondes. Conversion en chute. Le benchmark Dog is Human (51 600 reviews 5★) n'utilise **que des photos réelles** sur ses ads et son site — c'est pas un hasard.

### Cas d'usage validés pour Barky

| ✅ OK pour IA | ❌ Pas pour IA |
|---|---|
| Packshot pot brun ambré sur fond bleu pastel, light studio | Chien qui mange la bouchée |
| Moodboard apothicaire / cabinet vétérinaire | Before/after pelage |
| Scène nature abstraite (gazon, ciel, sans chien) | UGC propriétaire à la maison |
| Pattern textures (fond ad statique) | Témoignage face caméra |
| Concepts pour brief photo réel ensuite | Photo de famille avec chien |

### Connection (à faire au moment voulu)

```
Settings Claude → Connecteurs → URL : https://mcp.higgsfield.ai/mcp
→ OAuth Higgsfield → done
```

---

## 4. Workflow d'orchestration — le vrai gain

### Ce que Claude fait dans un prompt

```
USER : « Trouve les 5 hooks dominants en pet wellness FR cette semaine,
         compare avec ce qu'on a en tête (BARKY_CERVEAU.md §14.3),
         liste les angles non-couverts par nos 3 angles actuels,
         et propose 3 nouveaux hooks à briefer côté créa. »

CLAUDE :
  1. mcp__trendtrack__creative_inspiration_pack(niche="pet wellness", country="FR", period=7j)
  2. Read BARKY_CERVEAU.md §14.3
  3. Cross-référence + sortie structurée
  4. Update 02-marche/intel-veille-trendtrack.md avec les hooks détectés
  5. Optionnel : log dans 12-operations/journal/{date}.md
```

### Recettes de prompts opérationnelles

→ Voir [`08-ads/workflow-creative-mcp.md`](../08-ads/workflow-creative-mcp.md) pour les prompts copy-paste sur le pipeline créa.

→ Voir [`02-marche/intel-veille-trendtrack.md`](../02-marche/intel-veille-trendtrack.md) pour les prompts veille concurrents.

---

## 5. Garde-fous — ce qu'on ne fait PAS

1. **Pas de full-auto sur les ads.** Les MCP donnent du signal, mais c'est Thomas qui valide chaque créa avant push Meta. Le filtre humain reste sur l'authenticité de marque (voice-of-brand) et la légalité (DGCCRF).
2. **Pas de copy-paste de hooks détectés.** Trendtrack te montre ce qui marche dans la niche, pas ce qui te ressemble. On adapte au voice-of-brand Barky (`01-identite/voice-of-brand.md`).
3. **Pas de générique pet en images IA.** Voir restrictions Higgsfield ci-dessus.
4. **Pas de scan_ad / search_emails à tout va** — ces tools sont **Pro plan** et consomment des crédits. Vérifier `mcp__trendtrack__check_credits` avant d'enchaîner.
5. **Logger les insights majeurs.** Toute découverte significative (nouveau concurrent, hook qui scale, angle non-couvert) → journal du jour `12-operations/journal/{date}.md` + update fichier marché concerné.

---

## 6. Limites des outils (à savoir)

| Outil | Limite |
|---|---|
| Trendtrack | Surtout US/UK. Couverture FR plus mince — un faux négatif sur "absence de concurrent FR sur multivit daily" est possible (bias d'échantillon). Cross-checker avec recherche manuelle. |
| Meta Ads MCP | Ne lit que ton compte. Pas de competitive intel via cette voie. Combiner avec Trendtrack. |
| Higgsfield | Limites de cohérence sur séquences (vidéo) et sur fidélité de marque (couleurs précises). Brief = anglais + références fidèles + post-prod manuelle quasi systématique. |
| Claude orchestrateur | Pas un magic bullet. La qualité de l'output dépend du brief. Mauvais prompt = output générique. |

---

## 7. Liste de courses pour activer la stack complète

- [x] Trendtrack MCP branché (déjà fait, voir liste deferred tools)
- [ ] **Tester** Trendtrack sur les 3 prompts prioritaires (voir `02-marche/intel-veille-trendtrack.md` §Prompts à exécuter en S1)
- [ ] Brancher Meta Ads MCP au lancement de la première campagne payée (≥ M1)
- [ ] Brancher Higgsfield MCP en phase scaling (M2-M3 post-GO)
- [ ] Documenter les coûts réels (crédits Trendtrack consommés / mois) après 30 jours d'usage

---

*Fichier créé le 2026-05-01 suite à analyse du workflow MCP partagé sur X. Mis à jour à chaque ajout/retrait de MCP dans la stack.*
