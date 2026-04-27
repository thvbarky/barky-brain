# Bibliothèque média Barky

> Index unique de tous les assets visuels de la marque. À tenir à jour à chaque ajout.
>
> **Source de vérité palette / logo / typo :** [`../marque.md`](../marque.md).

---

## Arborescence

```
01-identite/assets/
├── logo/
│   ├── barky-logo-brun-sur-bleu.svg     ← version hero / pub
│   ├── barky-logo-bleu-sur-brun.svg     ← version deck / packaging
│   ├── barky-logo-brun-sur-bleu.png     ← fallback raster (1200×400 conseillé)
│   └── barky-logo-bleu-sur-brun.png
├── photos/
│   ├── packshot/                        ← pots, bouchées, étiquettes
│   ├── lifestyle/                       ← chiens + propriétaires en situation
│   ├── unboxing/                        ← box, balle brandée, carte fondateur
│   └── vetos/                           ← portraits comité scientifique (4 vétos)
└── media-library.md                     ← ce fichier
```

---

## Convention de nommage

`{type}-{sujet}-{variante}.{ext}`

Exemples :
- `logo-brun-sur-bleu.svg`
- `packshot-pot-face-1200x1200.jpg`
- `lifestyle-marianne-bella-lyon.jpg`
- `unboxing-box-ouverte-balle-carte.jpg`
- `veto-camille-berton-portrait-square.jpg`

Pas d'espaces, pas d'accents, tout en minuscules, tirets en séparateurs.

---

## Catalogue

### 🎨 Logo

| Fichier | Format | Dimensions | Usage | Statut |
|---|---|---|---|---|
| `logo/Barky.svg` | SVG | vectoriel (1000×1000 viewBox) | Logo brun ambré `#463432` sur fond bleu pastel `#CADCE4` — version hero/publicitaire, header landing | ✅ déposé |
| `logo/Barky marron sans fond.svg` | SVG | vectoriel (1000×1000 viewBox) | Logo brun ambré `#463432` transparent — usage sur fond clair quelconque | ✅ déposé |
| `logo/barky-logo-bleu-sur-brun.svg` | SVG | vectoriel | Logo bleu pastel `#CADCE4` sur fond brun ambré — packaging, footer dark | ⏳ à déposer (ou inversion CSS du SVG transparent) |
| `logo/barky-logo-bleu-sur-brun.png` | PNG | 1200×1200 | Fallback raster pour ads Meta | ⏳ à déposer |

### 📦 Packshot (pot + bouchées + étiquette)

| Fichier | Description | Usage recommandé | Statut |
|---|---|---|---|
| `photos/packshot/packshot-pot-ouvert-bleu-pastel.png` | Pot brun ouvert, couvercle posé dessus, fond bleu pastel uniforme | Hero landing, ads Meta | ✅ |
| `photos/packshot/packshot-pot-ferme-bleu-pastel.png` | Pot brun fermé avec couvercle bronze, fond bleu pastel uniforme | Hero alternative, ads | ✅ |
| `photos/packshot/packshot-pot-nuages.png` | Pot brun + 1 bouchée à droite, fond bleu nuageux atmosphérique | Section éditoriale, hero magazine | ✅ |
| `photos/packshot/packshot-pot-dos-ingredients.png` | Dos du pot avec étiquette ingrédients actifs visible, fond noir | Section "12 actifs" — **⚠️ contient texte « DOGISHUMAN.COM · 105 Ave Madison NY » du mockup, ne pas afficher cette zone, cropper l'étiquette uniquement** | ⚠️ usage limité |
| `photos/packshot/packshot-bouchees-3-nuages.png` | 3 bouchées en gros plan sur fond bleu nuageux | Section produit, social posts | ✅ |
| `photos/packshot/packshot-bouchees-vue-dessus.png` | Tas de bouchées vue du dessus, fond bleu pastel | Section "Format bouchée", thumbnails | ✅ |

### 🐶 Lifestyle (chien + pot en situation)

