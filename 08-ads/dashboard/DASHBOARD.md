# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-06 12h — J4 partiel**

---

## 🎯 Nord
Transcher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## 🆕 CE QUI A CHANGÉ depuis le dernier run (8h)

1. **⚠️ Ad2 IG = SEUIL ATTEINT** — CTR IG 4,09 % sur **n=562** (3e jour, n>200 confirmé). CBO alloue 78 % d'Ad2 sur IG (3,51 €). CPM 6,24 €. **→ Reco formelle : exclure IG pour Ad2.**
2. **🔴 Ad3 LP IG confirmé** — CTR IG 0,99 % sur n=202 (2e jour < 1 %). CPC 0,41 € (×3 vs FB). **→ Reco formelle : exclure IG pour Ad3 LP.**
3. **Ad1 PDP CBO 68,8 %** (↑ de 56,5 % à 8h). CTR FB 2,95 % · CPC 0,12 €. Star confirmée.
4. **Spend J4 à 12h : 17,35 €** (vs 4,67 € à 8h). Cumul total J1→J4 partiel = **94,14 €**.
5. **Shopify J4 : 11 sessions total · 5 social · 0 ATC** (trop peu pour espérer).

---

## 📊 Snapshot

| Métrique | J1 (03/06) | J2 (04/06) | J3 (05/06) VRAI | J4 (06/06) ~12h |
|---|---|---|---|---|
| Spend | 10,32 € | 39,02 € 🚨 | **27,45 €** ✅ | **17,35 €** (partiel) |
| CTR | 3,33 % | 9,84 % 🚨 | **2,34 %** ✅ | **2,37 %** ✅ |
| Sessions social | 42 | 13 | **11** | 5 (partiel) |
| ATC social | 0 | 0 | **1 🎯** | 0 |
| Commandes | 0 | 0 | 0 | 0 |

**Cumul J1→J4 partiel : 94,14 € · 1 ATC social · 0 commande**

---

## 🏆 Scorecard J4 (~12h)

| Rang | Créa | CTR FB | CTR IG | CBO % | Verdict |
|---|---|---|---|---|---|
| ⭐ | Ad1 PDP · cest-lage-reframe | **2,95 %** ⭐ | 1,52 % ✅ | **68,8 %** ↑↑ | ⭐ STAR · dominant 2 jours |
| ⚠️ | Ad2 · signes-mobilite | 2,90 % ✅ | **4,09 %** ⚠️ n=562 | 25,7 % ↑↑ | 🚨 Exclure IG — seuil atteint |
| 🔴 | Ad3 LP · 5-problemes | 2,17 % ✅ | **0,99 %** 🔴 n=202 | 5,5 % ↓ | 🚨 Exclure IG — confirmé ×2 |
| 📉 | Ad1 LP · cest-lage-reframe | — | — | **0 %** | Mort naturelle CBO |
| 🚨 | Ad8 Video | PAUSED | — | 0 % | Permanent — ne jamais réactiver |

---

## 🚨 Actions Thomas (2 actions)

1. **Exclure placement Instagram** sur `Ad2 · ProductHero · signes-mobilite-ete` — CTR IG 4,09 % / n=562 / CPM 6,24 €
2. **Exclure placement Instagram** sur `Ad3 · Typo · 5-problemes-1-formule · LP` — CTR IG 0,99 % / n=202 / CPC 0,41 €

Ces 2 exclusions libèrent ~**4,33 €/j** vers des placements à intent réel (FB sain sur les 2 créas).

---

## Funnel cumulé J1→J4 partiel

```
Spend total      : 94,14 €  (10,32 + 39,02 + 27,45 + 17,35)
  dont fantômes  : ~33,20 € (Ad8+Copie J2)
  dont IG suspect: ~4,20 €  (Ad2+Ad3 IG J3-J4)
Sessions social  :     71   (J1=42 · J2=13 · J3=11 · J4=5)
Sessions total   :    160   (J1=74 · J2=59 · J3=16 · J4=11)
ATC social       :      1   (J3) — coût/ATC = 27,37 €
Commandes        :      0   — 0,00 € CA
```

---

### Légende scorecard
- CTR : 🔴 <1% · 🟠 1–1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC : 🟢 <0,50 € · 🔴 >1 €
