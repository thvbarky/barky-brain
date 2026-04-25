# Meta Ads — Stratégie Barky

> **Source de vérité :** [`BARKY_CERVEAU.md`](../../BARKY_CERVEAU.md) §14. Ce fichier en est l'extrait opérationnel.
>
> Le **Creative Strategy Map** complet (méthode Lorenzo Pravata) est dans [`02-marche/`](../../02-marche/) :
> - [`personas.md`](../../02-marche/personas.md) — 4 personas review-driven
> - [`thought-map.md`](../../02-marche/thought-map.md) — 5 awareness levels
> - [`angles.md`](../../02-marche/angles.md) — angles starrés par evidence
> - [`test-plan.md`](../../02-marche/test-plan.md) — top 5 tests rankés (à briefer en priorité)

---

## Mix de canaux (acquisition An 1)

| Canal | Rôle | Budget % An 1 |
|---|---|---|
| **TikTok organique build-in-public** | Construction d'audience, signal de marque | 0 € (temps fondateur) |
| **Meta Ads** (Instagram + FB) | **Acquisition primaire**, test d'angles | 50-60% |
| **Google Ads** (SEM) | Intention haute (recherche *"complément chien démangeaisons"*) | 15-20% |
| **Influence micro-véto / pet influencers** | Social proof, content rights | 10-15% |
| **SEO / contenu** | Moyen terme, montée en puissance An 2 | 5-10% |
| **Email + abandoned cart** | Rétention, relance | Inclus stack |

---

## 3 angles à tester pour le SKU hero (test validation 6 sem.)

### Angle 1 — Articulations
- **Hook** : *"Votre chien a du mal à monter les marches ?"*
- **Promesse** : *"4 semaines. 1 bouchée par jour. Mobilité retrouvée."*
- **Social proof** : *"Rejoint par 2 000 propriétaires français"*
- **CTA** : Rejoindre la waitlist

### Angle 2 — Pelage / démangeaisons
- **Hook** : *"Votre chien se gratte toute la nuit ?"*
- **Visuel fort** : before / after pelage
- **Promesse** : *"Oméga-3 + Biotine. 1 bouchée/jour. Pelage brillant en 6 semaines."*
- **CTA** : Recevez votre échantillon

### Angle 3 — Stress / anxiété
- **Hook** : *"Feux d'artifice, visite véto, orage — votre chien tremble ?"*
- **Promesse** : *"Camomille + Ashwagandha. Apaisement sans somnolence."*
- **CTA** : Tester 7 jours

> **Le SKU qui convertit au meilleur CPL gagne** — voir [`12-operations/validation-6sem.md`](../../12-operations/validation-6sem.md).

---

## Structure de campagnes

### Phase 1 — Test créatifs (Mois 1)

**Campagne TOF — Awareness/Traffic**
- Objectif : générer du trafic qualifié
- Budget : [X€/jour]
- Audience : Broad 25-50 ans FR + intérêts pet care
- Créatifs : 4-6 angles à tester simultanément

**Campagne BOF — Conversion**
- Objectif : Purchase
- Budget : [X€/jour]
- Audience : Advantage+ Shopping Campaigns (laisser Meta optimiser)
- Créatifs : les 2 meilleurs performeurs du TOF

**Campagne Retargeting**
- Audience : visiteurs site sans achat (J1 à J7)
- Budget : 20-30% du budget total
- Créatifs : social proof + urgence

---

## 6 Angles créatifs à tester en priorité

1. **Éducatif** : "Saviez-vous que les croquettes ne couvrent pas tous les besoins ?"
2. **Émotionnel** : "Votre chien vous donne tout. Donnez-lui le meilleur."
3. **Social proof** : Reviews clients + photo chien
4. **Fondateur** : Thomas présente Barky (authentique, pas scripté)
5. **Problème/Solution** : Chien fatigué → Barky → chien plein d'énergie
6. **UGC** : Owner qui montre le produit naturellement

---

## Règles de décision

- **Stopper un créatif** : CTR <1% après 500 impressions OU CPP > 2x objectif
- **Scaler** : ROAS >2,5x stable sur 7 jours consécutifs
- **Ne pas toucher** : ne jamais modifier une campagne qui performe bien

---

## Contraintes légales Meta

- Pas d'allégations médicales (refus automatique)
- Pas d'images avant/après sur la santé
- Toujours vérifier `04-legal/allegations.md` avant soumission

