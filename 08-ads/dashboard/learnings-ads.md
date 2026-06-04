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

### 2026-06-03 — Placement Facebook = usine à clics fantômes
- **Constat :** CTR **12,4 % @ CPC 0,03 €** sur Facebook (529 link clicks) vs **2,4 %** sur Instagram (sain). Funnel : 7 979 impr → 534 clics → ~350 LPV Meta → **14 sessions Shopify** → 0 commande. ~28 € brûlés surtout en taps accidentels.
- **Décision (reco) :** isoler la *position* sur Facebook (Feed vs Reels). Si Reels crache le CTR pourri → l'exclure ou le sortir en ad set séparé.
- **Pourquoi :** ces clics ne deviennent jamais des sessions → budget cramé sans signal.
- **Résultat (J+1 confirmé — 04/06) :** Ad8 Video a capté **96% du budget J2** (25,80 € sur 30,06 €) quasi-exclusivement sur Facebook @ CTR 12,47-12,54%. 511 link_clicks → 9 sessions Shopify social (ratio 1,8%). Coût/session J2 = 3,34 € vs 0,25 € J1. Pattern 100% confirmé. → Entrée suivante pour la décision d'action.

### 2026-06-03 — Sessions Shopify comme seule vérité
- **Constat :** écart x25 entre vues page Meta et sessions Shopify.
- **Décision :** le dashboard affiche les 2 mais **ne calcule les taux que sur sessions Shopify**.
- **Pourquoi :** voir règles ci-dessus.
- **Résultat :** règle permanente.

### 2026-06-03 — CBO aveugle sur CTR fantôme — réallocation J1→J2 catastrophique
- **Constat :** J1 Ad8 Video = 0,56 € / CTR 15,79% FB (152 impr). J2 CBO lui alloue 25,80 € / 85,8% du budget. Coût/session J2 social = 3,34 € (×13 vs J1). 511 link_clicks → 9 sessions Shopify social.
- **Décision (reco) :** mettre Ad8 + Copie en pause immédiate. IDs : `120248464885400732` + `120248464880070732`. Le CBO réallouera vers Ad3/Ad1/Ad2 (signal propre).
- **Pourquoi :** sans event aval (ATC, purchase) comme objectif d'optimisation, le CBO optimise sur link_clicks/LPV qui incluent les taps fantômes. Il ne peut pas se corriger seul — seule la suppression du signal pourri fonctionne.
- **Résultat (J+2 clôturé — 04/06 FINAL) :** Pattern confirmé 2 jours consécutifs. J2 final = 30,84 € / Ad8+Copie = 29,88 € (96,8%). 10 sessions Shopify J2. Pause non exécutée → J3 à risque identique. Cumul J1+J2 = 41,16 € · 52 sessions · 0 ATC.

### 2026-06-03 — Vidéo portrait TikTok sur Facebook Reels = taps fantômes systématiques
- **Constat :** Ad8 Video (format portrait réutilisé depuis TikTok) → CTR 12-15% @ CPC 0,03 € quasi-exclusivement sur Facebook. Instagram J2 : CTR 4,17% sur 24 impr (sain pour vidéo). Pattern universel Reels : tap pour lancer/agrandir = link_click comptabilisé.
- **Décision (reco) :** toute vidéo portrait testée sur Meta → soit adset Instagram uniquement, soit campagne avec objectif ATC dès qu'il y a assez de signal aval.
- **Pourquoi :** le format autoplay portrait est pensé pour le scroll, pas la conversion. Le "tap accidentel" est une feature du format, pas une anomalie corrigeable par le ciblage.
- **Résultat (à compléter J+7) :** —

