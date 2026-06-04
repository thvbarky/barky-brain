# 📊 Barky Ads — Tableau de bord

> Vue humaine régénérée chaque jour par `/barky-ads-daily` (routine Cowork 12h, **reco seulement**).
> Data brute : [`ads-daily.csv`](ads-daily.csv) · Mémoire décisions : [`learnings-ads.md`](learnings-ads.md) · Plan : [`../../12-operations/2026-06-04-plan-3jours-signal-ads.md`](../../12-operations/2026-06-04-plan-3jours-signal-ads.md)

**Dernière mise à jour : 2026-06-04 (seed manuel — 1re exécution auto demain 12h)**

---

## 🎯 Nord
Trancher : **quel angle** (symptôme) et **quelle destination** (LP vs PDP) convertissent le mieux. Jugé sur le **coût par AddToCart** (sessions Shopify = vérité).

## Snapshot — 2026-06-04 (J1)

| Métrique | Valeur | Lecture |
|---|---|---|
| Spend | ~28 € | — |
| Impressions | 7 979 | — |
| Link clicks (Meta) | 534 | ⚠️ gonflés |
| Vues page (Meta) | ~350 | ❌ à ignorer comme dénominateur |
| **Sessions Shopify** | **14** | ✅ la seule vérité |
| AddToCart | — | à remonter demain |
| Commandes | 0 | J1, normal |

## 🚨 Alerte du jour
**Placement Facebook = clics fantômes.** CTR **12,4 % @ 0,03 €** (529 clics) vs Instagram **2,4 %** (sain). → demain : isoler Feed vs Reels, exclure le coupable.

## 🏆 Classement angles
*(en attente de la data par créa — dispo dès le 1er pull auto)*

## ⚔️ Duel LP vs PDP
*(en attente — métrique = coût par AddToCart sur sessions Shopify)*

## ✅ Décisions recommandées (2026-06-04)
1. **Ne rien couper aujourd'hui** — learning phase, <1000 impr/créa pour la plupart. On laisse respirer.
2. **Préparer** l'isolation du placement Facebook (Reels suspecté) pour demain.
3. Prochain point réel = **demain 12h** (1er pull auto) : classement angles + duel LP/PDP.

---

### Légende seuils (scorecard)
- CTR : 🔴 <1% (après ≥1000 impr) · 🟢 >1,5% · ⭐ >2,5% — **mais toujours splitté par placement**
- CPC : 🟢 <0,50 € · 🔴 >1 €
- Coût/ATC : juge du duel LP vs PDP · <8-10 € = encourageant (produit ~28 €)
