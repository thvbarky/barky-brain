# Workflow créatif Meta Ads avec Stack MCP

> Source de vérité : [`BARKY_CERVEAU.md §14`](../BARKY_CERVEAU.md) (acquisition) + [`08-ads/meta/strategy.md`](meta/strategy.md) (stratégie Meta) + [`15-machines/mcp-stack.md`](../15-machines/mcp-stack.md) (stack MCP).
>
> **But** : industrialiser la production de créas Barky en exploitant Trendtrack (intel marché) + Meta Ads MCP (own data) + Higgsfield (production), avec Claude comme orchestrateur.
>
> **Phase d'utilité** : à activer dès **post-validation S6 + GO**. Avant : sourcing créa manuel + photo réelle (UGC bêta-testeurs).

---

## 1. Pourquoi cette stack pour Barky (et où elle ne s'applique pas)

### Le ROI réel pour nous

Le post X qui a inspiré ce fichier annonce **"7 500€ économisés en évitant 5 produits ratés"**. Ce calcul est calé sur du **dropshipping testing** (5 produits × 4 créas × 50€/jour). **Ce n'est pas notre cas.**

Pour Barky, le ROI tient en 3 axes :

| Axe | Avant la stack | Avec la stack |
|---|---|---|
| **Sourcing créa** (briefer 10 créas pour la semaine) | 4-6 h de brainstorming + benchmark manuel | 30-45 min Claude orchestré |
| **Veille concurrents** (qui scale en pet wellness FR ?) | 2 h Meta Ad Library + capture screenshots | 10 min Trendtrack daily_radar |
| **Itération sur créa qui marche** (variations) | 1 jour pour briefer 5 variations + brief photographe | 15 min prompts Higgsfield (sur visuels packshot uniquement) |

### Là où la stack ne nous aide PAS

1. **Le storytelling fondateur** — Thomas build-in-public (parcours réel : voir [`01-identite/THOMAS_PROFIL_1.md`](../01-identite/THOMAS_PROFIL_1.md)), ça reste à scripter à la main. Trendtrack ne capture pas ça.
2. **Les UGC propriétaire-chien** — photos réelles requises (uncanny valley pet niche). Higgsfield ne remplace pas un bêta-testeur qui filme son Cavalier.
3. **La voix de marque Barky** — "Nourri comme il le mérite", registre adulte/warm. À chaque output IA, filtre humain obligatoire (`01-identite/voice-of-brand.md`).

---

## 2. Workflow type — semaine d'itération créa post-lancement

```
LUNDI MATIN — INTEL (10 min)
  ├─ daily_radar Trendtrack (qui a fait quoi en pet wellness 7j)
  ├─ creative_inspiration_pack (top hooks niche FR)
  └─ Output : 1 ligne d'insight par brand trackée
     → log 12-operations/journal/{date}.md

LUNDI APRÈS-MIDI — REVUE OWN DATA (15 min, post-M1)
  ├─ Meta Ads MCP : top créa CPM/CTR/CPP de la semaine écoulée
  ├─ Killer list : créas > 50 € spend avec CTR < 1%
  └─ Décision : 2 créas à scaler, 2 à killer, 3 nouveaux briefs

MARDI — BRIEF (45 min)
  ├─ Prompt 1 (Lorenzo Pravata) : extraire mécanisme + villain + claims
     depuis la LP Barky live
  ├─ Cross-réf intel marché Lundi → identifier les angles non-couverts
  ├─ Brief 5 créas : 2 hooks dérivés intel marché + 3 hooks propres Barky
  └─ Output : 5 briefs structurés (hook / promesse / format / CTA)

MERCREDI — PRODUCTION (60 min, post-validation)
  ├─ Higgsfield : 3 packshots variations + 2 moodboards (PAS de chien IA)
  ├─ Photo réelle / UGC bêta-testeurs : 2 créas (programmé en amont)
  └─ Output : 5 créas finales montées, prêtes pour push Meta

JEUDI — PUSH + MONITORING J1
  ├─ Upload Meta Ads (validation DGCCRF préalable obligatoire)
  ├─ Budget test : 10€/j par créa pendant 3 jours
  └─ Vérifier que les pixels remontent

LUNDI SUIVANT — BOUCLE
```

---

## 3. Recettes de prompts copy-paste

### Recette A — Brief créatif lundi matin (S2+ post-lancement)

```
Tu es l'orchestrateur créatif Barky. Pour la semaine qui démarre :

1. Avec Trendtrack MCP :
   - daily_radar sur mes brands trackées (period=7d)
   - creative_inspiration_pack niche="dog wellness", country=FR, period=14d
2. Avec Meta Ads MCP (si dispo) :
   - top 5 créas par CTR sur les 14 derniers jours
   - killer list (créas > 50€ spend, CTR < 1%)
3. Cross-réf avec :
   - 02-marche/angles.md (nos angles validés méthode Lorenzo Pravata)
   - 08-ads/meta/strategy.md (règles de décision)
   - 01-identite/voice-of-brand.md (filtre voix de marque)

Output structuré :
- 3 insights marché de la semaine (1 ligne chacun)
- 2 créas à scaler (notre data) + raison
- 2 créas à killer + raison
- 3 nouveaux briefs créa : hook / promesse / format / CTA
  → dont 1 dérivé d'un angle Trendtrack qu'on n'a pas encore testé
  → dont 2 propres au voice-of-brand Barky

Termine par : log dans 12-operations/journal/{date} bloc "Insights produit"
si insight majeur, sinon résumé en 5 lignes pour la weekly review.
```

