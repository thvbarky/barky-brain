# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée chaque jour par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-05 08:00 (J3 partiel — run 8h)**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## ✅ PIVOT CONFIRMÉ — Pause Ad8 prouvée par J3

| Métrique | J1 (03/06) | J2 (04/06) FINAL | J3 (05/06) 8h ↗️ |
|---|---|---|---|
| Spend | 10,32 € | 39,02 € | 1,58 € |
| **CTR** | 3,33% | **9,84%** 🚨 | **1,48%** ✅ |
| CPC | 0,11 € | 0,03 € (fantôme) | **0,11 € (réel)** |
| CPM | 2,84 € | 3,10 € | **1,67 €** |
| Sessions Shopify social | **42** | **13** | **2** |
| Sessions Shopify total | 74 | 59 | 2 |
| ATC social | 0 | 0 | 0 |
| ATC tous canaux | 1 | 3 ⭐ | 0 |

**J3 opère sans Ad8 : CTR 9,84 % → 1,48 %. CBO redistribue proprement sur 4 créas saines.**

---

## Répartition budget J3 (05/06 partiel 8h)

| Créa | Spend | % | CTR FB | Status | Signal |
|---|---|---|---|---|---|
| Ad1 · Lifestyle · LP | **0,67 €** | **42%** | 1,81% | ACTIVE | ✅ CBO LEADER |
| Ad2 · ProductHero · LP | 0,42 € | 27% | 1,42% | ACTIVE | ✅ borderline |
| Ad1 · Lifestyle · PDP | 0,32 € | 20% | 1,38% | ACTIVE | ✅ borderline |
| Ad3 · Typo · LP | 0,20 € | 13% | 1,15% | ACTIVE | ⚠️ étouffé · CTR réel 2% |
| Ad8 + Copie | **0,00 €** | 0% | — | **PAUSED** ✅ | — |

---

## 🏆 Scorecard créas (cumulatif J1+J2+J3)

| Rang | Créa | Impr. cumul | CTR FB | Verdict |
|---|---|---|---|---|
| ⭐ 1 | Ad3 · Typo · LP | **3 876** | ~2,0% | ✅ référence absolue · étouffé J3 |
| ✅ 2 | Ad2 · ProductHero · LP | **1 722** | 1,82% | ✅ scorable · borderline |
| ✅ 3 | Ad1 · Lifestyle · PDP | **1 484** | 1,97% | ✅ scorable |
| ⚠️ 4 | Ad1 · Lifestyle · LP | **734** | 1,81-2,70% | ⚠️ < 1 000 impr · CBO favori |
| 🔴 — | Ad8 · Video | PAUSED | — | 🚨 fantôme FB · ne pas réactiver |

---

## Funnel cumulé J1+J2+J3

```
Spend total         : 50,92 €  (10,32 + 39,02 + 1,58)
  dont fantômes     : ~33,20 € (Ad8+Copie J2 uniquement)
  dont clean        : ~17,72 € (toutes créas propres)
Link clicks Meta    :    833   (J1:96 · J2:726 · J3:11)
Sessions Shopify    :     57   (social : J1=42 · J2=13 · J3=2)
Sessions total      :    135   (J1=74 · J2=59 · J3=2)
ATC social          :      0
ATC tous canaux     :      4   (J1=1 · J2=3 · J3=0) ⭐
Commandes           :      0   — 0,00 € CA ads
```

---

## ✅ Décisions recommandées (2026-06-05 08h)

### ✅ CONFIRMÉ — Ad8+Copie PAUSED / CTR healthy
0€ spend J3. CTR 9,84% → 1,48%. Ne pas réactiver Ad8 sur objectif trafic/LPV.

---

### ✅ CLÔTURÉ — Alerte Ad1 LP CTR FB 15,38% (n=13)
J2 FINAL : CTR FB 2,70% sur n=296 impr. Faux positif. Entité saine.

---

### 🔵 WATCH — CBO J3 étoufffe Ad3 (13% budget)
Ad3 est la référence CTR (2,0-2,9% FB stable). Pourtant CBO lui donne 13%. Ad1 LP reçoit 42% sans encore avoir ≥1 000 impr. À surveiller au run 12h : si Ad1 LP dépasse 1 000 impr et CTR se confirme → CBO a raison. Sinon → signaler.

---

### ⚔️ Duel LP vs PDP : patience
0 ATC social encore. CBO alloue 80% LP / 20% PDP. Premier ATC social attendu fin J3 ou J4 si budget monte proprement.

---

### Légende seuils scorecard
- CTR : 🔴 <1% · 🟠 1-1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC lien : 🟢 <0,50 € · 🔴 >1 €
- Coût/ATC : <8-10 € encourageant sur produit 28 €
