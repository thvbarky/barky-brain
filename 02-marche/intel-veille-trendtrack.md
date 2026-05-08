# Veille concurrents — playbook Trendtrack MCP

> Source de vérité globale marché : [`BARKY_CERVEAU.md §5`](../BARKY_CERVEAU.md). Ce fichier est le **playbook opérationnel** pour exploiter le Trendtrack MCP branché à Claude Code.
>
> **Principe** : Trendtrack fait le scrape, Claude fait la synthèse, on capture dans les fichiers thématiques. La data brute reste dans l'API ; ici on garde les **insights actionables**.

---

## 1. Brands à surveiller en priorité (à brancher dans Trendtrack tracking)

### Tier 1 — concurrents directs FR/EU pet supplements

| Brand | URL | Pourquoi la suivre |
|---|---|---|
| **Vétalis** | vetalis.fr | Compléments co-détenus par 130 cliniques. Signal fort sur l'organisation véto FR. |
| **Hector Kitchen** | hectorkitchen.com | Repas frais FR + a tâté du complément. Voir s'ils étendent en multivit. |
| **Goodbro** | goodbro.fr | Snacks fonctionnels chien FR — concurrent direct format friandise fonctionnelle. |
| **Symbiopet / Vivomixx** | divers | Compléments vendus en pharma/parapharma FR. |

### Tier 2 — DNVB premium FR (modèles d'acquisition à étudier)

| Brand | URL | À tracker |
|---|---|---|
| **Elmut** | elmut.fr | Hooks, LPs, cadence email — modèle scale DTC pet FR (3 M€ levés sept 2025) |
| **Ultra Premium Direct** | ultrapremiumdirect.com | Vient d'être cédé à Inspired Pet Nutrition — voir comment leur stratégie évolue post-acquisition |
| **Japhy** | japhy.fr | Modèle abonnement croquettes personnalisées + service véto en ligne |
| **Pépette** | pepette.com | Sur-mesure bio chiens |

### Tier 3 — benchmarks internationaux (ne pas tracker en continu, scanner ponctuellement)

| Brand | URL | Pourquoi |
|---|---|---|
| **Dog is Human** | dogishuman.com | **Notre benchmark direct** sur le format multivit daily. 51k+ reviews 5★. |
| **Zesty Paws** | zestypaws.com | Le playbook supplements pet US (vendu 610 M$ à H&H Group en 2021) |
| **Petlab Co.** | thepetlabco.com | UK, scale énorme sur multivit/probiotics chien |
| **Native Pet** | nativepet.com | Premium clean label US |

---

## 2. Prompts à exécuter en S1 (premier scan baseline)

### Prompt A — État des lieux du marché FR pet supplements

```
Avec Trendtrack MCP, fais un scan complet du marché pet supplements FR.

1. find_winning_products niche="pet supplements OR dog health OR
   complément chien", country=FR, period=30d, prix=20-50€
2. search_shops country=FR, niche="dog wellness", traffic_growth=positive,
   period=30d
3. search_ads country=FR, niche="dog supplements", ad_duration=60d+,
   format=video → on cherche les pubs qui durent (= qui scalent)

Cross-réf avec BARKY_CERVEAU.md §5. Liste :
- Les nouveaux concurrents apparus depuis avril 2026 (pas dans le cerveau)
- Les hooks qui durent > 60 jours (signal de scale, pas test)
- Les estimations de spend mensuel des 5 plus gros

Output structuré + propose un draft d'update pour 02-marche/concurrents.md
si écarts détectés.
```

### Prompt B — Benchmark Dog is Human (intel transposable)

```
Avec Trendtrack MCP :

1. brief_competitor URL="dogishuman.com" → fiche complète
2. search_ads advertiser="Dog is Human", period=90d
3. search_emails URL="dogishuman.com", period=30d (Pro plan, vérifier crédits avant)

Question : quels sont les 3 hooks qui ont la plus grande longévité chez eux,
et comment les transposer en français sans copier littéralement ?

Cross-réf avec 02-marche/benchmark-dog-is-human.md déjà existant.
Update ce fichier si nouveaux insights.
```

### Prompt C — Hooks dominants pet wellness 2026

```
Avec Trendtrack MCP, sors-moi le creative_inspiration_pack pour la niche
"dog wellness OR pet supplements" sur les pays FR, BE, UK, US.

Période : 30 derniers jours.

Pour chaque pays :
- Top 5 hooks par fréquence
- Top 3 angles dominants
- Répartition format (vidéo / image / carrousel)
- Durée moyenne d'ad qui tourne (signal de scale)

Cross-réf avec 02-marche/angles.md (méthode Lorenzo Pravata) :
- Quels angles Barky sont déjà dans la mêlée mainstream → risque de banalité ?
- Quels angles dans Trendtrack qu'on n'a PAS dans nos 3 angles SKU hero
  (articulations / pelage / stress) ?

Output : draft d'update pour 02-marche/angles.md avec 2-3 angles à ajouter
au test plan si pertinents.
```

