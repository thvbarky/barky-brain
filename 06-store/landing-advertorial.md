# Landing Advertorial — Pattern haute conversion pour Barky

> **Source :** analyse de 2 landings Lumin Theme (US beauty) — `beauty.lumintheme.com/pages/listicle` et `/pages/listicle-1`. Ce sont des **advertorials** (article éditorial déguisé en landing) qui convertissent très fort sur cold traffic Meta/TikTok. À utiliser pour la landing Barky en cold acquisition.
>
> **Pivot acté le 26 avril 2026** — Barky abandonne l'approche problème-spécifique (3 angles testés en parallèle : pelage / articulations / stress) au profit d'un **SKU unique multivitaminé daily** (modèle Dog is Human DM-01). Conséquence pour ce playbook : **un seul angle, un seul advertorial** — pas trois. Voir [`BARKY_CERVEAU.md §3.2`](../BARKY_CERVEAU.md) et [`03-produit/skus.md`](../03-produit/skus.md).
>
> **Implémentation v1 :** [`landing-pages/multivitamin-v1.html`](landing-pages/multivitamin-v1.html) — page autoportante, advertorial éditorial multivitaminé, prête à importer dans Shopify (bloc `BARKY_LANDING_START` / `BARKY_LANDING_END`).
>
> **Liens analysés :**
> - https://beauty.lumintheme.com/pages/listicle (PDRN Pink Peptide Serum)
> - https://beauty.lumintheme.com/pages/listicle-1 (Booster Pro LED)
>
> **À combiner avec :** [`conversion.md`](conversion.md) (page produit Shopify classique) — l'advertorial est la **page d'atterrissage Meta Ads**, pas la fiche produit. Elle redirige vers la fiche produit pour le checkout.

---

## 1. C'est quoi un advertorial et pourquoi c'est puissant

**Définition :** une page qui ressemble à un article éditorial (blog post type "Top Dermatologues Révèlent…") mais qui est en réalité une landing avec CTA disséminés. Le visiteur ne se sent pas en train de lire une pub — il lit un contenu, et finit par cliquer.

**Pourquoi ça marche en cold traffic :**
- Lève la garde du visiteur (registre éditorial > registre commercial)
- Permet 1 500–2 500 mots de copy → temps long sur page → meilleur Pixel Meta
- Pré-vend le produit avant même la page produit → conversion 2–3x supérieure
- Le format "secret que les vétos ne te disent pas" exploite la curiosity gap

**Quand l'utiliser pour Barky :**
- Cold traffic Meta Ads sur l'angle multivitaminé daily (un seul angle suite au pivot 26/04/2026)
- TikTok organique → bio link
- Pas pour le retargeting (là on envoie sur fiche produit directe)

---

## 2. Plan de page reproductible pour Barky (16 sections)

| # | Section | Rôle | Adaptation Barky |
|---|---------|------|------------------|
| 1 | Mini-cart sticky en haut | Réassurance prix | "Livraison offerte · Garantie 60 j · Sans engagement" |
| 2 | Header éditorial | Casser le frame "pub" | Logo Barky discret + "CONSEILS SANTÉ CHIEN" + badge "Vu sur TikTok" |
| 3 | Breadcrumb | SEO + autorité | Accueil › Santé canine › Démangeaisons |
| 4 | **Headline éditorial** + byline | Hook curiosité | "Ce que les croquettes du commerce ne couvrent jamais — et pourquoi une nouvelle génération de vétérinaires français recommande désormais une bouchée multivitaminée par jour" · *Par Dr. [Vétérinaire comité] ✓ · 26 avril 2026* |
| 5 | Intro narrative (3 paragraphes) | Empathie problème | Validation frustration : "Soyons honnêtes. La plupart des compléments pour chien promettent des miracles. 99% n'agissent qu'en surface." |
| 6 | Transition mystère | Curiosity gap | "Voici ce que les vétos ne disent pas toujours en consultation…" |
| 7 | Star rating intégré | Social proof éditorial | "4,9/5 · 2 800+ avis" + 5⭐ (utiliser nos chiffres réels) |
| 8 | Section "Qu'est-ce que c'est ?" | Éducation produit | Explication des 12 actifs daily (Glucosamine, MSM, oméga-3, vitamines, probiotiques) avec image |
| 9 | **Présentation produit** | Reveal du produit | "Voici Barky Daily — une bouchée multivitaminée quotidienne formulée par 4 vétérinaires français" |
| 10 | Bullets bénéfices (5) | Promesse claire | Peau & pelage · Mobilité · Digestion · Défenses · Cœur — toujours en verbe d'action conforme DGCCRF (soutient / contribue / favorise) |
| 11 | Histoire / crédibilité scientifique | Légitimité | "Ce que les croquettes ne couvrent jamais" — les actifs viennent de la nutrition vétérinaire pro, comparaison directe avec le rayon fragmenté |
| 12 | **CTA principal** + 30 % OFF | Action 1 | "Vérifier la disponibilité ▶" + badge "-30% premier mois" + "Garantie 60 jours" |
| 13 | "Pour qui c'est fait ?" | Segmentation | Bullets par profil de chien (adulte / senior / chien BARF / chien aux croquettes industrielles / multi-chien) + posologie par poids |
| 14 | Carrousel témoignages | Social proof affective | 3 avis détaillés avec photo du chien + photo du propriétaire + ⭐⭐⭐⭐⭐ — choisir un témoignage par profil clé (senior, ration ménagère, multi-actif) |
| 15 | Bloc statistiques (3 chiffres) | Social proof rationnel | "87% des propriétaires constatent un changement en moins de 6 semaines · 4,9/5 sur 2 800+ avis · 12 actifs documentés · Étude interne Barky 2026, 200 chiens" |
| 16 | **CTA secondaire** + countdown | Urgence | "Profiter de −15% aujourd'hui ▶" + timer 24h glissantes (dynamique localStorage, pas faux) |
| 17 | Reviews agrégées + breakdown | Volume social proof | 4,8/5 · 88% 5⭐ · 10% 4⭐ · etc. + 6–8 commentaires courts |
| 18 | **CTA final** | Action 3 | Identique à CTA 1, ramène vers fiche produit |
| 19 | Footer disclaimers | Légal | Mention "Aliment complémentaire pour chiens" + DGCCRF + entité juridique |

