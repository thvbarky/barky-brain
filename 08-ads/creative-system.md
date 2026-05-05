# Barky Creative System — Higgsfield Production Bible

> **À quoi sert ce fichier.** C'est la **bible de production** des statics Meta Ads Barky via Higgsfield. Lu en tête de chaque session de génération. Définit l'identité visuelle non-négociable + les frameworks de prompt designer-grade qui sortent des visuels au niveau Aesop / Ritual / Hims, pas des banalités IA.
>
> **Source de vérité visuelle** : [`01-identite/marque.md`](../01-identite/marque.md) + [`01-identite/assets/media-library.md`](../01-identite/assets/media-library.md).
>
> **Source de vérité messages / personas** : [`16-veille/contexte-veille.md`](../16-veille/contexte-veille.md) + [`02-marche/personas.md`](../02-marche/personas.md) + [`02-marche/angles.md`](../02-marche/angles.md).
>
> **Source de vérité légal** : [`04-legal/allegations.md`](../04-legal/allegations.md).

---

## PARTIE 1 — IDENTITÉ VISUELLE (NON NÉGOCIABLE)

### 1.1 Palette absolue

```
PRIMAIRE (toujours, dans 100% des visuels)
┌─────────────────────┬─────────────────────┐
│  Bleu pastel        │  Brun ambré          │
│  #CADCE4            │  #463432             │
│  RGB 202,220,228    │  RGB 70,52,50        │
│  "Dusty pastel blue,│  "Warm dark amber,   │
│   muted, powdery"   │   chocolate-leather" │
└─────────────────────┴─────────────────────┘

SECONDAIRE (respiration, jamais dominante)
┌─────────────────────┬─────────────────────┐
│  Blanc cassé        │  Noir profond        │
│  #F5F0EB            │  #1A1412             │
│  "Warm off-white,   │  "Deep warm black,   │
│   cream linen"      │   espresso shadow"   │
└─────────────────────┴─────────────────────┘
```

**Règle de mix** : un visuel Barky ne dépasse JAMAIS 4 couleurs visibles. Idéal = 2 couleurs primaires + 1 respiration neutre.

### 1.2 Typographie