---

## 3. Routine récurrente — daily radar (post-tracking activation)

Une fois 5-10 brands tracked dans Trendtrack :

```
Lundi matin (avant la weekly review) :

mcp__trendtrack__daily_radar period=7d

→ Liste tous les changements de la semaine sur mes brands trackées :
   nouvelles pubs, nouvelles LPs, modifs cadence email, nouveaux SKUs lancés.

Synthèse :
- Quoi de neuf (1 ligne par brand)
- Pattern transversal détecté (si 3+ brands font la même chose, c'est un signal)
- Action Barky proposée (test à lancer / angle à explorer / risque à surveiller)

Log dans 12-operations/journal/{date}.md → bloc "Insights produit/marché".
Si insight majeur → update 02-marche/concurrents.md.
```

---

## 4. Déclencheurs ad hoc (à utiliser au cas par cas)

### Une boutique attire ton attention → fiche complète

```
mcp__trendtrack__brief_competitor URL="<url>"

Donne :
- Trafic + croissance
- Pubs actives + longévité
- Stack technique (thème Shopify, apps, pixel)
- Best-sellers
- Réseaux sociaux + grow rate
- Trustpilot / reviews
```

### Tu veux des "clones" — boutiques similaires à étudier

```
mcp__trendtrack__find_similar_shops URL="elmut.fr", country=FR, top=10

→ Donne 10 boutiques avec un angle similaire à Elmut, classées par
   signaux de croissance.
```

### Tu veux décortiquer une pub gagnante (Pro plan)

```
mcp__trendtrack__scan_ad ad_url="<url meta ad library>"

→ Hook, structure copy, page de vente liée, audience démo, durée de vie,
   verdict scaling.
```

---

## 5. Garde-fous & limites

1. **Crédits API** — `check_credits` avant d'enchaîner les calls Pro (`scan_ad`, `search_emails`, `analyze_shop_emails`). Si on est sur le plan gratuit / Starter, certains tools renvoient une erreur quota.
2. **Couverture FR limitée** — Trendtrack est très solide sur US/UK, plus mince sur FR. Une "absence de concurrent" peut être un faux négatif. Toujours cross-checker manuellement (Google + Meta Ad Library FR + Instagram explore).
3. **Pas de copy littéral** — les hooks détectés sont du signal, pas du copy à coller. Filtre voice-of-brand obligatoire (`01-identite/voice-of-brand.md`).
4. **Pas de claims santé qu'on ne peut pas tenir** — un concurrent peut avoir un hook agressif type "guérit l'arthrose" qui est illégal côté DGCCRF. Garde toujours le filtre `04-legal/allegations.md`.
5. **Logger ce qui mérite la mémoire** — un nouveau concurrent significatif → `02-marche/concurrents.md`. Un hook qui change la stratégie → `02-marche/angles.md` + journal du jour. Une décision actée → `12-operations/decisions.md` + `BARKY_CERVEAU.md`.

---

## 6. Coupling avec le reste du brain

| Si tu trouves… | Mets à jour… |
|---|---|
| Nouveau concurrent FR/EU significatif | `02-marche/concurrents.md` + `BARKY_CERVEAU.md §5` |
| Hook / angle qui scale et qu'on n'a pas | `02-marche/angles.md` + `02-marche/test-plan.md` |
| Stratégie pricing différente d'un concurrent FR | `03-produit/pricing.md` |
| Cadence email d'un benchmark | `09-email-sms/flows.md` |
| App Shopify intéressante chez un concurrent | `06-store/app-stack.md` (à créer si absent) |
| Pub qui dure > 6 mois sur un angle | `08-ads/meta/strategy.md` (insight de scale) |
| Insight ponctuel non-classifiable | journal du jour `12-operations/journal/{date}.md` |

---

## 7. Premiers tests à exécuter (S1 — semaine en cours)

- [ ] Prompt A (état des lieux marché FR pet supplements) — capturer les 3 surprises principales
- [ ] Prompt B (benchmark Dog is Human) — valider que `benchmark-dog-is-human.md` est à jour
- [ ] Prompt C (hooks pet wellness 4 pays) — output utilisable pour `02-marche/angles.md`
- [ ] Activer le tracking sur les 8 brands Tier 1 + Tier 2
- [ ] Mesurer le coût en crédits Trendtrack de cette session de scan

---

*Fichier créé le 2026-05-01. Update à chaque session de veille majeure ou quand on ajoute/retire une brand du tracking.*
