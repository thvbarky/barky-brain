# Workflow Génération Statics Barky

> **À quoi sert ce fichier.** C'est le **playbook opérationnel** que Claude (dans Barky OS / claude.ai / Claude Code) suit quand Thomas demande à générer des statics Meta Ads via Higgsfield. Process déterministe, lecture-éxécution-logging.
>
> **Source de vérité visuelle** : [`creative-system.md`](creative-system.md).
> **Source de vérité messages** : [`16-veille/contexte-veille.md`](../16-veille/contexte-veille.md) + [`02-marche/angles.md`](../02-marche/angles.md).
> **Mémoire des sessions** : [`creative-learnings.md`](creative-learnings.md).
> **Index assets** : [`assets/brand-assets.md`](assets/brand-assets.md).

---

## 🚦 Comment déclencher une session

Dans Barky OS (claude.ai), Thomas dit l'une de ces phrases :

| Phrase de déclenchement | Action attendue |
|---|---|
| *"Génère les statics du brief {date}"* | Lis `08-ads/briefs/brief-{date}.md` puis exécute la séquence |
| *"Lance une session créa {type}"* | Type = `lifestyle` / `product-hero` / `typo-forte` / `proof`. Pas de brief écrit, brief inline avec Thomas. |
| *"Statics pour l'angle {angle}"* | Cherche l'angle dans `02-marche/angles.md`, prend le brief inline |
| *"3 variations sur {asset existant}"* | Forke un visuel déjà bon score depuis `08-ads/statics/{date précédente}/` |

---

## 🔁 La séquence en 9 étapes (inviolable)

### ÉTAPE 1 — CHARGER LE BRIEF
- Si `08-ads/briefs/brief-{date}.md` existe → lire intégralement
- Sinon → demander à Thomas en 5 questions max (persona / angle / awareness / format / 1 contrainte spéciale ?)
- Si on forke un asset existant → lire le prompt original dans `creative-learnings.md`

