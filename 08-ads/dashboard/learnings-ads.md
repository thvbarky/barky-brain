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
- **Résultat J2 FINAL :** CTR FB 2,70 % sur **n=296 impr** → entité SAINE. Faux positif n=13. ✅ CLÔTURÉ.

### 2026-06-05 — Pause Ad8 confirmée · CTR compte 9,84 % → 1,48 %
- **Constat :** J3 partiel 8h avec Ad8+Copie à 0€ : CTR campagne **1,48 %** (vs 9,84 % J2 final). Tous CTR FB sains : Ad1 LP 1,81 % · Ad2 LP 1,42 % · Ad1 PDP 1,38 % · Ad3 LP 1,15 % (n=87). CPC 0,11 € (clics réels).
- **Décision :** Ne jamais réactiver Ad8 ou toute vidéo portrait sur un objectif Trafic/LPV. Si vidéo portrait à tester → adset Instagram-only ou objectif ATC.
- **Pourquoi :** La vidéo portrait sur Facebook Reels génère des taps accidentels comptés comme link_clicks. Pattern universel confirmé sur 3 jours consécutifs. Pas corrigeable par le ciblage.
- **Résultat (J3 18h FINAL) :** CTR campagne 1,48 % (8h) → **2,03 % (18h)** — stabilisation confirmée. Tous FB CTR sains (1,91-2,01 %). Budget 4,66 € · 2 064 impr · CPC 0,11 €. ✅ CLÔTURÉ.

### 2026-06-05 — CBO convergence post-pause · Ad1 LP = favori inattendu
- **Constat :** J3 8h : CBO alloue Ad1 LP 42 % / Ad2 LP 27 % / Ad1 PDP 20 % / Ad3 LP 13 %. Ad3 était la référence CTR (2-2,9 % FB stable J1+J2) mais reçoit le moins de budget.
- **Décision :** Ne pas intervenir. Laisser Ad1 LP atteindre ≥1 000 impr (734 cumul à 8h) avant de juger. Si CTR se confirme → CBO a raison. Surveiller au run 12h.
- **Pourquoi :** Le CBO optimise sur LPV (objectif campagne). Ad1 LP montre CTR propre et LPV élevé (LPV/click ratio à surveiller). Le CBO peut avoir un signal qualité non visible dans CTR seul.
- **Résultat (J3 18h) :** CBO J3 18h a rééquilibré : Ad3 LP remonte à 40 % · Ad1 LP 30 % · Ad2 LP 16 % · Ad1 PDP 14 %. Le CBO semble corriger vers le meilleur CTR historique (Ad3 LP). Ad1 LP a atteint ≥ 1 000 impr cumul = SCORABLE ✅. ✅ CLÔTURÉ.

### 2026-06-05 — Ad2 LP + Ad1 PDP scorables (≥1 000 impr)
- **Constat :** Ad2 LP (signes-mobilite-ete) : 1 722 impr cumul · CTR FB 1,82 % J2 FINAL. Ad1 PDP (cest-lage-reframe) : 1 484 impr cumul · CTR FB 1,97 % J2 FINAL.
- **Décision :** Les 2 entités sont saines. Pas de raison de couper. Attendre premier ATC social pour trancher l'angle et LP vs PDP.
- **Pourquoi :** CTR FB stable 1,8-2 % sur 2 jours consécutifs. CPC 0,08-0,10 €. Signal propre confirmé.
- **Résultat (J3 18h) :** Ad1 PDP : CTR J3 2,51 % (meilleur du compte ce jour) · 1 697 impr cumul. Ad2 LP : CTR J3 1,32 % → **tendance baissière** (voir entrée ci-dessous). Duel LP vs PDP toujours sans ATC social pour trancher.

---

### 2026-06-05 — Ad1 LP · ≥1 000 impr confirmé · CTR 2,18 % scorable
- **Constat :** Ad1 LP (cest-lage-reframe) atteint **1 040 impr cumul** (J2+J3). CTR J3 : 2,18 % ALL · 1,96 % FB. CPC 0,09 € = meilleur CPC du compte J3. CBO lui alloue 30 % budget.
- **Décision :** Créa pleinement scorable. CTR > 2 % stable = zone "bon" selon la scorecard. Laisser tourner pour générer des ATC.
- **Pourquoi :** Règle ≥ 1 000 impr respectée. Lifestyle + reframe âge ("c'est l'âge") est l'angle qui résonne le plus côté Facebook.
- **Résultat J3 FINAL :** CTR 2,28 % ALL · FB 2,06 % (n=923 J3) · 1 228 impr cumul. Signal propre et stable. CBO réduit à 16% (vs 30% à 18h) au profit d'Ad1 PDP. Créa confirmée saine. ✅ CLÔTURÉ.

