# Plan 3 jours — Extraire le signal ads (angle + destination gagnants)

> Établi le 04/06/2026 avec Thomas (mode `/brainstorming`, priorisation 80/20).
> **Nord du plan :** à la fin des 3 jours, savoir **quel angle (symptôme) et quelle destination (LP vs PDP) convertissent le mieux**, avec assez de data pour trancher.

---

## Contexte & contraintes

- **Temps Thomas :** 3-4 h/jour → suivi ads léger + 1 chantier de fond/jour.
- **Organique :** zappé sur ces 3 jours (focus 100% paid + funnel).
- **Budget :** CBO 25 €/j (choix acté, pas d'ABO).
- **Campagne :** `Barky · Trafic LP · Validation · 2026-06` (`120248461968180732`), ACTIVE.
  - Ad set 1 `Broad FR 25-60 · LP Views` (`120248461988160732`) → destination **LP**.
  - Ad set 2 `Broad FR 25-60 · Page Produit` (`120248462808000732`) → destination **PDP**.
  - 8 ads (4 angles × 2 destinations). Optim `LANDING_PAGE_VIEWS`.

## Approche retenue : C — « Funnel d'abord, puis signal »

Le levier 80/20 n'est PAS de produire plus de créas. C'est de **rendre le test lisible et de le laisser respirer**. On ne touche presque rien, on ne produit aucune nouvelle créa.

---

## Tâches par jour

Légende : `[T]` Thomas · `[C]` Claude (MCP/repo) · `[T+C]` ensemble · ⭐ = 80/20.

### JOUR 1 — Rendre le signal digne de confiance ✅ quasi bouclé
- [x] ⭐ **Parcours réel mobile, 2 chemins (LP + PDP)** · `[T]` — fait pendant la vérif pixel.
- [x] ⭐ **Vérif events pixel** · `[T+C]` — **un seul pixel `1053208107278240`, LP=PageView, PDP=PageView+ViewContent, AddToCart OK.** Funnel blindé.
- [ ] **Corriger fuites évidentes LP** · `[T+C]` — seulement si le parcours en a révélé (RAS à ce stade).
- [x] **Scorecard de décision** · `[C]` — voir section ci-dessous.
- Rituel ads : on ne touche RIEN (learning phase).

### JOUR 2 (05/06) — Lire + élaguer chirurgical
- [ ] ⭐ **Pull metrics complet** · `[C]` — par créa (CTR, CPC, CPM, hook rate vidéo) + par ad set (LP vs PDP : coût/vue LP, **coût par AddToCart**).
- [ ] ⭐ **Élaguer les créas mortes** · `[T+C]` — couper CTR <1% **après ≥1000 impressions**. Max 2-3 coupes.
- [ ] **Lire le signal destination** · `[C]` — LP vs PDP sur coût par AddToCart (tendance directionnelle).
- [ ] **Vérifier que le pixel chauffe** · `[C]` — ViewContent/ATC s'accumulent.
- [ ] **Créer audiences retargeting** · `[C]` — visiteurs LP 14j, ViewContent, ATC.

### JOUR 3 (06/06) — Trancher + concentrer + préparer la suite
- [ ] ⭐ **Lecture consolidée angle × destination** · `[C]` — tableau final = livrable des 3 jours.
- [ ] ⭐ **Concentrer le budget** · `[T+C]` — pause des angles/destinations perdants.
- [ ] **Activer le retargeting** · `[T+C]` — 1 ad set retargeting + offre -25% LANCEMENT10.
- [ ] **Préparer bascule pixel** · `[C]` — si assez de VC/ATC, planifier Traffic → AddToCart.
- [ ] **Documenter le learning** · `[C]` — journal + decisions.md.

---

## Scorecard de décision

> On juge le **duel LP vs PDP sur le coût par `AddToCart`** (la LP ne fire pas ViewContent → pas comparable là-dessus).

| Métrique | Niveau | Seuil | Action |
|---|---|---|---|
| **CTR (lien)** | 🔴 mort | < 1% (après ≥1000 impr) | couper la créa |
| | 🟠 surveiller | 1 – 1,5% | laisser, observer |
| | 🟢 bon | > 1,5% | garder |
| | ⭐ star | > 2,5% | candidate à scaler |
| **CPC** | 🟢 / 🟠 / 🔴 | <0,50 € / 0,50-1 € / >1 € | référence qualité du clic |
| **CPM** | référence | FR broad ~5-12 € | contexte coût |
| **Coût / vue LP** | référence | — | efficacité destination (haut funnel) |
| **Coût / AddToCart** | ⭐ **juge du duel** | comparer **LP vs PDP** en relatif ; <8-10 €/ATC = encourageant (produit ~28 €) | déclare la destination gagnante |
| **Taux clic→ATC** | par destination | ATC / vues LP | confirme le duel |
| **Hook rate vidéo** (Ad4) | — | 3s views / impressions | qualité accroche vidéo |

**Règles d'hygiène :**
- Ne rien toucher avant ≥1000 impressions/créa (sinon on tue du bruit).
- Max 2-3 modifs/jour (chaque modif risque de reset l'apprentissage).
- Pas de nouvelle créa pendant les 3 jours.

---

## ⚠️ Honnêteté signal + 2 leviers (à dégainer J2 si trop faible)

À 25 €/j sur 8 variantes : **signal angle/CTR solide** (haut funnel), mais signal **LP vs PDP directionnel**, pas tranché (volume par cellule faible). Pour durcir :
- **Lever budget** → 35-40 €/j (plus de volume par cellule).
- **Lever variantes** → resserrer 8 → 4 cellules (top 2 angles × 2 destinations).

---

## Watch-items techniques

- **AddToCart en méthode Manuel** : vérifier qu'il n'y a pas double-fire (manuel + app Shopify) → ATC gonflés. Ne casse pas le duel (impacte LP et PDP pareil) mais à déduplifier si les ATC paraissent anormaux.
- **Géo-blocage France-only** : impossible de tester le storefront via curl serveur (Markets FR). Vérifs storefront = côté navigateur Thomas.
- **Tools Meta gated** sur le compte : `ads_get_datasets/_stats`, `ads_get_creatives`, `ads_get_ad_preview`. Les reads créa/dataset passent par Thomas / Ads Manager.
