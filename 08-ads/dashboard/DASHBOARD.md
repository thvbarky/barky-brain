# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-07 12h — J5 PAUSED confirmé · 4h sans signal · exclusions IG toujours en attente**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## 🚨 CE QUI A CHANGÉ vs run 8h J5

1. **CAMPAGNE TOUJOURS PAUSED à 12h** — 4h sans signal depuis le run 8h. Status `CAMPAIGN_PAUSED / campaign_off` confirmé API Meta. Les exclusions IG n'ont pas été exécutées.
2. **J4 FINAL API confirmé : 40,12 €** (vs 40,10 € snapshot 8h) / 11 570 impr / 299 clics / CTR 2,58 %.
3. **Shopify J5 12h : 3 sessions direct** / 0 social / 0 ATC — inchangé vs 8h.
4. Cumul J1→J4 : **116,81 €** · 1 ATC social (J3) · 0 commande.

---

## 📊 Snapshot

| Métrique | J1 (03/06) | J2 (04/06) | J3 (05/06) FINAL | J4 (06/06) FINAL | J5 (07/06) 12h |
|---|---|---|---|---|---|
| Spend | 10,32 € | 39,02 € 🚨 | 27,37 € ✅ | **40,12 €** | **0 € 🚨 PAUSED** |
| CTR | 3,33 % | 9,84 % 🚨 | 2,34 % ✅ | 2,58 % ✅ | — |
| Sessions social | 42 | 13 | 11 | 9 | 0 |
| Sessions total | 74 | 59 | 16 | 21 | 3 (direct) |
| ATC social | 0 | 0 | **1 🎯** | 0 | 0 |
| Commandes | 0 | 0 | 0 | 0 | 0 |

**Cumul J1→J4 : 116,81 € · 1 ATC social · 0 commande**

---

## 🏆 Scorecard J4 FINAL

| Rang | Créa | CTR FB | CTR IG | CBO % | Verdict |
|---|---|---|---|---|---|
| ⭐ | Ad1 PDP · cest-lage-reframe | **2,81 %** ⭐ · CPC **0,10 €** | 1,77 % ✅ | **67,5 %** | ⭐ STAR · 4e jour consécutif dominant |
| 🚨 | Ad2 · signes-mobilite | 1,91 % ✅ | **3,83 %** n=1 671 🚨 | 30,1 % | **9,48 € fantômes J4** · EXCLURE IG avant relance |
| 📉 | Ad3 LP · 5-problemes | 2,17 % ✅ | **0,99 %** 🔴 n=202 | 2,4 % ↓ | CBO killed · EXCLURE IG avant relance |
| ❌ | Ad1 LP | — | — | 0 % | Mort naturelle CBO · clôturé |

---

## 🚨 ACTIONS AVANT RELANCE (ordre impératif)

1. **🔴 Exclure placement Instagram** sur `Ad2 · ProductHero · signes-mobilite-ete`
   - J4 FINAL : 9,48 € fantômes (79 % budget Ad2 sur IG), CTR IG 3,83 % n=1 671
   - FB Ad2 : 1,91 %, CPC 0,13 € → propre

2. **Exclure placement Instagram** sur `Ad3 · Typo · 5-problemes-1-formule · LP`
   - CTR IG 0,99 % / n=202 / CPC 0,41 € · FB 2,17 % sain

3. **Réactiver la campagne** après les 2 exclusions ci-dessus

Ces 2 exclusions = **~10 €/j** récupérés sur du trafic qualifié.

---

## Funnel cumulé J1→J4

```
Spend total      : 116,81 €  (10,32 + 39,02 + 27,37 + 40,10)
  dont fantômes  : ~43 €     (Ad8+Copie J2 ~33 € + Ad2 IG J3+J4 ~10 €)
Sessions social  :     75    (J1=42 · J2=13 · J3=11 · J4=9)
Sessions total   :    170    (J1=74 · J2=59 · J3=16 · J4=21)
ATC social       :      1    (J3) — coût/ATC = 27,37 €
Commandes        :      0    — 0,00 € CA
```

---

### Légende scorecard
- CTR : 🔴 <1% · 🟠 1–1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC : 🟢 <0,50 € · 🔴 >1 €
