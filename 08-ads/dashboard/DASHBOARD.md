# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-13 08h (J11 partiel · ⛔ CAMPAIGN_PAUSED ~184h · 8e jour · J10 FINAL CORRIGÉ: 34s · J11: 0s · RELANCE URGENTE)**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## 🆕 CE QUI A CHANGÉ depuis run J10 FIN (~20h 12/06)

1. **J10 FINAL CORRIGÉ = 34 sessions** (vs 12 loguées à ~20h) — API Shopify confirme 22 sessions nocturnes (20h→minuit) non capturées. 1 ATC / 1 checkout / 0 commande. Sessions total J1→J10 corrigé = **266**.
2. **J11 (13/06) 8h partiel : 0 sessions** — normal pour cette heure, campagne toujours PAUSED.
3. **Campagne toujours PAUSED ~184h** — 8e jour consécutif. API Meta confirme `effective_status: PAUSED` sur les 2 campagnes. 0€ depuis fin J4 (06/06).
4. **Les 4 bloqueurs restent non exécutés** depuis J5 (07/06) : Acquisition Test #1 non clarifié, IG Ad2 + Ad3 LP non exclus, campagne non relancée.

---

## 📊 Snapshot

| Métrique | J4 (06/06) FINAL | J5→J10 | J11 (13/06) 8h |
|---|---|---|---|
| Spend | **40,12 €** | **0 € ⛔** | **0 € ⛔** |
| CTR | 2,58 % ✅ | — | — |
| Sessions social | 9 | 0 | 0 |
| Sessions total | 21 | 5–34/j | **0** (8h partiel) |
| ATC | 0 | 0–2 (J8/J10 direct) | 0 |
| Commandes | 0 | 0 | 0 |

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
4. **Réactiver la campagne principale** — mini-learning inévitable (~100–150 impr/créa de chauffe)

---

## Funnel cumulé J1→J10 (J11 en cours)

```
Spend total      : 116,98 €  (J1→J4 · 0€ J5-J11 · API confirmé)
  dont fantômes  : ~53 €     (Ad8+Copie ~33€ + Ad2 IG ~10€ + Ad3 IG ~0,82€)
Sessions social  :     75    (J1=42 · J2=13 · J3=11 · J4=9 · J5-J11=0)
Sessions total   :    266    (J1=74 · J2=59 · J3=16 · J4=21 · J5=5 · J6=6 · J7=8 · J8=34 · J9=9 · J10=34 CORRIGÉ)
ATC social       :      1    (J3) — coût/ATC = 27,37 €
ATC direct       :      3    (J8:2 + J10:1 · trafic warm · 0 commande)
Commandes        :      0    — 0,00 € CA
```

---

### Légende scorecard
- CTR : 🔴 <1% · 🟠 1–1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC : 🟢 <0,50 € · 🔴 >1 €
