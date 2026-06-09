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
- **Constat :** CTR **12,4 % @ CPC 0,03 €** sur Facebook (529 link clicks) vs **2,4 %** sur Instagram (sain). Funnel : 7 979 impr → 534 clics → ~350 LPV Meta → **14 sessions Shopify** → 0 commande. ~28 € brülés surtout en taps accidentels.
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
- **Résultat :** Règle permanente confirmée J3-J4. ✅ CLÔTURÉ.

### 2026-06-04 — Ad8 non paused J2 · urgence J3
- **Constat :** Pause Ad8 recommandée le 03/06 non exécutée. J2 (04/06) : Ad8+Copie = **29,10 €** sur 30,06 € totaux (96,8%). Bilan J1+J2 : 40,38 € dépensés · 51 sessions Shopify social · **0 ATC · 0 commande ads**. Coût/session J2 = 3,34 € (×13 vs J1). Pendant ce temps Ad3 (seul signal propre) = 0,77 € J2 (2,6% du budget).
- **Décision (reco) :** Pause Ad8 `120248464885400732` + Copie `120248464880070732` AVANT le lancement de J3. Priorité absolue.
- **Pourquoi :** Chaque jour sans pause = ~30 € brülés sur Facebook fantômes avec 0 signal marketing. Ad3 est étouffé et ne peut pas générer de données de comparaison.
- **Résultat — ✅ EXÉCUTÉ le 04/06 (soir) par Thomas.** Vérifié via API : Ad8 `120248464885400732` + Copie `120248464880070732` = **PAUSED / delivery off**. Les 6 créas propres (Ad3 LP+PDP, Ad1 LP+PDP, Ad2 ×2) restent ACTIVE.

### 2026-06-04 — Ad3 Typo 5-problemes = seule créa scorable J1+J2
- **Constat :** Ad3 est la seule créa avec ≥1 000 impr et CTR propre : IG 2,43% (J1 / n=1975) · IG 2,38% (J2 / n=210). CTR FB sain : 3,01% (J1) · 4,00% (J2, n=75). CPC lien ~0,10-0,14 €.
- **Décision :** Ne pas juger Ad1/Ad2 avant qu'ils atteignent ≥1 000 impr. Post-pause Ad8, les laisser monter en puissance naturellement via le CBO.
- **Pourquoi :** règle <1 000 impr = ne pas couper.
- **Résultat (J3 05/06) :** Ad1/Ad2 ont atteint ≥1 000 impr post-pause. Tous CTR propres sur FB. ✅ CLÔTURÉ.

### 2026-06-04 — 3 ATC non-social · première intention d'achat confirmée
- **Constat :** J2 (04/06) = 3 sessions Shopify avec AddToCart (tous canaux). Non-social : trafic direct/organique. J1 = 1 ATC non-social.
- **Décision :** aucune action. Attendre J3 avec trafic propre post-pause Ad8.
- **Pourquoi :** 12 sessions social à 2,80 €/session → statistiquement impossible d'avoir un ATC.
- **Résultat (J3) :** 1 ATC social J3. ✅ CLÔTURÉ.

### 2026-06-04 — Ad1 Lifestyle LP Facebook CTR 15,38% (n=13) — risque fantôme
- **Constat :** Ad1 LP — FB CTR 15,38% sur 13 impr J2. Pattern identique signal initial Ad8.
- **Décision (reco) :** surveiller J3. Si FB CTR reste >10% avec n>100 → recommander pause.
- **Pourquoi :** Ad8 présentait CTR FB 15,79% dès J1 avec n=152 → signal confirmé J2.
- **Résultat J2 FINAL :** CTR FB 2,70 % sur **n=296 impr** → entité SAINE. Faux positif n=13. ✅ CLÔTURÉ.

### 2026-06-05 — Pause Ad8 confirmée · CTR compte 9,84 % → 1,48 %
- **Constat :** J3 partiel 8h avec Ad8+Copie à 0€ : CTR campagne **1,48 %** (vs 9,84 % J2 final). Tous CTR FB sains.
- **Décision :** Ne jamais réactiver Ad8 ou toute vidéo portrait sur un objectif Trafic/LPV.
- **Pourquoi :** La vidéo portrait sur Facebook Reels génère des taps accidentels comptés comme link_clicks. Pattern universel confirmé sur 3 jours consécutifs.
- **Résultat (J3 18h FINAL) :** CTR 2,03 % stabilisation confirmée. ✅ CLÔTURÉ.

