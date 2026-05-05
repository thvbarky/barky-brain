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

*Dernière mise à jour : 27 avril 2026 — palette figée + log pivot multivitaminé.*
