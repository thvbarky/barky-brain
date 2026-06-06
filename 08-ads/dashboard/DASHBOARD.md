# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-06 18h — J4 partiel**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## 🆕 CE QUI A CHANGÉ depuis le run 12h

1. **🚨 Ad2 IG NON EXÉCUTÉ · piège CBO qui s'accentue** — +5,58 € brûlés depuis 12h. n IG : 562 → **1 600** (×2,8). Budget Ad2 sur IG : 3,51 € → **9,09 €** (79 % d'Ad2). CBO a escaladé Ad2 : 25,7 % → **30,7 %** du compte. Même mécanique que Ad8 (J1-J2). Chaque heure = ~1,5 €/h fantômes.
2. **Ad1 PDP stable et dominant** — CTR FB **2,88 %** ⭐ · CPC **0,10 €** ⭐ (meilleur compte) · IG 1,68 % ✅ · CBO 66,7 %.
3. **Ad3 LP gelé par le CBO** — 0,96 € total inchangé depuis 12h. CBO killed 2,6 %. FB 2,17 % sain mais invisible.
4. **Ad1 LP mort naturelle confirmée** — 0 € en J4. CBO a tranché définitivement.
5. **Spend J4 total : 37,31 €** (vs 17,35 € à 12h). Cumul J1→J4 partiel = **113,02 €**.
6. **Shopify J4 à 18h : 18 sessions total · 9 social · 0 ATC**.

---

## 📊 Snapshot

| Métrique | J1 (03/06) | J2 (04/06) | J3 (05/06) FINAL | J4 (06/06) ~18h |
|---|---|---|---|---|
| Spend | 10,32 € | 39,02 € 🚨 | **27,37 €** ✅ | **37,31 €** (partiel) |
| CTR | 3,33 % | 9,84 % 🚨 | **2,34 %** ✅ | **2,58 %** ✅ |
| Sessions social | 42 | 13 | **11** | 9 (partiel) |
| ATC social | 0 | 0 | **1 🎯** | 0 |
| Commandes | 0 | 0 | 0 | 0 |

**Cumul J1→J4 partiel : 113,02 € · 1 ATC social · 0 commande**

---

## 🏆 Scorecard J4 (~18h)

| Rang | Créa | CTR FB | CTR IG | CBO % | Verdict |
|---|---|---|---|---|---|
| ⭐ | Ad1 PDP · cest-lage-reframe | **2,88 %** ⭐ | 1,68 % ✅ | **66,7 %** | ⭐ STAR · 3 jours consécutifs · CPC 0,10 € |
| 🚨 | Ad2 · signes-mobilite | 1,87 % ✅ | **3,88 %** n=1 600 🚨 | 30,7 % ↑↑ | **URGENT** exclure IG · non exécuté · 9,09 € fantômes J4 |
| 📉 | Ad3 LP · 5-problemes | 2,17 % ✅ | **0,99 %** 🔴 n=202 | 2,6 % ↓ | CBO killed · exclure IG pour libérer FB |
| ❌ | Ad1 LP · cest-lage-reframe | — | — | **0 %** | Mort naturelle · décision CBO finale |
| 🚨 | Ad8 Video | PAUSED | — | 0 % | Permanent — ne jamais réactiver |

---

## 🚨 ACTIONS URGENTES Thomas (pendantes depuis 12h)

1. **🔴 PRIORITÉ 1 — Exclure placement Instagram** sur `Ad2 · ProductHero · signes-mobilite-ete`
   - CTR IG **3,88 %** / n=1 600 / CPM 5,68 € / 79 % du budget Ad2 = 9,09 € fantômes aujourd'hui
   - FB Ad2 reste sain : CTR 1,87 %, CPC 0,13 €
   - **~1,5 €/h de fantômes tant que non exécuté. Même piège que Ad8.**

2. **Exclure placement Instagram** sur `Ad3 · Typo · 5-problemes-1-formule · LP`
   - CTR IG 0,99 % / n=202 / CPC 0,41 € (×3 vs FB)
   - CBO a déjà killed cette créa (2,6 %). FB 2,17 % sain mais étouffé.

Ces 2 exclusions libèrent **~10–12 €/j** vers du trafic qualifié.

---

## Funnel cumulé J1→J4 partiel

```
Spend total      : 113,02 €  (10,32 + 39,02 + 27,37 + 37,31)
  dont fantômes  : ~42,29 €  (Ad8+Copie J2 = ~33,20 € + Ad2 IG J3/J4 = ~9,09 €)
Sessions social  :     75    (J1=42 · J2=13 · J3=11 · J4=9)
Sessions total   :    169    (J1=74 · J2=59 · J3=16 · J4=18 partiel)
ATC social       :      1    (J3) — coût/ATC = 27,37 €
Commandes        :      0    — 0,00 € CA
```

---

### Légende scorecard
- CTR : 🔴 <1% · 🟠 1–1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC : 🟢 <0,50 € · 🔴 >1 €
