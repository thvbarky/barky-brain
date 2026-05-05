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

*(Vide au démarrage — sera enrichi à chaque session de génération.)*

---

## ✅ Patterns gagnants identifiés

> Au fil des sessions, lister les patterns qui sortent du score 4-5 de manière répétée. Format court et actionnable.

*(Vide au démarrage. Exemples futurs attendus :)*
- *"Citer Cass Bird + Kodak Portra 400 + Leica M6 dans la couche STYLE = +30% qualité instantanée"*
- *"Pour P1 senior, le mood 'fin de matinée dimanche' marche mieux que 'golden hour outdoor'"*
- *"Le frame qui garde 30% de negative space pour overlay typo en post → systématiquement gagnant"*

---

## ❌ Patterns à éviter

> Les défauts récurrents qui font échouer un visuel — à pousser dans le NEGATIVE PROMPT systématiquement.

*(Vide au démarrage. Exemples futurs attendus :)*
- *"Higgsfield qui dérive vers Beagle au lieu du Border Collie demandé → préciser race en début ET fin de prompt"*
- *"Quand le visuel contient le pot Barky → le pot est mal proportionné. Toujours composer le packshot réel en post."*
- *"Lighting golden hour saturé → output trop chaud. Préciser 'late golden hour, just past peak warmth' pour adoucir."*

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
