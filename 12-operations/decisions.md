# Log des décisions — Barky

> **Source de vérité :** [`BARKY_CERVEAU.md`](../BARKY_CERVEAU.md) §17. Ce fichier en est l'extrait opérationnel + log permanent.

Chaque décision importante loggée ici avec contexte et raisonnement.

---

## ✅ Décisions tranchées (actées)

| # | Décision | Date | Source/raison |
|---|---|---|---|
| 1 | **Format** : friandises fonctionnelles | Avril 2026 | > petfood classique et > multivitamines généraliste (trigger d'achat clair, marge supérieure, viralité TikTok) |
| 2 | **Voie de production** : private label (voie C, 8-20 k€) | Avril 2026 | Capital limité < 20 k€, time-to-market 6-10 sem, MOQ acceptable |
| 3 | **Identité visuelle** : bleu pastel `#CADCE4` + brun ambré `#463432` | 2026-04-27 | Palette définitive "apothicaire moderne / wellness pharma" — voir [`01-identite/marque.md`](../01-identite/marque.md) |
| 4 | **Nom** : Barky | Avril 2026 | Court, prononçable. Registre cute compensé par tagline + DA |
| 5 | **Tagline** : *"Nourri comme il le mérite."* | Avril 2026 | Tire le nom vers le premium |
| 6 | **Positionnement produit** : SKU unique multivitaminé daily | 2026-04-26 | Modèle Dog is Human DM-01. Voir [`BARKY_CERVEAU.md §3.2`](../BARKY_CERVEAU.md) — pivot depuis l'approche problème-spécifique |
| 7 | **Canaux validation** : Meta Ads + TikTok organique build-in-public | Avril 2026 | Profil fondateur narratif fort, capital-light |
| 8 | **Géographie initiale** : France métropolitaine DTC | Avril 2026 | Marché 6,3 Md€, 9,5M chiens, segment DTC sous-servi |
| 9 | **Modèle commercial** : abonnement mensuel (+ one-off + trimestriel) | Avril 2026 | LTV/CAC SaaS-like, payback < 3 mois |
| 10 | **Repo barky-brain créé** | 2026-04-24 | Source de vérité versionnée |
| 11 | **Creative Strategy Map exécuté** (méthode Pravata) | 2026-04-24 | 5 prompts complets, 4 personas extraits, 5 tests rankés |
| 12 | **BARKY_CERVEAU.md intégré comme master du repo** | 2026-04-25 | Source de vérité unique, chargée dans CLAUDE.md |
| 13 | **Rapport IndexPresse petfood juin 2024 intégré** | 2026-04-28 | Synthèse archivée dans [`02-marche/rapports/indexpresse-petfood-juin-2024.md`](../02-marche/rapports/indexpresse-petfood-juin-2024.md). Insights propagés dans `marche.md`, `tendances.md`, `concurrents.md` et §4.8-4.16 + §5.3 + §19.5 du master. **Apport principal** : citation Mars Petcare "90% croissance santé/bien-être" + 79% claim "qualité humaine" socialement validé + chiffres DNVB précis (UPD 110k abonnés 2023, Japhy panier 63€/+20% vs GD, Dogchef 20M€ CA 2023). |
| 14 | **Stack MCP Barky documentée** (Trendtrack ✅ branché, Meta Ads + Higgsfield à activer post-validation) | 2026-05-01 | Documentation cadre dans [`15-machines/mcp-stack.md`](../15-machines/mcp-stack.md). Playbook veille concurrents [`02-marche/intel-veille-trendtrack.md`](../02-marche/intel-veille-trendtrack.md). Workflow créatif [`08-ads/workflow-creative-mcp.md`](../08-ads/workflow-creative-mcp.md). **Garde-fou non-négociable** : Higgsfield interdit pour visuels chien réel (uncanny valley pet niche, casse la conversion — benchmark Dog is Human n'utilise que photo réelle). Trendtrack à exploiter dès maintenant pour 3 prompts baseline (état marché FR, benchmark Dog is Human, hooks pet wellness 4 pays). Meta MCP à brancher post-J7 de spend. Higgsfield uniquement post-scaling (M2-M3) sur packshots/moodboards. |
| 15 | **Refonte `BARKY_CERVEAU.md`** : 68k → 22k chars + suppression mentions erronées profil fondateur | 2026-05-05 | Master passé sous le seuil performance Claude Code (40k chars) — détail opérationnel déplacé vers fichiers thématiques (audit complet : tous égaux ou plus riches que le master, zéro perte d'info). Master devient **synthèse stratégique always-loaded + index navigable**. Inversion du flux de vérité : les fichiers thématiques sont désormais la source de vérité opérationnelle, le master tient le cap stratégique. **Profil fondateur corrigé** dans 5 fichiers (suppression "Dauphine/M&A" qui ne correspondait pas à Thomas) — source unique désormais [`01-identite/THOMAS_PROFIL_1.md`](../01-identite/THOMAS_PROFIL_1.md). Voir [`journal/2026-05-05.md`](./journal/2026-05-05.md). |
| 16 | **Fiche produit Barky Daily : sélecteur 3 étapes Besti-style** + borne 2→3 bouchées remontée 34kg → 35kg | 2026-05-26 | UX inspirée de Besti (`besti.fr/products/8-en-1-premium`) : étape 1 poids du chien (3 buckets : `<11kg` / `11-35kg` / `>35kg` — alignés sur la posologie 1/2/3 bouchées/jour actée master §3) → étape 2 bundle en mois de traitement (1/2/3 pots avec -5%/-7% remise volume) → étape 3 achat unique vs abonnement Recharge. Borne supérieure du palier 2 bouchées remontée de 34kg à 35kg (chiffre rond, sans impact posologique). Thème actif dupliqué en `barky-dev-weight-selector` (ID `203609243997`) pour bosser sans risque. Voir [`journal/2026-05-26.md`](./journal/2026-05-26.md). |
| 17 | **Cure minimum 2 mois imposée sur la fiche produit** (cohérence garantie 60j) | 2026-05-27 | Filtrage automatique des bundles selon le poids du chien : `<11kg` → 1/2/3 pots OK, `11-35kg` → 2/3 pots seulement (1 pot = 1 mois exclu), `>35kg` → 3 pots seulement. Raison : la garantie "satisfait ou remboursé 60j" exige que le client ait pu observer les bienfaits, donc cure complète. Suppression en parallèle des badges -5%/-7% sur les cartes (visuellement parasites, le compareAtPrice barré suffit). Voir [`journal/2026-05-27.md`](./journal/2026-05-27.md). |
| 18 | **Refonte mapping bundle dynamique par poids + ajout variants 4 et 6 pots** | 2026-05-27 | Évolution de la décision n°17 : Thomas voulait toujours **3 bundles affichés** quel que soit le poids (pas le filtrage qui faisait disparaître des cartes). Nouvelle architecture : chaque poids a son propre set de 3 bundles, le mapping est dynamique via JS — `<11kg` → 1/2/3 pots (2/4/6 mois), `11-35kg` → 2/3/4 pots (2/3/4 mois), `>35kg` → 3/4/6 pots (2/2,7/4 mois). Création des variants `4 pots` (125,12 € · ID 64802769797469) et `6 pots` (185,64 € · ID 64802789949789), grille de remise volume progressive -5/-7/-8/-9%. **Sélecteur de cadence d'abonnement** ajouté en parallèle (1/2/3 mois) — apparaît dans l'Étape 3 quand "Abonnement" est coché. |

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

### 26 avril 2026 — Pivot SKU unique multivitaminé daily
- **Décision** : abandonner l'approche problème-spécifique (3 angles testés) au profit d'un SKU unique multivitaminé daily, modèle Dog is Human DM-01
- **Why** : cible adressable 100% des chiens (vs 15-30%), récurrence native sans churn post-symptôme, narratif marque limpide ("le AG1 du chien"), production OEM simplifiée, risque DGCCRF plus faible
- **Implémentation** : réécriture `produit.md`, `skus.md`, `packaging.md`, `BARKY_CERVEAU.md §3.1-3.5 / §7.1-7.3` ; landing v1 multivitaminée créée

### 27 avril 2026 — Palette définitive : bleu pastel + brun ambré
- **Décision** : palette de marque actée — `#CADCE4` (bleu pastel) + `#463432` (brun ambré). Identité visuelle figée, plus aucune alternative à explorer.
- **Why** : la direction "apothicaire moderne / wellness pharma" est cohérente avec le positionnement premium "santé canine au plus haut standard" et compense le registre cute du nom Barky
- **Implémentation** : `marque.md` mis à jour, alignement `BARKY_CERVEAU.md §2.3-2.4 / §9.1-9.2 / §17.1`, `packaging.md`. Création arborescence `01-identite/assets/` pour logos + bibliothèque d'images. Landing v2 à refaire avec logo réel.

### 27 avril 2026 — Setup Shopify complet + déploiement landing v2 publique
- **Décision** : Custom App créée sur Dev Dashboard (`f7617aa00dab4bef3da6cc457f0cfca3`) avec scopes `write_files,write_online_store_pages,write_themes,write_products,write_content`. Token Admin API permanent stocké en `.env.local` (gitignored).
- **Why** : Shopify CLI OAuth flow plantait (callback store mismatch). Custom App + token = solution fiable, persistante, contrôlable depuis n'importe quel script Python.
- **Implémentation** :
  - Template Liquid `templates/page.barky-landing.liquid` (chrome-stripped) déployé sur Shrine Pro 1.3.3.1
  - 24 assets (logos + 6 fontes Recoleta + 17 photos) uploadés sur Shopify Files (CDN `cdn.shopify.com/s/files/1/1068/0146/3645/`)
  - Page live à `/pages/barky-daily-journal` (ID `Page/713609544029`)
  - 4 CTAs branchés sur fiche produit existante `/products/cf-01%E2%84%A2-multivitamines`
  - SEO complet : title_tag + description_tag (metafields) + OG + Twitter Card via template Liquid
  - 3 scripts Python opérationnels dans `scripts/`
- **Contexte technique** : shop interne `wcrkik-yd.myshopify.com` (alias public `barky-8363.myshopify.com`). MCP Shopify officiel `@shopify/dev-mcp@1.12.0` installé pour validation GraphQL.

### 27 avril 2026 — Routine quotidienne d'enrichissement du cerveau
- **Décision** : mise en place d'un cron quotidien à 17h00 qui synthétise l'activité du jour (git log + diff + journal) dans `BARKY_CERVEAU.md` + `decisions.md` + `12-operations/journal/`.
- **Why** : éviter que les apprentissages restent uniquement dans les conversations Claude éphémères. Capitaliser le savoir au fil de l'eau.
- **Implémentation** : `12-operations/journal/YYYY-MM-DD.md` écrit pendant les sessions par Claude au fil des décisions/insights. Cron CronCreate (durable) à 17h tous les jours déclenche un prompt de synthèse. Migration vers routine cloud (skill `schedule`) prévue après push GitHub du repo.

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

## Décisions actées 29 mai → 3 juin 2026 (session lancement Meta)

### DEC-2026-05-29-A — Domaine canonique = `barky.pet` (TLD `.pet`)

- **Date** : 2026-05-29
- **Décision** : URL publique canonique = `https://barky.pet` (TLD `.pet`, pas `.fr`). Master `BARKY_CERVEAU.md §5.1` corrigé en conséquence.
- **Qui** : Thomas
- **Contexte** : Découverte au moment de configurer Domain Verification Meta. Le master mentionnait `barky.fr` à tort depuis avril.
- **Raisonnement** : `.pet` est le TLD officiel acheté, déjà connecté à Shopify, SSL OK.
- **Résultat attendu** : cohérence partout — JSON-LD, footer, Klaviyo, Meta Pixel, AEM.

---

### DEC-2026-05-29-B — Stack d'offre : abo Recharge −25 % + LANCEMENT10 −10 % single-use

- **Date** : 2026-05-29
- **Décision** :
  - One-off : 34 € + 4,90 € port flat France métro
  - Abo Recharge : −25 % permanent (25,50 €/mois) + livraison gratuite
  - Code `LANCEMENT10` : −10 % single-use sur 100 premières commandes, cumulable abo, `appliesOnSubscription: true`, `recurringCycleLimit: 1`
  - **1re box abo = 22,95 € (0,76 €/j)** · abo récurrent = 25,50 € (0,85 €/j)
- **Qui** : Thomas
- **Contexte** : Avant ce matin, le master disait abo −18 %, LP affichait −30 % mensonger, fiche produit avait Recharge −25 % déjà configurée → tout incohérent.
- **Options considérées** : (A) −30 % lancement (visible) · (B) −25 % abo permanent · (C) Stack −25 % + LANCEMENT10 −10 %
- **Raisonnement** : Stack permet de garder un discours marque permanent fort (−25 % abo) + tension d'achat sans tuer la marge long-terme.
- **Résultat attendu** : message cohérent partout, code visible sur PDP/LP, conversion préservée.

---

### DEC-2026-05-29-C — Livraison gratuite UNIQUEMENT sur abonnement

- **Date** : 2026-05-29
- **Décision** : Port 4,90 € flat France métro sur one-off ; livraison gratuite incluse dans l'abonnement.
- **Raisonnement** : Différentiel clair (≈ 5 €) qui pousse vers l'abo, sans dissuader le test ponctuel. Pas de seuil de gratuité one-off (complique le messaging).

---

### DEC-2026-05-29-D — Garantie renommée « Queue Remuante 60 jours »

- **Date** : 2026-05-29
- **Décision** : remplacement de « Chien en forme 60 jours » par « **Garantie Queue Remuante 60 jours** » partout (LP, PDP, FAQ, footer, iCart drawer).
- **Raisonnement** : nom propriétaire défini en voice-of-brand §3.2. Plus chaleureux, plus mémorisable, drôle juste.

---

### DEC-2026-05-29-E — Byline LP retirée → signature « Comité scientifique Barky »

- **Date** : 2026-05-29
- **Décision** : retrait de la byline Dr. Camille Berton + retrait `author` JSON-LD. Pullquotes nominatives → attribution générique « Comité scientifique Barky ».
- **Raisonnement** : éviter le risque Google « ghost article » + risque réputation si on monte un vrai blog plus tard. Décision audit `12-operations/2026-05-29-audit-validation.md` option D.1.b.

---

### DEC-2026-05-29-F — Strategie ads = split-test LP vs PDP

- **Date** : 2026-05-29
- **Décision** : 1 campagne Sales / CBO 30 €/jour, 2 ad sets identiques sauf URL : Ad set A → LP, Ad set B → PDP. Audience broad FR 25-60 + intérêt « Chiens ».
- **Raisonnement** : on n'a pas de signal pixel historique, on doit apprendre vite quelle destination convertit le mieux. Split-test natif via 2 ad sets distincts (plus contrôlable qu'un A/B test Meta natif).

---

### DEC-2026-05-29-G — Meta BM existant réutilisé

- **Date** : 2026-05-29
- **Décision** : Thomas a déjà un Business Manager (autre activité) → on y ajoute compte pub `Barky FR` + Page FB Barky. Elias ajouté en admin BM + compte pub.
- **Raisonnement** : pas besoin de créer un BM neuf, réutilisation de l'historique de paiement + permissions déjà connues.

---

### DEC-2026-05-29-H — Thème dev `barky-dev-weight-selector` publié sur le live

- **Date** : 2026-05-29
- **Décision** : publication du thème dev (ID 203609243997). Ancien Shrine Pro 1.3.3.1 archivé en bibliothèque. Backup `Shrine Pro — Backup pre-launch 2026-05-29` créé avant.
- **Résultat réel** : OK, site live sur `barky.pet` avec sélecteur 3 étapes Besti-style, iCart drawer, code LANCEMENT10 auto.

---

### DEC-2026-06-02-A — iCart configuré + drawer Shrine Pro abandonné

- **Date** : 2026-06-02
- **Décision** : iCart configuré aux couleurs Barky (palette stricte, pas d'urgence artificielle, pas de progress bar tier discount). Remplace le drawer Shrine Pro natif qui restait en anglais avec widget Recharge non traduit.
- **Configs clés** : pot bleu pastel, brun ambré CTA, code LANCEMENT10 affiché en pill auto, garantie Queue Remuante en trust signal, livraison conditionnée au mode (abo gratuit / one-off 4,90 €), Discount widget HIDE (anti pattern), Express checkout activé (Apple/Google Pay).

---

### DEC-2026-06-02-B — AEM Meta reporté (interface introuvable)

- **Date** : 2026-06-02
- **Décision** : configuration Aggregated Event Measurement reportée. Interface Meta 2026 ne propose plus l'accès classique. Domain Verification `barky.pet` reste OK.
- **Raisonnement** : non-bloquant pour lancement. Pixel + CAPI tracking 80 events déjà actifs. AEM optimise iOS 14+ post-launch.

---

### DEC-2026-06-02-C — 3 angles ads validés + insight stratégique acquisition par symptôme

- **Date** : 2026-06-02
- **Décision** : 3 angles initialement validés (Une bouchée par jour / L'été tape chien souffre / C'est l'âge) → enrichis post-import swipe file concurrents.
- **Insight stratégique** (swipe file 2026-06-02) : le « multivitamine global » ne scale pas comme angle d'acquisition (Besti 8-en-1 = 6 455 reach vs Démangeaisons = 232 776 reach = ×35). Les ads d'acquisition doivent **attaquer par un symptôme précis** (signes mobilité, fatigue, pelage terne). Le « global » reste le territoire de marque / page produit, pas le hook ad.

---

### DEC-2026-06-02-D — Swipe file copies concurrents = source de vérité copywriting ads

- **Date** : 2026-06-02
- **Décision** : création de `08-ads/swipe-file-copies-concurrents.md`, rempli par Thomas avec 12 copies verbatim (Besti, Balto, Wuffes, Dog is Human). Mémoire `reference-swipe-file-copies-concurrents` ajoutée pour lecture systématique avant toute rédaction copy ads.
- **Patterns gagnants intégrés** : hook question-symptôme empilée, caution véto + 🇫🇷, bullets ✅ ingrédients, code promo intégré primary, CTA binaire SHOP NOW (direct) vs LEARN MORE (storytelling).

---

### DEC-2026-06-02-E — 1re campagne Meta : 8 créas (7 statics + 1 vidéo), pas de 9:16 static

- **Date** : 2026-06-02
- **Décision** : short-list finale Thomas = 7 statics 1:1 (`barky_legacy_62_v2`, `barky_legacy_42_v2`, `cest-lage_lifestyle_v2`, `qualite-humaine_17-vitamines`, `signes-mobilite_v2_balades-ete`, `pas-vieux-il-manque_v1`, `liste-complete-actifs_P2_v1`) + 1 vidéo 9:16 (Vidéo 1 TikTok races, 46s).
- **Bannies** : Barky-4 (avant/après santé), Vidéo 2 (avant/après santé), 4 statics avant/après (#49, 57, 60, 61) — refus Meta probable + DGCCRF rouge.
- **CTA différencié** : SHOP NOW (ads conversion directe) / LEARN MORE (storytelling reframe « C'est l'âge » + éducatif).

---

### DEC-2026-06-02-F — Mix pot brun + pot bleu pastel accepté en vague 1

- **Date** : 2026-06-02
- **Décision** : la short-list mélange deux designs de pot (brun = legacy, bleu pastel = batches récents). Acceptation explicite de cette inconsistance visuelle pour aller vite ; Meta optimise par créa unitaire.
- **Trade-off** : un client qui clique sur une ad « pot brun » verra le pot bleu pastel sur la PDP. Risque conversion mineur, à surveiller dans la data.

---

### DEC-2026-06-02-G — Statut Notion `À tester` ajouté (workflow campagne)

- **Date** : 2026-06-02
- **Décision** : ajout du statut `À tester` (orange) dans la DB Notion `Barky Creatives`. Workflow : `À valider` → `À tester` (sélectionnée pour campagne) → `Live Meta` (active dans Ads Manager) → `Validée` (winner) / `Rejetée`.

---

### DEC-2026-06-02-H — Toutes les créas legacy uploadées sur Shopify CDN avec naming structuré

- **Date** : 2026-06-02
- **Décision** : 22 PNG legacy (`/Downloads/Barky/`) uploadées sur Shopify CDN avec naming `barky_legacy_{num}_{descriptor-court}.png`. Mapping sauvegardé : `08-ads/statics/legacy-22-mapping.json`. Notion Visual field accepte URLs externes (validé).
- **Bénéfice** : visuels visibles dans Notion gallery view, plus de drag-drop manuel, source de vérité centralisée.

---

### DEC-2026-06-03-A — Catalogue Advantage+ Meta désactivé pour 1re campagne

- **Date** : 2026-06-03
- **Décision** : on n'utilise pas Dynamic Product Ads (DPA / Catalogue Advantage+) pour la 1re campagne. Format = Image unique ou Vidéo par ad.
- **Raisonnement** : DPA est conçu pour le retargeting sur un pixel chaud. Avec 0 visiteurs trackés au lancement, DPA ne sait pas quoi montrer = budget gaspillé. À réactiver vague 2-3 quand on aura 5 000+ visiteurs trackés.

---

### DEC-2026-06-03-B — MCP officiel Facebook Ads à intégrer

- **Date** : 2026-06-03
- **Décision** : ajout du MCP officiel Meta `https://mcp.facebook.com/ads` à claude.ai connectors pour pouvoir diagnostiquer/optimiser les campagnes en direct via Claude.
- **Scopes accordés** : `ads_read`, `ads_management`, `business_management`, `pages_read_engagement`.
- **À faire** : redémarrer Claude Code pour que les tools `mcp__claude_ai_Facebook_Ads__*` apparaissent.

---

*Dernière mise à jour : 3 juin 2026 — session lancement Meta complète (BM, pixel, code promo, thème live, iCart, copies ads, 8 créas, MCP Meta à activer).*
