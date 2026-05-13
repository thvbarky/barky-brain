# Barky Creatives — Dashboard de production

> **Rôle.** Source de vérité du pipeline créas Barky de A à Z : brief → génération Higgsfield → post-prod → push Meta → KPIs. Trackée dans une DB Notion unique "Barky Creatives".
>
> **Inputs (winners de référence)** → `08-ads/references/ads/` (disk-only, pas dans Notion)
> **Outputs (statics Barky finals)** → `08-ads/statics/YYYY-MM-DD/`
> **Bible de génération** → `08-ads/creative-system.md`
> **Personas** → `02-marche/personas.md`
> **Angles** → `02-marche/angles.md`

---

## Naming convention créas Barky

```
barky_{persona}_{angle-slug}_{static-type}_v{N}.{png|jpg}
```

| Élément | Valeurs | Exemples |
|---|---|---|
| `persona` | `p1` / `p2` / `p3` / `p4` | `p1` |
| `angle-slug` | kebab-case court | `cest-lage`, `carences`, `comite-veto`, `made-in-france` |
| `static-type` | `lifestyle` / `producthero` / `typo` / `proof` | `lifestyle` |
| `v{N}` | numéro version | `v1`, `v2`, `v3` |

**Exemple** : `barky_p1_cest-lage_lifestyle_v3.png`

Le format Meta (1080×1080 / 1080×1350 / 1080×1920) n'est PAS dans le filename — il vit dans la propriété Notion. Plusieurs formats du même slug = sous-dossiers `statics/YYYY-MM-DD/1080x1350/`.

⚠️ Le batch du 2026-05-05 (`v3-lifestyle-p1-cest-lage-nanobanana-1856x2304.png`) utilise une convention plus verbeuse. **Migrer vers la nouvelle convention au prochain batch** — le model + dimensions vivent en propriété Notion, pas dans le filename.

---

## Schéma DB Notion "Barky Creatives" — version validation

> **Workflow cible** : génération MCP Higgsfield → push auto Notion (status `À valider`) → Thomas valide/rejette + écrit Feedback → Claude apprend des choix pour les prochains briefs. Brand & Niche **n'existent pas** comme colonnes : toujours Barky, toujours friandises fonctionnelles chien.

### MVP — avant lancement Meta (12 champs)

| # | Propriété | Type | Valeurs |
|---|---|---|---|
| 1 | **Name** | Title | Slug créa (ex : `barky_p1_cest-lage_lifestyle_v1`) |
| 2 | **Visual** | Files | L'image générée (push auto via MCP Notion) |
| 3 | **Status** | Select | `À valider` (gris) · `Validée` (vert) · `Rejetée` (rouge) · `Live Meta` (violet) |
| 4 | **Persona** | Select | `P1` · `P2` · `P3` · `P4` |
| 5 | **Static type** | Select | `Lifestyle` · `Product Hero` · `Typo Forte` · `Proof` |
| 6 | **Angle** | Select | À peupler depuis `02-marche/angles.md` |
| 7 | **Format** | Select | `1080×1080` · `1080×1350` · `1080×1920` |
| 8 | **Copy overlay** | Text | Texte qui ira sur le visuel en post-prod (Recoleta) |
| 9 | **Référence winner** | Text | Slug du winner inspirant (ex : `20260513_exode_1080x1350_problem-solution`) |
| 10 | **Model** | Select | `Nano Banana Pro` · `Soul V2` · `Soul Cinema` · `GPT Image 2` · `Imagen 4` |
| 11 | **Date générée** | Date | Auto-remplie à la création de la row |
| 12 | **Feedback** | Text | **Champ critique d'apprentissage** — pourquoi rejetée, ce qu'on doit corriger, ce qui marche |

### Phase 2 — à ajouter quand on push en Meta (9 champs supplémentaires)

| Propriété | Type |
|---|---|
| Meta Ad ID | Text |
| Meta Ad URL | URL |
| Date live | Date |
| Budget alloué (€/j) | Number |
| CTR (%) | Number |
| CPC (€) | Number |
| CPM (€) | Number |
| CPA (€) | Number |
| ROAS (×) | Number |

---

## Pourquoi pas de relation Notion avec les winners

Decision actée 2026-05-13 (option A) : le slug du winner se met en champ Text dans `Référence winner`. Pas de seconde DB Notion. Les winners vivent sur disque (`08-ads/references/ads/`) avec leur README + leur `_winners-metadata.csv` pour les notes "why it works". Bascule vers une vraie relation Notion (option B) seulement si on sent un manque de traçabilité visuelle quotidienne — pas nécessaire pour démarrer.