### 2026-06-04 — Ad8 non paused J2 · urgence J3
- **Constat :** Pause Ad8 recommandée le 03/06 non exécutée. J2 (04/06) : Ad8+Copie = **29,10 €** sur 30,06 € totaux (96,8%). Bilan J1+J2 : 40,38 € dépensés · 51 sessions Shopify social · **0 ATC · 0 commande ads**. Coût/session J2 = 3,34 € (×13 vs J1). Pendant ce temps Ad3 (seul signal propre) = 0,77 € J2 (2,6% du budget).
- **Décision (reco) :** Pause Ad8 `120248464885400732` + Copie `120248464880070732` AVANT le lancement de J3. Priorité absolue.
- **Pourquoi :** Chaque jour sans pause = ~30 € brûlés sur Facebook fantômes avec 0 signal marketing. Ad3 est étouffé et ne peut pas générer de données de comparaison.
- **Résultat — ✅ EXÉCUTÉ le 04/06 (soir) par Thomas.** Vérifié via API : Ad8 `120248464885400732` + Copie `120248464880070732` = **PAUSED / delivery off**. Les 6 créas propres (Ad3 LP+PDP, Ad1 LP+PDP, Ad2 ×2) restent ACTIVE. À surveiller J3 (05/06) : le CBO doit réallouer vers Ad3 → coût/session attendu < 0,50 € (vs 3,34 € J2).

### 2026-06-04 — Ad3 Typo 5-problemes = seule créa scorable J1+J2
- **Constat :** Ad3 est la seule créa avec ≥1 000 impr et CTR propre : IG 2,43% (J1 / n=1975) · IG 2,38% (J2 / n=210). CTR FB sain : 3,01% (J1) · 4,00% (J2, n=75). CPC lien ~0,10-0,14 €. Aucune donnée ATC car budget trop faible pour générer du trafic qualifié en volume.
- **Décision :** Ne pas juger Ad1/Ad2 avant qu'ils atteignent ≥1 000 impr propres. Post-pause Ad8, les laisser monter en puissance naturellement via le CBO.
- **Pourquoi :** règle <1 000 impr = ne pas couper. Ad2 signes-mobilite IG (8,33% sur 24 impr J1) est prometteur mais non confirmable.
- **Résultat (à compléter J3 05/06 — quand Ad3 reçoit budget réel) :** —

### 2026-06-04 — 3 ATC non-social · première intention d'achat confirmée
- **Constat :** J2 (04/06) = 3 sessions Shopify avec AddToCart (tous canaux). Non-social : trafic direct/organique (56 sessions total vs 12 social). J1 = 1 ATC non-social. Pattern : le trafic qualifié convertit. ATC social = 0 avec seulement 12 sessions social (trop peu pour espérer).
- **Décision :** aucune action. Attendre J3 avec trafic propre post-pause Ad8 pour avoir du volume social qualifié.
- **Pourquoi :** 12 sessions social à 2,80 €/session → statistiquement impossible d'avoir un ATC. Post-redistribution CBO (attendu ≥10 €/j sur Ad3), volume social suffisant pour générer de l'intention.
- **Résultat (J+1 = 05/06) :** à compléter — premier ATC social attendu si Ad3 reçoit budget.

### 2026-06-04 — Ad1 Lifestyle LP Facebook CTR 15,38% (n=13) — risque fantôme
- **Constat :** Ad1 · Lifestyle · cest-lage-reframe · LP — adset LP Views — FB CTR 15,38% sur 13 impr J2. CPC FB = 0,02 €. Pattern identique au signal initial de Ad8 (J1 : CTR 15,79% sur n=152). Budget J2 = 0,04 € (négligeable).
- **Décision (reco) :** surveiller J3. Si FB CTR reste >10% avec n>100 impr → recommander pause Ad1 LP Facebook (ou toute la créa si Instagram CTR aussi nul).
- **Pourquoi :** Ad8 présentait CTR FB 15,79% dès J1 avec n=152 → signal confirmé J2 à 12,54% avec n=7265. Le pattern se répète. 0,04 € aujourd'hui = pas urgent, mais si CBO le booste demain → risque fantôme n°2.
- **Résultat (J+1 = 05/06 run 8h-12h) :** à compléter.
