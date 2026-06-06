# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-06 fin journée — J4 quasi-final**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## 🆕 CE QUI A CHANGÉ vs run 18h (données quasi-finales J4)

1. **Spend J4 figé à ~40 €** — 37,31 → **40,05 €** (+2,74 € en fin de soirée). Cap journalier quasi-atteint. J4 = **40,05 €**.
2. **Ad2 IG : n=1 671** (était 1 600), budget 9,09 → **9,48 €** — exclusion toujours non exécutée.
3. **Shopify J4 : 19 total / 9 social / 0 ATC** (stable).
4. **Ad1 PDP CPC FB : 0,10 €** sur n=5 713 — confirmé sur volume élevé. ⭐
5. Cumul J1→J4 : **116,76 €**.

---

## 📊 Snapshot J4 (quasi-final)

| Métrique | J1 (03/06) | J2 (04/06) | J3 (05/06) FINAL | J4 (06/06) fin journée |
|---|---|---|---|---|
| Spend | 10,32 € | 39,02 € 🚨 | **27,37 €** ✅ | **40,05 €** |
| CTR | 3,33 % | 9,84 % 🚨 | **2,34 %** ✅ | **2,58 %** ✅ |
| Sessions social | 42 | 13 | **11** | 9 |
| ATC social | 0 | 0 | **1 🎯** | 0 |
| Commandes | 0 | 0 | 0 | 0 |

**Cumul J1→J4 : 116,76 € · 1 ATC social · 0 commande**

---

## 🏆 Scorecard J4 (final)

| Rang | Créa | CTR FB | CTR IG | CBO % | Verdict |
|---|---|---|---|---|---|
| ⭐ | Ad1 PDP · cest-lage-reframe | **2,80 %** ⭐ · CPC **0,10 €** | 1,77 % ✅ | **67,5 %** | ⭐ STAR J4 · 3 jours consécutifs |
| 🚨 | Ad2 · signes-mobilite | 1,91 % ✅ | **3,83 %** n=1 671 🚨 | 30,1 % | **9,48 € fantômes J4** · exclure IG avant J5 |
| 📉 | Ad3 LP · 5-problemes | 2,17 % ✅ | **0,99 %** 🔴 n=202 | 2,4 % ↓ | CBO killed · exclure IG avant J5 |
| ❌ | Ad1 LP | — | — | **0 %** | Mort naturelle · clôturé |

---

## 🚨 ACTIONS AVANT J5 (demain matin, avant que le CBO relance)

1. **🔴 Exclure placement Instagram** sur `Ad2 · ProductHero · signes-mobilite-ete`
   - J4 : 9,48 € fantômes (79 % du budget Ad2 sur IG), CTR IG 3,83 % n=1 671
   - FB Ad2 sain : 1,91 %, CPC 0,13 €

2. **Exclure placement Instagram** sur `Ad3 · Typo · 5-problemes-1-formule · LP`
   - CTR IG 0,99 % / n=202 / CPC 0,41 € · FB 2,17 % sain mais étouffé

Ces 2 exclusions = **~10–12 €/j** récupérés sur du trafic qualifié dès demain.

---

## Funnel cumulé J1→J4

```
Spend total      : 116,76 €  (10,32 + 39,02 + 27,37 + 40,05)
  dont fantômes  : ~42,68 €  (Ad8+Copie J2 = ~33,20 € + Ad2 IG J3/J4 = ~9,48 €)
Sessions social  :     75    (J1=42 · J2=13 · J3=11 · J4=9)
Sessions total   :    170    (J1=74 · J2=59 · J3=16 · J4=19)
ATC social       :      1    (J3) — coût/ATC = 27,37 €
Commandes        :      0    — 0,00 € CA
```

---

### Légende scorecard
- CTR : 🔴 <1% · 🟠 1–1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC : 🟢 <0,50 € · 🔴 >1 €
