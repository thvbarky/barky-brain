# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-08 08h — J6 partiel · CAMPAIGN_PAUSED 48h+ · URGENCE MAXIMALE**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## 🚨 CE QUI A CHANGÉ vs run 18h J5

1. **Campagne TOUJOURS PAUSED — J6 (08/06) confirmé 0 € dépensé.** Maintenant **48h+ sans budget**.
2. **Shopify J5 FINAL : 5 sessions direct** (vs 4 estimé à 18h) / 0 social / 0 ATC — confirmé.
3. **Shopify J6 partiel 8h : 2 sessions direct**, 0 social, 0 ATC.
4. **Risque reset learning phase quasi-certain** si pause dépasse 72h (demain matin 09/06).
5. Aucune exclusion IG effectuée. Aucune relance.

---

## 📊 Snapshot

| Métrique | J3 (05/06) FINAL | J4 (06/06) FINAL | J5 (07/06) FINAL | J6 (08/06) partiel 8h |
|---|---|---|---|---|
| Spend | 27,37 € ✅ | **40,12 €** | **0 € 🚨 PAUSED** | **0 € 🚨 PAUSED** |
| CTR | 2,34 % ✅ | 2,58 % ✅ | — | — |
| Sessions social | 11 | 9 | 0 | 0 |
| Sessions total | 16 | 21 | 5 (direct) | 2 (direct) |
| ATC social | **1 🎯** | 0 | 0 | 0 |
| Commandes | 0 | 0 | 0 | 0 |

**Cumul J1→J5 : 116,81 € · 1 ATC social · 0 commande**

---

## 🏆 Scorecard J4 FINAL (dernière session active)

| Rang | Créa | CTR FB | CTR IG | CBO % | Verdict |
|---|---|---|---|---|---|
| ⭐ | Ad1 PDP · cest-lage-reframe | **2,81 %** ⭐ · CPC **0,10 €** | 1,77 % ✅ | **67,5 %** | ⭐ STAR · 4 jours dominant |
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

⚠️ **CRITIQUE** : Si pause >72h (09/06 matin) → reset learning probable. Post-relance : laisser 100–150 impr/créa avant de juger la réallocation CBO.

---

## Funnel cumulé J1→J5

```
Spend total      : 116,81 €  (10,32 + 39,02 + 27,37 + 40,12 + 0)
  dont fantômes  : ~43 €     (Ad8+Copie J2 ~33 € + Ad2 IG J3+J4 ~10 €)
Sessions social  :     75    (J1=42 · J2=13 · J3=11 · J4=9 · J5=0)
Sessions total   :    175    (J1=74 · J2=59 · J3=16 · J4=21 · J5=5)
ATC social       :      1    (J3) — coût/ATC = 27,37 €
Commandes        :      0    — 0,00 € CA
```

---

### Légende scorecard
- CTR : 🔴 <1% · 🟠 1–1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC : 🟢 <0,50 € · 🔴 >1 €
