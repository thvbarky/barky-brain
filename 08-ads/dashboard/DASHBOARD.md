# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-11 08h00 (J9 run matin) · ⛔ CAMPAIGN_PAUSED ~130h · J8 corrigé : 34s direct · 🎯 2 ATC + 2 checkouts · 0 commande · RELANCE URGENTE**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## 🆕 CE QUI A CHANGÉ vs run J8 18h (10/06)

1. **J8 FINAL corrigé :** 32s → **34s** + **0 ATC → 2 ATC + 2 reached checkout** — premier signal checkout reach de l'historique du compte. Taux ATC direct = 5,9 %. Toutes sources = direct (0 social, campagne PAUSED). 0 commande.
2. **Friction checkout identifiée** — 2 personnes ont atteint le checkout mais n'ont pas acheté. Investiguer : frais de livraison, trust badges, méthode de paiement (Shopify admin → Orders → Abandoned checkouts).
3. **J9 partiel 8h :** 2 sessions direct, 0 ATC. Meta toujours PAUSED ~130h, 0 €.
4. **Pause toujours critique** — exclusions IG (Ad2 + Ad3 LP) toujours non exécutées. Chaque heure = coût d'opportunité + learning phase plus longue à la relance.

---

## 📊 Snapshot

| Métrique | J4 (06/06) FINAL | J5→J7 | J8 (10/06) FINAL | J9 (11/06) 8h |
|---|---|---|---|---|
| Spend | **40,12 €** | **0 € ⛔** | **0 € ⛔** | **0 € ⛔** |
| CTR | 2,58 % ✅ | — | — | — |
| Sessions social | 9 | 0 | 0 | 0 |
| Sessions total | 21 | 5–8/j | **34** (spike · 2 ATC 🎯) | 2 |
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
