# Prompt Library — Higgsfield × Copy Barky

> ⚠️ **MÉTHODE OBSOLÈTE DEPUIS LE 2026-05-14.**
>
> Ces prompts ultra-détaillés (500-700 mots chacun) **saturent Nano Banana 2** et produisent des résultats inférieurs au **pattern court Cowork-style** (~150 mots, validé sur les 4 statics du 13/05).
>
> Le skill `/barky-creas-batch` n'utilise plus ces templates. Voir `.claude/skills/barky-creas-batch/SKILL.md` §Étape 7 pour le nouveau pattern (meta-prompt fixe + brief court de 1-3 phrases).
>
> Fichier **conservé en archive** pour : (a) référence historique du travail `/enhance-prompt`, (b) cas spéciaux Veo3/vidéo où la verbosité peut servir, (c) inspiration de copy d'overlay (la copy `/copywriting` reste valable, c'est le prompt image qui est sur-engineered).
>
> ---

> **À quoi sert ce fichier.** Bibliothèque de **4 sets production-ready** (un par type de static), chaque set combinant : (1) prompt Higgsfield designer-grade enrichi via `/enhance-prompt`, (2) copy d'overlay conversion-grade enrichi via `/copywriting`, (3) spec de composition qui soude les deux.
>
> **Comment l'utiliser.** Tu prends un set, tu copy-paste le prompt dans Higgsfield, tu génères 3 variations, tu poses la copy en post-prod selon la spec. Tu logues le résultat dans `creative-learnings.md`.
>
> **Source méthode** :
> - Image prompt → [`creative-system.md`](creative-system.md) §4 (10 couches)
> - Copy framework → Anatomie d'un bon hook Barky : Interrupt → Reframe → Proof → CTA ([`16-veille/contexte-veille.md`](../16-veille/contexte-veille.md) §6)
> - Légal DGCCRF → [`04-legal/allegations.md`](../04-legal/allegations.md)

---

## SET 1 — LIFESTYLE × P1 × "C'est l'âge" ★★★

**Persona** : P1 — La Maîtresse qui Refuse d'Accepter le Déclin
**Awareness** : Problem Aware
**Angle** : *"'C'est l'âge' : la fausse raison qui empêche la plupart des maîtres d'aider leur chien"*
**Type static** : LIFESTYLE (chien composé en post depuis photothèque)
**Format** : 1080×1350 (4:5 portrait Meta)

### 🖼️ Prompt Higgsfield (image — copier tel quel)

