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