### ÉTAPE 2 — LIRE creative-system.md
**OBLIGATOIRE.** Pas de prompt sans avoir relu :
- La palette (#CADCE4 + #463432)
- Les 4 types de static
- Le template master 10 couches
- Les règles DGCCRF si overlay texte prévu

### ÉTAPE 3 — LIRE creative-learnings.md
**OBLIGATOIRE.** Récupérer :
- Les patterns gagnants à reproduire
- Les patterns à éviter à pousser dans le NEGATIVE
- Les prompts haute performance similaires à forker

### ÉTAPE 4 — LIRE brand-assets.md
Vérifier :
- Quel packshot utiliser si Product Hero
- Quelle photo lifestyle pour le chien (pas de chien IA)
- Quel asset référence si génération autour d'un existant

### ÉTAPE 5 — CONSTRUIRE LES PROMPTS (3 minimum)
- Construire **3 variations minimum** par session (jamais une seule)
- Chaque prompt = template 10 couches du `creative-system.md`
- Chaque prompt = 250-500 mots minimum (un prompt court = un visuel pauvre)
- Chaque prompt = en **anglais** (Higgsfield performe mieux)
- Le texte / overlay reste **toujours en français**, à composer en post-prod

#### Distribution standard des 3 variations

| Variation | Logique de différenciation |
|---|---|
| **V1 — Le canon** | Application stricte du template, lisible, safe, le visuel "bench" |
| **V2 — L'angle décalé** | Cadrage différent (close-up vs wide), moment différent (avant/après le geste) |
| **V3 — L'option contrarian** | Lumière, mood, ou registre opposé pour ouvrir une piste créative non couverte |

### ÉTAPE 6 — GÉNÉRER VIA HIGGSFIELD MCP

> Higgsfield MCP est la couche d'exécution. Le serveur dispo dans le repo est `mcp__02f9a7d6-3011-44c1-8c95-7d35dbb440fa__*` (alias Higgsfield).

Tools clés :
- `mcp__02f9a7d6-...__balance` — vérifier les crédits avant
- `mcp__02f9a7d6-...__select_workspace` — Barky workspace si pas déjà sélectionné
- `mcp__02f9a7d6-...__models_explore` — lister les modèles dispo (pour choisir le meilleur Soul / image model)
- `mcp__02f9a7d6-...__generate_image` — la génération elle-même (paramètres : prompt, négative, ratio, model)
- `mcp__02f9a7d6-...__job_display` — récupérer le job pour voir les outputs
- `mcp__02f9a7d6-...__show_generations` — galerie des dernières générations
- `mcp__02f9a7d6-...__media_upload` — uploader un asset de référence (style transfer)
- `mcp__02f9a7d6-...__soul_train` — entraîner un Soul custom Barky (à activer post-validation)

**Settings standards Barky** :
- Format : 1080×1350 (4:5) par défaut Meta feed
- Modèle : le plus récent / qualité max disponible (vérifier `models_explore`)
- Négative prompt : toujours inclus, copié depuis `creative-system.md` §4.2 NEGATIVE
- Seed : laissée libre pour exploration, ou fixée si on cherche à itérer sur un look

### ÉTAPE 7 — PRÉSENTER LES VISUELS À THOMAS

Format de présentation obligatoire :

```
🎨 Session {date} — {description}

📁 Sauvegardés dans `08-ads/statics/{date}/`

────────────────────────────────────────
V1 — {sous-titre}
[image]

Pourquoi ce choix créatif :
- [3 lignes max sur la décision artistique]

Ancrage stratégique :
- Persona : P{1 ou 2}
- Angle : "{angle exact}"
- Awareness : {Problem/Solution/Product}
────────────────────────────────────────
V2 — {sous-titre}
[image]
[idem]
────────────────────────────────────────
V3 — {sous-titre}
[image]
[idem]
────────────────────────────────────────

Ton score (1-5) sur chacun ?
Tes corrections / pistes pour V4 ?
```

### ÉTAPE 8 — DEMANDER SCORE + FEEDBACK

Les 3 questions à Thomas :
1. **Score 1-5 par variation** (rapide, intuitif)
2. **Pour les 4-5** : qu'est-ce qui fait que ça marche ? (instructif)
3. **Pour les 1-2** : on garde l'angle mais on change quoi ? (correctif)

Si Thomas dit *"v2 est bonne mais le chien est mal proportionné"* → on note le pattern dans learnings + on relance V4 corrigée.

### ÉTAPE 9 — LOGGER DANS creative-learnings.md

**OBLIGATOIRE avant de fermer la session.** Bloc complet :
- Date, brief, type, persona, angle, awareness
- Tableau des variations + scores
- Le prompt complet de la meilleure variation
- Ce qui a marché / ce qui n'a pas marché
- Ajustement pour next fois

Si un pattern gagne 2 sessions de suite → l'écrire dans la section "Patterns gagnants identifiés".
Si un défaut revient 2 sessions de suite → l'écrire dans "Patterns à éviter" + le pousser dans le NEGATIVE par défaut du `creative-system.md`.

---

## 🎯 Structure d'un prompt Higgsfield optimisé Barky

> Ne jamais sauter aucune des 10 couches. Un prompt qui en a 7 est un prompt mauvais.

```
[STYLE & MEDIUM]
Editorial lifestyle photography (or: still life, or: 
documentary), shot on [film stock — Kodak Portra 400 
default for Barky], [grain level], [analog warmth].

[ART DIRECTION REFERENCE]
In the visual language of [Aesop / Kinfolk / Cereal /
The Gentlewoman / Hims / Ritual / Le Labo — pick 2-3].
Photographer reference: [Cass Bird / Annie Spratt /
Wim Wenders / Tim Walker / Annie Leibovitz portraiture
— pick 1-2].

[SCENE / SUBJECT]
[Describe precisely : who, what, where, when, what 
emotional state, what they're doing right now, what's
in their hands, what's behind them. 50-100 words 
minimum on this layer.]

[COMPOSITION & FRAMING]
[Shot type — medium / close / wide], [angle — eye-level
/ slight high / low], [rule of thirds — subject at 
which third], [negative space placement], [aspect 
ratio — explicit "4:5 portrait orientation" for Meta].

[CAMERA / LENS / TECHNIQUE]
Shot on [Leica M6 / Hasselblad 500cm / Mamiya RZ67 / 
Canon AE-1] with [Summilux 35mm f/1.4 / Zeiss Planar 
80mm f/2.8 / specific lens], aperture [f/1.4 to f/4],
ISO [100-400 default], shutter [1/125 to 1/500],
depth of field [shallow / medium], focus on [eyes /
hands / product].

[LIGHTING]
[Time of day — late morning / golden hour / overcast
midday], [direction — north window left / 45° from
upper right / backlit], [quality — soft diffused /
hard rim with soft fill / single softbox], 
[falloff — gentle gradient to amber shadow / sharp
to deep black]. NO flash, NO overhead fluorescent,
NO mid-day sun.

[COLOR PALETTE]
Dominant: [color from Barky palette — cite hex].
Secondary: [color from Barky palette — cite hex].
Breathing space: [neutral from Barky palette — cite hex].
Skin tones: Portra-warm if subject. Total saturation:
desaturated 15-20% from raw. AVOID bright primaries,
saturated reds, neon, electric blue, navy, orange.

[MOOD / ATMOSPHERE]
[2-3 specific feelings — quiet love / methodical 
calm / Sunday morning intimacy / apothecary ritual /
contemplative trust]. The feeling of [one specific
sensory anchor — the smell of dried eucalyptus /
the warmth of late morning oak / the sound of a 
slow kettle].

[POST-PRO / GRADING]
Visible film grain at 100%, [vignette intensity —
subtle / medium / heavy], [shadow lift — slight /
medium], [highlight roll-off — gentle warm / sharp
clean], [halation — fine on light sources / none],
[fade — slight on blacks / none].

[NEGATIVE PROMPT — AVOID ABSOLUTELY]
[Coller bloc complet depuis creative-system.md §4.2
NEGATIVE — toujours, jamais raccourcir]
```

---

## 🚫 Anti-patterns du workflow

> À ne jamais faire, sous aucun prétexte.

| Anti-pattern | Pourquoi mauvais | À faire à la place |
|---|---|---|
| Générer un prompt de 50 mots "vite fait" | Qualité de sortie médiocre, on perd les crédits Higgsfield | Toujours 10 couches, 250-500 mots |
| Une seule variation | Pas de comparaison possible, pas d'apprentissage | Minimum 3 variations |
| Skipper la lecture de creative-learnings.md | On répète les erreurs passées | Lecture obligatoire, sans exception |
| Générer le pot Barky en IA | Forme exacte non reproductible, AI slop | Toujours composer le packshot réel |
| Générer un chien en gros plan en IA | Uncanny valley pet niche, conversion tuée | Photo réelle, ou silhouette/blur background |
| Ignorer le NEGATIVE PROMPT | Output dérive vers les défauts IA standards | Bloc NEGATIVE complet, jamais raccourci |
| Composer la typo dans Higgsfield | Gibberish 99% du temps | Typo posée en post-prod (Figma) |
| Pas logger après la session | Pas d'apprentissage cumulé | Bloc complet dans creative-learnings.md |
| Pousser un visuel sans checklist 12 points | DGCCRF ou cohérence brand violée | Checklist `creative-system.md` §7 |

---

## 🎯 Variations à toujours générer (par TYPE)

### LIFESTYLE
- **V1** : medium shot, sujet 1/3 gauche, espace négatif droit pour overlay typo
- **V2** : close-up sur main + détail (pot, geste, expression), max intimité
- **V3** : wide cinematic, environnement dominant, sujet petit dans le frame

### PRODUCT HERO
- **V1** : top-down 45°, flat-lay éditorial avec props
- **V2** : eye-level natural, pot sur surface lifestyle (table, étagère)
- **V3** : macro contre-jour, packaging en silhouette / texture

### TYPO FORTE
- **V1** : fond plâtre brun ambré texturé, vignette douce
- **V2** : fond bleu pastel dégradé soft, atmosphère matin
- **V3** : fond avec photo abstraite (texture pelage chien close-up, ou contre-jour ingrédient)

### PROOF
- **V1** : flat-lay table de cuisine avec lettre + ingrédients réels
- **V2** : portrait du véto (quand dispo) ou main de fondateur tenant le pot
- **V3** : cadre vide éditorial pour intégrer screenshot review

---

## ⚙️ Settings Higgsfield par défaut Barky

À utiliser sauf brief contraire :

```
ratio: "4:5"  # Meta feed default 1080×1350
model: "soul-pro" ou équivalent qualité max — vérifier models_explore
quality: "max" / "high"
seed: random (sauf itération sur un visuel précis)
guidance_scale: 7.5-8.5 (medium-high pour respecter le brief)
steps: 50+ (qualité, pas vitesse)
negative_prompt: [bloc complet du creative-system.md §4.2]
```

---

## 📅 Conservation et nommage des outputs

```
08-ads/statics/{YYYY-MM-DD}/
├── _session-log.md                                   ← brief + contexte de la session
├── v1-{type}-p{n}-{angle-slug}-1080x1350.png         ← variation 1
├── v2-{type}-p{n}-{angle-slug}-1080x1350.png
├── v3-{type}-p{n}-{angle-slug}-1080x1350.png
└── final/                                            ← compositions finales avec typo overlay
    ├── final-v1-...png
    └── final-v1-...psd                               ← .psd Photoshop si disponible
```

**Règle de garbage** : si une variation score ≤ 2 → elle reste dans le dossier daté pour archive (apprentissage), mais ne sort jamais sur Meta. Si une variation score 4-5 → la copier ET dans `final/` ET tagger dans `creative-learnings.md` "Prompts haute performance".

---

## 🔁 Rythme cible (post-validation S6)

| Cadence | Action |
|---|---|
| **Hebdo (lundi)** | 1 session 3 variations sur l'angle prio de la semaine |
| **Hebdo (jeudi)** | 1 session "fork" sur la variation gagnante de la semaine d'avant (continuité créative) |
| **Mensuel** | 1 session "exploration radicale" — sortir du template, tester un registre nouveau (mood-board contrarian) |

**Total mensuel attendu** : 8-12 statics validés, dont 5-7 pushés en Meta Ads.

---

*Fichier créé le 2026-05-05.*
*À mettre à jour quand un nouveau MCP / outil change la séquence, ou quand on identifie un nouvel anti-pattern.*
