# Brand Assets — Index automatique

> **À quoi sert ce fichier.** Avant chaque génération Higgsfield, Claude lit ce fichier pour savoir quels assets physiques sont disponibles dans le repo. **Les assets eux-mêmes vivent dans `01-identite/assets/`** (source de vérité unique). Ce fichier est leur **table d'aiguillage** pour le workflow ads.
>
> **Règle.** Pas de duplication. Si tu as besoin d'un visuel, tu pointes vers `01-identite/assets/...`. Si tu génères un nouveau visuel, il atterrit dans `08-ads/statics/{date}/` avec un nom explicite.
>
> **Mise à jour.** À chaque ajout d'asset dans `01-identite/assets/`, mets à jour ici aussi. Le détail descriptif et les droits sont dans [`../../01-identite/assets/media-library.md`](../../01-identite/assets/media-library.md) — ne pas dupliquer.

---

## 🎨 Logo

| Asset | Chemin | Usage prompt Higgsfield |
|---|---|---|
| Logo brun ambré sur fond bleu pastel | `01-identite/assets/logo/Barky.svg` | Hero, ads, header landing |
| Logo brun ambré transparent (sans fond) | `01-identite/assets/logo/Barky marron sans fond.svg` | À poser sur n'importe quel fond clair |
| Logo brun ambré sur fond brun (alt) | `01-identite/assets/logo/Barky fond marron.svg` | Packaging, footer dark |