### Recette B — Génération packshots Higgsfield

```
Tu es le directeur créatif Barky. Génère 5 packshots Higgsfield pour :

PRODUIT : pot Barky multivit hero, brun ambré #463432, étiquette
   bleu pastel #CADCE4, typographie Recoleta serif, 60 bouchées dedans.

CONTRAINTES :
- Palette stricte bleu pastel + brun ambré (zéro autre couleur dominante)
- Registre apothicaire moderne / wellness pharmaceutique (réf : Hims, Ritual, Kin Euphorics)
- Format : 1:1 et 9:16 (un de chaque)
- AUCUN chien IA dans les visuels (uncanny valley pet niche)
- Texte affiché si présent : en français entre guillemets

VARIATIONS À PRODUIRE :
1. Hero packshot fond brun ambré, pot en lumière studio rasante
2. Pot sur fond dégradé bleu pastel → blanc cassé, ambiance matin clair
3. Flat-lay : pot + balle de tennis brandée + carte manuscrite (pas de chien)
4. Macro sur la texture d'une bouchée (close-up, pas de chien)
5. Mood scientifique : pot + structure moléculaire en arrière-plan abstrait

Brief en anglais (meilleur rendu IA), texte affiché en français.

Output : 5 prompts Higgsfield finalisés + 1 ligne de critique post-prod
prévue pour chaque (couleurs à corriger en Photoshop, etc.)
```

### Recette C — Détection angle blanc

```
Avec Trendtrack MCP, sors-moi les 20 hooks les plus utilisés en pet
wellness FR + UK + US sur les 60 derniers jours, classés par fréquence.

Cross-réf avec 02-marche/angles.md (nos angles starrés Lorenzo Pravata).

Question : quels angles sont :
A) Mainstream et qu'on devrait éviter (saturation)
B) Mainstream et où on a un voice-of-brand qui peut différencier
C) Sous-utilisés ou absents et qui matchent les personas Barky
   (`02-marche/personas.md`)

Termine par 3 propositions d'angles Catégorie C à ajouter au test plan
avec evidence directe (review concurrent / data Trendtrack).
```

---

## 4. Règles non-négociables (filtres humains obligatoires)

Avant chaque push Meta, Thomas valide manuellement sur 4 critères :

1. **DGCCRF** : aucune allégation médicale interdite (`04-legal/allegations.md`). Par défaut : "soutient", "contribue à", "favorise". Jamais "guérit", "traite", "prévient".
2. **Voice-of-brand** : registre adulte/warm/empathique (`01-identite/voice-of-brand.md`). Pas d'emoji chien, pas de "woof woof", pas de paternalisme.
3. **Authenticité visuelle** : si chien dans le visuel → photo réelle obligatoire. Si Higgsfield → packshot/mood seulement.
4. **Cohérence palette** : bleu pastel `#CADCE4` + brun ambré `#463432`. Zéro orange, zéro navy. Non-négociable.

---

## 5. Anti-patterns à éviter

| Anti-pattern | Pourquoi c'est mauvais | Que faire à la place |
|---|---|---|
| Copy-paste d'un hook Trendtrack en français | Banalité, pas de voice-of-brand, risque DGCCRF si claim agressif | Adapter au registre Barky + filtre légal |
| Higgsfield "chien adorable mange Barky" | Uncanny valley, repérable, casse la conversion | Photo réelle bêta-testeur ou packshot abstrait |
| Brief créa sans avoir lu `02-marche/angles.md` | Tu ré-invente la roue, tu sors des angles déjà starrés ou écartés | Toujours commencer par lire le cerveau |
| Push 10 créas sans monitoring J1 | Cramer le budget sans signal exploitable | Max 5 créas/test, monitoring J1 obligatoire |
| Lancer la stack avant le GO/NO-GO S6 | Zéro data own = Meta MCP inutile, sourcing créa prématuré | Sourcing manuel + photo réelle jusqu'au GO |

---

## 6. KPIs de la stack (à mesurer après 30 jours d'usage)

- Temps moyen pour briefer 5 créas : avant vs après
- Nombre de créas produites / semaine
- CTR moyen des créas issues du workflow vs hors workflow
- Coût Trendtrack (crédits API) / créa produite
- % de créas killées en J1 (signal de qualité du sourcing)

À reporter dans la weekly review (`12-operations/weekly-reviews/`) après le 1er mois d'opération réelle.

---

## 7. Roadmap d'activation

| Phase | Période | Activité |
|---|---|---|
| **Pré-test (maintenant — S6)** | mai 2026 | Trendtrack pour intel marché + benchmark Dog is Human. **Pas** de Higgsfield, **pas** de Meta MCP (pas de data). |
| **Test validation (S1-S6)** | mai-juin 2026 | Trendtrack continue. Sourcing créa **manuel + photo bêta-testeurs**. |
| **GO + lancement (M0-M1)** | post-juin 2026 | Brancher Meta Ads MCP dès J7 de spend. Continuer sourcing créa hybrid. |
| **Scaling (M2-M3)** | été 2026 | Brancher Higgsfield. Industrialiser le workflow lundi → jeudi décrit §2. |
| **Cruising (M4+)** | automne 2026 | Routine établie. Mesurer KPIs §6. Affiner. |

---

*Fichier créé le 2026-05-01. À mettre à jour quand un MCP est branché ou retiré, ou quand on identifie un nouvel anti-pattern.*