### 2026-06-05 — Ad2 LP signes-mobilite : CTR en baisse tendancielle
- **Constat :** CTR ALL sur 3 mesures : J2 FINAL 1,81 % (n=1 218) → J3 8h 1,40 % (n=214) → J3 18h **1,32 %** (n=303). CPC 0,18 € = plus cher du compte. Tendance baissière confirmée sur 1 521 impr cumul.
- **Décision (reco) :** Si CTR final J3 ≤ 1,5 % → recommander pause Ad2 LP à J4. Budget libéré → Ad3 LP + Ad1 LP.
- **Pourquoi :** Tendance baissière sur 3 points de mesure consécutifs sans rebond. L'angle "signes de mobilité + été" ne génère pas d'engagement croissant. Après 1 500 impr propres, un CTR qui décline indique un angle peu différenciant.
- **Résultat J3 FINAL :** CTR ALL **2,10 %** (n=334) · FB **1,61 %** (n=311) — seuil 1,5 % non atteint. Les 31 dernières impr (après 18h) ont capté 3 clics supplémentaires à 9,7% CTR sur cette tranche → rebond tardif. Pas de pause. CBO l'écarte naturellement à 7%. ✅ CLÔTURÉ.

### 2026-06-05 — CBO pivote massivement vers Ad1 PDP (14 % → 35 %)
- **Constat :** Entre le run 18h et le FINAL, le CBO a redéployé : Ad1 PDP 14 % → **35 %**, Ad1 LP 30 % → 16 %, Ad2 LP 16 % → 7 %. Ad3 LP reste leader à 41 %.
- **Décision :** Ne pas intervenir. Laisser le CBO exprimer sa préférence J4. Si Ad1 PDP reste ≥ 30 % deux jours consécutifs → c'est la créa star du compte.
- **Pourquoi :** Le CBO optimise sur LPV. Ad1 PDP obtient un CTR plus élevé (2,92 %) et un signal IG valide (3,82 % n=131). La page produit semble capter mieux l'intention post-clic que la landing page.
- **Résultat (à compléter J4) :** —

### 2026-06-05 — Ad1 PDP · signal IG validé · CTR 3,82 % sur n=131
- **Constat :** Première fois qu'Ad1 PDP a assez d'impr IG (n=131) pour être scorable. CTR IG 3,82 % · CPC 0,11 €. Créa performante de façon homogène FB et IG.
- **Décision :** Confirme que l'angle reframe-âge fonctionne en statique sur IG Feed aussi, pas uniquement Facebook. Pas de risque fantôme détecté.
- **Pourquoi :** Les statiques sur IG ont moins de risque de tap accidentel que les vidéos portrait. CTR IG 3,82 % > CTR FB 2,82 % = créa qui sur-performe sur IG quand elle y est distribuée.
- **Résultat (à compléter J4) :** —

### 2026-06-05 — Shopify J3 total = 9 sessions (vs 59–74 J1-J2) · anomalie trafic organique
- **Constat :** J3 total toutes sources : 9 sessions (social=6, non-social=3). J1=74, J2=59. Trafic organique/direct : ~30-46 sessions/j J1-J2 → 3 sessions J3.
- **Décision :** Surveiller J4. Si total < 20 → investiguer source organique (post TikTok absent ? trafic direct disparu ?).
- **Pourquoi :** Si le trafic "free" s'est tari, les futurs ATC viendront quasi-exclusivement du paid. Ratio qualité/volume plus lisible mais CAC plus élevé.
- **Résultat (à compléter J4) :** —

### 2026-06-05 — Budget J3 lent post-pause Ad8
- **Constat :** 4,66 € dépensés à 18h J3. Track pour ~6 € final vs 10,32 € J1. CPM plus bas (2,26 € vs 2,84 €) mais CTR normal (2 %) donc CPC réel plus élevé → le CBO dépense moins vite.
- **Décision :** Thomas confirme le budget journalier CBO. Si ≥ 15 €/j et spend < 8 € → mini learning phase post-pause Ad8. Si budget = 10 €/j → normal.
- **Pourquoi :** Sans créa à CTR 12 % pour capter de l'inventaire cheap en volume (Facebook Reels), le CBO dépense plus lentement mais sur des clics réels. Comportement attendu, pas une anomalie critique.
- **Résultat J3 VRAI FINAL :** **27,37 €** (pas 12,79 € — la mesure "FINAL" J3 était un snapshot partiel mi-journée). Le CBO a continué le soir. → Voir entrée ci-dessous.

---

