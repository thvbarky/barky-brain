# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-10 18h00 (J8 run soir) · ⛔ CAMPAIGN_PAUSED ~116h · 32s direct (spike stabilisé) · 0 ATC · RELANCE URGENTE**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## 🆕 CE QUI A CHANGÉ vs run J8 12h (10/06)

1. **Spike 32s stabilisé** — 32 sessions à 12h → **toujours 32 à 18h** (0 nouvelle session dans l'après-midi). Spike matinal terminé. Source probable : email ou partage de lien le matin. À investiguer.
2. **Campagne toujours PAUSED** — 0 € J5→J8. ~116h de pause cumulées.
3. **Inventaire compte complet révélé** : **24 créas** au total. Dans la campagne principale : `Ad2 · PDP` + `Ad3 · PDP` existent mais n'avaient jamais été allouées (écrasées par Ad1 PDP dominant CBO). La 2ème campagne `Acquisition Test #1` contient 16 créas (8 × 2 adsets = duplicatas par design).
4. **Cumul sessions pause** : 5+6+8+32 = 51 sessions direct sans ads → 0 ATC.

---

## 📊 Snapshot

| Métrique | J4 (06/06) FINAL | J5 (07/06) | J6 (08/06) | J7 (09/06) FINAL | J8 (10/06) FINAL |
|---|---|---|---|---|---|
| Spend | **40,12 €** | **0 € ⛔** | **0 € ⛔** | **0 € ⛔** | **0 € ⛔** |
| CTR | 2,58 % ✅ | — | — | — | — |
| Sessions social | 9 | 0 | 0 | 0 | 0 |
| Sessions total | 21 | 5 | 6 | **8** | **32** (spike matinal stabilisé) |
| ATC | 0 | 0 | 0 | 0 | 0 |
| Commandes | 0 | 0 | 0 | 0 | 0 |

---

## 🏆 Scorecard (dernière session active = J4 FINAL)

| Rang | Créa | CTR FB | CTR IG | CBO % | Verdict |
|---|---|---|---|---|---|
| ⭐ | Ad1 PDP · cest-lage-reframe | **2,81 %** · CPC **0,10 €** | 1,77 % ✅ | **67,5 %** | STAR · seul ATC social |
| 🚨 | Ad2 · signes-mobilite | 1,91 % ✅ | **3,83 %** n=1 671 🚨 | 30,1 % | **9,48 € fantômes** · EXCLURE IG |
| 📉 | Ad3 LP · 5-problemes | 2,17 % ✅ | **0,99 %** 🔴 n=202 | 2,4 % | CBO killed · EXCLURE IG |
| ❌ | Ad1 LP | — | — | 0 % | Mort naturelle CBO |

---

## ⛔ ACTIONS AVANT RELANCE (ordre impératif)

1. **🔴 Clarifier `Acquisition Test #1`** — Archiver ou activer ? Budget ? Ne pas relancer sans réponse.
2. **Exclure IG** sur `Ad2 · ProductHero · signes-mobilite-ete` (CTR IG 3,83 % n=1 671 · 9,48 € fantômes J4)
3. **Exclure IG** sur `Ad3 · Typo · 5-problemes-1-formule · LP` (CTR IG 0,99 % n=202 · CPC 0,41 €)
4. **Réactiver la campagne principale** — mini-learning inévitable (~100–150 impr/créa de chauffe, ~12–24h de stabilisation CBO)

---

## Funnel cumulé J1→J8

```
Spend total      : 116,81 €  (J1→J4 · 0€ J5-J8)
  dont fantômes  : ~53 €     (Ad8+Copie J2 ~33€ + Ad2 IG J3+J4 ~10€ + 0 spend J5-J8)
Sessions social  :     75    (J1=42 · J2=13 · J3=11 · J4=9 · J5-J8=0)
Sessions total   :    221    (J1=74 · J2=59 · J3=16 · J4=21 · J5=5 · J6=6 · J7=8 · J8=32 · Shopify confirmé)
ATC social       :      1    (J3) — coût/ATC = 27,37 €
Commandes        :      0    — 0,00 € CA
```

---

### Légende scorecard
- CTR : 🔴 <1% · 🟠 1–1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC : 🟢 <0,50 € · 🔴 >1 €