### 2026-06-05 — CBO convergence post-pause · Ad1 LP = favori inattendu
- **Constat :** J3 8h : CBO alloue Ad1 LP 42 % / Ad2 LP 27 % / Ad1 PDP 20 % / Ad3 LP 13 %.
- **Décision :** Ne pas intervenir. Laisser Ad1 LP atteindre ≥1 000 impr (734 cumul à 8h).
- **Pourquoi :** Le CBO optimise sur LPV. Ad1 LP montre CTR propre et LPV élevé.
- **Résultat (J3 18h) :** CBO rééquilibré : Ad3 LP 40 % · Ad1 LP 30 %. Ad1 LP = SCORABLE ✅. ✅ CLÔTURÉ.

### 2026-06-05 — Ad2 LP + Ad1 PDP scorables (≥1 000 impr)
- **Constat :** Ad2 LP : 1 722 impr cumul · CTR FB 1,82 % J2. Ad1 PDP : 1 484 impr cumul · CTR FB 1,97 % J2.
- **Décision :** Les 2 entités sont saines. Attendre premier ATC social pour trancher LP vs PDP.
- **Résultat (J3 18h) :** Ad1 PDP CTR J3 2,51 % (meilleur du compte). Ad2 LP tendance baissière. ✅ CLÔTURÉ.

---

### 2026-06-05 — Ad1 LP · ≥1 000 impr confirmé · CTR 2,18 % scorable
- **Constat :** Ad1 LP (cest-lage-reframe) atteint **1 040 impr cumul** (J2+J3). CTR J3 : 2,18 % ALL · 1,96 % FB. CPC 0,09 € = meilleur CPC du compte J3.
- **Décision :** Créa pleinement scorable. CTR > 2 % stable = zone "bon". Laisser tourner.
- **Résultat J3 FINAL :** CTR 2,28 % ALL · FB 2,06 % (n=923 J3). Signal propre et stable. ✅ CLÔTURÉ.

### 2026-06-05 — Ad2 LP signes-mobilite : CTR en baisse tendancielle
- **Constat :** CTR ALL sur 3 mesures : J2 FINAL 1,81 % → J3 8h 1,40 % → J3 18h **1,32 %**. Tendance baissière confirmée sur 1 521 impr cumul.
- **Décision (reco) :** Si CTR final J3 ≤ 1,5 % → recommander pause Ad2 LP à J4.
- **Résultat J3 FINAL :** CTR ALL **2,10 %** (n=334) — seuil 1,5 % non atteint. Rebond tardif. Pas de pause. CBO l'écarte naturellement à 7%. ✅ CLÔTURÉ.

### 2026-06-05 — CBO pivote massivement vers Ad1 PDP (14 % → 35 %)
- **Constat :** Entre le run 18h et le FINAL, le CBO a redéployé : Ad1 PDP 14 % → **35 %**, Ad1 LP 30 % → 16 %, Ad2 LP 16 % → 7 %. Ad3 LP reste leader à 41 %.
- **Décision :** Ne pas intervenir. Laisser le CBO exprimer sa préférence J4. Si Ad1 PDP reste ≥ 30 % deux jours consécutifs → c'est la créa star du compte.
- **Pourquoi :** Le CBO optimise sur LPV. Ad1 PDP obtient un CTR plus élevé (2,92 %) et un signal IG valide (3,82 % n=131).
- **Résultat (J4 ~12h) :** CBO J4 = **68,8 %** (↑ 55,8 % J3 → 68,8 % J4). Deux jours consécutifs > 50 % → créa star confirmée. ✅ CLÔTURÉ.

