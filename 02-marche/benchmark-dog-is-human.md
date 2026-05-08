# Benchmark — Dog is Human (US)

> **Source de vérité :** [`BARKY_CERVEAU.md`](../BARKY_CERVEAU.md) §5.4. Ce fichier en est l'extrait enrichi sur le benchmark visuel/produit direct identifié dans le master.
>
> **Données :** TrendTrack public API · workspace ID `2c68d18e-1794-4176-9f29-b755a11609b3` · brandtracker `0671b9a5-c148-471b-87f6-3469fd067475`
>
> *Dernière mise à jour : 28 avril 2026 — première extraction TrendTrack complète*

---

## Pourquoi ce benchmark

Dog is Human est cité dans `BARKY_CERVEAU.md §5.4` comme **le benchmark visuel et produit direct** de Barky : DM-01™ Daily Multivitamin, "human-grade", positionnement abonnement, formulé par vétérinaires, narratif "one product a day". Leur trajectoire valide ou invalide les arbitrages stratégiques de Barky (notamment §3.2 sur le pivot multivitaminé, §7 sur l'architecture SKU, §10 sur les unit economics).

---

## 1. Échelle & trajectoire trafic

| Metric | Valeur (avril 2026) | Note |
|---|---|---|
| Visites mensuelles (mars 2026) | **630 906** | Pic à 823k en janvier 2026 (post-fêtes / sale) |
| Croissance trafic 90j | **+34%** | Pas un plateau |
| Croissance trafic 180j | **+35%** | Cohérent |
| Marché US | **91%** du trafic | TH 1,3% · VN 0,7% · AE 0,6% · DE **0,5%** |
| Reach Meta 30j | **597 568** | Acquisition principale = Meta Ads |
| Active ads (snap actuel) | **305** | Moyenne 30j : **484** · Pic : **554** (mi-mars 2026) |

### Historique trafic 6 mois

| Mois | Visites |
|---|---|
| oct 2025 | 541 099 |
| nov 2025 | 506 459 |
| déc 2025 | 472 036 |
| **jan 2026** | **823 183** |
| fév 2026 | 642 087 |
| mar 2026 | 630 906 |

**Lecture** : saisonnalité claire avec pic post-fêtes/New Year's Sale, plateau autour de 600-650k entre fév et mars. La croissance YoY n'est pas dérivable des données TrendTrack actuelles.

---

## 2. Catalogue produit (10 SKUs)

### La structure réelle

| # | SKU | Prix | Date publication | Rôle |
|---|---|---|---|---|
| 1 | **Daily Multivitamin (Chicken)** | **$46** | mars 2022 | Hero historique — 4 ans en marché |
| 2 | **Daily Multivitamin (Beef)** | $58 | janv 2024 (publié sept 2024) | Variante saveur premium **+$12** |
| 3 | The Daily Duo (Multi + Fish Oil) | $81 | juil 2024 | Bundle 2 SKU |
| 4 | The Daily Duo (Beef) | $93 | juil 2024 | Bundle 2 SKU premium |
| 5 | 3-Jar Bundle (Chicken) | $138 | juil 2025 | Pack trimestriel équivalent ($46/jar = pas de remise volume affichée) |
| 6 | 3-Jar Bundle (Beef) | $174 | juil 2025 | Idem en variante Beef |
| 7 | Wild Alaskan Fish Oil | $35 | juin 2024 | Complément, pas un curatif |
| 8 | **Advanced Hip and Joint** | $58 | juin 2025 (publié août 2025) | **Premier curatif — 3 ans après le hero** |
| 9 | Slow Feeder Dog Bowl | $28 | 2023 | Accessoire / unboxing |
| 10 | Wishbone Blue Hoodie | $48 | 2022 | Merch communauté |

### Lecture stratégique

**7 SKUs sur 10 = écosystème autour du DM-01™.** Le multivitaminé daily est le pivot absolu du catalogue. Pas une gamme problème-spécifique à la Zesty Paws (6 SKU différents). Pas une matrice d'âges/tailles non plus.

**Ils ont étendu via 3 axes, dans cet ordre temporel :**
1. **Variante saveur premium** (Beef, +$12) — janv 2024 = **22 mois après le lancement**
2. **Bundle de SKUs** (Daily Duo Multi+Fish Oil) — juil 2024
3. **Pack trimestriel volume** (3-Jar Bundle) — juil 2025 = **40 mois après le lancement**
4. **Premier vrai curatif** (Advanced Hip and Joint) — juin 2025 = **39 mois après le lancement**

Aucune fragmentation par âge (puppy/adult/senior) ni par taille (small/large breed) sur la durée observée.

---

## 3. Stratégie Meta Ads — whitelist industrielle

### Le pattern UGC scalé

**75 pages Facebook liées comme advertisers** dans le compte Dog is Human. Chaque grand compte de chien influenceur lance ses propres ads — c'est de la **whitelist ad** (le créateur prête sa page, Dog is Human paie le push).

### Top 10 advertisers par volume d'ads actives

| Rang | Page | Active ads |
|---|---|---|
| 1 | **Dog is Human** (officiel) | 305 |
| 2 | Britt + Wince | 58 |
| 3 | Smart Dog Health | 52 |
| 4 | Tracy's Dog Life | 41 |
| 5 | Walter Geoffrey | 36 |
| 6 | The Wise Vet | 30 |
| 7 | Kash.d.frenchie | 25 |
| 8 | The Adventures of Oso and Koa | 20 |
| 9 | lavenderandlatte | 12 |
| 10 | Otto the Lab | 10 |

Conséquence : **multiplication des "sources" d'ads × 75**, ce qui contourne le pixel fatigue, démultiplie le reach, et fait paraître Dog is Human partout sur Meta sans que l'utilisateur identifie une seule marque.

### Ads scaled actives (échantillon TrendTrack)

- **Hook narratif émotionnel (vidéo)** : *"Cause time wasn't in our favor"* — angle "j'ai pas eu le temps avec mon chien précédent, je veux pas refaire la même erreur". Pivot émotionnel → préventif.
- **Hook produit rationnel (image)** : *"DM-01™ Daily Multivitamin is formulated to help your dog thrive. Its 12 clinically + scientifically studied ingredients (commonly deficient in the normal dog…)"*
- **Format dominant** : video (3 latest sur 3).

### Distribution géographique des ads

100% US sur les ad stats brutes. La `countryDistribution` du summary mentionne 94,6% US · 4,7% CA · 0,7% GB. **Pas d'expansion européenne en cours.**

---

## 4. Email marketing — playbook content-driven (Klaviyo)

### Cadence et mix

- **~3 emails / semaine**
- **70% non-promotionnels** (pas de discount, focus éditorial)
- **30% promotionnels** (sale Easter, New Year, etc.)

### Templates récurrents (échantillon 25 emails dec 2025 → avr 2026)

| Template | Fréquence | Exemples |
|---|---|---|
| **"Build a Bowl with [chien]"** | 8/25 (32%) | Build a Bowl with Poppy & Ruby · Maple · Miso · Olive · Milo |
| **"Recipe of the Week"** | 6/25 (24%) | Squash Chips · Salmon Bites · Beef Treats · Christmas Tree Treats · Carrot Dental Chew |
| **Tips santé** | 3/25 (12%) | Hip and Joint Tip · Broccoli Dental Chew |
| **Sale / promo** | 5/25 (20%) | Easter Sale · New Year Surprise (30% off) |
| **Enrichment games** | 3/25 (12%) | Egg Enrichment Game · Fruit Bobbing Bowl |

### Pattern dominant

Les emails ne vendent pas le DM-01 frontalement. Le pattern est : *"voici une recette / une activité / un tip santé qui complète ton DM-01"*. Le produit apparaît en bas de mail, jamais comme objet principal. C'est de l'**éducation lifestyle**, pas de la conversion directe.

Ils utilisent ~5-6 chiens "ambassadeurs" récurrents (**Poppy, Ruby, Maple, Miso, Olive, Milo**) qui personnalisent chaque email. Ce sont leurs propres contenus, pas du UGC client.

### Promo intensité

Promos concentrées sur **2 événements/an** observés : **Easter (avril)** et **New Year (déc/jan)**. Pas de discount hebdomadaire = pas de brand erosion premium.

---

## 5. Stack technique Shopify

### Theme et apps

| Catégorie | Outil identifié |
|---|---|
| **Thème Shopify** | **Dawn** (gratuit officiel Shopify) |
| Reviews | **Junip** ‑ Product Reviews App |
| Cart drawer | Wowcart ‑ Slide Cart Drawer |
| Free gift | EG Auto Add to Cart Free Gift |
| Conversion tracking | **Elevar Conversion Tracking** (CAPI Meta + GA4) |
| Email/SMS | **Klaviyo** |
| Live chat AI | VanChat AI Chatbot & Live Chat |
| Insights | Infinite Microsoft Clarity (heatmaps gratuites) |
| Instagram feed | Instafeed |
| Partner channel | Shoppable Partner Channel |
| App suite | Apps by Mintt Studio |

### Pixels actifs (8 réseaux)

Facebook · Google Ads · Microsoft Ads · Pinterest Ads · Reddit Ads · Snap Pixel · TikTok Pixel · Applovin · Google Analytics · Google Tag Manager.

### Lecture

**Dawn (theme gratuit)** = leur "premium feel" vient du product photography + copy + custom sections, **pas du theme**. Leur stack apps est standard DTC US (Junip, Klaviyo, Elevar) sans extravagance.

---

## 6. Socials

| Plateforme | Followers | Croissance 30j |
|---|---|---|
| Instagram (@dogishuman) | **404 220** | **+6,1%** |
| Facebook | 267 000 | +4,3% |
| TikTok | présent (handle @dogishuman) | données indispo |
| YouTube · Pinterest · LinkedIn · Twitter | absent / non actif | — |

**Instagram > Facebook** sur la croissance. Cohérent avec leur stratégie de contenu visuel autour des chiens ambassadeurs (Poppy, Miso, etc.) et UGC whitelisté.

---

## 7. Trustpilot vs reviews on-site

| Source | Note | Volume |
|---|---|---|
| **Trustpilot** (officiel) | **4 / 5** | **153 avis** |
| Junip on-site (cité dans `BARKY_CERVEAU.md §5.4`) | 5⭐ revendiqué | ~51 600+ avis revendiqués |

**À noter** : le brain mentionne "51 600+ avis 5⭐" pour DM-01 — c'est le compteur Junip on-site, **pas Trustpilot**. Trustpilot est notablement plus modeste (4/5 sur 153). Précision à intégrer dans le master au prochain refresh.

---

## 8. Lectures stratégiques (pas de décisions actées)

> Cette section liste des **patterns observés** chez Dog is Human qui peuvent informer Barky. Aucune décision n'est tranchée ici — voir `12-operations/decisions.md` pour les décisions actées.

### Sur la trajectoire produit

- **3 ans avec 1 SKU hero avant d'élargir** (DM-01 chicken seul de mars 2022 à janv 2024).
- **L'extension passe par la variante saveur premium (+$12) avant le SKU problème-spécifique.** Le seul curatif (Advanced Hip and Joint) arrive **39 mois après le hero**.
- **Pas de fragmentation par âge ni taille** sur la durée observée.

### Sur les ads

- **75 pages whitelisted** = arme de scaling Meta. Modèle adaptable en France quand base d'ambassadeurs en place.
- Les hooks scalés mélangent **émotionnel narratif** (deuil, prévention) et **rationnel produit** (12 actifs). Pas de hook "before/after" évident dans l'échantillon scanné.
- **Format video dominant** sur les ads les plus récentes.

### Sur l'email

- **Cadence 3/sem dont 70% non-promo** = posture éditoriale qui protège le pricing premium.
- **Personnalisation via 5-6 chiens ambassadeurs récurrents** crée un univers narratif sans dépendre du UGC client.
- **Promo concentrée sur 2 événements/an** (Easter + Year-end). Brand premium préservée.

### Sur la stack

- **Dawn theme gratuit** + Klaviyo + Junip + Elevar = stack DTC standard sans surcoût premium. Le moat n'est pas dans le theme.
- **Elevar = critique pour le tracking CAPI Meta** post-iOS14.5. À considérer avant tout test paid Meta.

### Sur la géo

- **0,5% du trafic en Allemagne, pas d'expansion EU active.** La France est un boulevard ouvert vis-à-vis de Dog is Human.

---

## Annexe A — Identifiants TrendTrack

| Entité | ID |
|---|---|
| Brandtracker | `0671b9a5-c148-471b-87f6-3469fd067475` |
| Shop | `2c68d18e-1794-4176-9f29-b755a11609b3` |
| Advertiser primary (Facebook page) | `101490992275683` |
| Domain | `dogishuman.com` |
| myShopifyDomain | `dog-is-human.myshopify.com` |

## Annexe B — Méthodologie

Données extraites le 28 avril 2026 via `mcp__trendtrack__brief_competitor`. Sources internes TrendTrack : Meta Ad Library (ads), SimilarWeb (trafic), Shopify Storefront (catalogue), Klaviyo (emails publics), Trustpilot (reviews).

Limites :
- `reach30d` non disponible sur l'advertiser primary à la date d'extraction.
- Les ads "scaling" identifiées dans `scanComposition` ont un verdict "Inconclusive — missing performance history" (3 scans observés).
- Le compteur "51 600+ reviews 5⭐" du brain n'est pas vérifié par TrendTrack (Trustpilot = 153 avis).

---

*Dernière extraction TrendTrack : 28/04/2026 14h22 UTC. Refresh recommandé tous les 90 jours ou avant tout pivot stratégique majeur.*
