# Winning Statics — Swipe File

> **Rôle.** Bibliothèque de statics Meta gagnantes (toutes niches) qui servent de référence pour les créas Barky. **Pas de génération ici** — c'est le dossier des inputs, pas des outputs.
>
> **Outputs Barky** → `08-ads/statics/YYYY-MM-DD/`
> **Mood / inspiration générale (non-Meta)** → `08-ads/references/moodboards/`
> **Brand kits concurrents** → `08-ads/references/brands/`

---

## Convention de nommage fichier

```
YYYYMMDD_marque_format_hook.{jpg|png}
```

| Élément | Règles | Exemples |
|---|---|---|
| `YYYYMMDD` | Date de capture (pas de la création de l'ad) | `20260513` |
| `marque` | slug kebab-case, minuscules, sans accents | `ag1`, `dog-is-human`, `huel`, `besti` |
| `format` | `1080x1080` · `1080x1350` · `1080x1920` · `1200x628` | `1080x1350` |
| `hook` | slug kebab-case du type de hook dominant | `before-after`, `founder-pov`, `ingredient-breakdown` |

**Exemples valides** :
- `20260513_ag1_1080x1350_before-after.jpg`
- `20260513_dog-is-human_1080x1080_founder-pov.png`
- `20260513_huel_1080x1350_problem-solution.jpg`

⚠️ Un fichier = une ad unique. Si la même marque a plusieurs variations sur **le même hook + même format**, ajouter un suffixe `-NN` (deux chiffres) :

- `20260513_exode_1080x1350_promo-01.jpg`
- `20260513_exode_1080x1350_promo-02.jpg`
- `20260513_exode_1080x1350_promo-03.jpg`

L'ordre des `-NN` n'a pas de signification (premier dépôt = -01). Les notes différenciantes vivent dans la colonne "Why it works" de Notion, pas dans le filename.

---

## Taxonomie hooks (multi-select Notion)

| Slug | Description courte |
|---|---|
| `before-after` | Transformation visible (état avant vs après) |
| `product-hero` | Packshot dominant, environnement minimal |
| `testimonial` | Avis client / review screenshot |
| `problem-solution` | Problème nommé → produit comme réponse |
| `founder-pov` | Fondateur face caméra, narratif vérité |
| `social-proof` | Chiffres ventes / followers / médias |
| `ingredient-breakdown` | Composition / actifs mis en avant |
| `comparison` | Vs concurrent ou vs alternative |
| `ugc-style` | Faux UGC, photo iPhone, lo-fi authentique |
| `routine` | Geste quotidien, rituel, séquence |
| `science-claim` | Étude / pourcentage / data |
| `promo` | Discount / bundle / upsell / cart push — le hook EST l'offre |
| `product-launch` | Annonce nouveau produit / nouvelle version / nouvelle formule |

Si un hook ne rentre dans aucune case → ajouter ici avant de l'utiliser.

---

## Niches à scraper en priorité (par ordre de proximité Barky)

1. **Compléments humains DTC** — AG1, Ritual, Seed, Huel, Symprove (modèle abonnement daily = parent direct du positionnement Barky)
2. **Petfood DTC scale** — Dog is Human, Zesty Paws, The Farmer's Dog, Butternut Box, UPD, Japhy, Elmut, Besti, Balto, Woofilab
3. **Wellness adulte** — Hims, Hers, Roman, Kin Euphorics, Sunday Riley
4. **Beauty Clean** — Aesop, Le Labo, Saie, Tower 28
5. **Skincare/santé routine** — Curology, Nurish by Nature Made

⚠️ **À éviter** : pet industry GMS (Pedigree, Royal Canin, Pro Plan), animalerie digitale grand public, marques cute / pastel saturé. Ces réfs orientent vers ce que Barky **ne veut pas** être.

---

## Workflow

```
1. Scrape sur TrendTrack / Meta Ad Library
2. Renomme selon convention ci-dessus
3. Dépose le fichier dans ce dossier
4. Crée la row Notion correspondante (DB "Winning Statics")
5. Quand prêt à adapter en créa Barky → mets le status "À adapter"
6. Session de génération Higgsfield → output dans 08-ads/statics/YYYY-MM-DD/
7. Une fois adaptée → attache la version Barky à la row Notion (champ "Adapted version")
```

---

## Pas de DB Notion pour les winners

Les winners restent **disk-only**. La DB Notion track uniquement les créas **Barky en production** (cf. `08-ads/dashboard-creatives.md` une fois créé).

Le fichier `_winners-metadata.csv` à côté contient les notes "why it works" pour chaque winner, à consulter offline quand on brief Higgsfield. Pas à importer dans Notion.

Pour référencer un winner depuis une row Barky Creatives → coller le slug du fichier (ex : `20260513_exode_1080x1350_problem-solution`) dans le champ `Référence winner`.

---

## Anti-patterns à ne pas mettre ici

- ❌ Statics Barky déjà générées (elles vont dans `08-ads/statics/`)
- ❌ Moodboards Pinterest / refs photo sans contexte ad (vont dans `08-ads/references/moodboards/`)
- ❌ Logos / brand kits concurrents (vont dans `08-ads/references/brands/`)
- ❌ Vidéos (ce dossier est statics uniquement — vidéo plus tard, dossier dédié)
- ❌ Captures de timeline sans isoler une ad précise

---

*Convention posée le 2026-05-13. À mettre à jour si la taxonomie hooks ou la liste niches évolue.*