### 2026-06-05 — Ad1 PDP · signal IG validé · CTR 3,82 % sur n=131
- **Constat :** Première fois qu'Ad1 PDP a assez d'impr IG (n=131) pour être scorable. CTR IG 3,82 % · CPC 0,11 €.
- **Décision :** Confirme que l'angle reframe-âge fonctionne en statique sur IG Feed aussi.
- **Résultat (J4 ~12h) :** CTR IG J4 = **1,52 %** sur n=1 975 impr — toujours sain. ✅ CLÔTURÉ.

### 2026-06-05 — Shopify J3 total = 9 sessions (vs 59–74 J1-J2) · anomalie trafic organique
- **Constat :** J3 total toutes sources : 9 sessions (social=6, non-social=3). J1=74, J2=59.
- **Décision :** Surveiller J4. Si total < 20 → investiguer source organique.
- **Résultat (J4 ~12h) :** J3 vrai = 16 sessions. J4 partiel = 11 sessions. Trafic organique revenu à un minimum (~5-6 sess/j). Le paid social est désormais la source principale. ✅ CLÔTURÉ.

### 2026-06-05 — Budget J3 lent post-pause Ad8
- **Constat :** 4,66 € dépensés à 18h J3. Track pour ~6 € final vs 10,32 € J1.
- **Décision :** Thomas confirme le budget journalier CBO. Si ≥ 15 €/j et spend < 8 € → mini learning phase post-pause Ad8.
- **Résultat J3 VRAI FINAL :** **27,37 €** (pas 12,79 € — snapshot partiel mi-journée). → Voir entrée règle FINAL.

---

### 2026-06-05 — RÈGLE : ne jamais tagger FINAL un run en cours de journée
- **Constat :** Le run précédent a taggé "J3 FINAL" à ~12,79 €. L'API Meta J3 confirmé le lendemain = **27,37 €** (8 813 impr · CTR 2,34 %). Ad1 PDP est passé de 35 % (18h) à **55,8 %** en fin de soirée.
- **Décision :** **FINAL = uniquement le lendemain matin** quand le spend de la veille est confirmé stable. Tagger "(partiel HHh)" pendant la journée.
- **Résultat :** Règle permanente. Cumul vrai J1+J2+J3 = **76,71 €**.

### 2026-06-05 — PREMIER ATC SOCIAL confirmé (J3 vrai)
- **Constat :** Shopify J3 vrai : 16 sessions total · 11 sessions social · **1 ATC social** · 0 commande. Coût/ATC social = **27,37 €**.
- **Décision :** Milestone acté. Cible coût/ATC ≤ 8–10 € → gap ×3 à combler.
- **Résultat (J4 ~12h) :** 0 ATC social sur 5 sessions (volume insuffisant). Cumul social : 71 sessions · 1 ATC · coût/ATC = 27,37 €. ✅ CLÔTURÉ.

### 2026-06-05 — Ad1 PDP · cest-lage-reframe = créa dominante du compte
- **Constat :** CBO J3 vrai = **55,8 %** (15,28 €). Confirmé J4 partiel = **56,5 %**. CTR FB : 2,49 % J3 → **3,78 %** J4 ↑↑.
- **Décision :** Créa confirmée star. Ne pas intervenir.
- **Pourquoi :** Deux jours de CBO > 50 % = pas une fluctuation. L'angle "c'est l'âge reframe" + PDP est la combinaison gagnante.
- **Résultat (J4 ~12h) :** CBO 68,8 % · CTR FB 2,95 % · CPC 0,12 €. Dominant 2 jours complets consécutifs > 50 %. ✅ CLÔTURÉ.

### 2026-06-06 — Ad2 IG CTR élevé sur 2 jours consécutifs
- **Constat :** Ad2 IG : **7,48 %** (n=107, J3 vrai) → **5,21 %** (n=96, J4 partiel). CPM anormal : 7–8 € vs 2–4 € normaux. FB Ad2 reste sain (1,39–2,21 %).
- **Décision (reco) :** Surveiller J4 final. Si CTR IG > 5 % sur n > 200 impr → recommander exclusion placement IG pour Ad2.
- **Pourquoi :** Le CPM IG élevé suggère que Ad2 est distribué en IG Stories/Reels → taps accidentels.
- **Résultat (J4 ~12h) :** CTR IG = **4,09 %** sur n=**562** · CPM 6,24 € · CBO alloue 78 % d'Ad2 sur IG (3,51 €/4,45 €). Seuil n>200 atteint. **→ Reco formelle : exclure IG pour Ad2.** ✅ CLÔTURÉ → voir entrée 2026-06-06 exclusions IG.

