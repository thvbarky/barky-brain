# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-10 (J8 partiel) · ⛔ CAMPAIGN_PAUSED ~140h · 2ème campagne détectée · RELANCE URGENTE**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## 🆕 CE QUI A CHANGÉ vs run J7 18h (09/06)

1. **J7 FINAL corrigé : 8 sessions** (5 à 18h → 8 final — pattern habituel, sessions Shopify se consolident en soirée).
2. **J8 partiel (10/06) : 4 sessions, 0 social, 0 ATC** — campagne toujours PAUSED.
3. **Pause à ~140h** (↑ depuis 105h J7 18h). Chaque heure supplémentaire érode l'historique CBO.
4. **🚨 NOUVEAU : 2ème campagne détectée** — `Barky · Acquisition Test #1 · 2026-06` (ID 120248349620690732, PAUSED). Contient des créas v2 (Ad1 Proof, Ad2 Typo v2, Ad3 Lifestyle v2, Ad4/5/6/7). À clarifier avec Thomas avant toute relance.

---

## 📊 Snapshot

| Métrique | J4 (06/06) FINAL | J5 (07/06) | J6 (08/06) | J7 (09/06) FINAL | J8 (10/06) partiel |
|---|---|---|---|---|---|
| Spend | **40,12 €** | **0 € ⛔** | **0 € ⛔** | **0 € ⛔** | **0 € ⛔** |
| CTR | 2,58 % ✅ | — | — | — | — |
| Sessions social | 9 | 0 | 0 | 0 | 0 |
| Sessions total | 21 | 5 | 6 | **8** (corrigé) | 4 (partiel) |
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
Sessions total   :    197    (J1=74 · J2=59 · J3=16 · J4=21 · J5=5 · J6=6 · J7=8 · J8=4p)
ATC social       :      1    (J3) — coût/ATC = 27,37 €
Commandes        :      0    — 0,00 € CA
```

---

### Légende scorecard
- CTR : 🔴 <1% · 🟠 1–1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC : 🟢 <0,50 € · 🔴 >1 €