### 2026-06-05 — RÈGLE : ne jamais tagger FINAL un run en cours de journée
- **Constat :** Le run précédent a taggé "J3 FINAL" à ~12,79 € (snapshot probablement en après-midi). L'API Meta J3 confirmé le lendemain = **27,37 €** (8 813 impr · CTR 2,34 %). Ad1 PDP est passé de 35 % (18h) à **55,8 %** en fin de soirée.
- **Décision :** **FINAL = uniquement le lendemain matin** quand le spend de la veille est confirmé stable (pas de nouvelles impr depuis >8h). Tagger "(partiel HHh)" pendant la journée.
- **Pourquoi :** Le CBO réalloue régulièrement en fin de soirée sur des créneaux d'enchères cheap. Un snapshot 18h ≠ FINAL.
- **Résultat :** Règle permanente. Cumul vrai J1+J2+J3 = **76,71 €** (vs 62,13 € noté précédemment).

### 2026-06-05 — PREMIER ATC SOCIAL confirmé (J3 vrai)
- **Constat :** Shopify J3 vrai : 16 sessions total · 11 sessions social · **1 ATC social** · 0 commande. Coût/ATC social = **27,37 €** (tout le budget J3 / 1 ATC). Sans breakdown créa pixel, impossible d'attribuer l'ATC à LP ou PDP.
- **Décision :** Milestone acté. Premier signal d'intention réelle. Cible coût/ATC ≤ 8–10 € → gap ×3 à combler. Volume social cumulé désormais = 66 sessions : le trafic paid est qualifié (les 0 ATC J1-J2 venaient du manque de volume propre post-Ad8).
- **Pourquoi :** Le trafic direct/organique J1-J2 avait généré 4 ATC (dont 3 le J2). Le paid social est plus récent mais commence à convertir. CAC ads social à surveiller.
- **Résultat (à compléter J4) :** 2e ATC social attendu si volume dépasse ~11 sessions social.

### 2026-06-05 — Ad1 PDP · cest-lage-reframe = créa dominante du compte
- **Constat :** CBO J3 vrai = **55,8 %** (15,28 €). Confirmé J4 partiel = **56,5 %** (2,64 €). CTR FB : 2,49 % J3 → **3,78 %** J4 ↑↑. Deux jours consécutifs avec > 50 % du budget sur cette créa.
- **Décision :** Créa confirmée star. Ne pas intervenir. Si CBO maintient > 50 % au run 18h J4 → envisager augmenter le budget CBO pour générer 5+ ATC/semaine.
- **Pourquoi :** Deux jours de CBO > 50 % = pas une fluctuation. L'angle "c'est l'âge reframe" + destination Page Produit est la combinaison gagnante. La PDP convertit mieux que la LP sur cet angle car le propriétaire est déjà dans un état d'acceptation (pas dans le déni).
- **Résultat (à compléter J4 FINAL) :** —

### 2026-06-06 — Ad2 IG CTR élevé sur 2 jours consécutifs
- **Constat :** Ad2 IG : **7,48 %** (n=107, J3 vrai) → **5,21 %** (n=96, J4 partiel). CPM anormal : 7–8 € vs 2–4 € normaux. FB Ad2 reste sain (1,39–2,21 %).
- **Décision (reco) :** Surveiller J4 final. Si CTR IG > 5 % sur n > 200 impr → recommander exclusion placement IG pour Ad2. Pas d'urgence à ce stade.
- **Pourquoi :** Pas encore au niveau critique Ad8 (12 %) mais le CPM IG élevé suggère que Ad2 est distribué en IG Stories/Reels → taps accidentels. Le format ProductHero (statique dense) est moins adapté à ce placement que le Feed.
- **Résultat (à compléter J4 FINAL) :** —

### 2026-06-06 — Ad3 LP IG · CTR 1,00 % sur n=201 — premier seuil rouge scorable
- **Constat :** Ad3 LP IG J4 partiel : CTR **1,00 %** sur n=201 impr · CPC 0,41 € (vs 0,12 € FB). Ad3 LP FB J4 reste sain : CTR **2,17 %** (n=46). En J3 vrai, Ad3 LP IG était à 1,71 % (sain).
- **Décision (reco) :** Surveiller run 12h/18h. Si CTR IG < 1 % sur n > 400 impr → recommander exclusion placement IG pour Ad3 LP. Le FB peut continuer seul.
- **Pourquoi :** Ad3 LP est une créa typographique dense (5 problèmes / 1 formule). Ce format résonne en Feed Facebook (lecture active) mais moins en scroll IG (lecture passive). Possible incompatibilité créa/format sur IG.
- **Résultat (à compléter J4 FINAL) :** —
