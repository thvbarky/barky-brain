# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-05 18:00 (J3 — run 18h)**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## ✅ Pause Ad8 — Résultat J3 confirmé

| Métrique | J1 (03/06) | J2 (04/06) FINAL | J3 (05/06) 18h |
|---|---|---|---|
| Spend | 10,32 € | 39,02 € | **4,66 €** (lent) |
| **CTR** | 3,33% | **9,84%** 🚨 | **2,03%** ✅ |
| CPC | 0,11 € | 0,03 € (fantôme) | **0,11 € (réel)** |
| CPM | 2,84 € | 3,10 € | **2,26 €** |
| Sessions Shopify social | **42** | **13** | **3** (partiel) |
| ATC social | 0 | 0 | 0 |
| ATC tous canaux | 1 | 3 ⭐ | 0 |

CTR J3 : 9,84 % (J2 fantôme) → 1,48 % (8h) → **2,03 % (18h)**. Signal propre et stable.

---

## 🏆 Scorecard créas J3 18h (toutes ≥ 1 000 impr cumul)

| Rang | Créa | Impr cumul | CTR J3 | CPC J3 | Budget CBO | Verdict |
|---|---|---|---|---|---|---|
| ⭐ | Ad1 PDP · cest-lage-reframe | **1 697** | **2,51 %** | 0,08 € | 14% | ✅ STAR CTR J3 |
| ✅ | Ad1 LP · cest-lage-reframe | **1 040** | **2,18 %** | 0,09 € | 30% | ✅ Vient de passer ≥1000 |
| ✅ | Ad3 LP · 5-problemes | **4 485** | **1,98 %** | 0,13 € | 40% | ✅ Référence CTR · CBO leader |
| 🟠 | Ad2 LP · signes-mobilite | **1 521** | **1,32 %** ↘ | 0,18 € | 16% | 🟠 Tendance baissière |
| 🔴 | Ad8 Video | PAUSED | — | — | 0% | 🚨 Ne pas réactiver |

Tous CTR Facebook sains (1,91–2,01 %). 0 fantôme détecté en J3.

---

## ⚠️ Alertes actives

### 🟠 Ad2 LP CTR en baisse tendancielle
CTR sur 3 mesures : J2 FINAL 1,82 % → J3 8h 1,40 % → **J3 18h 1,32 %**.
CPC 0,18 € = plus cher du compte. **Si CTR final J3 ≤ 1,5 % → recommander pause J4.**

### ⚠️ Budget J3 anormalement lent
4,66 € à 18h (on track ~6 € final vs 10,32 € J1). **Thomas : confirmer budget CBO journalier.**
Si ≥ 15 €/j → mini learning phase post-pause Ad8. Si = 10 €/j → dans les clous.

---

## Funnel cumulé J1+J2+J3

```
Spend total          : 54,00 €  (10,32 + 39,02 + 4,66)
  dont fantômes      : ~33,20 € (Ad8+Copie J2 uniquement)
  dont clean         : ~20,80 € (créas propres)
Link clicks Meta     :    864   (J1:96 · J2:726 · J3:42)
Sessions social      :     58   (J1=42 · J2=13 · J3=3)
Sessions total       :    139   (J1=74 · J2=59 · J3=6)
ATC social           :      0
ATC tous canaux      :      4   (J1=1 · J2=3) ⭐
Commandes            :      0   — 0,00 € CA ads
```

---

## ⚔️ Duel LP vs PDP : patience

0 ATC social sur 58 sessions J1-J3. CBO tient 86/14 LP/PDP.
Ad1 PDP montre le meilleur CTR (2,51 %) mais on ne coupe pas LP avant le 1er ATC social.

---

### Légende seuils scorecard
- CTR : 🔴 <1% · 🟠 1-1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC lien : 🟢 <0,50 € · 🔴 >1 €
- Coût/ATC : <8-10 € encourageant sur produit 28 €
