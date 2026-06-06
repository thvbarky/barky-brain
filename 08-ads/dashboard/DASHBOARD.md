# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée par `/barky-ads-daily` (reco seulement — aucune action sans validation Thomas).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire : [`learnings-ads.md`](learnings-ads.md)

**Dernière mise à jour : 2026-06-06 08h — J4 partiel**

---

## 🎯 Nord
Trancher : **quel angle** et **quelle destination (LP vs PDP)** convertissent le mieux — jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

---

## 🆕 CE QUI A CHANGÉ depuis le dernier run

1. **J3 vrai FINAL = 27,37 €** — le run précédent avait capturé un état partiel (12,79 €). Le CBO a continué à dépenser le soir. **Règle permanente : ne jamais tagger FINAL avant le lendemain matin.**
2. **🎯 PREMIER ATC SOCIAL** — Shopify J3 vrai : 11 sessions social · **1 ATC** · coût/ATC = 27,37 €
3. **Ad1 PDP = créa dominante** — CBO 55,8 % J3 · 56,5 % J4. CTR FB : 2,49 % → **3,78 %** ↑
4. **Ad1 LP écarté en J4** — 0 € ce matin. Probable mort naturelle CBO
5. **Ad2 IG suspect (2e jour)** — CTR 7,48 % J3 (n=107) → 5,21 % J4 (n=96). À surveiller
6. **Ad3 LP IG borderline** — CTR 1,00 % sur n=201 (J4). FB reste sain à 2,17 %

---

## 📊 Snapshot

| Métrique | J1 (03/06) | J2 (04/06) | J3 (05/06) VRAI | J4 (06/06) 8h |
|---|---|---|---|---|
| Spend | 10,32 € | 39,02 € 🚨 | **27,37 €** ✅ | 4,67 € (partiel) |
| CTR | 3,33 % | 9,84 % 🚨 | **2,34 %** ✅ | **2,55 %** ✅ |
| Sessions social | 42 | 13 | **11** | 1 (partiel) |
| ATC social | 0 | 0 | **1 🎯** | 0 (partiel) |
| Commandes | 0 | 0 | 0 | 0 |

**Cumul vrai J1+J2+J3 : 76,71 € · 1 ATC social · 0 commande**

---

## 🏆 Scorecard J4 (partiel)

| Rang | Créa | CTR FB J4 | CTR IG J4 | CBO % | Verdict |
|---|---|---|---|---|---|
| ⭐ | Ad1 PDP · cest-lage-reframe | **3,78 %** ⭐ | 1,97 % ✅ | **56,5%** | ⭐ STAR · dominant 2 jours consécutifs |
| 🟠 | Ad2 · signes-mobilite | 2,21 % ✅ | **5,21 %** ⚠️ | 22,9% ↑↑ | ⚠️ IG suspect · FB sain |
| ⚠️ | Ad3 LP · 5-problemes | 2,17 % ✅ | **1,00 %** 🔴 | 20,6% | ⚠️ IG sous seuil sur n=201 |
| 📉 | Ad1 LP · cest-lage-reframe | — | — | **0%** | Écarté par CBO |
| 🚨 | Ad8 Video | PAUSED | — | 0% | Permanent — ne jamais réactiver |

---

## ⚠️ Alertes actives

- **Ad3 LP IG** : CTR 1,00 % (n=201) — surveiller run 12h. Si < 1 % sur n > 400 → exclure IG
- **Ad2 IG** : CTR 5-7 % sur 2 jours — surveiller J4 final. Si > 5 % sur n > 200 → exclure IG
- **Coût/ATC social = 27,37 €** (cible ≤ 8-10 €) — volume insuffisant pour trancher LP vs PDP

---

## Funnel cumulé vrai J1+J2+J3

```
Spend total     : 76,71 €  (10,32 + 39,02 + 27,37)
  dont fantômes : ~33,20 € (Ad8+Copie J2)
  dont clean    : ~43,51 €
Sessions social :     66   (J1=42 · J2=13 · J3=11)
Sessions total  :    149   (J1=74 · J2=59 · J3=16)
ATC social      :      1   (J3) — coût/ATC = 27,37 €
Commandes       :      0   — 0,00 € CA
```

---

### Légende scorecard
- CTR : 🔴 <1% · 🟠 1–1,5% · 🟢 >1,5% · ⭐ >2,5% — **toujours splitté par placement**
- CPC : 🟢 <0,50 € · 🔴 >1 €
