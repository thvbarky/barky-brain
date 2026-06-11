# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-11 18h00 (J9 run 18h) · ⛔ CAMPAIGN_PAUSED ~140h · J9: 9s direct (+7 vs 12h · 0 ATC) · J8 FINAL confirmé API: 34s · 🎯 2 ATC · 2 checkouts · 0 commande · RELANCE URGENTE**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## 🆕 CE QUI A CHANGÉ vs run J9 12h (11/06)

1. **J9 sessions : 2 → 9 (+7)** — trafic organique/direct de l'après-midi. 0 ATC. Pas de signal d'intent d'achat.
2. **Abandoned checkouts API vide** — la requête GraphQL `abandonedCheckouts` a retourné 0 résultat pour J8+J9. Cause probable : scope Admin API insuffisant (`read_orders` ?) ou délai de conservation Shopify. Le signal Shopify Analytics reste valide (2 sessions_that_reached_checkout J8).
3. **Meta toujours PAUSED ~140h**, 0 €. Aucun changement depuis J4 FINAL (06/06).
4. **0 commande confirmé** J8 + J9 (API sales Shopify).

---

## 📊 Snapshot

| Métrique | J4 (06/06) FINAL | J5→J7 | J8 (10/06) FINAL | J9 (11/06) 18h |
|---|---|---|---|---|
| Spend | **40,12 €** | **0 € ⛔** | **0 € ⛔** | **0 € ⛔** |
| CTR | 2,58 % ✅ | — | — | — |
| Sessions social | 9 | 0 | 0 | 0 |
| Sessions total | 21 | 5–8/j | **34** (spike · 2 ATC 🎯) | **9** (+7 PM) |
| ATC | 0 | 0 | **2 direct** 🎯 | 0 |
| Commandes | 0 | 0 | 0 | 0 |

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

0. **🔍 Investiguer abandoned checkouts** — Shopify admin → Orders → Abandoned checkouts (J8 = 2 checkouts non finalisés).
1. **🔴 Clarifier `Acquisition Test #1`** — Archiver ou activer ? Budget ? Ne pas relancer sans réponse.
2. **Exclure IG** sur `Ad2 · ProductHero · signes-mobilite-ete` (CTR IG 3,83 % n=1 671 · 9,48 € fantômes J4)
3. **Exclure IG** sur `Ad3 · Typo · 5-problemes-1-formule · LP` (CTR IG 0,99 % n=202 · CPC 0,41 €)
4. **Réactiver la campagne principale** — mini-learning inévitable (~100–150 impr/créa de chauffe, ~12–24h de stabilisation CBO)

---

## Funnel cumulé J1→J9

```
Spend total      : 116,81 €  (J1→J4 · 0€ J5-J9)
  dont fantômes  : ~53 €     (Ad8+Copie J2 ~33€ + Ad2 IG J3+J4 ~10€)
Sessions social  :     75    (J1=42 · J2=13 · J3=11 · J4=9 · J5-J9=0)
Sessions total   :    225    (J1=74 · J2=59 · J3=16 · J4=21 · J5=5 · J6=6 · J7=8 · J8=34 · J9=2 · Shopify confirmé)
ATC social       :      1    (J3) — coût/ATC = 27,37 €
ATC direct       :      2    (J8 · trafic warm direct · 0 commande)
Commandes        :      0    — 0,00 € CA
```

---

### Légende scorecard
- CTR : 🔴 <1% · 🟠 1–1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC : 🟢 <0,50 € · 🔴 >1 €
