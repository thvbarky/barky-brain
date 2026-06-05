# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-05 FINAL (J3 — run tardif)**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## ✅ J3 FINAL — CTR propre stabilisé, CBO pivote vers Ad1 PDP

| Métrique | J1 (03/06) | J2 (04/06) FINAL | J3 (05/06) FINAL |
|---|---|---|---|
| Spend | 10,32 € | 39,02 € 🚨 | **12,79 €** ✅ |
| **CTR** | 3,33% | **9,84%** 🚨 | **2,35%** ✅ |
| CPC | 0,11 € | 0,03 € (fantôme) | **0,12 € (réel)** |
| CPM | 2,84 € | 3,10 € | **2,81 €** |
| Sessions social | **42** | **13** | **6** |
| Sessions total | 74 | 59 | **9** ⚠️ |
| ATC tous canaux | 1 | 3 | 0 |

---

## 🏆 Scorecard créas J3 FINAL

| Rang | Créa | Impr cumul | CTR J3 ALL | CTR FB J3 | CBO % | Verdict |
|---|---|---|---|---|---|---|
| ⭐ | Ad1 PDP · cest-lage-reframe | **2 642** | **2,92 %** | **2,82 %** | **35% ↑↑** | ⭐ STAR · CBO le booste massivement |
| ✅ | Ad1 LP · cest-lage-reframe | **1 228** | **2,28 %** | **2,06 %** | 16% | ✅ BON · stable |
| ✅ | Ad3 LP · 5-problemes | **5 706** | **2,02 %** | **2,18 %** | 41% | ✅ Référence CBO leader |
| 🟠 | Ad2 LP · signes-mobilite | **1 842** | **2,10 %** | **1,61 %** | 7% ↓↓ | 🟠 FB borderline · CBO l'écarte |
| 🔴 | Ad8 Video | PAUSED | — | — | 0% | 🚨 Permanent — ne pas réactiver |

CBO allocation J3 : Ad3 LP 41% · Ad1 PDP 35% · Ad1 LP 16% · Ad2 LP 7%

---

## 🆕 CE QUI A CHANGÉ (run FINAL vs run 18h)

1. **CBO pivote massivement vers Ad1 PDP : 14% → 35%** — signal fort, surveiller J4
2. **Spend J3 FINAL : 12,79 €** (vs 4,66 € mesure partielle à 18h) — normal
3. **Ad2 LP CTR J3 final : 2,10 %** — alerte tendance baissière non déclenchée
4. **Ad1 PDP IG : CTR 3,82 % sur n=131** — signal IG désormais valide
5. **Shopify total J3 : 9 sessions** (vs 59–74 J1-J2) — anomalie trafic organique à surveiller

---

## ⚠️ Alertes actives

### ⚠️ 0 ATC social — volume insuffisant
61 sessions social J1-J3, 0 ATC. Budget ou objectif à revoir pour générer des signaux aval.
**Question Thomas : augmenter budget CBO OU passer l'objectif sur Purchase/ATC ?**

### ⚠️ Shopify J3 = 9 sessions total
Trafic organique/direct quasi absent J3 (3 non-social vs ~30-46 J1-J2). Surveiller J4.

---

## Funnel cumulé J1+J2+J3

```
Spend total          :  62,13 €  (10,32 + 39,02 + 12,79)
  dont fantômes      : ~33,20 € (Ad8+Copie J2 uniquement)
  dont clean         : ~28,93 € (créas propres)
Sessions social      :     61   (J1=42 · J2=13 · J3=6)
Sessions total       :    142   (J1=74 · J2=59 · J3=9)
ATC social           :      0
ATC tous canaux      :      4   (J1=1 · J2=3 · J3=0) ⭐
Commandes            :      0   — 0,00 € CA
```

---

## ⚔️ Duel LP vs PDP : CBO commence à trancher

CBO J3 : 65% LP / 35% PDP (vs 86/14 à 18h). Bascule vers PDP en cours.
0 ATC social — pas encore de signal coût/ATC pour trancher. Ad1 PDP (CTR 2,92%) et Ad1 LP (CTR 2,28%) portent le même angle `cest-lage-reframe` : quand le 1er ATC social arrivera, l'angle sera validé, pas la destination.

---

### Légende seuils scorecard
- CTR : 🔴 <1% · 🟠 1–1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC lien : 🟢 <0,50 € · 🔴 >1 €
- Coût/ATC : <8–10 € encourageant sur produit 28 €