| Fichier | Description | Usage recommandé | Statut |
|---|---|---|---|
| `photos/lifestyle/lifestyle-jack-russell-canape.png` | Jack Russell sur canapé qui regarde le pot tenu par main féminine | Témoignages, lifestyle premium home | ✅ |
| `photos/lifestyle/lifestyle-beagle-cuisine-bouchee.png` | Beagle qui mange une bouchée directement du pot, cuisine | Section "appétence", démo produit | ✅ |
| `photos/lifestyle/lifestyle-goldendoodle-herbe.png` | Goldendoodle dans l'herbe avec pot, en plein air | Témoignages outdoor, énergie | ✅ |
| `photos/lifestyle/lifestyle-corgi-gazon.png` | Corgi avec langue qui sort, main tenant pot, gazon | Cute / palatabilité, témoignage | ✅ |
| `photos/lifestyle/lifestyle-bouledogue-francais-tapis.png` | Bouledogue français qui regarde main tenant pot, tapis berbère, second chien en fond | Lifestyle premium home, témoignages multi-chien | ✅ |
| `photos/lifestyle/lifestyle-bichon-cuisine-dos.png` | Bichon de dos observant pot Barky sur planche en cuisine, lumière chaude | Section "rituel quotidien", éditorial | ✅ |
| `photos/lifestyle/lifestyle-cane-corso-foulard.png` | Grand chien gris avec foulard à carreaux, main donnant bouchée, fond bleu pastel | Témoignage senior / grand gabarit | ✅ |
| `photos/lifestyle/lifestyle-couple-petit-chien.png` | Couple jeune avec petit chien dans bras, main tenant bouchée, cercle brun ambré | Hero aspirationnel "famille" | ✅ |

### 🎁 Unboxing

| Fichier | Description | Usage recommandé | Statut |
|---|---|---|---|
| `photos/unboxing/unboxing-box-pot-balle-tagline.png` | Box bleu pastel ouverte avec pot brun + balle bleue brandée Barky + texte intérieur "Santé Canine au Plus Haut Standard" | **Featured image landing**, hero unboxing, ads, deck | ✅ |

### 👨‍⚕️ Vétos comité

| Fichier | Description | Usage recommandé | Statut |
|---|---|---|---|
| *(à shooter — 4 portraits comité scientifique)* | | Section "Formulé et loué par 4 vétérinaires" | ⏳ à venir |

### 📰 Editorial / ressources

| Fichier | Description | Usage recommandé | Statut |
|---|---|---|---|
| `photos/editorial/editorial-composition-aliments-actifs.png` | Composition stylisée d'aliments (saumon, fruits, baies, huile) sur disques transparents, fond bleu pastel | Section "12 actifs qualité humaine", éditorial premium | ✅ |
| `photos/editorial/editorial-benchmark-infographic-en-DO-NOT-USE.png` | Infographic icônes "5 Core Benefits" en anglais — **benchmark Dog is Human** | ⚠️ **Référence inspiration uniquement, ne pas utiliser sur landing FR** (claims non DGCCRF + langue) | 🚫 |

---

## Comment alimenter la bibliothèque

**Option A — Drag & drop local (simple)**
1. Glisser le fichier dans le bon sous-dossier `01-identite/assets/...`
2. Renommer selon la convention ci-dessus
3. Ajouter une ligne dans le tableau correspondant ci-dessus
4. `git add` + commit (les SVG/PNG passent sans souci ; au-delà de 5 Mo on bascule sur Git LFS)

**Option B — Lien externe (Drive, Dropbox, Notion)**
1. Mettre un lien partagé public dans le tableau ci-dessus à la place d'un chemin de fichier local
2. Préciser le format et les droits dans la colonne « Description »
3. L'IA téléchargera l'asset au moment d'en avoir besoin (ad, landing, deck)

**Pour la prod web (landing, ads)**
- Compresser les JPG via TinyPNG ou Squoosh (cible : < 200 Ko par image)
- Toujours fournir un alt-text descriptif lors de l'intégration HTML
- Pour les visages humains : autorisation droit à l'image écrite avant publication

---

## Droits & licences

- **Logo Barky** : marque déposée (à confirmer dépôt INPI classes 31, 5, 35)
- **Photos clients / chiens** : autorisation écrite obligatoire avant usage public
- **Photos vétos comité** : contrats à signer (cf. comité scientifique en cours de constitution)
- **Stock externe** (Unsplash, Pexels) : licence CC0 acceptée mais à éviter sur la landing finale → toujours préférer du shooting Barky une fois le produit en main

---

*Dernière mise à jour : 27 avril 2026 — création du dossier.*