---

## ROAS cibles

- Mois 1 : ROAS >2x (breakeven ou légèrement positif)
- Mois 2 : ROAS >2,5x
- Mois 3 : ROAS >3x (scalable)

---

## Creative Strategy Map — méthode Lorenzo Pravata ($100M+ spend Meta)

> Source : article Lorenzo Pravata (avril 2026). Principe central : 1h de mapping avant production = 30 jours de créatifs qui ont du sens. La plupart des marques sautent cette étape, produisent dans le vide, puis se demandent pourquoi rien ne gagne après 6 semaines. On écrit des hooks sans savoir à qui on parle.

### Les 5 prompts Claude à exécuter dans l'ordre

**Prompt 1 — Fondation produit**
Extraire de la page produit :
- **Mécanisme** (pas feature) : comment le produit fonctionne biologiquement/physiquement. Ex : "17 enzymes digestives qui cassent les groupes alimentaires" > "aide à la digestion"
- **Villain** : ce que le produit bat, dans le langage EXACT de la marque (jamais inventé)
- **Claims + evidence séparés** : "90% moins ballonnés" (claim) vs "panel 28 personnes sur 14 jours" (evidence)
- **Buyer visé par la page** : à qui la page parle déjà
- **Top 10 phrases les plus citables** du site, rankées

**Prompt 2 — Personas depuis les reviews**
- Un persona = UNE raison d'acheter, JAMAIS une démographie. "Le ballonné chronique qui a abandonné les probiotiques" ≠ "femmes 35-54"
- Chaque persona ancré dans des quotes directes de reviews
- Capturer l'état émotionnel (résigné vs curieux vs pressé)
- 3-4 personas, rankés par force du signal dans les reviews

**Prompt 3 — Thought map (5 awareness levels d'Eugene Schwartz)**
Écrire la pensée interne de chaque persona à chaque étape, en première personne, brute (avec contradictions et hésitations) :
- **Unaware** : sait pas qu'il y a un problème
- **Problem Aware** : connaît le problème, pas le label de solution
- **Solution Aware** : connaît la catégorie, pas choisi de produit
- **Product Aware** : évalue cette marque
- **Most Aware** : client récurrent / convaincu

Le gap le plus large entre personas à une même étape = là où la segmentation créative a le plus de levier.

**Prompt 4 — Angles par persona × awareness level**
- Un angle = UNE phrase, entry point dans la douleur. Pas un hook, pas une headline.
- 3 à 5 angles par awareness level sur les 2 personas prioritaires
- Varier le registre émotionnel : peur, curiosité, relief, reframing contrarian
- Starrer les angles avec evidence directe dans reviews/page produit

**Prompt 5 — Ordre de test + formats**
Ranker par **confiance (evidence)**, pas par nouveauté. Format par défaut selon awareness level :

| Awareness level | Format recommandé |
|---|---|
| Unaware / Problem Aware | VSL long, podcast-style |
| Solution Aware | Expert, clinical |
| Product Aware | Testimonial, UGC |
| Most Aware | Static offer |

Top 5 tests doivent spread sur plusieurs awareness levels (pas tous au même étage du funnel). Flaguer ce qui manque comme data pour sharper l'ordre.

---

### Application pour Barky — à faire AVANT de produire les premiers créatifs

1. **Prompt 1** → coller la page produit Barky (quand LP sera prête) pour extraire mécanisme multivitamines + villain (carences cachées ? croquettes insuffisantes ?)
2. **Prompt 2** → collecter 30-50 reviews (Amazon/concurrents FR multivitamines chien) pour sortir 3-4 personas ancrés
3. **Prompt 3** → thought map sur les 2 personas prioritaires
4. **Prompt 4** → angles. Remplacer les 6 angles génériques ci-dessus par des angles issus de la méthode
5. **Prompt 5** → ordre de test ranké par evidence, avec format matché à l'awareness level

### Règles clés à retenir

- **Mécanisme > feature**. Toujours.
- **Le villain vient du langage de la marque**, jamais inventé.
- **Personas = raisons d'acheter**, pas démographies.
- **Angle ≠ hook**. L'angle est la porte, le hook est comment on l'ouvre.
- **Diversité créative sur tous les awareness levels** = condition pour scaler sur Meta en 2026.
- **Ranker par evidence, pas par créativité.**
