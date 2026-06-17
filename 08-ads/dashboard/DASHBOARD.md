# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-17 12h00 (J15 partiel · ⛔ CAMPAIGN_PAUSED ~287h · 12e jour · J14 FINAL=55s ✅ · J15: 23s · ⚠️ 4ème ATC direct · 4/4 checkout abandonné · 7ème spike en formation · PRIORITÉ #0: fixer checkout avant relance)**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## 🆕 CE QUI A CHANGÉ depuis run J15 8h (17/06)

1. **J15 partiel 12h = 23 sessions** (vs 2 à 8h — +21s depuis le run précédent). **7ème spike en formation.** 1 ATC + 1 checkout (inchangés depuis 8h — les 21 nouvelles sessions n'ont pas converti).
2. **J14 FINAL = 55 sessions** ✅ confirmé API (stable vs run 8h — pas de correction).
3. **Meta API non disponible** ce run (OTID error) — statut campagne inféré depuis historique : toujours PAUSED ~287h · 12e jour.
4. **4 bloqueurs toujours non exécutés** depuis J5 (07/06).

---

## 📊 Snapshot

| Métrique | J4 (06/06) FINAL | J5→J13 | J14 FINAL | J15 partiel |
|---|---|---|---|---|
| Spend | **40,12 €** | **0 € ⛔** | **0 € ⛔** | **0 € ⛔** |
| CTR | 2,58 % ✅ | — | — | — |
| Sessions social | 9 | 0 | 0 | 0 |
| Sessions total | 21 | 5–63/j | **55 ✅** | **23 (partiel 12h)** |
| ATC | 0 | 0–2 (J8/J10) | 0 | **1 ⚠️** |
| Commandes | 0 | 0 | 0 | 0 |

---

## 🏆 Scorecard (dernière session active = J4 FINAL · cumul API confirmé)

| Rang | Créa | CTR ALL | Cumul dépensé | CBO % J4 | Verdict |
|---|---|---|---|---|---|
| ⭐ | Ad1 PDP · cest-lage-reframe | **2,49 %** · CPC **0,12 €** | 44,60 € | **67,5 %** | STAR · seul ATC social · placement IG sain |
| 🟠 | Ad2 · signes-mobilite (LP) | 2,66 % (pollué IG) | 16,62 € | 30,1 % | FB 1,91% ✅ · **EXCLURE IG avant relance** |
| ✅ | Ad3 LP · 5-problemes | **2,30 %** · CPC **0,12 €** | 16,40 € | 2,4 % | FB 2,17% ✅ · **EXCLURE IG avant relance** |
| ❌ | Ad1 LP | 2,33 % | 5,59 € | 0 % | Mort naturelle CBO (J4) |
| 🚨 | Ad8 + Copie | CTR 12,5 % fantôme | 33,76 € | PAUSED | Bloqués définitivement |

---

## ⛔ ACTIONS AVANT RELANCE (ordre impératif)

0. **🔴 PRIORITÉ #0 — Fixer friction checkout** — 4 ATC directs, 4 checkouts abandonnés, 0 commande = **100% abandon rate**. Shopify admin → Orders → Abandoned checkouts. Causes probables : frais livraison tardifs, absence trust badges, méthode paiement manquante (PayPal). **À résoudre avant toute relance paid.**
1. **🔍 Clarifier `Acquisition Test #1`** — PAUSED · 0,04€ · 7 créas v2 dedans. Archiver ou planifier ?
2. **Exclure IG** sur `Ad2 · ProductHero · signes-mobilite-ete` (CTR IG 3,83 % n=1 671 · 9,48 € fantômes J4)
3. **Exclure IG** sur `Ad3 · Typo · 5-problemes-1-formule · LP` (CTR IG 0,99 % n=202 · CPC 0,41 €)
4. **Réactiver la campagne principale** — reset CBO total inévitable (~100–150 impr/créa de chauffe)

---

## Funnel cumulé J1→J14 FINAL + J15 partiel

```
Spend total      : 116,98 €  (J1→J4 · 0€ J5-J15 · API confirmé)
  dont fantômes  : ~53 €     (Ad8+Copie ~33€ + Ad2 IG ~10€ + Ad3 IG ~0,82€)
Sessions social  :     75    (J1=42 · J2=13 · J3=11 · J4=9 · J5-J15=0)
Sessions total   :    501    (J1→J14 FINAL=478 + J15 partiel 12h: 23s)
ATC social       :      1    (J3) — coût/ATC = 27,37 €
ATC direct       :      4    (J8:2 + J10:1 + J15:1 · trafic warm · 0 commande · 4/4 abandonné checkout)
Commandes        :      0    — 0,00 € CA
Spikes pause     :      7    (J8=34 · J10=34 · J11=63 · J12=55 · J13=39 · J14=55 · J15=23@partiel 12h)
```

---

### Légende scorecard
- CTR : 🔴 <1% · 🟠 1–1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC : 🟢 <0,50 € · 🔴 >1 €
