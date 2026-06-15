# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-15 12h (J13 · ⛔ CAMPAIGN_PAUSED ~239h · 10e jour · J13 partiel: 29s ⚠️ 5ème spike en formation · 0 ATC · RELANCE URGENTE)**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## 🆕 CE QUI A CHANGÉ depuis run J13 08h (15/06)

1. **J13 partiel 12h = 29 sessions direct** (vs 0 à 8h) — **⚠️ 5ème spike en formation**. Baseline pause = 5–8s/j. 29s dès 12h dépasse déjà la baseline journalière. 0 ATC · 0 social · FINAL à confirmer au run 18h.
2. **Meta : toujours PAUSED** — 2 campagnes `PAUSED` confirmées API. 0€ J12 et J13. ~239h de pause (10e jour).
3. **Spikes désormais quotidiens** : J8 (10/06) · J10 (12/06) · J11 (13/06) · J12 (14/06) · J13 (15/06) — fréquence 1/jour depuis J10. Taux ATC : 5,9% → 2,9% → 0% → 0% → 0% attendu J13.
4. **Rien de nouveau** sur les 4 bloqueurs — non exécutés depuis J5 (07/06).

---

## 📊 Snapshot

| Métrique | J4 (06/06) FINAL | J5→J11 | J12 FINAL | J13 (08h) |
|---|---|---|---|---|
| Métrique | J4 (06/06) FINAL | J5→J11 | J12 FINAL | J13 (12h partiel) |
|---|---|---|---|---|
| Spend | **40,12 €** | **0 € ⛔** | **0 € ⛔** | **0 € ⛔** |
| CTR | 2,58 % ✅ | — | — | — |
| Sessions social | 9 | 0 | 0 | 0 |
| Sessions total | 21 | 5–63/j | **55 ✅ FINAL** | **29 ⚠️** |
| ATC | 0 | 0–2 (J8/J10 direct) | 0 | 0 |
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

0. **🔍 Investiguer abandoned checkouts** — Shopify admin → Orders → Abandoned checkouts (3 abandons sans achat : J8=2, J10=1).
1. **🔴 Clarifier `Acquisition Test #1`** — PAUSED · 0,04€ · 7 créas v2 dedans. Archiver ou planifier ?
2. **Exclure IG** sur `Ad2 · ProductHero · signes-mobilite-ete` (CTR IG 3,83 % n=1 671 · 9,48 € fantômes J4)
3. **Exclure IG** sur `Ad3 · Typo · 5-problemes-1-formule · LP` (CTR IG 0,99 % n=202 · CPC 0,41 €)
4. **Réactiver la campagne principale** — reset CBO total inévitable (~100–150 impr/créa de chauffe)

---

## Funnel cumulé J1→J12 FINAL

```
Spend total      : 116,98 €  (J1→J4 · 0€ J5-J13 · API confirmé)
  dont fantômes  : ~53 €     (Ad8+Copie ~33€ + Ad2 IG ~10€ + Ad3 IG ~0,82€)
Sessions social  :     75    (J1=42 · J2=13 · J3=11 · J4=9 · J5-J13=0)
Sessions total   :    413    (J1→J12 FINAL=384 + J13 partiel 12h: 29s ⚠️ spike en formation)
ATC social       :      1    (J3) — coût/ATC = 27,37 €
ATC direct       :      3    (J8:2 + J10:1 · trafic warm · 0 commande)
Commandes        :      0    — 0,00 € CA
Spikes pause     :    5⚠️   (J8=34s · J10=34s · J11=63s · J12=55s · J13=29s@12h · taux ATC 5,9%→0%)
```

---

### Légende scorecard
- CTR : 🔴 <1% · 🟠 1–1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC : 🟢 <0,50 € · 🔴 >1 €
