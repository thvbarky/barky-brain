# Log des décisions — Barky

> **Source de vérité :** [`BARKY_CERVEAU.md`](../BARKY_CERVEAU.md) §17. Ce fichier en est l'extrait opérationnel + log permanent.

Chaque décision importante loggée ici avec contexte et raisonnement.

---

## ✅ Décisions tranchées (actées)

| # | Décision | Date | Source/raison |
|---|---|---|---|
| 1 | **Format** : friandises fonctionnelles | Avril 2026 | > petfood classique et > multivitamines généraliste (trigger d'achat clair, marge supérieure, viralité TikTok) |
| 2 | **Voie de production** : private label (voie C, 8-20 k€) | Avril 2026 | Capital limité < 20 k€, time-to-market 6-10 sem, MOQ acceptable |
| 3 | **Identité visuelle** : orange `#FF5500` + navy `#0D1B5E` | Avril 2026 | Retour après exploration alternative bleu pastel + brun ambré |
| 4 | **Nom** : Barky | Avril 2026 | Court, prononçable. Registre cute compensé par tagline + DA |
| 5 | **Tagline** : *"Nourri comme il le mérite."* | Avril 2026 | Tire le nom vers le premium |
| 6 | **Positionnement produit** : problème-spécifique > multivitamines | Avril 2026 | Trigger clair, légitimité scientifique, justification prix |
| 7 | **Canaux validation** : Meta Ads + TikTok organique build-in-public | Avril 2026 | Profil fondateur narratif fort, capital-light |
| 8 | **Géographie initiale** : France métropolitaine DTC | Avril 2026 | Marché 6,3 Md€, 9,5M chiens, segment DTC sous-servi |
| 9 | **Modèle commercial** : abonnement mensuel (+ one-off + trimestriel) | Avril 2026 | LTV/CAC SaaS-like, payback < 3 mois |
| 10 | **Repo barky-brain créé** | 2026-04-24 | Source de vérité versionnée |
| 11 | **Creative Strategy Map exécuté** (méthode Pravata) | 2026-04-24 | 5 prompts complets, 4 personas extraits, 5 tests rankés |
| 12 | **BARKY_CERVEAU.md intégré comme master du repo** | 2026-04-25 | Source de vérité unique, chargée dans CLAUDE.md |

---

## 🟡 Décisions ouvertes (à trancher)

| # | Décision | Deadline | Critère |
|---|---|---|---|
| A | **SKU hero** — démangeaisons / pelage OR anti-stress OR articulations | Post-test Meta Ads (S3-S5) | Le SKU avec le meilleur CPL gagne |
| B | **GO / NO-GO Barky** | Fin S6 du test validation | Voir [`validation-6sem.md`](./validation-6sem.md) |
| C | **Comité scientifique vétérinaire** — combien de vétos au lancement | Avant brief packaging final | 3 minimum réaliste / 6 ambitieux |
| D | **Fournisseur OEM** | Avant commande MOQ | Voir [`05-supply-chain/private-label.md`](../05-supply-chain/private-label.md) |
| E | **Pivot Felis** si Barky NO-GO | Conditionnel S6 | Voir [`14-knowledge/plan-b-felis.md`](../14-knowledge/plan-b-felis.md) |
| F | **Projet Fresh Patch** | — | Lancé, mis en pause, ou archivé ? |
| G | **Code lab SKU** — VK-01 / CF-01 / Barky Core | Avant dépôt INPI | Décision design + dépôt classe 31, 5, 35 |
| H | **Offre découverte** | Avant ouverture Shopify | Kit 7 jours OR -20% 1er mois OR rien |

---

## Architecture de décision (rappel)

```
Semaine 1-6 → Test Barky (260-400 €)
               │
               ├─ ✅ GO (waitlist>150, CPL<3€, 20+ pré-ventes)
               │   └─ Commande private label
               │       └─ M3 — lancement réel
               │
               └─ ❌ NO-GO
                   └─ Pivot Felis (compléments chat DTC)
                        │
                        ├─ Test S7-S14 (600-900 €)
                        │   ├─ ✅ GO → Felis M4+
                        │   └─ ❌ NO-GO → Fresh Patch ou pause
                        └─
```

---

## Log historique

### Avril 2026 — Lancement du projet
- **Décision** : Lancement de Barky le 28 avril 2026
- **Qui** : Thomas (THV), Elias, Thomas Lebert
- **Contexte** : Période essai 3 mois — friandises fonctionnelles chiens DTC
- **Résultat attendu** : Valider le modèle en 3 mois, atteindre 250+ commandes cumulées

### 24 avril 2026 — Repo barky-brain créé
- **Décision** : versionner le second cerveau Barky en repo GitHub privé
- **Why** : centraliser la connaissance, historique des décisions, collaboration future
- **URL** : github.com/thvbarky/barky-brain

### 24 avril 2026 — Creative Strategy Map (méthode Pravata)
- **Décision** : appliquer les 5 prompts Lorenzo Pravata avant production créative
- **Output** : 4 personas review-driven, thought map 5 awareness levels, angles starrés, top 5 tests rankés
- **Test #1 retenu** : *"'C'est l'âge' : la fausse raison qui empêche la plupart des maîtres d'aider leur chien"* (P1 × Problem Aware × UGC founder)

### 25 avril 2026 — Intégration BARKY_CERVEAU.md dans le repo
- **Décision** : faire du document complet la source de vérité unique du repo
- **Why** : éviter la dispersion de connaissance, charger automatiquement dans toute conversation Claude
- **Implémentation** : `BARKY_CERVEAU.md` à la racine + import via `CLAUDE.md` du repo + extraits opérationnels distribués dans les 15 dossiers thématiques

---

## Template de décision

```markdown
### [Date] — [Titre]
- **Décision** :
- **Qui** :
- **Contexte** :
- **Options considérées** :
- **Raisonnement** :
- **Résultat attendu** :
- **Résultat réel** : (à remplir après)
```

---

*Dernière mise à jour : 25 avril 2026*
