# Learnings Ads — loop d'apprentissage

> Journal **append-only** des décisions ads + leur pourquoi + le résultat constaté après coup.
> La routine `/barky-ads-daily` **lit** ce fichier pour ne pas re-proposer ce qui a déjà été tranché, et y **écrit** chaque nouvelle décision. C'est la mémoire qui rend les recos plus justes dans le temps.

## Format d'une entrée

```
### YYYY-MM-DD — <titre court>
- **Constat :** (la data observée)
- **Décision :** (ce qu'on fait / recommande)
- **Pourquoi :** (le raisonnement)
- **Résultat (à compléter J+N) :** (ce que ça a donné)
```

---

## Règles de lecture des métriques (fondations, ne pas réapprendre)

- **🥇 Sessions Shopify = dénominateur de vérité, JAMAIS les « vues de page » Meta.** Le 04/06 : ~350 vues page Meta vs **14 sessions Shopify**. Causes : pixel Meta en `<head>` (fire `PageView` instantané sur un rebond <1 s) + clics fantômes. Tout taux de conversion se calcule sur les **sessions Shopify** ou les **events pixel aval** (ATC), pas sur les clics/LPV Meta.
- **CTR anormalement haut + CPC ridicule = clics poubelle.** Repère : CTR >5-6 % avec CPC <0,10 €. Toujours **splitter le CTR par placement** (Facebook vs Instagram, Feed vs Reels) avant de juger une créa.
- **Duel LP vs PDP = coût par `AddToCart`** (la LP ne fire pas `ViewContent`). Jamais sur les vues de page.
- **Un seul pixel `1053208107278240`** sur LP + PDP → signal unifié.

---

## Entrées

### 2026-06-04 — Placement Facebook = usine à clics fantômes
- **Constat :** CTR **12,4 % @ CPC 0,03 €** sur Facebook (529 link clicks) vs **2,4 %** sur Instagram (sain). Funnel : 7 979 impr → 534 clics → ~350 LPV Meta → **14 sessions Shopify** → 0 commande. ~28 € brûlés surtout en taps accidentels.
- **Décision (reco) :** isoler la *position* sur Facebook (Feed vs Reels). Si Reels crache le CTR pourri → l'exclure ou le sortir en ad set séparé.
- **Pourquoi :** ces clics ne deviennent jamais des sessions → budget cramé sans signal.
- **Résultat (J+1 confirmé — 04/06) :** Ad8 Video a capté **96% du budget J2** (28,60 €) quasi-exclusivement sur Facebook @ CTR 12,47%. 557 link_clicks → 9 sessions Shopify (ratio 1,6%). Coût/session J2 = 3,28 € vs 0,25 € J1. Pattern 100% confirmé. → Entrée suivante pour la décision d'action.

### 2026-06-04 — Sessions Shopify comme seule vérité
- **Constat :** écart x25 entre vues page Meta et sessions Shopify.
- **Décision :** le dashboard affiche les 2 mais **ne calcule les taux que sur sessions Shopify**.
- **Pourquoi :** voir règles ci-dessus.
- **Résultat :** règle permanente.

### 2026-06-04 — CBO aveugle sur CTR fantôme — réallocation J1→J2 catastrophique
- **Constat :** J1 Ad8 Video = 0,56 € / CTR 15,79% FB (152 impr). J2 CBO lui alloue 28,60 € / 96% du budget. Coût/session J2 = 3,28 € (×13 vs J1). 557 link_clicks → 9 sessions Shopify (ratio 1,6% vs 44% J1).
- **Décision (reco) :** mettre Ad8 + Copie en pause immédiate. IDs : `120248464885400732` + `120248464880070732`. Le CBO réallouera vers Ad3/Ad1/Ad2 (signal propre).
- **Pourquoi :** sans event aval (ATC, purchase) comme objectif d'optimisation, le CBO optimise sur link_clicks/LPV qui incluent les taps fantômes. Il ne peut pas se corriger seul — seule la suppression du signal pourri fonctionne.
- **Résultat (à compléter J+2 — 06/06) :** —

### 2026-06-04 — Vidéo portrait TikTok sur Facebook Reels = taps fantômes systématiques
- **Constat :** Ad8 Video (format portrait réutilisé depuis TikTok) → CTR 12-15% @ CPC 0,03 € quasi-exclusivement sur Facebook. Instagram : CTR 4% sur 24 impr (sain pour vidéo). Pattern universel Reels : tap pour lancer/agrandir = link_click comptabilisé.
- **Décision (reco) :** toute vidéo portrait testée sur Meta → soit adset Instagram uniquement, soit campagne avec objectif ATC dès qu'il y a assez de signal aval.
- **Pourquoi :** le format autoplay portrait est pensé pour le scroll, pas la conversion. Le "tap accidentel" est une feature du format, pas une anomalie corrigeable par le ciblage.
- **Résultat (à compléter J+7) :** —
