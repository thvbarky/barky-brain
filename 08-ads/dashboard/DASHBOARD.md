# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée chaque jour par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-04 12:00 (pull API confirmé)**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## 🚨 ALERTE — Ad8 toujours en vie J2 · 96,8% du budget sur clics fantômes

| Métrique | J1 (03/06) complet | J2 (04/06) pull 12h |
|---|---|---|
| Spend | 10,32 € | **30,06 €** ⚠️ overspend |
| Impressions | 3 635 | 8 410 |
| Link clicks Meta | 96 | **574** |
| **Sessions Shopify social** | **42** ✅ | **9** 🚨 |
| **ATC social** | **0** | **0** |
| Commandes | 0 | 0 |
| Coût / session social | **0,25 €** ✅ | **3,34 €** 🚨 ×13 |

**J2 = J1 en pire.** La pause Ad8 recommandée hier n'a pas été exécutée. Le CBO a encore alloué 25,80 € sur Ad8 (CTR FB 12,54% @ CPC 0,03 €) + 3,30 € sur sa Copie.

---

## Répartition budget J2 (04/06)

| Créa | Spend | % budget | CTR | Placement dominant | Signal |
|---|---|---|---|---|---|
| Ad8 Video races-poids | **25,80 €** | 85,8% | 12,51% | 100% Facebook | 🔴 fantôme |
| Ad8 Copie | 3,30 € | 11,0% | 12,93% | 100% Facebook | 🔴 fantôme |
| Ad3 Typo 5-problemes | 0,77 € | 2,6% | 2,85% | IG dominant | ✅ propre |
| Ad1 Lifestyle cest-lage | 0,06 € | 0,2% | 0% | — | ⚠️ étouffé |

---

## 🏆 Classement angles (J1 complet · seule base fiable)

| Rang | Angle | Créa | CTR IG | CTR FB | Verdict |
|---|---|---|---|---|---|
| ⭐ 1 | 5-problemes-1-formule | Ad3 Typo LP | **2,43%** (n=1975) | 3,01% | ✅ signal propre · référence |
| ⚠️ 2 | signes-mobilite-ete | Ad2 ProductHero | 8,33% (n=24) | 1,50% | prometeur · n trop faible |
| ⚠️ 3 | cest-lage-reframe | Ad1 Lifestyle PDP | 0% (n=46) | 5,28% | IG mort · FB suspect |
| 🔴 ✗ | races-poids (vidéo) | Ad8 Video | 4,17% (n=24) | **12,54%** | clics fantômes FB |

> CTR lu par placement. CTR IG = vérité. CTR Facebook toujours splitté avant jugement.

---

## ⚔️ Duel LP vs PDP

| | LP Views | Page Produit |
|---|---|---|
| Spend J1+J2 | **37,04 €** | 4,11 € |
| Sessions Shopify | — | — |
| **ATC** | **0** | **0** |
| Coût / ATC | — | — |

⚠️ **0 ATC social sur les 2 destinations** — pas tranchable. Attendre J3-J4 de trafic propre post-pause Ad8.

---

## Funnel cumulé J1+J2

```
Spend total        : 40,38 €  (J1: 10,32 € + J2: 30,06 €)
Impressions        : 12 045
Link clicks Meta   :    670  (dont ~567 fantômes Ad8+Copie FB ≈ 85%)
Sessions Shopify   :     51  (social : J1=42 · J2=9)
ATC social         :      0
Commandes          :      0  — 0,00 € CA ads
```

*Note : 1 ATC "tous canaux" le 03/06 et 1 le 04/06 — trafic non-social (organique/direct). 1 commande 64,60 € le 02/06 pré-campagne.*

---

## ✅ Décisions recommandées (2026-06-04)

### 🔴 PRIORITÉ 1 — Pause Ad8 Video + Ad8 Copie MAINTENANT

**Constat** : 2e jour consécutif à 96,8% du budget sur Facebook fantômes. J1 = 0,56 € (signal initial) → J2 = 29,10 € (désastre). La pause recommandée hier n'a pas été exécutée.

**IDs à pauser :**
- `120248464885400732` — Ad8 · Video · races-poids-tiktok (LP adset)
- `120248464880070732` — Ad8 · Video · races-poids-tiktok - Copie (PDP adset)

*Résultat attendu* : CBO réalloue vers Ad3 (signal propre). Coût/session devrait repasser < 0,50 €.

---

### 🟡 PRIORITÉ 2 — Vérifier J3 redistribution CBO (demain 12h)

Post-pause, Ad3 Typo devrait recevoir ≥10 €/j automatiquement. Si le CBO alloue vers Ad1 ou Ad2 plutôt qu'Ad3 — le signaler.

---

### ⚪ INFO — Duel LP vs PDP : patience

0 ATC des 2 côtés avec seulement 51 sessions totales (dont 85% issues de clics fantômes). Aucun signal exploitable avant trafic propre.

---

### Légende seuils scorecard
- CTR IG : 🔴 <1% (≥1 000 impr) · 🟠 1-1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC lien : 🟢 <0,50 € · 🔴 >1 €
- Coût/ATC : <8-10 € encourageant sur produit 28 €
