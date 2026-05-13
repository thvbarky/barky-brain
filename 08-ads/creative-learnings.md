# Barky Creative Learnings — Mémoire des générations

> **À quoi sert ce fichier.** Capitaliser sur chaque session de génération Higgsfield. Ce qui marche, ce qui ne marche pas, les ajustements à faire la prochaine fois. **Lu automatiquement avant chaque nouveau prompt.** Plus il est riche, meilleures sont les générations suivantes.
>
> **Règle d'or.** Pas de génération sans logging. À la fin de chaque session, Claude écrit ici. Si Thomas score un visuel < 3 sur 5, on note pourquoi et la correction. Si on score 4-5, on note **ce qui a fait que ça a marché** (c'est plus rare et plus précieux).

---

## Format de log (à dupliquer pour chaque session)

```
### Session {YYYY-MM-DD} — {description courte}

**Brief source** : `08-ads/briefs/brief-{date}.md` (ou inline si pas de fichier)
**Type(s) static** : Lifestyle / Product Hero / Typo Forte / Proof
**Persona ciblé** : P1 / P2
**Angle** : [phrase de l'angle ★★★ depuis 02-marche/angles.md]
**Awareness** : Problem Aware / Solution Aware / Product Aware

**Variations générées** :
| # | Type | Score (1-5) | Verdict |
|---|---|---|---|
| v1 | ... | ... | ... |
| v2 | ... | ... | ... |
| v3 | ... | ... | ... |

**Prompt v{n} (le meilleur)** :
[copier le prompt complet — utile pour réutiliser et fork]

**Ce qui a marché** :
- ...

**Ce qui n'a pas marché** :
- ...

**Ajustement pour la prochaine fois** :
- ...

**Asset(s) gardé(s)** :
- `08-ads/statics/{date}/v{n}-...png` (chemin relatif)
```

---

## 📋 Logs de sessions

### Session 2026-05-13 — RÈGLE ABSOLUE : winner requis pour toute génération

**Verbatim Thomas (lors du 1er test `/barky-creas-batch` 25 combos)** :
> *« Je veux en aucun cas que tu me génères une statique si tu n'as pas de modèle Winner en référence. Ça, là-dessus, c'est intolérable ! Tu me fais des statiques que si et seulement si tu as des références Winner. »*

**Règle absolue actée** : aucune statique générée sans winner de référence concret du swipe file `08-ads/references/ads/`. Tout combo `Référence winner = n/a` est **rejeté de la matrice**. Si pool insuffisant → backlog scrapage avant la prochaine génération.

**Conséquences immédiates** :
- Sur la matrice de 25 combos du 1er batch auto, **8 combos `n/a` retirés** (Lifestyle FR ×5, Proof testimonial ×3) → matrice trimée à 17 combos
- Skill `/barky-creas-batch` §2 et §3.3 mis à jour avec garde-fou strict
- `creative-system.md` Partie 9 : "Winner requis" devient le 1er des 6 commandements
- Mémoire `feedback-creas-winner-required` sauvegardée

**Backlog scrapage prioritaire pour débloquer les angles couverts** :
- Lifestyle FR maître + chien senior (P1) → Dog is Human, Japhy, Elmut, The Farmer's Dog
- Lifestyle FR maître + chien cuisine maison (P2) → idem + Butternut Box
- Testimonial / Proof vétéran chien → Zesty Paws, Dog is Human reviews-driven
- Typo Forte pur fond bleu pastel (non-pet) → Hims, Ritual, AG1
- Founder-pov DTC FR → Lemonade, Elmut founder content
- Science-claim / ingredient-breakdown → AG1, Seed, Symprove

---

### Session 2026-05-13 — Pivot Nano Banana 2 ALL-IN-ONE (validé sur le principe)

**Brief source** : clone du winner Exode `20260513_exode_1080x1080_problem-solution-01` (hook question rhétorique + packshot + 3 icônes bénéfices). Adapté Barky P1 angle ★★★ `cest-lage`.

**Type** : PRODUCT HERO (winner-clone)
**Persona** : P1
**Angle** : `cest-lage` (variante hook ouvert : *"Un complément qui marche VRAIMENT, ça existe ?"*)
**Awareness** : Problem Aware
**Stratégie** : 3e tentative de la journée après 2 rejets bloc (Typo Forte fond brun derive orange + Product Hero Python compositing pas charismatique). Nouveau workflow tout-en-un : Nano Banana 2 rend image + texte FR + icônes en un seul prompt, avec packshot Barky en référence.