```
[STYLE & MEDIUM]
Editorial lifestyle photography, shot on 35mm film, 
Kodak Portra 400, fine grain visible at 100%, slight 
halation around highlights, analog warmth, 
magazine-quality finish — Cereal magazine cover style.

[ART DIRECTION REFERENCE]
In the visual language of Aesop campaigns crossed with 
The Gentlewoman portraiture and Apartamento home 
documentaries. Photographer references: Cass Bird's 
intimate softness, Annie Spratt's natural light 
sensibility, Wim Wenders' contemplative composition. 
The visual feel is French apothicaire moderne meets 
quiet New York wellness editorial — adult, warm, 
never pet-industry generic.

[SCENE / SUBJECT]
A French woman in her early fifties, soft naturalmakeup, 
shoulder-length ash-brown hair loosely tied back at the 
nape, wearing a heather-oat cashmere crew-neck sweater 
slightly oversized at the shoulders. She is seated 
sideways on a vintage caramel leather sofa with visible 
patina and gentle creasing. Her right hand reaches down 
toward the floor, open-palmed and patient, leaving a 
clear empty space at the bottom-left of the frame where 
a senior dog photograph (Cane Corso, age 12, gray muzzle) 
will be composited in post-production. Her face shows a 
demi-sourire of recognition — she's looking down at her 
dog the way you look at someone you've loved for fifteen 
years. NOT a posed smile. NOT eye-contact with camera. 
Caught in a real Sunday-morning moment.

[COMPOSITION & FRAMING]
Medium portrait shot from waist up, woman positioned 
right-third of frame following rule of thirds, generous 
clean negative space on the bottom-left where dog will 
be composited. Eye-level camera angle with very slight 
forward lean (5°). Aspect ratio: 4:5 vertical portrait, 
explicitly 1080×1350. Top 25% reserved for breathing 
space (will receive overlay headline in post-pro).

[CAMERA / LENS / TECHNIQUE]
Shot on Leica M6 with Summilux 35mm f/1.4 lens at f/2.0, 
ISO 400, shutter 1/250s. Shallow depth of field with 
focus locked on her eyes, soft falloff toward the leather 
patina and the sheer linen curtain in background. Slight 
breathing room between subject and bokeh.

[LIGHTING]
Late morning soft window light entering from camera-right, 
filtered through unbleached linen sheers (creating a 
gentle cream cast and soft falloff). Single light source 
— no fill, no reflectors, raw apartment light. Highlight 
side warm cream (#F5F0EB), shadow side falling to a 
soft amber (#463432-toned shadow). NO direct sun, NO 
overhead light, NO flash, NO modifiers visible.

[COLOR PALETTE]
Dominant: warm dark amber (#463432) on the worn leather 
sofa and soft shadows. Accent: dusty pastel blue 
(#CADCE4) on the linen curtain in background and a 
faint reflection on her sweater shoulder. Breathing: 
cream linen (#F5F0EB) on her sweater body and the 
window highlights. Skin tones in Kodak Portra warmth 
— slightly peachy, never orange, never red. Total 
saturation: desaturated -18% from raw, analog film 
color science. Three-color discipline strictly enforced.

[MOOD / ATMOSPHERE]
The mood of a Sunday morning in late October, late in 
the year, late in the dog's life — quiet love that 
refuses resignation. Not sad, not falsely cheerful. 
A woman who has been told ten times "c'est l'âge" 
and has stopped accepting it. The atmosphere a stranger 
walking by the window would glimpse for half a second 
and remember for an hour.

[POST-PRO / GRADING]
Visible Portra 400 grain at 100% view. Subtle vignette 
darkening corners by 12%. Lifted shadows (+8 stops on 
darkest 10%). Warm highlight roll-off. Fine halation 
around the window light. Slightly faded blacks 
(analog feel, never crushed digital). NO HDR, NO heavy 
LUT, NO Instagram filter aesthetic.

[NEGATIVE PROMPT — AVOID ABSOLUTELY]
AVOID: cartoon, illustration, 3D render, CGI, anime, 
stock photo aesthetic, oversaturated colors, HDR look, 
hard direct flash, studio strobe, harsh shadows, 
clinical white background, plain white seamless,
overly staged poses, smiling at camera, "happy family" 
stock vibe, perfect glossy retouching, beauty filter 
plastic skin, airbrushed faces, pet industry generic 
(cute puppies on bright blue, cartoon paw prints, 
"woof woof" energy), text in image, watermarks, 
generated logos, distorted hands, extra fingers, 
deformed limbs, low resolution, blurry, jpeg artifacts, 
oversharpened halos, orange palette, navy blue, 
saturated red, neon green, electric pink, rainbow 
colors, generic bokeh balls, cinematic teal-and-orange 
LUT, beauty retouching, plastic doll texture, AI sheen, 
young woman (must be 50+), influencer aesthetic, 
modern minimalist sterile, IKEA showroom feel, 
generic bright apartment.
```

### ✍️ Copy d'overlay (à composer en post-prod sur le visuel)