**Convention overlay** : ne JAMAIS demander à Higgsfield de générer le logo Barky (le modèle n'est pas trained dessus, résultat dégueu garanti). Le logo se compose **toujours en post-prod** (Figma / Photoshop) sur le visuel généré.

---

## 🎨 Palette officielle (à coller en RGB/HEX dans tous les prompts)

| Couleur | HEX | RGB | Rôle |
|---|---|---|---|
| Bleu pastel | `#CADCE4` | `202, 220, 228` | Accent principal, fonds clairs |
| Brun ambré | `#463432` | `70, 52, 50` | Fond premium, autorité |
| Blanc cassé | `#F5F0EB` | `245, 240, 235` | Respiration, texte sur fond brun |
| Noir profond | `#1A1412` | `26, 20, 18` | Body text, contraste maximum |

**Palette à BANNIR de tous les prompts** (verbe "AVOID" obligatoire) : `orange`, `navy blue`, `bright primary colors`, `saturated reds`, `electric blue`, `neon`, `rainbow`.

---

## 🔤 Typographie

| Police | Chemin | Usage |
|---|---|---|
| Recoleta Regular | `01-identite/assets/Recoleta/Recoleta Regular.otf` | Titres body |
| Recoleta Medium | `01-identite/assets/Recoleta/Recoleta Medium.otf` | Sous-titres |
| Recoleta SemiBold | `01-identite/assets/Recoleta/Recoleta SemiBold.otf` | Headlines secondaires |
| Recoleta Bold | `01-identite/assets/Recoleta/Recoleta Bold.otf` | Hero headlines |
| Recoleta Black | `01-identite/assets/Recoleta/Recoleta Black.otf` | Display max impact |
| Recoleta Light | `01-identite/assets/Recoleta/Recoleta Light.otf` | Body élégant |
| Recoleta Alt (toutes les graisses) | `01-identite/assets/Recoleta/Recoleta Alt *.otf` | Variante alternative |

**Police body / fallback web** : Instrument Sans (Google Fonts) ou Inter (system).

**Convention overlay** : la typo se compose **toujours en post-prod** (jamais générée par Higgsfield — les modèles d'image sont catastrophiques sur le texte).

---

## 📦 Packshot disponibles

| Asset | Chemin | Description courte | Idéal pour |
|---|---|---|---|
| Pot fermé bleu pastel | `01-identite/assets/photos/packshot/packshot-pot-ferme-bleu-pastel.png` | Pot brun ambré fermé, fond bleu pastel uniforme | Hero ad, product reveal |
| Pot ouvert bleu pastel | `01-identite/assets/photos/packshot/packshot-pot-nuages.png` | Pot brun + 1 bouchée, fond bleu nuageux | Editorial, magazine |
| Pot dos ingrédients | `01-identite/assets/photos/packshot/packshot-pot-dos-ingredients.png` | Étiquette ingrédients visible (⚠️ contient texte du benchmark Dog is Human, cropper) | Section "12 actifs" — usage limité |
| Bouchées 3 nuages | `01-identite/assets/photos/packshot/packshot-bouchees-3-nuages.png` | 3 bouchées fond bleu nuageux | Feature texture, social |
| Bouchées vue dessus | `01-identite/assets/photos/packshot/packshot-bouchees-vue-dessus.png` | Tas vue du dessus, fond bleu pastel | Format bouchée, thumbnails |

**Règle d'or packshot** : on ne génère PAS le pot Barky en IA (forme exacte non reproductible). Le packshot vient toujours de la photothèque réelle, et Higgsfield génère **autour** (background, lifestyle, mood).

---

## 🐶 Lifestyle (chien + maître + situation réelle)

| Asset | Chemin | Race / situation | Persona ciblé |
|---|---|---|---|
| Beagle cuisine | `01-identite/assets/photos/lifestyle/lifestyle-beagle-cuisine-bouchee.png` | Beagle mange bouchée, cuisine | P1 / appétence |
| Bichon dos cuisine | `01-identite/assets/photos/lifestyle/lifestyle-bichon-cuisine-dos.png` | Bichon de dos, planche cuisine | P2 / rituel |
| Bouledogue tapis | `01-identite/assets/photos/lifestyle/lifestyle-bouledogue-francais-tapis.png` | Bouledogue + 2e chien fond, tapis berbère | P1 / multi-chien |
| Cane Corso foulard | `01-identite/assets/photos/lifestyle/lifestyle-cane-corso-foulard.png` | Grand chien gris, foulard, main donne bouchée | P1 / senior grand gabarit |
| Corgi gazon | `01-identite/assets/photos/lifestyle/lifestyle-corgi-gazon.png` | Corgi, langue, gazon | P1 / palatabilité |
| Couple petit chien | `01-identite/assets/photos/lifestyle/lifestyle-couple-petit-chien.png` | Couple jeune, petit chien dans bras | P1 / aspirationnel famille |
| Goldendoodle herbe | `01-identite/assets/photos/lifestyle/lifestyle-goldendoodle-herbe.png` | Goldendoodle outdoor + pot | P1 / outdoor énergie |
| Jack Russell canapé | `01-identite/assets/photos/lifestyle/lifestyle-jack-russell-canape.png` | Jack Russell sur canapé regarde pot, main féminine | P1 / lifestyle home |

**Règle d'or lifestyle** : si la créa demande un chien → **photo réelle de la photothèque ou UGC bêta-testeur**. Higgsfield ne génère **PAS** de chien en gros plan (uncanny valley ravageuse en pet niche). Si Higgsfield génère un chien, c'est uniquement en **silhouette / arrière-plan flou / pelage texture macro abstrait**.

---

## 🎁 Unboxing

| Asset | Chemin | Usage |
|---|---|---|
| Box ouverte + pot + balle | `01-identite/assets/photos/unboxing/unboxing-box-pot-balle-tagline.png` | Hero unboxing, social proof, deck |

---

## 📰 Editorial / inspiration

| Asset | Chemin | Usage |
|---|---|---|
| Composition aliments actifs | `01-identite/assets/photos/editorial/editorial-composition-aliments-actifs.png` | Section "12 actifs", éditorial premium |
| Benchmark Dog is Human (EN) | `01-identite/assets/photos/editorial/editorial-benchmark-infographic-en-DO-NOT-USE.png` | 🚫 Référence inspiration uniquement, ne pas utiliser tel quel |

---

## 📁 Dossiers de travail (pour les générations à venir)

```
08-ads/
├── statics/
│   └── {YYYY-MM-DD}/         ← chaque session crée son dossier daté
│       ├── v1-{type}-{persona}-{angle}.png
│       ├── v2-{...}.png
│       ├── v3-{...}.png
│       └── _session-log.md   ← log de la session (prompts + scores)
├── references/
│   ├── ads/                  ← screenshots ads concurrents inspirants
│   ├── brands/               ← refs DA hors-niche (Aesop, Ritual, Hims, Le Labo, AG1)
│   └── moodboards/           ← planches de mood par angle/persona
└── assets/
    ├── logo/                 ← lien symbolique conceptuel vers 01-identite/assets/logo/
    ├── palette/              ← (vide — palette dans creative-system.md)
    ├── packaging/            ← lien symbolique conceptuel vers 01-identite/assets/photos/packshot/
    └── fonts/                ← lien symbolique conceptuel vers 01-identite/assets/Recoleta/
```

**Convention nommage statics générés** :
`v{n}-{type}-{persona}-{angle-slug}-{format}.png`

Exemples :
- `v1-lifestyle-p1-cest-lage-1080x1350.png`
- `v2-typo-p1-cest-lage-1080x1350.png`
- `v3-product-hero-p2-7-carences-1080x1080.png`

---

## ⏳ Manquants identifiés (à shooter / produire)

- [ ] **Portraits comité véto** (4 portraits carrés, fond bleu pastel) — pour section autorité
- [ ] **Founder Thomas** (portrait pro + behind-the-scenes labo) — pour build-in-public TikTok + ads founder voice
- [ ] **Macro bouchée croquée** (close-up texture, lumière rasante) — pour section appétence
- [ ] **Logo bleu pastel sur brun PNG 1200×1200** — fallback raster pour ads Meta
- [ ] **Photothèque chien senior** (8+ ans, vraies bêtes, P1 dominante) — actuellement on n'a qu'un Cane Corso et un Goldendoodle, manque de vrais seniors visibles
- [ ] **Packshot avec balle de tennis brandée seule** (sans box) — pour visuels gimmick UGC

---

*Dernière mise à jour : 2026-05-05 — création du fichier.*