### 2026-06-06 — Ad3 LP IG · CTR 1,00 % sur n=201 — premier seuil rouge scorable
- **Constat :** Ad3 LP IG J4 partiel : CTR **1,00 %** sur n=201 impr · CPC 0,41 € (vs 0,12 € FB). Ad3 LP FB J4 reste sain : CTR **2,17 %** (n=46).
- **Décision (reco) :** Surveiller run 12h/18h. Si CTR IG < 1 % sur n > 400 impr → recommander exclusion placement IG pour Ad3 LP.
- **Pourquoi :** Ad3 LP est une créa typographique dense. Ce format résonne en Feed Facebook (lecture active) mais moins en scroll IG (lecture passive).
- **Résultat (J4 ~12h) :** CTR IG = **0,99 %** sur n=**202** · CPC 0,41 € (×3 vs FB). Seuil rouge confirmé 2e jour consécutif. **→ Reco formelle : exclure IG pour Ad3 LP.** ✅ CLÔTURÉ → voir entrée 2026-06-06 exclusions IG.

### 2026-06-06 — Deux exclusions IG recommandées (Ad2 + Ad3 LP)
- **Constat :** Ad2 IG CTR 4,09 % n=562 (CPM 6,24 €) + Ad3 LP IG CTR 0,99 % n=202 (CPC 0,41 €). Deux patterns distincts : Ad2 = clics accidentels sur IG Reels/Stories ; Ad3 LP = format typo très dense non lisible en scroll IG. Les deux drainent du budget sans intent.
- **Décision (reco) :** Exclure Instagram des placements pour (1) `Ad2 · ProductHero · signes-mobilite-ete` et (2) `Ad3 · Typo · 5-problemes-1-formule · LP`. FB reste actif pour les deux (CTR FB sain : Ad2 FB 2,90 % · Ad3 LP FB 2,17 %). Impact estimé : ~4,33 €/j réalloués vers du trafic qualifié.
- **Pourquoi :** Le CBO alloue 78 % du budget Ad2 sur IG (3,51 €/4,45 €) avec CPM 6,24 € — soit ~3× plus cher que FB. Ad3 LP IG brüle 0,82 € pour 2 clics à CPC 0,41 €. Ces deux exclusions IG sont le pendant des "placements fantômes" découverts avec Ad8 — même mécanisme, forme moins extrême mais tout aussi inefficace à l'échelle.
- **Résultat (J4 FINAL — non exécutées) :** Toujours non exécutées J4. Ad2 IG J4 FINAL = 9,48 € · CTR 3,83 % n=1 671. Ad3 LP IG = 0,82 € · CTR 0,99 % n=202. Cumul fantômes IG J3+J4 ≈ 10 €. → Campagne PAUSED J5 matin — exclusions à faire avant relance.

---

### 2026-06-06 — Ad2 IG · CBO escalade post non-action · piège identique Ad8
- **Constat :** Reco exclusion IG Ad2 émise à 12h, non exécutée. Run 18h : Ad2 IG = **n=1 600 impr** (×2,8 vs 562 à 12h) · CTR 3,88 % · CPM 5,68 € · budget 3,51 € → **9,09 €** (+5,58 € en 6h). CBO a escaladé Ad2 : 25,7 % → **30,7 %** du budget total. 79 % d'Ad2 part sur IG. Soit ~1,5 €/h de fantômes actifs.
- **Décision (reco) :** Exclure IG pour Ad2 **immédiatement**. Ce n'est plus une surveillance — c'est le même piège CBO que Ad8 (J1-J2), juste à vitesse plus lente car Ad1 PDP est en compétition.
- **Pourquoi :** J1-J2 : CBO avait réalloué 85 % budget à Ad8 en ~24h. Ad2 est sur la même trajectoire : sans event aval (ATC/Purchase), le CBO voit des link_clicks IG et pompe sans se corriger. Si non exécuté J4, Ad2 atteindra probablement 40 %+ CBO sous 24-48h.
- **Résultat (J4 FINAL) :** Toujours non exécuté. Ad2 total J4 FINAL = 12,06 € / 79 % IG = **9,48 €** fantômes. CBO Ad2 = 30,1 % du budget. Campagne PAUSED J5 matin (07/06) → exclusions à faire avant toute relance.