**Règle :** 3 CTA minimum, espacés (~25%, ~60%, ~95% de la page). Tous pointent vers la **même fiche produit Shopify**.

---

## 3. Copy patterns à adapter — par section

### Hook headline (le plus important)

**Pattern Lumin :** *"Why Top Dermatologists Are Calling PDRN The Future of Anti-Aging — And How You Can Use It at Home"*

**Adaptation Barky (angle unique multivitaminé daily)**

> *"Ce que les croquettes du commerce ne couvrent jamais — et pourquoi une nouvelle génération de vétérinaires français recommande désormais une bouchée multivitaminée par jour"*

**Variantes A/B testables (même angle, même promesse)**
- *"Pourquoi des milliers de propriétaires français remplacent sept flacons par une seule bouchée — et ce que les vétérinaires en disent"*
- *"Le format qui a transformé la nutrition humaine arrive enfin pour les chiens — voici ce que les vétérinaires français en pensent"*

> **Règle pivot 26/04/2026** : on ne teste plus l'angle (pelage / articulations / stress), on teste **les variantes du même angle multivitaminé daily**. Le SKU est tranché — la copie cherche le meilleur framing.

### Intro narrative (3 paragraphes type)

```
Soyons honnêtes.

La plupart des compléments pour chien promettent des miracles. 99% d'entre eux
agissent à peine en surface. Les pâtes appétentes masquent. Les comprimés sont
recrachés. Les régimes véto coûtent 80 €/mois.

Pendant ce temps, dans votre placard, l'armoire à compléments grossit chaque
mois. Une boîte d'huile de saumon. Une de glucosamine. Un sachet de probiotiques.
Sept produits, sept marques, sept oublis quotidiens.

Et si on pouvait simplement faire en sorte que le corps de votre chien
fonctionne mieux ? Pas masquer, pas couvrir — soutenir, restaurer, renforcer.
Une fois par jour. Avec ce que les vétérinaires nutritionnistes ont identifié
comme l'essentiel — et rien de plus.
```

### Transition mystère (curiosity gap)

> *"Voici ce que les vétérinaires ne disent pas toujours en consultation, parce qu'ils n'ont ni le temps ni la mission commerciale de le faire : les croquettes sèches du commerce sont conçues pour répondre aux besoins minimaux d'un chien moyen. Pas pour optimiser sa peau, son système digestif, ses articulations, ses défenses ou son cœur. Elles sont tenues à un référentiel — la norme FEDIAF — qui définit un plancher, pas un plafond."*

### CTA wording (3 niveaux d'urgence)

| Niveau | Wording FR | Quand l'utiliser |
|---|---|---|
| Neutre | `Vérifier la disponibilité ▶` | CTA 1 (post-éducation) |
| Offre | `Profiter de -30% aujourd'hui ▶` | CTA 2 (post-social proof) |
| Urgence | `✨ Réserver mon pot — stock limité ▶` | CTA final (post-countdown) |

**À éviter :** "Acheter maintenant" (trop commercial, casse le frame éditorial). On reste dans le registre "vérifier", "découvrir", "réserver".

### Bullets bénéfices (rester DGCCRF-compliant)

Les **5 bénéfices revendiqués du SKU multivitaminé daily** :

```
✓ Peau & pelage      — Contribue à un pelage brillant et sain
✓ Mobilité           — Soutient la mobilité articulaire au quotidien
✓ Digestion          — Favorise un microbiote intestinal équilibré
✓ Défenses naturelles — Soutient les défenses naturelles du chien
✓ Vitalité cardiaque — Contribue au bon fonctionnement cardiaque
```

**Vocabulaire interdit :** *traite, guérit, prévient, soigne, élimine.* Voir `04-legal/allegations.md` et `BARKY_CERVEAU.md §8.5`.

---

## 4. Éléments de social proof à constituer avant le lancement

