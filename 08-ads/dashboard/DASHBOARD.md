# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-16 08h (J14 · ⛔ CAMPAIGN_PAUSED ~259h · 11e jour · J13 FINAL=39s · J14 partiel: 3s · 0 ATC · RELANCE URGENTE)**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## 🆕 CE QUI A CHANGÉ depuis run J13 18h (15/06)

1. **J13 FINAL = 39 sessions** (38 direct + 1 search — vs 36 à 18h · +3 sessions nocturnes post-18h). 0 ATC. API Shopify confirmé 16/06 8h.
2. **J14 partiel 8h = 3 sessions direct** · baseline normale · pas de spike en cours.
3. **Meta : 0€ J13 + 0€ J14 confirmés API** — 2 campagnes `PAUSED` ~259h (11e jour).
4. **Rien de nouveau** sur les 4 bloqueurs — non exécutés depuis J5 (07/06).

---

## 📊 Snapshot

| Métrique | J4 (06/06) FINAL | J5→J11 | J12 FINAL | J13 FINAL | J14 (8h) |
|---|---|---|---|---|---|
| Spend | **40,12 €** | **0 € ⛔** | **0 € ⛔** | **0 € ⛔** | **0 € ⛔** |
| CTR | 2,58 % ✅ | — | — | — | — |
| Sessions social | 9 | 0 | 0 | 0 | 0 |
| Sessions total | 21 | 5–63/j | **55 ✅** | **39 ✅** | **3 (8h)** |
| ATC | 0 | 0–2 (J8/J10 direct) | 0 | 0 | 0 |
| Commandes | 0 | 0 | 0 | 0 | 0 |

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

## Funnel cumulé J1→J13 FINAL + J14 partiel

```
Spend total      : 116,98 €  (J1→J4 · 0€ J5-J14 · API confirmé)
  dont fantômes  : ~53 €     (Ad8+Copie ~33€ + Ad2 IG ~10€ + Ad3 IG ~0,82€)
Sessions social  :     75    (J1=42 · J2=13 · J3=11 · J4=9 · J5-J14=0)
Sessions total   :    426    (J1→J13 FINAL=423 + J14 partiel 8h: 3s)
ATC social       :      1    (J3) — coût/ATC = 27,37 €
ATC direct       :      3    (J8:2 + J10:1 · trafic warm · 0 commande)
Commandes        :      0    — 0,00 € CA
Spikes pause     :    5     (J8=34s · J10=34s · J11=63s · J12=55s · J13=39s · taux ATC 5,9%→0%)
```

---

### Légende scorecard
- CTR : 🔴 <1% · 🟠 1–1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC : 🟢 <0,50 € · 🔴 >1 €