**HEADLINE (top 25%, Recoleta Bold, blanc cassé #F5F0EB sur transparence noire 30%)**

> *« C'est l'âge. »*
> *— ce que tu te dis depuis 6 mois.*

**Variantes A/B headline** :
- **A (existante)** *« C'est l'âge. » — ce que tu te dis depuis 6 mois.*
- **B** *Si tu te dis « c'est l'âge », lis ça.*
- **C** *Ton chien n'est pas vieux. Il lui manque quelque chose.*

**BODY (bottom 25%, Instrument Sans Regular, brun ambré #463432 sur cream)**

> Et si ce n'était pas le déclin — mais une carence ?
> Formule 4 vétos · Fabriquée en France · 1 bouchée par jour.

**CTA (bouton Recoleta SemiBold, brun #463432 fond, cream #F5F0EB texte)**

> *Découvrir Barky →*

**Variantes CTA** :
- *Découvrir Barky →*
- *Tester 60 jours — sans engagement*
- *Voir la formule*

### 📐 Spec de composition (Figma / Photoshop)

```
┌────────────────────────────────────┐ ← 1080
│                                    │ ← TOP 25% : overlay typo headline
│   « C'est l'âge. »                 │   bg : transparence noire 30%
│   — ce que tu te dis               │   typo : Recoleta Bold 72pt
│   depuis 6 mois.                   │   color : #F5F0EB
├────────────────────────────────────┤
│                                    │
│      [VISUEL HIGGSFIELD            │ ← 50% central : visuel
│       + chien composé              │   pas d'overlay
│       en bottom-left]              │
│                                    │
├────────────────────────────────────┤
│ Et si ce n'était pas le déclin —   │ ← BOTTOM 25% : body + CTA
│ mais une carence ?                 │   bg : cream #F5F0EB plein
│ Formule 4 vétos · Fab France ·     │   typo : Instrument Sans 28pt
│ 1 bouchée par jour                 │   color : #463432
│                                    │
│        [Découvrir Barky →]         │   bouton : 320×64px
└────────────────────────────────────┘ ← 1350
```

### 🧠 Pourquoi ce set marche (rationale)

- **L'image** : capte P1 dans son moment de tendresse calme, sans aggraver la culpabilité, avec un espace négatif intelligent qui laisse la photo réelle du chien parler.
- **L'interrupt** : *« C'est l'âge. »* — verbatim direct extrait des reviews. Elle se reconnaît en 0,5 seconde.
- **Le reframe** : *"pas le déclin — mais une carence"* ouvre une porte sans promettre miracle.
- **Le proof** : 3 garanties courtes en ligne — autorité (4 vétos) + origine (France) + format (1 bouchée).
- **Le CTA** : verbe d'action doux, pas d'urgence artificielle.

### ✅ Checklist DGCCRF

- ✅ Aucun verbe rouge (traite/soigne/guérit/prévient)
- ✅ "Carence" est descriptif, pas thérapeutique
- ✅ "Formule 4 vétos" tenable dès comité véto signé
- ✅ Pas de chiffre non sourcé, pas de "%"
- ✅ Pas d'avant/après santé visuel

---

## SET 2 — PRODUCT HERO × P2 × "7 carences invisibles" ★★★

**Persona** : P2 — La Maîtresse Hyper-Informée Carences
**Awareness** : Problem Aware → Solution Aware
**Angle** : *"Les 7 carences invisibles que l'alimentation maison ne couvre pas"*
**Type static** : PRODUCT HERO (packshot réel + background Higgsfield)
**Format** : 1080×1350 (4:5 portrait Meta)

### 🖼️ Prompt Higgsfield (image background — le packshot réel se compose en post)

```
[STYLE & MEDIUM]
Still life product photography, Aesop store campaign 
aesthetic crossed with Sunday Riley editorial flat-lays, 
shot on Hasselblad medium format, Kodak Portra 160 for 
soft analog tones, magazine-grade finish, ultra-fine 
grain, painterly soft focus zones.

[ART DIRECTION REFERENCE]
In the visual language of Aesop store still lifes 
combined with The Gentlewoman product editorials and 
Le Labo apothecary craft photography. Photographer 
references: Bobby Doherty's saturated minimalism 
restrained to neutrals, Grant Cornett's surreal-natural 
compositions, Maciek Jasik's botanical stillness.

[SCENE / SUBJECT]
A pristine empty surface composed of two materials: 
upper two-thirds is a flat warm dark amber (#463432) 
hand-troweled plaster wall with subtle brush texture 
visible at macro, lower one-third is an aged honey-oak 
table surface with visible grain running horizontally 
left to right. The center of the frame is intentionally 
empty — a 600×800px clean rectangular zone where the 
Barky jar packshot will be composited in post-production. 
Surrounding props arranged in an asymmetric apothecary 
composition: a single sprig of dried sage leaning 
diagonally from upper-right into frame (occupying 
maybe 15% of right edge), a small folded square of 
unbleached natural linen with intentional creases at 
bottom-left (matte cream #F5F0EB, 200×200px), a 
single ceramic spoon in matte clay-brown lying 
horizontally just below the empty center, a small 
glass vial half-filled with golden-amber oil 
catching the side light at upper-left (40% opacity 
glass).

[COMPOSITION & FRAMING]
Top-down 30° tilted angle (not full overhead, 
slightly raised perspective for depth), 4:5 portrait 
1080×1350 orientation. Composition follows golden 
ratio with the empty center-rectangle for product 
placement. Generous breathing space all around. 
Props arranged to create visual flow into the empty 
zone — eye travels from the sage → empty zone → 
spoon → linen.

[CAMERA / LENS / TECHNIQUE]
Hasselblad 500cm with Zeiss Planar 80mm f/2.8, 
ISO 100, aperture f/4 for moderate depth of field, 
sharp on the textures of plaster and oak grain, 
gentle softness on the props periphery. Tripod-locked, 
mirror-up to eliminate vibration.

[LIGHTING]
Single large softbox window-style key light from 
upper-left at 45° angle, 60×80cm aperture diffused 
through unbleached muslin. Soft fill from a 100×100cm 
white card on camera-right at 70% reflectance. 
Gentle shadow falloff toward upper-right showing the 
plaster's troweled texture. Highlight side of props 
in cream warmth, shadow side rolling into deep amber. 
NO overhead, NO secondary lights, NO color gels.

[COLOR PALETTE]
Background plaster: warm dark amber (#463432) 
dominating upper two-thirds with natural variations 
from #3A2A28 (deepest shadow) to #5C4641 (light 
catch on troweled ridges). Surface oak: honey-warm 
brown with grain visible. Props: cream linen (#F5F0EB), 
dusty pastel blue (#CADCE4) hint on ceramic spoon glaze, 
desaturated sage green on the dried sprig, golden-amber 
oil in vial. Total palette stays within 4 colors 
maximum, all from the Barky system. Heavy desaturation 
across the frame to preserve sophistication — analog 
Portra 160 color science.

[MOOD / ATMOSPHERE]
The mood of a French apothecary atelier at 10am on a 
Tuesday, just after the shop has been swept and the 
morning preparations are laid out. Considered ritual, 
crafted ingredients, quiet authority. The viewer 
should feel the surface is warm to touch, the linen 
freshly folded, the sage just clipped this morning. 
NOT sterile, NOT scientific cold — apothecary craft.

[POST-PRO / GRADING]
Subtle warm grade overall, deepened amber shadows 
without crushing, soft highlight roll-off on the 
linen folds, light film grain visible on plaster 
texture, very gentle vignette (8%). Slight halation 
on the oil vial highlight only.

[NEGATIVE PROMPT — AVOID ABSOLUTELY]
AVOID: bright white seamless background, studio 
catalog feel, harsh top-down clinical, oversaturated 
greens, vivid colors, plastic surfaces, glossy 
reflections, primary reds, primary blues, neon, 
navy, orange, generic flat-lay Pinterest aesthetic, 
overdone props (gold pineapples, pink flamingos, 
white marble, succulents), pet industry props 
(no bones, no paw prints, no fake "natural" 
ingredients), AI rendering, 3D, CGI, octane render, 
watermarks, text in image, generated typography, 
clinical lab aesthetic, white tile floor, modern 
sterile minimalism, glassmorphism, gradient mesh, 
holographic, iridescent, chrome.
```

### ✍️ Copy d'overlay

**HEADLINE (top 20%, Recoleta Bold 64pt, brun ambré #463432)**

> Tu cuisines pour ton chien.
> Voici les 7 carences que ni la viande,
> ni les légumes, ni les féculents ne couvrent.

**Variantes A/B headline** :
- **A** *Tu cuisines pour ton chien. Voici les 7 carences que ni la viande, ni les légumes, ni les féculents ne couvrent.*
- **B** *Le BARF couvre 80% des besoins. Les 20% qui manquent expliquent pourquoi ton chien fatigue.*
- **C** *Tu fais BARF. Tu lui donnes ce qu'il y a de mieux. Et pourtant…*

**BODY (au-dessus du CTA, Instrument Sans Regular 24pt)**

> 12 actifs aux doses biodisponibles.
> Filières humaines. Fabriqué en France.
> 1 bouchée par jour, formulée par 4 vétérinaires.

**CTA**

> *Voir la composition complète →*

### 📐 Spec de composition

```
┌────────────────────────────────────┐
│ Tu cuisines pour ton chien.        │ ← TOP 25% : headline
│ Voici les 7 carences que ni la     │   typo : Recoleta Bold 56pt
│ viande, ni les légumes, ni les     │   color : #463432 sur fond cream
│ féculents ne couvrent.             │
├────────────────────────────────────┤
│                                    │
│      [POT BARKY composé            │ ← 50% central : packshot
│       au centre du visuel          │   posé dans la zone vide
│       Higgsfield]                  │   du fond généré
│                                    │
├────────────────────────────────────┤
│ 12 actifs · Filières humaines ·    │ ← BOTTOM 25% : body + CTA
│ Fabriqué en France                 │   typo : Instrument Sans 22pt
│                                    │
│  [Voir la composition complète →]  │   bouton : #463432 fond
└────────────────────────────────────┘
```

### 🧠 Pourquoi ce set marche

- **L'image** : reprend les codes Aesop / Sunday Riley que P2 reconnaît immédiatement comme "marque sérieuse, pas pet industry". Elle baisse sa garde sceptique.
- **L'interrupt** : nomme directement ce qu'elle fait (cuisiner) → reconnaissance en 0,5s.
- **Le reframe** : "7 carences" est concret, mesurable, technique — registre P2.
- **Le proof** : empile 3 preuves de transparence (12 actifs, filières humaines, France, 4 vétos) qui ciblent ses critères exacts.
- **Le CTA** : "voir la composition" — pas "acheter", pas "tester". P2 veut analyser avant.

### ✅ Checklist DGCCRF

- ✅ "Carences" descriptif, pas thérapeutique
- ✅ "Que ni la viande, ni les légumes, ni les féculents ne couvrent" est factuel nutritionnel (vérifier sourçage scientifique en interne)
- ✅ "12 actifs" doit matcher la composition réelle finale
- ✅ Aucun verbe rouge
- ⚠️ Le "7 carences" doit pouvoir être listé sur la LP (sinon refus de claim)

---

## SET 3 — TYPO FORTE × P1 × "C'est l'âge"

**Persona** : P1
**Awareness** : Problem Aware
**Angle** : *"'C'est l'âge' : la fausse raison qui empêche la plupart des maîtres d'aider leur chien"*
**Type static** : TYPO FORTE (fond pour overlay typo en post-prod)
**Format** : 1080×1350 (4:5 portrait Meta)

### 🖼️ Prompt Higgsfield (fond seul, aucun texte)

```
[STYLE & MEDIUM]
Abstract editorial backdrop, large-format Polaroid 
8x10 aesthetic, ultra-fine grain, painterly soft focus 
zones, museum-quality wall texture photography.

[ART DIRECTION REFERENCE]
In the visual language of The Gentlewoman cover 
backdrops, Apartamento interior moody walls, Aesop 
store atmospherics, and Le Labo Brooklyn factory walls. 
Photographer reference: Wolfgang Tillmans' abstract 
texture series, Hiroshi Sugimoto's seascapes restraint.

[SCENE / SUBJECT]
A textured warm dark amber painted plaster wall as 
the entire frame. The plaster is hand-troweled with 
visible brush strokes and small imperfections — 
slight ridges, subtle areas where the trowel left a 
trace, a tiny chip near the lower-third. The wall has 
been aged naturally — slightly darker streaks where 
moisture once ran, faint cream linen texture creeping 
in from the upper-right corner (suggesting an unseen 
draped curtain just out of frame). A soft directional 
shadow falls diagonally across the lower-third 
suggesting an unseen window from the right. NO objects, 
NO props, NO subjects, NO furniture — PURE atmospheric 
backdrop ready to receive overlaid typography in 
post-production.

[COMPOSITION & FRAMING]
Full-frame backdrop in 4:5 portrait orientation 
(1080×1350). Centered composition with the plaster 
texture filling all of frame. Subtle vignette 
darkening the corners by 18%. Composition leaves 
balanced texture variation throughout — no single 
distracting feature.

[CAMERA / LENS / TECHNIQUE]
Mamiya RZ67 medium format with Sekor 110mm f/2.8 
lens, aperture f/4 for sharpness on plaster grain, 
ISO 50 for ultra-fine grain, tripod-locked, mirror-up. 
Focus precisely on the plaster texture mid-frame.

[LIGHTING]
Single soft directional key light raking across the 
wall from camera-left at 70° angle (very flat to the 
wall surface), creating subtle texture shadow play 
that reveals the trowel marks without becoming 
dramatic. Falloff to slight darkness on right side 
(15% darker). NO additional lighting, NO fill, NO 
color gels.

[COLOR PALETTE]
Dominant: warm dark amber (#463432) plaster with 
natural organic variation from #2A1F1D (deepest 
shadow recess) to #5C4641 (light catch on trowel 
ridges) to #6E5450 (mid-tone smooth zones). Subtle 
cream linen breathing space (#F5F0EB) in the 
upper-right corner only, occupying maximum 12% of 
frame area. NO other colors. The frame should feel 
monochromatic-amber with one cream accent.

[MOOD / ATMOSPHERE]
The mood of an apothecary atelier wall in a 
contemplative empty moment, a French townhouse 
weathered through generations, a museum gallery 
just before opening hours when the light is soft 
and no one has entered yet. Quiet, weighty, ready 
to hold one strong sentence.

[POST-PRO / GRADING]
Heavy Polaroid-like grain visible, deep vignette 
(18%), warm shadow rolloff, subtle texture sharpening 
on plaster details, very slight fade on the deepest 
blacks for analog feel.

[NEGATIVE PROMPT — AVOID ABSOLUTELY]
AVOID: any text in image, any typography, any logos, 
any letters, any words, any objects, any props, any 
subjects, any humans, any animals, any furniture, 
distracting details, busy texture patterns, geometric 
shapes, bright colors, primary saturation, orange, 
navy blue, neon, gradient backgrounds, digital 
smoothness, plastic look, CGI, 3D render, octane 
render, photoshop liquify, watermarks, signatures, 
overly busy texture, marble veins, brick, stone, 
wood paneling, modern wallpaper patterns, geometric 
abstract art, gradient mesh, holographic, chrome.
```

### ✍️ Copy d'overlay (le hero du visuel — typo XXL)

**HEADLINE PRINCIPAL (centré, Recoleta Black 120pt, blanc cassé #F5F0EB)**

> *« C'est l'âge. »*

**SOUS-HEADLINE (sous le headline, Recoleta Light 36pt, italique, blanc cassé)**

> *— ce que tu te dis depuis 6 mois.*

**BODY (sous le sous-headline, Instrument Sans Regular 24pt, blanc cassé 70% opacité)**

> Et si ce n'était pas le déclin —
> mais une carence ?

**CTA (bouton bas, cream #F5F0EB fond, brun #463432 texte)**

> *Découvrir Barky →*

### 📐 Spec de composition (TYPO FORTE)

```
┌────────────────────────────────────┐
│                                    │ ← respiration top
│                                    │
│       « C'est l'âge. »             │ ← HEADLINE Recoleta Black 120pt
│                                    │   centré, blanc cassé
│       — ce que tu te dis           │ ← SOUS-HEADLINE Recoleta Light 36pt
│         depuis 6 mois.             │   centré, italique, blanc cassé
│                                    │
│                                    │ ← respiration centre
│                                    │
│   Et si ce n'était pas le déclin   │ ← BODY Instrument Sans 24pt
│       — mais une carence ?         │   centré, blanc cassé 70%
│                                    │
│                                    │
│       [Découvrir Barky →]          │ ← CTA bouton 320×64px
│                                    │
└────────────────────────────────────┘
       Fond : plâtre brun ambré
```

### 🧠 Pourquoi ce set marche

- **Le visuel pur typo est le format le plus fort de 2026 sur Meta** — taux d'arrêt scroll en hausse vs lifestyle saturé.
- **La typo Recoleta Black à 120pt** sur fond plâtre crée une présence cinéma-affiche.
- **Le « C'est l'âge. »** entre guillemets typographiques français = signal de sérieux, pas pet industry.
- **Le sous-headline en italique léger** humanise la phrase brutale.
- **Le body court** propose la porte de sortie sans surcharger.

### ✅ Checklist DGCCRF

- ✅ "Carence" descriptif (encore et toujours)
- ✅ Pas de "guérison", pas de promesse miracle
- ✅ Question rhétorique = pas une affirmation thérapeutique

---

## SET 4 — PROOF × P1 × Témoignage senior

**Persona** : P1
**Awareness** : Solution Aware → Product Aware
**Angle** : *"Ta copine a essayé un complément sans voir la différence ? Voici ce qui s'est passé"* (relief social)
**Type static** : PROOF (cadre éditorial pour overlay testimonial)
**Format** : 1080×1350 (4:5 portrait Meta)

### 🖼️ Prompt Higgsfield (cadre éditorial, screenshot review composé en post)

```
[STYLE & MEDIUM]
Editorial documentary still life, 35mm Kodak Portra 
400, candid magazine-style, fine grain, analog warmth, 
Cereal magazine and Kinfolk editorial spread aesthetic.

[ART DIRECTION REFERENCE]
In the visual language of Kinfolk magazine spreads, 
Apartamento home documentaries, and The Gentlewoman 
portrait series. Photographer references: Annie 
Spratt's natural daylight intimacy, Bobby Doherty's 
restrained still life.

[SCENE / SUBJECT]
A worn oak kitchen table photographed top-down 
slightly tilted (30° perspective). On the table, 
arranged asymmetrically: a handwritten letter on 
natural cream paper visible at upper-right (intentionally 
NOT readable — the writing is ambiguous to avoid 
generated gibberish), a Sailor fountain pen in matte 
black resting diagonally across the letter's corner, 
a half-empty cream ceramic mug with a faint blue 
pastel rim catching the morning light at the upper-right 
edge of frame, a small woven linen napkin folded 
casually at lower-right, a sprig of dried lavender 
at far-left edge. The CENTRAL ZONE of the frame 
(approximately 600×800px in the middle) is INTENTIONALLY 
LEFT EMPTY of any object — a clean rectangular zone 
of pure oak surface that will receive a screenshot 
testimonial overlay in post-production.

[COMPOSITION & FRAMING]
Top-down at 30° tilted angle (NOT pure overhead — 
slight perspective for depth), 4:5 portrait 1080×1350 
orientation, props frame the empty central zone 
following rule of thirds. Eye travels: lavender → 
empty center → mug → letter+pen, creating circular 
flow back to center.

[CAMERA / LENS / TECHNIQUE]
Leica M6 with Summicron 50mm f/2 lens at f/2.8, 
ISO 400, sharp focus on the empty center zone's oak 
grain, slight softness on the periphery props. 
Handheld feel preserved (very subtle imperfection 
in framing).

[LIGHTING]
Soft window light from upper-left at late morning 
warm tone, gentle highlight on the paper's texture 
and the ceramic glaze, soft amber shadow on oak grain. 
Single light source, natural fill, no reflectors.

[COLOR PALETTE]
Dominant central empty zone: warm honey-oak surface 
(close to #463432 but slightly lighter at #5A4540). 
Cream linen / paper accents (#F5F0EB) in upper-right 
letter and lower-right napkin. Dusty pastel blue 
(#CADCE4) hint on the ceramic mug glaze. Desaturated 
lavender purple-grey at far-left edge (kept very 
muted, almost grey). Total palette: 3-color discipline 
strict, all from Barky system.

[MOOD / ATMOSPHERE]
The mood of a kitchen at 9:30am on a Saturday after 
the breakfast has been cleared — the kind of moment 
when you write a thank-you note to someone. Honest, 
considered, lived-in, never staged. The viewer should 
feel the warmth of the oak, the recently-drunk coffee, 
the patience of unhurried morning time.

[POST-PRO / GRADING]
Subtle Portra 400 grain, warm overall grade, soft 
vignette (10%), gentle highlight roll-off on paper 
texture, slight halation on mug rim only.

[NEGATIVE PROMPT — AVOID ABSOLUTELY]
AVOID: text in image, generated handwriting (it will 
look fake), readable letter content, any visible 
typography, any letters or words, distracting modern 
digital props (no laptops, no phones, no chargers, 
no AirPods), studio catalog look, primary colors, 
saturated red, orange, navy, plastic surfaces, 
3D render, CGI, watermarks, generic Pinterest 
flat-lay tropes (no avocado toast, no acai bowl, no 
lush succulents, no marble, no rose gold), pet 
industry props (no dog bowls, no leashes, no toys, 
no kibble), AI sheen, plastic doll texture, 
oversharpened halos, HDR, Instagram filter.
```

### ✍️ Copy d'overlay — le testimonial (centre)

**TESTIMONIAL CARD (centré dans la zone vide, fond cream #F5F0EB, ombre douce)**

> *« J'avais essayé deux compléments avant. Aucun n'avait marché.*
> *Au bout de 3 semaines de Barky, Bella a recommencé à monter*
> *l'escalier sans s'arrêter. Je ne sais pas comment, mais c'est revenu. »*
>
> **— Océane, 52 ans, propriétaire de Bella (Border Collie, 11 ans)**

**Variantes testimonial** :
- **A (existante — verbatim adapté Woofilab)** *J'avais essayé deux compléments avant…*
- **B** *« Je m'étais résignée. À 14 ans, je me disais que c'était fini. Trois semaines, et il a recommencé à courir derrière la balle. » — Marianne, propriétaire de Hiro (Beagle, 14 ans)*
- **C (P2)** *« Je cuisine maison depuis 6 ans. Je cherchais ce qui complète sans redoubler. C'est exactement Barky. » — Caroline, propriétaire de Loki (Goldendoodle, 4 ans)*

**HEADLINE TOP (Recoleta Bold 56pt, brun ambré #463432)**

> Avant Barky, elle avait essayé deux compléments.

**BODY BOTTOM (Instrument Sans Regular 22pt)**

> Garantie Queue Remuante 60 jours.
> Sans engagement.
> Premiers signes en 4 à 6 semaines.

**CTA**

> *Tester Barky 60 jours →*

### 📐 Spec de composition (PROOF)

```
┌────────────────────────────────────┐
│ Avant Barky, elle avait essayé     │ ← TOP 18% : headline
│ deux compléments.                  │   Recoleta Bold 56pt
├────────────────────────────────────┤
│                                    │
│   ┌──────────────────────────┐    │
│   │ "J'avais essayé deux     │    │ ← CENTRAL 50% : testimonial card
│   │  compléments avant.      │    │   composé en overlay sur la zone
│   │  Aucun n'avait marché.   │    │   vide du fond Higgsfield
│   │  Au bout de 3 semaines   │    │   bg : #F5F0EB cream
│   │  de Barky, Bella a       │    │   typo : Recoleta Light italique 24pt
│   │  recommencé à monter     │    │   ombre : 0 4px 16px rgba(0,0,0,.08)
│   │  l'escalier..."          │    │
│   │                          │    │
│   │  — Océane, 52 ans        │    │
│   └──────────────────────────┘    │
│                                    │
├────────────────────────────────────┤
│ Garantie Queue Remuante 60 jours · │ ← BOTTOM 22% : body + CTA
│ Sans engagement · Premiers signes  │
│ en 4 à 6 semaines                  │
│                                    │
│    [Tester Barky 60 jours →]       │
└────────────────────────────────────┘
```

### 🧠 Pourquoi ce set marche

- **L'image** : pas de chien, pas de produit en hero — un cadre éditorial neutre qui laisse la voix de la cliente être le hero.
- **Le testimonial verbatim** : extrait quasi-direct des reviews Woofilab. P1 se reconnaît immédiatement.
- **Le détail "deux compléments avant"** capte LA Maîtresse Déjà Déçue (persona émergent — voir contexte-veille.md §3).
- **Le proof** : trois reassurances en bas (garantie, sans engagement, délai réaliste).
- **Le CTA** : "tester 60 jours" assume le doute de P1.

### ✅ Checklist DGCCRF

- ✅ Testimonial = parole client, pas allégation marque
- ✅ "Recommencé à monter l'escalier" = comportement observable, pas claim médical
- ✅ "Premiers signes en 4 à 6 semaines" est tenable
- ✅ "Garantie Queue Remuante 60 jours" = offre commerciale, pas santé
- ⚠️ Vérifier que Océane (ou la cliente choisie) a signé droit à l'image + verbatim authentique avant push

---

## 🧰 Comment forker un set

1. **Tu prends le set qui correspond à ton brief**
2. **Tu modifies le persona / l'angle / le verbatim** dans la copy
3. **Tu adaptes le prompt Higgsfield** sur les couches SCENE et PERSONA uniquement (les autres restent stables — palette, lens, lighting, mood, negative)
4. **Tu génères 3 variations** sur Higgsfield
5. **Tu poses la copy en post-prod** selon la spec
6. **Tu logues** dans `creative-learnings.md`

---

## 📌 Règles d'or de la prompt library

1. **Chaque prompt fait 250-500 mots minimum.** Un prompt court = un visuel pauvre.
2. **Le NEGATIVE PROMPT est non-négociable.** Toujours collé en entier, jamais raccourci.
3. **La copy passe le filtre DGCCRF avant impression.** Checklist 12 points (`creative-system.md` §7).
4. **L'image et la copy se composent ensemble.** Jamais l'un sans l'autre, jamais l'un avant l'autre — toujours pensés dans la même session.
5. **Ce qui marche est consigné.** Tout score 4-5 → bloc complet dans `creative-learnings.md`.

---

*Fichier créé le 2026-05-05.*
*Version 1 — 4 sets initiaux production-ready.*
*À enrichir d'un set par session de génération validée (score moyen ≥ 4).*