| Élément | Cible minimale | Comment l'obtenir |
|---|---|---|
| Avis ⭐ avec photo | **20+** | Bêta-testeurs (groupe Facebook + amis) — voir checklist `BARKY_CERVEAU.md §19.6` |
| Note moyenne | 4,7/5 minimum | Modérer — un 1⭐ tue la page |
| Volume reviews affiché | "1 500+ avis" | Cumul reviews + commentaires UGC (légitime) |
| Statistiques internes | 3 chiffres | Étude interne sur les bêta-testeurs (200 chiens cible) |
| Citations vétérinaires | 2–3 | Comité scientifique Barky |
| Logos médias | 3–5 | Si presse/blog couvre le lancement (Konbini Animaux, Wamiz, Atelier Canin) |
| Before/after pelage | 5+ paires | Visuel fort sur l'argument peau/pelage du multivitaminé daily — autorisation écrite obligatoire |

---

## 5. Pièges à éviter (vus sur les pages Lumin)

1. **❌ Pas de duplication de bullets** — la page PDRN répète "Fade hyperpigmentation" deux fois. Relecture obligatoire.
2. **❌ Pas de countdown faux** — le timer Lumin affiche 7h59m statique. Si on utilise un countdown, qu'il soit dynamique et lié au panier (Shopify app type Hextom, Ultimate Sales Boost).
3. **❌ Pas de Lorem Ipsum oublié** — un avis Lumin contient encore du lorem ipsum. Honteux.
4. **❌ Pas de noms d'auteur fake** — "Maria Doe ✓" sans page bio derrière = ça pue. Si on cite un véto, **vraie page bio + vraie photo + vrai diplôme**.
5. **❌ Pas de claims US transposés** — "FDA-Registered", "NASC-Preferred", "Made in Vermont" = aucune valeur en France et risque DGCCRF. Voir `BARKY_CERVEAU.md §8.5`.
6. **❌ Pas d'incohérence produit** — la page Booster Pro mélange copy "PDRN Serum" et photo "Booster Pro LED". Une page = un SKU.
7. **❌ Pas de % de réduction qui se contredisent** — Lumin annonce 30% puis 40% puis 60% sur la même page. Choisir un seul taux et le tenir partout.

---

## 6. Stack technique pour construire la page

| Brique | Recommandation | Coût |
|---|---|---|
| **Builder** | Shopify (template article enrichi) ou app Replo / GemPages | 0–30 €/mois |
| **Countdown** | App Hextom (countdown lié au panier, pas factice) | Gratuit |
| **Reviews widget** | Loox ou Judge.me (photos clients) | 10–35 €/mois |
| **Sticky cart** | Native Shopify ou app Ultimate Sales Boost | Inclus |
| **Pixel & tracking** | Meta Pixel + GA4 + Triple Whale (si budget Ads > 5 k€/mois) | 0–129 €/mois |
| **A/B test** | Shopify Audiences ou Intelligems | À partir de 50 €/mois |

---

## 7. Checklist de lancement advertorial Barky

- [ ] 1 seul advertorial multivitaminé daily (pivot 26/04/2026 — un seul angle, une seule page)
- [ ] Headline éditorial validé (pas de wording commercial)
- [ ] Byline avec un véto réel du comité (photo + bio + RPPS si applicable)
- [ ] Intro 3 paragraphes en mode "honnêteté + frustration + question ouverte"
- [ ] CTA 1 placé après ~30% du scroll (mobile)
- [ ] CTA 2 placé après témoignages (~65%)
- [ ] CTA 3 placé après reviews agrégées (~95%)
- [ ] 20+ reviews avec photos (bêta-testeurs)
- [ ] 3 statistiques internes sourcées ("Étude interne Barky 2026, 200 chiens")
- [ ] Mentions DGCCRF en footer + "Aliment complémentaire pour chiens"
- [ ] Garantie 60 jours visible 3x sur la page
- [ ] Livraison offerte affichée en sticky top
- [ ] Pixel Meta + événements custom (scroll 50%, scroll 90%, click CTA)
- [ ] Test mobile prioritaire (80%+ du trafic Meta = mobile)
- [ ] Vitesse < 3 s (compresser images, lazy load)

---

## 8. KPIs cibles d'une page advertorial Barky

| KPI | Plancher viable | Bon | Excellent |
|---|---|---|---|
| Temps moyen sur page | > 1 min | > 2 min | > 3 min |
| Scroll dépassant 90% | > 25% | > 40% | > 55% |
| CTR vers fiche produit | > 8% | > 15% | > 25% |
| Conversion landing → achat | > 1% | > 2,5% | > 4% |
| Bounce rate | < 60% | < 45% | < 30% |

> Ces benchmarks viennent du marché US DTC supplements. Sur le marché FR petfood premium, on peut s'attendre à -20% sur la conversion la première année (marché moins éduqué au format advertorial). À recalibrer après 30 jours de data.

---

*Source de vérité du repo : [`BARKY_CERVEAU.md`](../BARKY_CERVEAU.md) §14 (Stratégie d'acquisition) et §8 (Claims compliance DGCCRF).*