---

### 2026-06-07 — J5 08h · CAMPAIGN_PAUSED inattendu
- **Constat :** J5 matin : tous les adsets montrent `CAMPAIGN_PAUSED / delivery: campaign_off`. 0 € dépensé. Shopify J5 = 3 sessions direct, 0 social. La campagne a été mise en pause entre la fin de J4 et le run 8h J5.
- **Décision (reco) :** (1) Vérifier si Thomas a pausé manuellement (pour faire les exclusions IG — ce serait la bonne démarche). (2) Faire les exclusions IG Ad2 + Ad3 LP. (3) Réactiver immédiatement. Chaque heure de pause = budget non dépensé ET pas de signal d'apprentissage.
- **Pourquoi :** Si la pause est volontaire pour les exclusions → bonne pratique. Si involontaire (budget épuisé, politique Meta, erreur) → corriger en urgence.
- **Résultat (18h FINAL) :** Toujours PAUSED à 18h — **24h+ de pause totale**. API Meta : 0 € J5. Shopify J5 18h = 4 sessions direct, 0 social, 0 ATC. Les exclusions IG n'ont toujours pas été exécutées. J4 FINAL API = 40,12 € confirmé. Signal supplémentaire : 0 ATC organique sur 4 sessions directes = le problème est l'acquisition qualifiée, pas la page seule. Risque croissant de reset learning phase si pause > 3 jours. ✅ CLÔTURÉ (à réouvrir si relance ne survient pas J6).

### 2026-06-07 — J4 FINAL : 0 ATC tous canaux · signal landing/PDP insuffisant
- **Constat :** Shopify J4 FINAL = 21 sessions totales (9 social + 12 direct) / **0 ATC tous canaux**. Y compris le trafic direct/organique (12 sessions = visiteurs type-in/bookmark) = 0 ATC. Cumul J1→J4 : 116,81 € · 75 sessions social · 1 ATC social (J3) · 0 commande.
- **Décision :** Pas d'action directe sur les créas. La question devient : est-ce un problème de ciblage/créa ou de la PDP/LP elle-même ?
- **Pourquoi :** 12 sessions direct avec 0 ATC = les visiteurs qui arrivent en connaissance de cause n'achètent pas non plus. Cela pointe vers la PDP ou le prix plutôt que vers le ciblage. À surveiller post-exclusions IG quand le trafic qualifié augmentera.
- **Résultat (J5 18h) :** J5 direct : 4 sessions, 0 ATC. Confirme le pattern : même les visiteurs "chauds" (type-in/bookmark) ne passent pas en ATC. Signal mixte : peut être volume trop bas (4 sessions) ou friction PDP. Priorité = relancer d'abord, investiguer PDP si le coût/ATC reste > 15 € après 200+ sessions qualifiées. ✅ CLÔTURÉ.

### 2026-06-07 — Créas jamais tournées détectées dans le compte (Ad4/5/6/7 + v2)
- **Constat :** API révèle 13+ entités ad à 0 impr avec `effective_status: CAMPAIGN_PAUSED` : Ad4 Typo 17-vitamines-manquantes, Ad5 ProductHero signes-mobilite v2, Ad6 Lifestyle pas-vieux-il-manque, Ad7 ProductHero liste-actifs-P2, et variantes v2 d'Ad2/Ad3 (Typo, Lifestyle). Toutes ACTIVE mais bloquées par la pause campagne.
- **Décision :** Ne pas les activer simultanément à la relance. Laisser le CBO actuel (Ad1 PDP + Ad2 FB + Ad3 LP FB) exprimer ses préférences post-exclusions IG d'abord. Si coût/ATC stagne > 15 € après 5 jours de trafic propre → introduire 1 nouvelle créa.
- **Pourquoi :** Introduire 5+ nouvelles créas en même temps fragmente le signal CBO et rallonge la période d'apprentissage. L'ordre est : (1) nettoyer les placements fantômes, (2) mesurer le coût/ATC propre, (3) challenger les angles.
- **Résultat (à compléter) :** —