---

## Setup Notion — étapes

1. **Créer la DB** : nouvelle page Notion → `/database` → Full Page
2. **Renommer** : `Barky Creatives`
3. **Créer les 12 colonnes MVP** dans l'ordre du tableau ci-dessus, en sélectionnant les bons types
4. **Pré-peupler les Select** :
   - `Static type` (4 options)
   - `Persona ciblée` (4 options)
   - `Format Meta` (3 options)
   - `Status` (8 options — utiliser des couleurs distinctes : Brief = gris, À générer = jaune, En génération = orange, Générée = bleu, Validée = vert, Rejetée = rouge, Live Meta = violet, Pausée = marron)
   - `Model Higgsfield` (5 options)
   - `Angle Barky` → laisser vide pour l'instant, le peupler depuis `02-marche/angles.md` à la prochaine session
5. **Vues à créer** :
   - **Par status** (Board view, groupée par Status) — vue principale, tu déplaces les cards À valider → Validée/Rejetée
   - **Par persona** (Board view, groupée par Persona) — pour vérifier qu'on couvre P1 et P2 équitablement
   - **Galerie** (Gallery view, cover = Visual) — vue mobile-friendly pour scanner les créas générées
6. **Coller l'URL** de la DB dans ce fichier (remplace le placeholder ci-dessous)

URL Notion DB Barky Creatives :
https://www.notion.so/35ffd75e0c44809189a0ead944464f3c

Data source ID (pour MCP Notion lors des push de rows) : `35ffd75e-0c44-80a1-8a6a-000b3a36b22c`

Vues créées :
- **Board by Status** (vue principale validation) — `view://35ffd75e-0c44-81f7-a8e9-000cd0f89095`
- **Board by Persona** (équilibre P1/P2) — `view://35ffd75e-0c44-81da-8c82-000c3fd1dced`
- **Gallery** (cover = Visual, trié par date desc) — `view://35ffd75e-0c44-817f-b855-000c9b632df2`

⚠️ Le Select `Angle` contient un placeholder `(à peupler depuis 02-marche/angles.md)` à supprimer dès que les vraies valeurs sont injectées.

---

## Workflow type d'une créa Barky

```
1. Claude (via MCP Higgsfield) génère un visuel en s'inspirant d'un winner de 08-ads/references/ads/
2. Claude (via MCP Notion) crée une row "À valider" avec :
   - Name = slug barky_*
   - Visual = l'image générée uploadée dans le champ Files
   - Persona / Static type / Angle / Format / Copy overlay / Référence winner / Model / Date générée pré-remplis
3. Thomas reçoit la créa dans la vue "Par status > À valider"
4. Thomas valide ou rejette :
   - Validée → status = Validée
   - Rejetée → status = Rejetée + Feedback (champ critique : "palette dérive vers orange", "persona P1 trop jeune", "copy ne respecte pas DGCCRF", etc.)
5. Claude relit régulièrement les Feedback récents pour calibrer les prochains briefs (capitalisation dans creative-learnings.md)
6. Push Meta (Phase 2) — status = Live Meta + champs Meta Ad ID / URL / Budget / KPIs
```

**Le champ Feedback est le signal d'apprentissage.** Chaque rejet doit avoir un Feedback. Sans Feedback, Claude ne peut pas s'améliorer.

---

## Mapping avec les fichiers déjà existants

| Fichier | Lien avec la DB |
|---|---|
| [`creative-system.md`](creative-system.md) | Bible de génération — définit les 4 Static types, les règles palette/typo, les prompts par type |
| [`prompt-library.md`](prompt-library.md) | Prompts Higgsfield testés et leur résultat — à consulter avant de briefer |
| [`workflow-creative-mcp.md`](workflow-creative-mcp.md) | Comment appeler MCP Higgsfield depuis une session Claude |
| [`workflow-generation.md`](workflow-generation.md) | Étapes opérationnelles de génération |
| [`creative-learnings.md`](creative-learnings.md) | Retours d'expérience à chaque batch — alimenter après chaque génération |
| [`references/ads/`](references/ads/) | Swipe file winners (input du brief) |
| [`statics/YYYY-MM-DD/`](statics/) | Outputs Barky (file source pour les uploads Notion) |

---

*Dernière mise à jour : 2026-05-13 — création du fichier suite à décision schéma DB Notion (option A).*
