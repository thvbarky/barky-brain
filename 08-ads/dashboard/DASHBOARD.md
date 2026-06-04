# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée chaque jour par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-04 18:00 (pull API confirmé)**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## ✅ PIVOT J2→J3 — Ad8 PAUSED, premier ATC en vue

| Métrique | J1 (03/06) complet | J2 (04/06) run 18h |
|---|---|---|
| Spend | 10,32 € | **33,58 €** (Ad8 a tourné jusqu'au soir) |
| Impressions | 3 635 | 9 405 |
| Link clicks Meta | 96 | 662 |
| **Sessions Shopify social** | **42** ✅ | **12** |
| **Sessions Shopify total** | **74** | **56** |
| **ATC social** | **0** | **0** |
| **ATC tous canaux** | 1 | **3** ⭐ |
| Coût / session social | **0,25 €** ✅ | 2,80 € |

**✅ Ad8 + Copie PAUSED (status API confirmé).** J3 (05/06) = premier jour propre. 3 ATC non-social aujourd'hui : la page convertit pour le trafic qualifié.

---

## Répartition budget J2 · run 18h

| Créa | Spend | % budget | CTR FB | CTR IG | Status | Signal |
|---|---|---|---|---|---|---|
| Ad8 Video races-poids | **28,91 €** | 86,1% | **12,80%** | 4,00% | **PAUSED** ✅ | 🔴 fantôme FB |
| Ad8 Copie | 3,62 € | 10,8% | **12,29%** | — | **PAUSED** ✅ | 🔴 fantôme FB |
| Ad3 Typo 5-problemes LP | 0,79 € | 2,4% | 4,00% (n=75) | **2,38%** (n=210) | ACTIVE | ✅ propre |
| Ad1 LP | 0,07 € | 0,2% | ⚠️ 15,38% (n=13) | 0% (n=5) | ACTIVE | ❓ surveiller |
| Autres clean ads | 0,11 € | 0,3% | — | — | ACTIVE | < 20 impr |

---

## 🏆 Classement angles (J1+J2 · base fiable)

| Rang | Angle | Créa | CTR IG | CTR FB | Verdict |
|---|---|---|---|---|---|
| ⭐ 1 | 5-problemes-1-formule | Ad3 Typo LP | **2,43%** (J1 · n=1975) | 3,01-4,00% | ✅ référence absolue |
| ⚠️ 2 | signes-mobilite-ete | Ad2 ProductHero | 8,33% (n=24) | 1,50% | prometeur · n trop faible |
| ❓ 3 | cest-lage-reframe LP | Ad1 Lifestyle LP | 0% (n=5) | ⚠️ 15,38% (n=13) | suspect FB · à surveiller |
| 🔴 ✗ | races-poids (vidéo) | Ad8 Video | 4,00% (n=25) | **12,77%** | fantômes FB · **PAUSED** |

---

## Funnel cumulé J1+J2

```
Spend total         : 43,90 €  (J1: 10,32 € + J2: 33,58 €)
  dont fantômes     : ~42,50 € (Ad8+Copie J1+J2)
  dont clean        :   1,40 € (Ad3 + autres)
Link clicks Meta    :    758   (dont ~97% fantômes J2)
Sessions Shopify    :     54   (social : J1=42 · J2=12)
Sessions total      :    130   (J1=74 · J2=56)
ATC social          :      0
ATC tous canaux     :      4   (J1=1 · J2=3) ⭐
Commandes           :      0   — 0,00 € CA ads
```

---

## ✅ Décisions recommandées (2026-06-04 18h)

### ✅ FAIT — Ad8 + Copie PAUSED
**Status API : PAUSED / delivery off sur les 2 créas.** J3 opère sans pollution fantôme.

---

### ⚠️ WATCH — Ad1 Lifestyle LP · Facebook
CTR FB = 15,38% sur **n=13 impr** : trop petit pour conclure mais pattern Ad8. Au run 8h du 05/06 : si FB CTR reste >10% avec n>100 → **pause recommandée**.

---

### 🎯 J3 (05/06) — vérif redistribution CBO
Ad3 Typo LP doit recevoir ≥10 €/j. Si CBO alloue ailleurs → signaler au run 8h.

---

### ⚔️ Duel LP vs PDP : patience
0 ATC social des 2 côtés. Verdict J4-J5 avec trafic propre.

---

### Légende seuils scorecard
- CTR IG : 🔴 <1% (≥1 000 impr) · 🟠 1-1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC lien : 🟢 <0,50 € · 🔴 >1 €
- Coût/ATC : <8-10 € encourageant sur produit 28 €