### 2026-06-06 — Ad1 LP · mort naturelle CBO · décision finale
- **Constat :** Ad1 LP = **0 €** en J4 (journée entière). CBO a complètement arrêté de lui allouer du budget.
- **Décision :** Créa officiellement abandonnée par le CBO. Pas d'action manuelle nécessaire.
- **Pourquoi :** L'angle reframe-âge fonctionne sur PDP (destination directe avec signal d'achat) mais pas sur la LP storytelling. Le CBO a fait la discrimination lui-même en 4 jours.
- **Résultat :** Décision CBO finale. ✅ CLÔTURÉ.

---

### 2026-06-09 — Seuil 72h dépassé · mini-learning inévitable · procédure relance
- **Constat :** J7 (09/06) : campagne toujours `CAMPAIGN_PAUSED` · ~105h de pause (18h run). Seuil 72h franchi ~20h-22h le 08/06. J6 FINAL Shopify = 6 sessions direct, 0 ATC. J7 partiel 18h = **5 sessions direct** (3 à 12h → 5 à 18h), 0 ATC. API Meta : 0 € J5+J6+J7. Exclusions IG (Ad2 + Ad3 LP) toujours non exécutées.
- **Décision (reco) :** (1) Exclure IG sur Ad2 `signes-mobilite-ete` + Ad3 LP `5-problemes-1-formule · LP`. (2) Réactiver la campagne. (3) Ne pas juger le CBO avant 100–150 impr/créa (mini-learning inévitable). (4) Ne pas activer les créas à 0 impr (Ad4/5/6/7 + v2) tant que le coût/ATC post-relance n'est pas mesuré.
- **Pourquoi :** Au-delà de 72h, Meta recalibre l'ensemble des signaux CBO. L'historique reste partiellement en mémoire (Ad1 PDP dominant à 67,5 %) mais la distribution de budget repart de ~0. La fenêtre "propre" est fermée — il faut accepter le mini-learning et relancer proprement.
- **Résultat (à compléter après relance) :** —

### 2026-06-08 — Pause 60h+ confirmée · risque reset learning critique · seuil 72h ce soir
- **Constat :** J6 (08/06, run 12h) : campagne toujours `CAMPAIGN_PAUSED` — API Meta confirme `effective_status: PAUSED` sur les 2 campagnes du compte. 0 € J5 (07/06 full day) + 0 € J6 (08/06 partiel 12h). Shopify J5 FINAL = **5 sessions direct** / 0 ATC. Shopify J6 partiel 12h = **3 sessions direct** (2 à 8h → 3 à 12h) / 0 ATC. Pause cumulative : **~60h+**. Seuil 72h atteint ce soir/nuit (09/06 matin). Exclusions IG Ad2 + Ad3 LP toujours non exécutées.
- **Décision (reco) :** Relancer **aujourd'hui avant 20h Paris** (08/06) pour passer sous le seuil 72h — ordre impératif : (1) exclure IG sur `Ad2 · ProductHero · signes-mobilite-ete`, (2) exclure IG sur `Ad3 · Typo · 5-problemes-1-formule · LP`, (3) réactiver la campagne. Si pause passe >72h (09/06 matin) → mini-learning inévitable, 100–150 impr/créa avant de juger la réallocation CBO.
- **Pourquoi :** Meta CBO sort de learning sur la régularité des dépenses. Au-delà de ~3 jours de pause, les algorithmes d'attribution de budget redémarrent quasi-intégralement. Ad1 PDP reste le favori établi — devrait récupérer ~50–70 % CBO rapidement post-relance.
- **Résultat (J6 18h) :** Toujours PAUSED. Shopify J6 partiel 18h = 3 sessions direct (inchangé depuis 12h) · 0 ATC. ~66h de pause. Seuil 72h estimé atteint entre 20h et minuit ce soir. Fenêtre relance < 6h. Exclusions IG (Ad2 + Ad3 LP) toujours non exécutées. → À clôturer après relance ou passage du seuil.
