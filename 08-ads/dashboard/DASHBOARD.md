# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée chaque jour par `/barky-ads-daily` (routine Cowork 12h, **reco seulement**).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire décisions : [`learnings-ads.md`](learnings-ads.md) · Plan : [`../../12-operations/2026-06-04-plan-3jours-signal-ads.md`](../../12-operations/2026-06-04-plan-3jours-signal-ads.md)

**Dernière mise à jour : 2026-06-04 (pull auto — J1 complet + J2 en cours)**

---

## 🎯 Nord
Trancher : **quel angle** (symptôme) et **quelle destination** (LP vs PDP) convertissent le mieux. Jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## Snapshot — 2026-06-03 (J1 complet)

| Métrique | Valeur | Lecture |
|---|---|---|
| Spend | 10,32 € | sous-dépense J1 (budget 25 €/j) |
| Impressions | 3 635 | — |
| Link clicks Meta | 96 | ✅ signal exploitable |
| **Sessions Shopify (social)** | **42** | ✅ vérité J1 |
| AddToCart Shopify | **0** | ⚠️ 0 sur 42 sessions |
| Commandes | 0 | — |
| Coût / session | **0,25 €** | sessions propres |

## Snapshot — 2026-06-04 (J2 en cours)

| Métrique | Valeur | Lecture |
|---|---|---|
| Spend | **29,55 €** | ⚠️ overspend vs 25 €/j — Meta compense J1 |
| Impressions | 8 237 | — |
| Link clicks Meta | 557 | 🚨 96% = Ad8 fantômes |
| **Sessions Shopify (social)** | **9** | ✅ vérité partielle J2 |
| AddToCart Shopify | **0** | — J2 en cours |
| Commandes | 0 | — |
| Coût / session | **3,28 €** | 🚨 ×13 vs J1 — preuve directe des fantômes |

---

## 🚨 Alerte principale : CBO déraillé — Ad8 Video capte 96% du budget J2

| Créa | J1 (03/06) | J2 (04/06) |
|---|---|---|
| Ad3 Typo 5-problemes LP | **8,25 €** (80%) | 0,77 € (3%) |
| Ad8 Video races-poids | 0,56 € (5%) | **25,36 €** (86%) |
| Ad8 Video races-poids Copie | — | 3,24 € (11%) |
| Ad1 cest-lage PDP | 0,74 € (7%) | 0,06 € |
| Ad2 signes-mobilite | 0,77 € (7%) | 0,05 € |

**Mécanique** : J1, Ad8 a affiché CTR 15,79% sur Facebook (152 impr, petit budget). J2, le CBO l'a promu à 96% du budget. Ces clics sont 100% fantômes (Reels/Feed mobile) : 25,29 € sur Facebook @ CTR 12,47% → seuls 9 sessions Shopify sur les 29,55 € totaux. Le CBO optimise sur link_clicks sans event aval pour se corriger.

---

## 🏆 Classement des angles

> Règle : CTR Instagram fait foi. CTR Facebook toujours splitté avant jugement.

| Rang | Angle | Créa | Impr totales | CTR Insta | CTR FB | CPC lien | Verdict |
|---|---|---|---|---|---|---|---|
| ⭐ 1 | 5-problemes-1-formule | Ad3 · Typo · LP | 2 840 | **2,43%** | 3,01% | 0,14 € | ✅ seul signal propre ≥1k impr · référence |
| ⚠️ 2 | signes-mobilite-ete | Ad2 · ProductHero | 290 | 8,33% (n=24) | 1,50% | 0,11 € | prometeur · trop peu · ne pas couper |
| ⚠️ 3 | cest-lage-reframe | Ad1 · Lifestyle · PDP | 349 | 0% | 5,28% | 0,06 € | CTR FB suspect · IG mort · <1k impr |
| 🔴 ✗ | races-poids (vidéo) | Ad8 · Video | 7 287 | 4,17% (n=24) | **12,47%** | 0,05 € | clics fantômes FB · signal inutilisable |

---

## ⚔️ Duel LP vs PDP

| | LP Views | Page Produit |
|---|---|---|
| Spend J1+J2 cumulé | **36,07 €** | 4,05 € |
| Link clicks | 584 | 69 |
| Sessions Shopify | — | — |
| **AddToCart** | **0** | **0** |
| Coût / ATC | — | — |

⚠️ **Pas tranchable** : 0 ATC sur 2 jours. Bloquer Ad8 d'abord pour avoir des sessions propres, puis laisser tourner 3-4 jours.

---

## Funnel J1+J2 (complet)

```
Spend total        : 39,87 €  (J1: 10,32 € + J2: 29,55 €)
Impressions        : 11 872
Link clicks Meta   :    653  (dont ~558 fantômes Ad8 Facebook ≈ 85%)
Sessions Shopify   :     51  (social J1: 42 + J2 partiel: 9)
AddToCart          :      0
Commandes          :      0  — 0,00 € CA
```

---

## ✅ Décisions recommandées (2026-06-04)

### 🔴 PRIORITÉ 1 — Mettre Ad8 Video en pause (les 2 instances)

**Constat** : Ad8 + Copie = 28,60 € brûlés J2, 96% du budget, sur des clics Facebook fantômes. Aucune session qualifiée. Le CBO ne se corrigera pas sans suppression du signal pourri.

**Appels MCP à exécuter (Thomas confirme, puis exécute) :**
```
# Pause Ad8 principal (LP adset)
ads_update_entity(
  ad_account_id="4693134220923451",
  entity_id="120248464885400732",
  level="ad",
  fields={"status": "PAUSED"}
)

# Pause Ad8 Copie (PDP adset)
ads_update_entity(
  ad_account_id="4693134220923451",
  entity_id="120248464880070732",
  level="ad",
  fields={"status": "PAUSED"}
)
```
*Résultat attendu* : le CBO réalloue vers Ad3 (signal propre), Ad1, Ad2. Coût/session devrait repasser < 0,50 €.

---

### 🟡 PRIORITÉ 2 — Ne pas couper Ad1, Ad2 (< 1 000 impr propres)

Ad1 Lifestyle cest-lage et Ad2 ProductHero signes-mobilite ont < 400 impr chacune. Règle absolue : pas de coupe avant 1 000 impr. Une fois Ad8 éteint, ils récupèreront du budget et pourront être scorés.

---

### 🟡 PRIORITÉ 3 — Valider LP vs PDP après J3-J4 de trafic propre

0 ATC = 0 signal sur la destination. Pas de panique. Si aucun ATC après J5 avec trafic propre, vérifier : temps de chargement LP, CTA, continuité message↔landing, prix visible sans scroll.

---

### ⚪ INFO — Budget engagé vs objectif

| | Prévu | Réel |
|---|---|---|
| J1 (03/06) | 25 € | 10,32 € |
| J2 (04/06) | 25 € | 29,55 € |
| Total 2j | 50 € | 39,87 € |

Meta regularise sur 7 jours — pas d'alarme sur l'overspend J2 isolé.

---

### Légende seuils (scorecard)
- CTR Insta : 🔴 <1% (≥1 000 impr) · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC lien : 🟢 <0,50 € · 🔴 >1 €
- Coût/ATC : <8-10 € = encourageant sur produit 28 € · juge du duel LP vs PDP