**Variations générées** :
| # | Modèle | Workflow | Format / Résolution | Job ID Higgsfield | Statut |
|---|---|---|---|---|---|
| v5 | `nano_banana_2` | All-in-one | 1:1 / 2k (2048×2048) | `cd76b9fa-f932-4e77-9c64-474b76f77ada` | À valider Notion |
| v6 | `nano_banana_2` | All-in-one | 1:1 / 2k (2048×2048) | `7dfeae51-51e9-4eaa-8187-6725c974ee07` | À valider Notion |

**Verdict Thomas (verbatim 2026-05-13)** : *« Écoute, c'est déjà beaucoup mieux ! Il y aurait quelques ajustements à faire, mais ça, je veux te dire, ce sera au cas par cas. Mais, sur le principe, on est déjà bien. »* → **Validé sur le principe**, ajustements précis attendus row par row dans Notion.

**Patterns gagnants (à reproduire)** :
- ✅ **Nano Banana 2 all-in-one** = image + texte FR + icônes en un seul prompt. Texte FR rendu PARFAITEMENT (`complément`, `VRAIMENT`, `ça existe`, `FORMULÉ`, `VÉTÉRINAIRES`, `BOUCHÉE` tous corrects avec accents). Aucun gibberish.
- ✅ **Référence packshot réel** passée en `medias[].role = "image"` → le pot Barky est gardé INTACT (label, drapeau FR, "MULTIVITAMINES", sous-texte 60 bouchées tous lisibles). Crucial pour la cohérence brand.
- ✅ **Fond bleu pastel #CADCE4 dominant** = contraste fort avec pot brun ambré → scroll-stop power. Pas le drapé cream linen pâle qui dilue.
- ✅ **Spell-out explicite** des accents dans le prompt (`é`, `ç`, `É`, `è`) → Nano Banana respecte les caractères français.
- ✅ **Encadré "VRAIMENT" en pill brun/cream** = clone fidèle du pattern "NATUREL" du winner Exode, texte qui pope.
- ✅ **3 icônes line-art simples** (drapeau / stéthoscope / bouchée) demandées explicitement comme `thin outline strokes, NOT illustrated, NOT cartoon` → exactement le rendu obtenu.
- ✅ **Resolution 2k native** : `2048×2048` (au-dessus des 1080 Meta requis → marge pour crop/recompose).

**Ce qui ne marche PAS — patterns à abandonner** :
- ❌ **Higgsfield + Python Pillow compositing** : rejet bloc le 2026-05-13. Verbatim Thomas : *« Le texte a été ajouté par dessus, il n'y a aucune esthétisme ou aucun charisme. Ça n'a rien à voir avec les Winners. »* → workflow définitivement écarté.
- ❌ **`marketing_studio_image` sans texte généré** : visuel propre mais sans hook intégré = "fadasse". Rejeté le 2026-05-13.
- ❌ **Fond brun ambré pur** (Typo Forte) : Nano Banana 2 dérive vers orange-caramel saturé. Voir mémoire `feedback-nano-banana-palette-brune`.
- ❌ **Drapé cream linen pâle** : pas assez de contraste pour faire popper le pot brun, manque de scroll-stop.

**Ajustements pour la prochaine session** :
- Continuer Nano Banana 2 all-in-one comme default Barky (toutes créas, pas juste Product Hero)
- Élargir le pool winners pour d'autres angles : besoin de winners type `ugc-style`, `before-after`, `testimonial` pour les adaptations futures
- Tester un autre angle (carences-invisibles P2, ou compl-moitie-marchent-pas P1) avec le même workflow Nano Banana all-in-one

**Asset(s) gardé(s)** :
- `08-ads/statics/2026-05-13/barky_p1_cest-lage_producthero_v6-nanobanana-allinone.png` (4.7 Mo, 2048×2048)
- `08-ads/statics/2026-05-13/barky_p1_cest-lage_producthero_v5-nanobanana-allinone.png` (4.6 Mo, 2048×2048)
- Raws des sessions précédentes (Typo Forte + Product Hero Pillow) gardés en archive locale pour learning patterns à éviter.

---

### Session 2026-05-13 — Premier test SET 3 Typo Forte P1 "C'est l'âge"

