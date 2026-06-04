# Snippet à coller dans la tâche Cowork — Phase 2 génération auto

> À ajouter à la fin du prompt de la tâche programmée Cowork sur claude.ai (celle qui tourne tous les matins 11h00 et qui produit `brief-YYYY-MM-DD.md` dans le projet *Barky OS*).
>
> **Règle d'or :** zéro reformulation du brief. Le brief est la source de vérité, on l'exécute tel quel.

---

## Phase 2 — Générer les statiques + push Notion

Une fois `brief-YYYY-MM-DD.md` écrit dans le projet *Barky OS*, parser le fichier pour identifier les briefs à exécuter.

### Étape 0 — Quels blocs traiter ?

- ✅ Traiter **tout bloc qui commence par `## BRIEF N — ...`** (N entier, suivi d'un titre).
- ❌ **Skipper tout bloc `## RAPPEL URGENT — BRIEF N`** (ces briefs ont déjà été émis et générés un jour précédent — pas de re-génération).
- Le nombre de briefs nouveaux varie chaque jour (0 à 3+). Traiter ce qui est là, pas plus.
- Si 0 brief nouveau → ne rien générer, logger en commit message « pas de brief actionnable aujourd'hui ».

### Étape 1 — Pour chaque brief nouveau, construire le prompt Higgsfield

```
Statique Meta 1:1 1080×1080. Marque Barky — friandises fonctionnelles
multivitamine quotidien pour chiens. Palette stricte : bleu pastel #CADCE4
+ brun chocolat-leather #463432 + cream #F5F0EB. Typo Recoleta serif.
Registre apothicaire moderne, wellness pharmaceutique. JAMAIS orange,
caramel, terracotta, navy.

RÉFÉRENCE PACKSHOT — l'image jointe est le packshot officiel Barky. Si
le brief affiche le pot, reproduis-le tel quel (brun chocolat #463432,
label blanc "Barky.", écusson France). Jamais de pot transparent / verre
/ illustration cartoon. Sinon, ignore la référence.

Génère le statique décrit dans ce brief, en suivant à la lettre la
ligne "Format recommandé" et la "variante statique" si elle existe :

[COLLER ICI LE BLOC BRIEF INTÉGRAL, du "## BRIEF N — ..." jusqu'au "---" suivant]
```

### Étape 2 — Appeler Higgsfield

`mcp__claude_ai_Higgsfield__generate_image` avec :
- `model`: `"gpt_image_2"` (préférence Thomas 14/05/2026 ; Nano Banana 2 reste utilisable en fallback)
- `prompt`: le prompt construit à l'étape 1
- `aspect_ratio`: `"1:1"`
- `resolution`: `"2k"`
- `quantity`: `1`
- `medias`: `[{"value": "https://cdn.shopify.com/s/files/1/1068/0146/3645/files/packshot-pot-ferme-bleu-pastel.png?v=1777296328", "role": "reference"}]`

> **Pourquoi le packshot en référence** : sans cette référence visuelle, le modèle (Nano Banana 2 ou GPT Image 2) invente le pot Barky à partir du texte (résultat observé 2026-05-14 sur Nano Banana 2 : pot transparent en verre + illustration cartoon de chien sur le label, palette qui dérive vers orange/caramel). Le packshot officiel ancre la marque, indépendamment du modèle.
>
> **Choix du packshot** : `packshot-pot-ferme-bleu-pastel.png` — pot fermé sur fond bleu pastel, c'est la référence par défaut Barky (cf. memory `feedback_packshot_dos_ingredients_banni`). Le packshot dos-ingrédients est banni.
>
> Si Higgsfield rejette le `role: "reference"` (varie par modèle), basculer sur `"input"` ou appeler `models_explore` pour la liste valide.

Récupérer l'URL de l'image générée.

### Étape 3 — Push row Notion

DB Notion : `Barky Creatives`
data_source_id : `35ffd75e-0c44-80a1-8a6a-000b3a36b22c`

Via `mcp__claude_ai_Notion__notion-create-pages`, créer une row avec :
- **Name** : titre exact du brief (la ligne `BRIEF N — ...` sans le `##`)
- **Status** : `À valider`
- **Model** : `gpt_image_2`
- **Date générée** : date du jour (`YYYY-MM-DD`)
- **Visual** : URL de l'image générée (champ Files)
- **Body de la page** (contenu Notion sous les properties) : bloc brief intégral verbatim, du `## BRIEF N` jusqu'au `---` suivant

Les autres champs (Persona, Static type, Angle, Format, Copy overlay, Référence winner, Feedback) restent **vides**. Thomas les complète manuellement à la validation si pertinent.

### Étape 4 — Répéter pour chaque brief nouveau

### Étape 5 — Commit GitHub

Commit dans `barky-brain` :
- Path : `08-ads/briefs/brief-YYYY-MM-DD.md` (contenu identique au fichier projet)
- Message : `feat(veille): brief + N statique(s) générée(s) YYYY-MM-DD` (N = nombre de briefs nouveaux traités)

---

## Règles non-négociables

1. **Zéro reformulation du brief**. Pas de résumé, pas de traduction, pas de polish. Le brief part tel quel chez Higgsfield et tel quel dans Notion.
2. **Pas de référence au swipe file local** (`08-ads/references/ads/`). Ces statiques partent *from scratch* à partir du brief. Note : depuis la refonte du 14/05/2026, le skill `/barky-creas-batch` n'exige plus de winner local non plus (winner = inspiration optionnelle). Les 2 pipelines convergent désormais sur le même pattern court (meta-prompt + brief court).
3. **Skip systématique des `## RAPPEL URGENT`** — ce sont des reminders pour Thomas, pas des briefs à exécuter.
4. **Nombre variable**. Pas de minimum, pas de maximum. Traiter ce que la veille a produit.
5. **Si Higgsfield ou Notion échoue** sur un brief, logger l'erreur dans le commit message et passer au suivant. Pas de retry automatique.

---

*Maintenu dans le repo pour version control. La source qui tourne est dans le system prompt de la tâche Cowork sur claude.ai.*