- **Display & headlines** : Recoleta (toutes graisses, mais privilégier Bold / SemiBold pour l'impact)
- **Body / micro-copy** : Instrument Sans (web) ou Inter (système)
- **Règle absolue** : la typo se compose **TOUJOURS en post-prod** (Figma / Photoshop). Higgsfield n'écrit jamais de texte sur le visuel — les modèles d'image génèrent du gibberish, c'est le signe #1 d'AI slop.

### 1.3 Mood — l'ADN visuel

> **Le brief en une phrase** : *Apothicaire moderne français rencontre wellness éditorial New York. Sérieux pharma + chaleur humaine. Calme adulte, jamais cute, jamais clinique froid.*

**Références mood (à NOMMER explicitement dans les prompts)** :
- **Aesop** — apothicaire chic, photographie ambient, palette terreuse
- **Ritual** — wellness pharma adulte, packshot premium minimaliste
- **Hims / Hers** — modern apothecary, feel premium accessible
- **Le Labo** — artisan éditorial, papiers craft, lumière rasante
- **AG1 (Athletic Greens)** — moléculaire scientifique mais chaleureux
- **Sunday Riley** — packshot lifestyle muted tones
- **Kin Euphorics** — cinematic dreamy mais grounded
- **Magazine refs** : Cereal, Kinfolk, Apartamento, The Gentlewoman

**Mood à BANNIR (verbe AVOID dans les prompts)** :
- ❌ Pet industry standard (chiot mignon, fond bleu ciel saturé, typo arrondie cute)
- ❌ Stock photo générique (souriants devant fond blanc)
- ❌ Clinical médical froid (labo blanc, gants bleus)
- ❌ Cartoon, illustration, 3D rendering, CGI
- ❌ Saturation HDR, ombres dures, flash on-camera

### 1.4 Direction lumière

| Type de visuel | Lumière prescrite |
|---|---|
| Lifestyle home | Soft window light, north-facing, late morning, soft shadows |
| Lifestyle outdoor | Golden hour (1h avant coucher), backlight, hazy atmosphere |
| Product hero | Soft directional studio light, single softbox, gradient shadow |
| Editorial flat-lay | Overcast diffused light, no hard shadows, slight vignette |
| Macro / détail | Hard rim light + soft fill, dramatic but warm |

**Règle absolue** : **JAMAIS** de flash on-camera, **JAMAIS** de néon, **JAMAIS** de mid-day sun écrasant, **JAMAIS** de fluorescent strip lighting.

### 1.5 Palette filmique (à demander explicitement à Higgsfield)

> Citer **un film stock réel** dans chaque prompt = +30% de qualité instantanée vs "natural color".

| Film stock | Caractère | Quand l'utiliser |
|---|---|---|
| **Kodak Portra 400** | Tons chair chauds, peau réaliste, légère désaturation | Lifestyle avec maître + chien (DEFAULT) |
| **Kodak Gold 200** | Doré chaleureux, golden hour intensifié | Outdoor matin / fin d'aprèm |
| **Fuji Pro 400H** | Pastels doux, désaturation poétique | Product hero, packshot lifestyle |
| **Cinestill 800T** | Tungsten, halations rouges, mood cinematic | Indoor mood, ambient soir |
| **Ilford HP5+ 400** | Noir & blanc grain prononcé | Founder content, build-in-public |

---

## PARTIE 2 — RÈGLES DE COMPOSITION META ADS

### 2.1 Formats

| Format | Dimensions | Usage |
|---|---|---|
| **Portrait 4:5** | **1080×1350px** | **DEFAULT** Meta feed (le plus performant 2026) |
| Carré 1:1 | 1080×1080px | Polyvalent feed, IG profile grid |
| Story 9:16 | 1080×1920px | IG/FB Stories, Reels covers |
| Landscape 1.91:1 | 1200×628px | Lien dans l'ad (rare en 2026) |

### 2.2 Zones de sécurité

```
┌────────────────────────────┐  ← top safe zone : 250px
│      [bandeau libre]       │
├────────────────────────────┤  ← début zone éditable
│                            │
│                            │
│        ZONE TEXTE          │
│      (centrée, 60%         │
│       de la largeur)       │
│                            │
│                            │
├────────────────────────────┤  ← fin zone éditable
│   [bandeau CTA optionnel]  │
└────────────────────────────┘  ← bottom safe zone : 250px
```

- **Marge sécurité** : 20% de chaque bord (ne jamais coller un élément contre le bord)
- **Texte sur visuel** : 20% max de la surface (règle Meta historique, soft-removed mais reach pénalisé si dépassé)
- **CTA / logo** : toujours dans le tiers inférieur, jamais bord à bord

### 2.3 Hiérarchie visuelle (loi obligatoire)

Un static Barky a **UN SEUL point focal**. Pas deux. Pas trois.

```
RANG 1 — Point focal (le sujet ou la phrase qui interrompt)
RANG 2 — Contextualisation (qui parle ? à qui ? pourquoi ?)
RANG 3 — Logo + CTA (toujours en bas, discret, fixe)
```

**Test des 0,5 secondes** : montre le visuel à quelqu'un pendant une demi-seconde. Si la personne ne peut pas répéter l'idée principale → le visuel a échoué la hiérarchie.

---

## PARTIE 3 — LES 4 TYPES DE STATICS BARKY

> Chaque type a son propre prompt template. **Ne jamais mélanger les types** dans un même visuel — un static Barky est soit Lifestyle, soit Product Hero, soit Typo Forte, soit Proof. La fusion crée de l'AI slop.

### TYPE 1 — LIFESTYLE
*Chien + maître dans contexte quotidien authentique. Pas de pose, pas de regard caméra forcé.*

**Quand l'utiliser** : ouvrir un funnel froid (Problem Aware), vendre l'émotion avant le produit. P1 surtout.

**Photo réelle obligatoire pour le chien.** Higgsfield génère uniquement le **contexte / mood / lumière** autour, ou des silhouettes d'arrière-plan flou.

### TYPE 2 — PRODUCT HERO
*Packaging Barky dans un environnement lifestyle premium, jamais sur fond blanc plein.*

**Quand l'utiliser** : Solution Aware → Product Aware. Audiences chaudes, retargeting visiteurs LP.

**Packshot réel** (depuis `01-identite/assets/photos/packshot/`) **+ background Higgsfield généré** (table en chêne, drap de lin, contre-jour soft window).

### TYPE 3 — TYPO FORTE
*Phrase courte percutante (l'angle hero) sur fond mood Barky, chien en filigrane / arrière-plan, ou fond uni travaillé.*

**Quand l'utiliser** : interrupt direct. *"'C'est l'âge' : la fausse raison qui empêche..."*. Le hero des hero.

**Higgsfield génère uniquement le fond** (texture, gradient, photo abstraite). La typo se pose en post-prod.

### TYPE 4 — PROOF
*Avis client, témoignage, screenshot review, ou ingrédient mis en avant avec autorité (scientifique sans être clinique).*

**Quand l'utiliser** : audiences chaudes, retargeting BOF, dernière brique de réassurance.

**Souvent zéro Higgsfield** (collage propre de screenshots), ou Higgsfield uniquement pour le mood-frame autour.

---

## PARTIE 4 — LE PROMPT HIGGSFIELD DESIGNER-GRADE

> **Principe** : un prompt basique sort un visuel basique. Un prompt riche en spécifications photographiques précises sort un visuel exceptionnel. Higgsfield est **trained sur 100M+ images annotées photographiquement** — il répond mieux à du jargon photo qu'à du jargon marketing.

### 4.1 Architecture du prompt master (10 couches)

Un prompt Barky de classe pro contient ces 10 couches, dans cet ordre :

```
[COUCHE 1 — STYLE & MEDIUM]
[COUCHE 2 — ART DIRECTION REFERENCE]
[COUCHE 3 — SCENE / SUBJECT]
[COUCHE 4 — COMPOSITION & FRAMING]
[COUCHE 5 — CAMERA / LENS / TECHNIQUE]
[COUCHE 6 — LIGHTING]
[COUCHE 7 — COLOR PALETTE]
[COUCHE 8 — MOOD / ATMOSPHERE]
[COUCHE 9 — POST-PRO / GRADING]
[COUCHE 10 — NEGATIVE PROMPT]
```

### 4.2 Template master (à customiser par brief)

```
[STYLE & MEDIUM]
Editorial lifestyle photography, shot on 35mm film,
Kodak Portra 400, fine grain, slight halation,
analog warmth, magazine-quality.

[ART DIRECTION REFERENCE]
In the visual language of Aesop campaigns crossed with
Kinfolk magazine and Cereal magazine — quiet apothecary
modern, French wellness editorial, never pet-industry
generic. Photographer reference: Cass Bird softness,
Annie Spratt natural light intimacy, Wim Wenders
contemplative composition.

[SCENE / SUBJECT]
[Decrire ICI précisément la scène : qui / quoi / où / 
quand / dans quel état émotionnel — voir §4.3 par TYPE]

[COMPOSITION & FRAMING]
[Ex : medium shot from waist up, rule of thirds, subject
left third, generous negative space right, eye-level
camera, slight high-angle to compress depth]

[CAMERA / LENS / TECHNIQUE]
Shot on Leica M6 with Summilux 35mm f/1.4, 
shallow depth of field f/2, ISO 400, 1/250s, 
subtle motion blur if movement, sharp on the eyes.

[LIGHTING]
Soft directional north-facing window light, late morning,
diffused through linen curtain, falloff into soft amber
shadow. No flash, no hard shadows, no overhead light.

[COLOR PALETTE]
Muted earth tones dominated by dusty pastel blue
(#CADCE4 — powdery, almost grey-blue) and warm dark
amber (#463432 — chocolate-leather brown). Cream linen
whites (#F5F0EB) for breathing space. Desaturated overall,
analog film color science, Portra warmth on skin tones.
NO bright primary colors, NO saturated reds or oranges,
NO neon, NO electric blue, NO navy.

[MOOD / ATMOSPHERE]
Calm, trusted, premium accessible, real and lived-in.
Adult, never cute. Warm but not sentimental. Quiet
confidence. The mood of someone who cares deeply but
without anxiety. French apothicaire moderne meets
New York wellness editorial.

[POST-PRO / GRADING]
Subtle film grain, gentle vignette, slightly lifted
shadows, warm highlights, fine halation around 
light sources. Slightly faded blacks (analog feel,
not crushed digital).

[NEGATIVE PROMPT — AVOID ABSOLUTELY]
AVOID: cartoon, illustration, 3D render, CGI, anime,
stock photo aesthetic, oversaturated colors, HDR,
hard direct flash, studio strobe, harsh shadows,
clinical white background, plain white seamless,
overly staged poses, smiling at camera, "happy 
family" stock vibe, pet industry generic
(cute puppies on bright blue, cartoon paw prints,
"woof woof" energy), text in image, watermarks,
logos generated, distorted hands, distorted dog
anatomy, uncanny valley dog, AI plastic skin,
extra fingers, deformed limbs, low resolution,
blurry, jpeg artifacts, oversharpened,
orange palette, navy blue, primary saturated red,
neon green, electric pink, rainbow colors,
generic bokeh balls, film LUT overkill,
Instagram filter, beauty retouching, 
airbrushed skin, plastic doll texture.
```

### 4.3 Prompt par TYPE de static

#### TYPE 1 — LIFESTYLE (avec photo chien réelle composée en post)

```
[STYLE]
Editorial lifestyle photography, 35mm film, Kodak Portra
400, magazine-grade, analog warmth, fine grain.

[REF]
Aesop campaign meets Kinfolk magazine. Cass Bird
softness. Quiet, lived-in, French apothecary modern.

[SCENE — exemple P1 angle "C'est l'âge"]
A French woman in her late forties, soft natural makeup,
casual cashmere sweater in dusty oat color, sitting on 
a worn leather sofa in a sun-dappled Parisian apartment, 
hand reaching down towards a senior dog out of frame
(off-frame intentionally — leaves room for compositing
the actual photo), tender expression, looking down at
the dog with quiet love, not posing for the camera,
caught in a real moment.

[FRAMING]
Medium shot from waist up, woman positioned right third
of frame, generous negative space on the left where
the dog will be composited in post-production, 
eye-level camera, slight forward lean of subject.

[CAMERA]
Leica M6, Summilux 35mm f/1.4 wide open, ISO 400,
shallow depth of field, focus on her eyes,
soft falloff on the leather and curtains.

[LIGHTING]
Late morning soft window light from the right, 
filtered through linen sheers, warm cream highlights,
soft amber shadow falloff into the leather sofa.
Single light source, no fill, real apartment light.

[COLOR]
Dusty pastel blue (#CADCE4) on the linen curtain in 
background, warm dark amber (#463432) on the worn
leather sofa, cream linen whites (#F5F0EB) on her 
sweater. Skin tones in Portra warmth — slightly
peachy, never orange. Overall desaturated 15%.

[MOOD]
Quiet love, recognized care, the calm of a Sunday
morning. Not sad, not falsely happy. The kind of 
intimate moment a stranger walking by a window would
glimpse for half a second.

[POST]
Film grain visible at 100%, subtle vignette, lifted
shadows, warm highlights, fine halation on the 
window light.

[AVOID]
AVOID: studio look, smiling at camera, posed, 
stock photo "happy lifestyle" feel, harsh light, 
saturated colors, primary reds, navy, orange, 
pet industry cliches, cartoon, 3D, HDR.
```

#### TYPE 2 — PRODUCT HERO (autour du packshot réel)

```
[STYLE]
Still life product photography, Aesop / Le Labo
campaign aesthetic, shot on Hasselblad medium format,
Kodak Portra 160, magazine-grade, soft analog tones.

[REF]
Aesop store still life crossed with Sunday Riley
flat-lay editorials. Apothicary modern, premium
accessible, French wellness adulthood.

[SCENE]
A pristine empty wooden surface (oak, faded honey
warm tones, visible grain) on which a small product
will be composited (the actual Barky jar — placeholder
in background for now). Surrounding props: a single
sprig of dried eucalyptus leaning into frame from the 
right, a folded square of natural undyed linen with 
slight wrinkles bottom-left, a single ceramic spoon
in matte clay-brown left of center.

[FRAMING]
Top-down 45° angle, square composition, product
placeholder centered, generous breathing space all
around, props arranged in asymmetric balance with 
golden ratio.

[CAMERA]
Hasselblad 500cm, Zeiss Planar 80mm f/2.8, ISO 100,
f/4 aperture, sharp full-depth, slight perspective
compression.

[LIGHTING]
Single large softbox window-style light from upper
left at 45°, soft fill from white card right, gentle
shadow falloff to upper right showing warm wood grain.

[COLOR]
Background: warm dark amber (#463432) wooden surface
with honey-oak warm tones. Props: cream linen
(#F5F0EB), dusty pastel blue (#CADCE4) hint on 
ceramic glaze. Eucalyptus desaturated sage. Total 
palette: 3 colors max, all from the Barky system.

[MOOD]
Quiet ritual, considered ingredients, apothecary
craft. The viewer should feel the surface is warm
to touch, the linen freshly washed, the eucalyptus
just clipped this morning.

[POST]
Subtle warm grade, deepened amber shadows, soft 
highlight rolloff, light film grain.

[AVOID]
AVOID: bright white seamless background, studio
catalog feel, harsh top-down clinical, oversaturated
greens, vivid colors, plastic surfaces, glossy 
reflections, primary reds or blues, neon, navy,
orange, generic flat-lay Pinterest look,
"flatlay aesthetic" overdone tropes (gold pineapples,
pink flamingos, marble), pet industry props
(no bones, no paw prints, no fake "natural" 
ingredients), AI rendering, 3D, CGI.
```

#### TYPE 3 — TYPO FORTE (fond pour pose typo en post)

```
[STYLE]
Abstract editorial backdrop, large-format film
photography, Polaroid 8x10 aesthetic, ultra-fine 
grain, painterly soft focus zones.

[REF]
The Gentlewoman magazine cover backdrops, Apartamento
interior moody walls, Aesop store atmospherics.

[SCENE]
A textured warm dark amber painted plaster wall
(#463432 base), uneven brushwork visible at macro,
faint cream linen texture creeping in from one corner,
soft directional shadow falling across the lower third
suggesting an unseen window. NO objects in frame,
PURE atmospheric backdrop ready to receive overlaid
typography in post-production.

[FRAMING]
Full frame backdrop, 4:5 portrait orientation 
(1080×1350), centered composition, plaster texture
filling all of frame, subtle vignette darkening the
corners by 20%.

[CAMERA]
Mamiya RZ67 medium format, Sekor 110mm f/2.8,
shallow texture depth, sharpness on plaster grain.

[LIGHTING]
Single soft directional light raking across the wall
from left at 70° angle, creating subtle texture
shadow play. Falloff to slight darkness right side.

[COLOR]
Dominant: warm dark amber (#463432) plaster, with
natural variation from #3A2A28 (deeper shadow) to
#5C4641 (light catch). Subtle cream linen breathing
space (#F5F0EB) in upper corner, occupying max 15%
of frame. NO other colors.

[MOOD]
Apothecary atelier wall, weathered French townhouse,
contemplative empty space, ready for one strong
sentence. The mood of a museum gallery just before
opening hours.

[POST]
Heavy film grain (Polaroid-like), deep vignette,
warm shadow rolloff, subtle texture sharpening.

[AVOID]
AVOID: any text in image, any typography, any logos,
any objects, distracting details, busy texture, 
patterns, geometric shapes, bright colors, primary
saturation, orange, navy, neon, gradient backgrounds,
digital smoothness, plastic look, CGI, 3D render.
```

#### TYPE 4 — PROOF (mood-frame autour de testimonial)

```
[STYLE]
Editorial documentary photography, 35mm Kodak Portra
400, candid magazine-style, slight motion blur if
applicable.

[REF]
The Gentlewoman portrait series crossed with 
Apartamento home documentaries. Real people in 
real spaces.

[SCENE]
A handwritten letter on natural cream paper visible
on a worn oak kitchen table, fountain pen resting
diagonally beside it, half-empty cream ceramic mug 
top right, soft daylight from out-of-frame window
left. Composition leaves a clean rectangular zone
center-frame for compositing review screenshot or
testimonial typography in post-production.

[FRAMING]
Top-down vertical 4:5, slight asymmetric balance,
composition leaves clean rectangle 60% of central 
area for post-prod overlay.

[CAMERA]
Leica M6, Summicron 50mm f/2 at f/2.8, ISO 400,
focused on letter's texture, slight blur on mug
edges.

[LIGHTING]
Soft window light from upper left, late morning
warm tone, gentle highlight on paper texture, 
soft amber shadow on oak grain.

[COLOR]
Cream linen / paper (#F5F0EB) dominant in cleared
zone, warm dark amber (#463432) oak table around,
dusty pastel blue (#CADCE4) hint on the ceramic
mug. 3-color discipline.

[MOOD]
Honest, lived-in, considered. The kind of letter
someone writes once a year to thank someone they
care about. Quiet authenticity.

[POST]
Subtle film grain, warm grade, soft vignette,
analog feel.

[AVOID]
AVOID: text in image, generated handwriting (it
will look fake), readable letter content, 
distracting details, modern digital props
(no laptops, no phones), studio look, primary
colors, orange, navy, plastic, 3D, CGI.
```

---

## PARTIE 5 — INCARNATION DES PERSONAS DANS LES VISUELS

> Ne jamais générer un personnage générique. Spécifie l'âge, la décennie, la classe sociale visible, l'état émotionnel, et l'environnement. Higgsfield répond beaucoup mieux à un brief précis.

### P1 — La Maîtresse qui Refuse d'Accepter le Déclin
**Âge** : 45-58 ans
**Apparence** : naturelle, soft makeup discret, cheveux mi-longs souvent attachés bas, lunettes lecture éventuelles, mains qui ont vécu (légère usure, alliance)
**Vêtements** : cashmere oat, lin écru, jean droit, pull col rond, foulard léger, palette neutre — JAMAIS streetwear, JAMAIS color block
**Lieu type** : appartement parisien lumineux, maison ancienne dans le sud, jardin clos, balade en forêt domaniale
**Chien** : 8-16 ans, **PHOTO RÉELLE de la photothèque** (Cane Corso senior, Goldendoodle, ou bêta-testeur futur)
**État émotionnel à capter** : tendresse calme, regard vers le bas, demi-sourire pas pour la caméra, présence patiente

**Verbes pour le prompt** : *quiet love, tender, lived-in, contemplative, patient, considered, warm-eyed*

### P2 — La Maîtresse Hyper-Informée Carences
**Âge** : 32-45 ans
**Apparence** : cheveux propres souvent en chignon ou couette, lunettes éventuelles, vernis nude ou nu, traits réfléchis
**Vêtements** : pull oversize cachemire, chemise lin, pantalon ample lin / coton bio, palette terreuse — bio-mode adulte, JAMAIS fast fashion saturée
**Lieu type** : cuisine ouverte propre avec ingrédients frais visibles (fenil, herbes en pots), table de prep en chêne, ustensiles inox brossé, livre de nutrition canine ouvert
**Chien** : 2-7 ans, race moyenne ou grande active (Border Collie, Bouvier Bernois, Goldendoodle), **photo réelle**
**État émotionnel à capter** : concentration sereine, regard analytique, mains qui mesurent / préparent, contrôle apaisé

**Verbes pour le prompt** : *focused, considered, methodical, calm precision, informed care*

### À NE JAMAIS générer
- ❌ Femme < 28 ans (P1 et P2 sont des adultes mûres, pas des étudiantes)
- ❌ Famille nucléaire générique souriante face caméra
- ❌ Couple jeune et "fun" en mode lifestyle Instagram
- ❌ Personnage qui regarde directement l'objectif avec un grand sourire
- ❌ Streetwear, sportswear, mode rapide saturée
- ❌ Background luxe ostentatoire (granit poli, dorures, marbre vit)

---

## PARTIE 6 — RÈGLES LÉGALES DGCCRF DANS LE TEXTE OVERLAY

> Le visuel Higgsfield ne contient JAMAIS de texte. Le texte se pose en post-prod. Mais c'est dans cette phase que la conformité légale se joue.

### ✅ Verbes safe (utilisation libre)
- *soutient · contribue à · favorise · participe à · accompagne*
- *complète · enrichit · optimise · apporte · couvre*

### 🟡 Verbes zone jaune (valider avant push)
- *renforce* (borderline médical — préférer "soutient")
- *cliniquement testé* (uniquement si étude réelle)
- *recommandé par les vétérinaires* (uniquement si comité véto réel et nommé)

### ❌ Verbes interdits (refus Meta + risque DGCCRF)
- *traite · soigne · guérit · prévient · remplace*

### ❌ Termes à BANNIR absolument
- "vet-grade" / "qualité vétérinaire"
- "cliniquement prouvé" sans étude sourcée
- Chiffres non sourcés (*"90% des chiens..."*, *"3x plus efficace"*)
- Comparaisons médicament vétérinaire
- Avant/après santé visuels (refus Meta automatique)
- "FDA-Registered", "NASC", "Made in Vermont" (références US, non pertinentes en FR)

### Reformulations safe (mécaniques)

| Au lieu de | Dire |
|---|---|
| "Renforce l'immunité" | "Soutient la vitalité au quotidien" |
| "Soigne les carences" | "Complète l'alimentation pour un apport optimal" |
| "Traite les douleurs articulaires" | "Soutient la mobilité quotidienne" |
| "Guérit l'anxiété" | "Contribue à un état apaisé" |
| "Prévient les démangeaisons" | "Favorise une peau saine et un pelage brillant" |

### ✅ Claims tenables au lancement
- Clean Label · Fabriqué en France · Certifié FEDIAF · Garantie Queue Remuante 60 jours · Abonnement sans engagement · Tests indépendants par lot · Formulé avec un comité vétérinaire (quand effectif)

### Mention obligatoire packaging
*« Aliment complémentaire pour chiens »*

---

## PARTIE 7 — CHECKLIST PRÉ-PUSH (à passer avant chaque export final)

Avant qu'un static parte sur Meta, il passe ces 12 contrôles :

- [ ] **Palette** : 100% bleu pastel + brun ambré + neutres, ZÉRO orange/navy/saturé
- [ ] **Hiérarchie** : un seul point focal, test 0,5s passé
- [ ] **Format** : exporté à la dimension exacte (1080×1350 ou 1080×1080)
- [ ] **Zone sécurité** : 20% de marge sur les 4 bords respectée
- [ ] **Texte ≤ 20%** de la surface
- [ ] **Logo** : posé en post-prod, pas généré, dans le tiers inférieur
- [ ] **Typo** : Recoleta uniquement pour les titres, pas de typo générique
- [ ] **Persona** : conformité P1 ou P2, vêtements + lieu + état émotionnel
- [ ] **Chien** : si présent en gros plan = photo réelle, jamais Higgsfield
- [ ] **DGCCRF** : aucun verbe rouge, claims sourçables
- [ ] **Mood** : adulte / warm / apothicaire — pas cute, pas clinique, pas stock
- [ ] **AI slop check** : zéro mains déformées, zéro doigts en trop, zéro texte gibberish, zéro chien à 5 pattes

---

## PARTIE 8 — POURQUOI CES PROMPTS SONT LONGS

> "On me dira que mes prompts sont longs. Je dirais qu'ils sont précis."

Higgsfield (et tous les modèles diffusion modernes) répondent à la **densité d'information photographique** plus qu'à la longueur. Les 10 couches du template existent parce que :

1. **STYLE & MEDIUM** force le modèle hors du registre "stock photo" par défaut
2. **ART DIRECTION REF** ancre dans des esthétiques que le modèle a vraiment apprises (Aesop, Kinfolk = des tonnes de training data)
3. **SCENE / SUBJECT** précis = le modèle ne brode pas
4. **FRAMING** dirige la composition (sinon le modèle centre tout)
5. **CAMERA / LENS** est la couche la plus sous-utilisée — citer un lens réel + un f-stop = qualité photographique réelle
6. **LIGHTING** sépare un visuel pro d'un visuel amateur. Sans cette couche, fluorescent par défaut.
7. **COLOR** verrouille la palette Barky. Sans cette couche, le modèle dérive vers la saturation.
8. **MOOD** est la couche émotionnelle — sans elle, expressions vides
9. **POST-PRO** ajoute le grain et l'analogique qui font la différence cinéma vs digital
10. **NEGATIVE** est la couche la plus puissante — elle bloque les défauts récurrents IA. **Toujours la garder, même longue.**

---

## PARTIE 9 — RÈGLES MÉTA (les 5 commandements)

1. **Mécanisme > feature.** Le visuel doit montrer comment Barky agit (l'ingrédient en gros plan, le rituel quotidien, la conséquence concrète sur le chien), pas juste qu'il existe.
2. **Le maître culpabilise — n'aggrave jamais.** Barky est un acte d'amour éclairé, pas un reproche. Pas de visuels qui pointent du doigt l'erreur du maître.
3. **Le chien n'est jamais en premier plan produit.** Le chien est dans la scène, mais le hero c'est le rituel, le pot, ou le maître. Sinon on devient pet industry standard.
4. **Une créa = une idée.** Si tu hésites entre deux angles, tu fais deux créas. Pas une qui essaie de tout dire.
5. **Si ça pourrait être une ad pour Royal Canin → tu rates.** Si ça pourrait être une ad pour Aesop, Hims, ou Ritual → tu y es.

---

*Dernière mise à jour : 2026-05-05 — création du fichier.*
*Mise à jour automatique attendue à chaque session de génération qui révèle un nouveau pattern.*
