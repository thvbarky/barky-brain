# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-09 12h — J7 partiel 12h · ⛔ CAMPAIGN_PAUSED ~88h · SEUIL 72h DÉPASSÉ · mini-learning inévitable · RELANCER AUJOURD'HUI**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## ⛔ CE QUI A CHANGÉ vs run 08h J7 (09/06)

1. **Aucun changement de données** — 3 sessions Shopify direct confirmées à 12h (identique 8h). 0 ATC. 0 commande.
2. **Campaign toujours PAUSED** — API Meta confirmé 12h07 : 0 € J6 + 0 € J7. ~88h de pause cumulée.
3. **Seuil 72h dépassé depuis ~20h le 08/06** — mini-learning inévitable, chaque heure supplémentaire creuse le trou.
4. **Exclusions IG Ad2 + Ad3 LP toujours non exécutées** — c'est le seul prérequis avant relance.
5. **Cumul J1→J4 : 116,81 € · 1 ATC social · 0 commande** — pas de dépense depuis J5.

---

## 📊 Snapshot

| Métrique | J4 (06/06) FINAL | J5 (07/06) FINAL | J6 (08/06) FINAL | J7 (09/06) partiel 12h |
|---|---|---|---|---|
| Spend | **40,12 €** | **0 € ⛔ PAUSED** | **0 € ⛔ PAUSED** | **0 € ⛔ PAUSED** |
| CTR | 2,58 % ✅ | — | — | — |
| Sessions social | 9 | 0 | 0 | 0 |
| Sessions total | 21 | 5 (direct) | 6 (direct) | 3 (direct, partiel) |
| ATC social | 0 | 0 | 0 | 0 |
| Commandes | 0 | 0 | 0 | 0 |

**Cumul J1→J6 : 116,81 € · 1 ATC social (J3) · 0 commande**

---

## 🏆 Scorecard J4 FINAL (dernière session active)

| Rang | Créa | CTR FB | CTR IG | CBO % | Verdict |
|---|---|---|---|---|---|
| ⭐ | Ad1 PDP · cest-lage-reframe | **2,81 %** ⭐ · CPC **0,10 €** | 1,77 % ✅ | **67,5 %** | ⭐ STAR confirmée · 4 jours dominant |
| 🚨 | Ad2 · signes-mobilite | 1,91 % ✅ | **3,83 %** n=1 671 🚨 | 30,1 % | **9,48 € fantômes J4** · EXCLURE IG avant relance |
| 📉 | Ad3 LP · 5-problemes | 2,17 % ✅ | **0,99 %** 🔴 n=202 | 2,4 % ↓ | CBO killed · EXCLURE IG avant relance |
| ❌ | Ad1 LP | — | — | 0 % | Mort naturelle CBO · clôturé |

---

## ⛔ ACTIONS AVANT RELANCE (ordre impératif) — SEUIL 72h DÉPASSÉ · Mini-learning inévitable

1. **🔴 Exclure placement Instagram** sur `Ad2 · ProductHero · signes-mobilite-ete`
   - J4 FINAL : 9,48 € fantômes (79 % budget Ad2 sur IG), CTR IG 3,83 % n=1 671
   - FB Ad2 : 1,91 %, CPC 0,13 € → propre

2. **Exclure placement Instagram** sur `Ad3 · Typo · 5-problemes-1-formule · LP`
   - CTR IG 0,99 % / n=202 / CPC 0,41 € · FB 2,17 % sain

3. **Réactiver la campagne** après les 2 exclusions ci-dessus

⚠️ Le seuil 72h est dépassé. Mini-learning inévitable (~100–150 impr/créa de chauffe). Ne pas juger la réallocation CBO avant ce seuil. Ad1 PDP devrait récupérer sa position dominante rapidement vu l'historique signal — mais prévoir 12–24h de stabilisation.

---

## Funnel cumulé J1→J6

```
Spend total      : 116,81 €  (10,32 + 39,02 + 27,37 + 40,12 + 0 + 0)
  dont fantômes  : ~53 €     (Ad8+Copie J2 ~33 € + Ad2 IG J3+J4 ~10 € + budget 3j pause)
Sessions social  :     75    (J1=42 · J2=13 · J3=11 · J4=9 · J5=0 · J6=0)
Sessions total   :    186    (J1=74 · J2=59 · J3=16 · J4=21 · J5=5 · J6=6 · J7=3p)
ATC social       :      1    (J3) — coût/ATC = 27,37 €
Commandes        :      0    — 0,00 € CA
```

---

### Légende scorecard
- CTR : 🔴 <1% · 🟠 1–1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC : 🟢 <0,50 € · 🔴 >1 €