**Brief source** : `08-ads/prompt-library.md` SET 3 (Typo Forte × P1 × angle ★★★ "C'est l'âge")
**Type** : TYPO FORTE
**Persona** : P1 — La Maîtresse qui Refuse d'Accepter le Déclin
**Angle** : *"'C'est l'âge' : la fausse raison qui empêche la plupart des maîtres d'aider leur chien"*
**Awareness** : Problem Aware
**Stratégie** : 1ère génération qui passe par le pipeline complet (winner ref → brief → Higgsfield → push Notion auto). Tester si le SET 3 sort un mur amber suffisamment texturé pour porter un overlay typo XXL en post-prod. Pas de winner direct du pool (les 15 winners 2026-05-13 sont dominés UGC promo, pas Typo Forte pur).

**Variations générées** :
| # | Modèle | Format / Résolution | Job ID Higgsfield | Statut Notion |
|---|---|---|---|---|
| v1 | nano_banana_2 | 4:5 / 1k (928×1152) | `87fcd570-dfc5-4316-8c0f-6a00a0c1de4a` | À valider (https://www.notion.so/35ffd75e0c44818e8a57d3375361b568) |
| v2 | nano_banana_2 | 4:5 / 1k (928×1152) | `2c9a81f2-1ea5-4c9e-9329-830d344ff5b2` | À valider (https://www.notion.so/35ffd75e0c4481c0ad04f4ad93f6144d) |

**Prompt utilisé** : SET 3 du `prompt-library.md` (lignes 392-479), copié intégralement avec ajustement mineur — ajout dans NEGATIVE de "orange palette, caramel saturation" (renforcement explicite du learning 5 mai sur Soul Cinema, gardé par sécurité même sur Nano Banana).

**Insights techniques (avant validation Thomas)** :
- ⚠️ **Resolution 1k par défaut, pas 2k** — `nano_banana_2` n'avait pas de `resolution` explicite dans les params, Higgsfield a appliqué 1k par défaut. Le batch 5 mai avait 2k. **Ajustement : toujours préciser `resolution: "2k"` explicitement dans les params du futur**.
- Dimensions sorties = 928×1152, pas 1080×1350 exact (Nano Banana sort en multiples de 32 sur 1k). À l'export final Figma/Photoshop, upscaler vers 1080×1350 ou regénérer en 2k pour avoir > 1080 native.

**Ce qui a marché** :
- *(rien — les 2 variations rejetées en bloc par Thomas)*

**Ce qui n'a pas marché — verbatim Thomas (2026-05-13)** :
> *« C'est quoi ce résultat de merde ? Le but, c'est d'avoir une putain de créative qui soit sortie la même qu'une Winner, et là tu m'envoies un mur orange, ce truc nul ! Soit j'ai mal compris et pas trouvé le résultat, soit on s'est mal compris. Le but est d'avoir une statique prête à être envoyée sur Meta, copiée d'une statique Winners de notre marque, et là je m'envoie un mur orange. »*

**Diagnostic des 2 erreurs distinctes** :

1. **Palette dérive orange-caramel** — Nano Banana 2 a poussé la saturation vers l'orange chocolat malgré le NEGATIVE PROMPT explicite (`AVOID orange palette, caramel saturation`). **Même pattern que Soul Cinema banni le 2026-05-05**. La citation directe d'un hex brun (`#463432`) sans renforcement extrême incite les modèles diffusion à pousser la saturation. → **Banissement temporaire Nano Banana 2 pour fonds bruns dominants**. Mémoire `feedback-nano-banana-palette-brune` sauvegardée.

2. **Mauvaise interprétation du brief (le plus grave)** — j'ai suivi à la lettre `creative-system.md` §1.2 qui dit *"la typo se compose TOUJOURS en post-prod, Higgsfield n'écrit jamais de texte sur le visuel"* → j'ai sorti un fond Typo Forte ambient attendant overlay Figma. **Thomas voulait une statique COMPLÈTE Meta-ready clonée d'un winner précis du swipe file**, copy intégrée dans l'image, prête à push Meta direct, sans étape Figma intermédiaire. Les 2 règles du pipeline (`creative-system.md` "typo en post-prod" vs intention concrète Thomas "statique Meta-ready") sont en désaccord et j'ai pris la mauvaise. Mémoire `feedback-creas-meta-ready` sauvegardée.

**Ajustements pour la prochaine fois** :
- **Toujours préciser `resolution: "2k"` dans les params Higgsfield** (sinon défaut 1k = sous-résolution Meta)
- **Plus jamais "from scratch / pas d'analogue"** → on part TOUJOURS d'un winner précis du swipe file ; si aucun pertinent, on complète le pool avant de générer
- **Le livrable Notion = statique complète Meta-ready**, copy intégrée dans le PNG final, format 1080×1350 ou 1080×1080 exact, pas un fond
- **Pour les fonds bruns dominants** : éviter Nano Banana 2 en V1, tester Soul V2 ou GPT Image 2 (texte FR fiable)
- **Compléter le pool winners** avec : Hims, Ritual, AG1 backdrops type Typo Forte ; et plus globalement des winners "ads complètes" (DR archétype) pour les premières adaptations Barky

**Asset(s) gardé(s)** :
- `08-ads/statics/2026-05-13/barky_p1_cest-lage_typo_v1.png` (1.9 Mo)
- `08-ads/statics/2026-05-13/barky_p1_cest-lage_typo_v2.png` (1.8 Mo)

**Étape suivante** : attendre que Thomas score chaque variation dans Notion (status → Validée/Rejetée + Feedback). Une fois validée, composition typo XXL en post-prod selon `prompt-library.md` SET 3 §spec.

---

### Session 2026-05-05 — Premier test SET 1 Lifestyle P1 "C'est l'âge"

**Brief source** : `08-ads/prompt-library.md` SET 1 (Lifestyle × P1 × angle ★★★ "C'est l'âge")
**Type** : LIFESTYLE
**Persona** : P1 — La Maîtresse qui Refuse d'Accepter le Déclin
**Angle** : *"'C'est l'âge' : la fausse raison qui empêche la plupart des maîtres d'aider leur chien"*
**Awareness** : Problem Aware
**Stratégie** : tester 3 modèles différents sur le même prompt 500 mots pour identifier le modèle de référence Barky lifestyle.

**Variations générées** :
| # | Modèle | Format | Score Thomas | Verdict |
|---|---|---|---|---|
| v1 | Higgsfield Soul 2.0 | 1536×2048 (3:4) | 2.5/5 | Belle photo mais composition fausse (sujet centré, regard latéral, zone négative occupée par le bras). |
| v2 | Higgsfield Soul Cinema | 1536×2048 (3:4) | **0/5 (rejet net)** | Palette dérive sur le canapé en orange-caramel saturé qui sort de la zone amber `#463432`. Regard caméra forcé. Léger défaut main. |
| v3 | Google Nano Banana Pro 2k | 1856×2304 (4:5 natif) | **4/5 — gardé** | Composition parfaite (femme tiers haut, regard vers le bas vers chien off-frame, zone vide bas-gauche), palette respectée (cream + amber + hint bleu pastel), skin tones Portra naturels, demi-sourire authentique. Format 4:5 natif. |

**Prompt v3 (le winner)** :
Le prompt master du SET 1 du `prompt-library.md`, copy intégralement. 500 mots, 10 couches, NEGATIVE bloc complet inclus.
Settings Higgsfield : `model: nano_banana_2`, `aspect_ratio: 4:5`, `resolution: 2k`, `count: 1`.

**Ce qui a marché (V3 Nano Banana)** :
- Le NEGATIVE PROMPT bloc complet a tenu — zéro défaut IA visible (mains, doigts, anatomie)
- Citer "Cass Bird softness", "Annie Spratt natural light", "Cereal magazine cover style" en couche STYLE+REF a clairement orienté le modèle vers le mood éditorial
- Préciser "4:5 portrait orientation" en couche FRAMING + utiliser aspect_ratio 4:5 natif Nano Banana = composition parfaite
- "Demi-sourire of recognition", "looking down with quiet love, not posing for the camera, caught in a real moment" = expression authentique

**Ce qui n'a pas marché (V1 Soul 2.0, V2 Soul Cinema)** :
- Soul 2.0 : le prompt SCENE qui dit "right hand reaches down toward the floor, leaving a clear empty space at the bottom-left" est mal interprété — le modèle laisse parfois le bras dans la zone supposée vide.
- Soul Cinema : la couche COLOR PALETTE qui dit "warm dark amber #463432 on the leather sofa" est interprétée comme "saturer fort le orange du canapé". Soul Cinema pousse les bruns vers l'orange par défaut. **Modèle banni pour Barky.**

**Ajustement pour la prochaine fois** :
- Pour Lifestyle → toujours Nano Banana Pro 2k en V1 systématique
- V2/V3 : forks Nano Banana avec seeds différents OU Soul 2.0 si on veut variante "fashion editorial"
- **Ne plus tester Soul Cinema** sur Barky
- Sur la couche COLOR : toujours préciser "muted, desaturated" autour des hex pour éviter les modèles qui poussent la saturation

**Asset(s) gardé(s)** :
- `08-ads/statics/2026-05-05/v3-lifestyle-p1-cest-lage-nanobanana-1856x2304.png` ★ winner
- `08-ads/statics/2026-05-05/v1-lifestyle-p1-cest-lage-soul2-1536x2048.png` (archive)
- `08-ads/statics/2026-05-05/v2-lifestyle-p1-cest-lage-soulcinema-1536x2048.png` (archive — patterns à éviter)

**Étape suivante** : composition de V3 en final 1080×1350 avec headline "« C'est l'âge. »" + body + CTA + logo Barky.

---

## ✅ Patterns gagnants identifiés

> Au fil des sessions, lister les patterns qui sortent du score 4-5 de manière répétée. Format court et actionnable.

- **Nano Banana Pro 2k** = modèle de référence Barky pour Lifestyle. Respecte la composition tiers, la palette amber+cream, les skin tones Portra naturels. (Validé 2026-05-05, score 4/5.)
- **Citer "Cass Bird softness" + "Annie Spratt natural light" + "Cereal magazine cover style"** dans la couche STYLE+REF = mood éditorial verrouillé. (Validé 2026-05-05.)
- **NEGATIVE PROMPT en bloc complet jamais raccourci** → zéro défaut IA (mains, doigts, anatomie) sur Nano Banana. (Validé 2026-05-05.)
- **"Caught in a real moment, not posing for the camera, demi-sourire of recognition"** → expression authentique sans regard caméra forcé. (Validé 2026-05-05.)
- **Aspect ratio 4:5 natif Nano Banana** > génération 3:4 + crop : la composition est calibrée pour le format final. (Validé 2026-05-05.)

---

## ❌ Patterns à éviter

> Les défauts récurrents qui font échouer un visuel — à pousser dans le NEGATIVE PROMPT systématiquement.

- **Higgsfield Soul Cinema BANNI pour Barky.** Pousse les bruns vers l'orange-caramel saturé qui viole la palette `#463432`. (Validé 2026-05-05, score 0/5.)
- **Higgsfield Soul 2.0 ne respecte pas systématiquement la spec composition** ("right hand reaches down toward the floor, empty space bottom-left"). Sujet centré + regard latéral fréquent. À utiliser uniquement en V3 fork pour mood "fashion editorial" différencié, pas en V1 canon.
- **Sur la couche COLOR** : citer un hex sans préciser "muted, desaturated" → certains modèles (Soul Cinema typiquement) poussent la saturation. Toujours dire "muted dark amber #463432, desaturated, almost chocolate-leather" plutôt que juste "warm dark amber #463432".

---

## 🏆 Prompts haute performance (score 4-5)

> Bibliothèque de prompts qui ont sorti des visuels validés. Format : un bloc par prompt, taggé par TYPE et persona. À forker quand on génère des variations.

*(Vide au démarrage.)*

```
[TEMPLATE — quand le 1er prompt 4-5 sera produit]

#### Prompt #1 — TYPE / Persona / Angle
Score : X/5
Date : YYYY-MM-DD
Asset : 08-ads/statics/.../...png

[prompt complet]
```

---

## 🎯 Insights cumulés sur Higgsfield

> Apprentissages sur le modèle lui-même, pas sur Barky. Reusable pour tout brief.

*(Vide au démarrage. Exemples futurs attendus :)*
- *"Higgsfield Soul rend mieux les peaux humaines que les chiens — toujours composer le chien en photo réelle"*
- *"Le format 1080×1350 demande une mention explicite '4:5 portrait' dans la couche FRAMING"*
- *"Citer un photographe réel = ancrage fort. Citer 'wedding photographer' générique = sortie cheap"*

---

## 📊 Stats de session

> Tableau cumulatif. Mis à jour à chaque session.

| Date | Type | Persona | Variations | Score moy. | Gardés |
|---|---|---|---|---|---|
| *(à venir)* | | | | | |

---

*Fichier créé le 2026-05-05. À enrichir à chaque session de génération sans exception.*
