# Plan B — Pivot Felis (compléments chat)

> **Source de vérité :** [`BARKY_CERVEAU.md`](../BARKY_CERVEAU.md) §18. Ce fichier en est l'extrait opérationnel.
>
> ⚠️ **À activer uniquement si Barky NO-GO** au S6 du plan validation. Voir [`12-operations/validation-6sem.md`](../12-operations/validation-6sem.md).

---

## Pourquoi les chats ?

- **France = n°1 européen en chats** (21% de part dans la population animale vs 11,4% chiens)
- **Marché chat = 1,91 Md€** en valeur 2023 contre 896 M€ chien → **2× plus gros**
- **Quasi toutes les DNVB premium** (Elmut, UPD, Edgar & Cooper) ont lancé sur le chien d'abord → **segment chat structurellement sous-servi**
- Pathologies fréquentes : obésité, problèmes rénaux (IRC), urinaire, stérilisation, arthrose sénior — beaucoup liées à l'alimentation industrielle inadaptée

---

## Positionnement Felis

DNVB **compléments chat avec angle vétérinaire fort**.

### SKUs prioritaires

1. **Urinaire / rénal** — pathologie #1 chez chat stérilisé d'intérieur
2. **Stress / anxiété** — cystites idiopathiques déclenchées par stress
3. **Articulations senior** — arthrose du chat vieillissant

### Pricing

- **25-35 €/mois** abonnement
- LTV potentiel **très élevé** (chat senior = arthrose + IRC chroniques sur plusieurs années)

---

## Cible Felis

- **30-55 ans** (la pathologie urinaire démarre tôt)
- Propriétaire de chat(s) **stérilisé(s)**, souvent d'intérieur
- Sensible au véto mais **lassée des régimes thérapeutiques rayons**
- Disposition à payer 25-35 €/mois

---

## Plan validation Felis (8 semaines, 600-900 €)

### Semaines 1-2 — Préparation
- 2 SKU hero (urinaire + calm)
- 2 landing pages

### Semaines 3-6 — Test
- **Meta Ads 50 €/j × 10 jours = 500 €**
- Compte TikTok build-in-public, **3 posts/sem**

### Semaines 7-8 — Pré-commande réelle
- CB Stripe (vraie pré-vente, pas juste email)

---

## Critère GO Felis

> **40+ pré-commandes payées sur 2 semaines** → GO Felis

---

## Réutilisation de la stack Barky (80% transférable)

| Composant | Réutilisable | Notes |
|---|---|---|
| Landing builder (Carrd / Framer) | ✅ | Juste changer copy + visuels |
| Stripe + Shopify | ✅ | Reconfigurer produits |
| Logique Meta Ads + TikTok | ✅ | Adapter ciblage chat |
| Identité visuelle | 🟡 | Nouvelle palette + logo, mais même DA premium |
| Voice of brand | ✅ | Même registre adulte/warm |
| Comité scientifique | 🟡 | Trouver vétos chat plutôt que chien |
| Process validation lean | ✅ | Méthode identique |
| Fournisseur OEM | 🟡 | Trouver un OEM compléments chat |

→ **Tu ne pars jamais de zéro.** C'est précisément la valeur du Plan B.

---

## Architecture de décision (rappel)

```
Test Barky S1-S6 (260-400 €)
    │
    ├─ ✅ GO Barky → commande private label Barky
    │
    └─ ❌ NO-GO Barky
        │
        └─ Pivot Felis S7-S14 (600-900 €)
                │
                ├─ ✅ GO Felis → lancement Felis M4+
                │
                └─ ❌ NO-GO Felis
                        │
                        └─ Fresh Patch ou pause stratégique
```

---

## Ce que ce plan B n'est PAS

- ❌ **Ce n'est pas une excuse pour ne pas se battre sur Barky.** Le Plan B existe pour réduire le risque, pas pour faciliter l'abandon.
- ❌ **Ce n'est pas un Plan A déguisé.** Si tu te surprends à préférer Felis à Barky avant le test, c'est que Barky n'est plus le bon véhicule pour toi (cf. [`anti_patterns.md` core docs Thomas](../) — syndrome objet brillant).
- ❌ **Ce n'est pas activable avant les résultats du test S1-S6.** Aucune ressource Felis avant la décision GO/NO-GO Barky.

---

*Dernière mise à jour : 25 avril 2026*
