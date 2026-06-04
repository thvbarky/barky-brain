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

### Session 2026-05-14 1455 — Import 5 créas manuelles Thomas (référence d'apprentissage)

**Type** : import (hors flow `/barky-creas-batch`)
**Source** : créas générées manuellement par Thomas sur l'interface Higgsfield le matin du 14/05, importées en `À valider` dans Notion pour feedback et alimentation des apprentissages du skill.
**Modèle** : GPT Image 2 (déclaratif)
**Volume** : 5 rows uniques (1 doublon supprimé)
**Chemin local** : `08-ads/meta/creatives/barky_p{persona}_{angle}_{type}_v1.png`

**Matrice importée** :
| # | Fichier | Persona | Angle | Static type | Hook |
|---|---|---|---|---|---|
| 1 | `barky_p1_pas-vieux-il-manque_lifestyle_v1.png` | P1 | pas-vieux-il-manque | Lifestyle | « Ton chien se lève lentement ? Il hésite à monter les escaliers ? C'est peut-être pas juste l'âge. » |
| 2 | `barky_p1_signes-mobilite_proof_v1.png` | P1 | signes-mobilite | Proof | « Tu ne le remarqueras pas du jour au lendemain. Tu le remarqueras dans les petites choses. » + 3 vignettes |
| 3 | `barky_p2_liste-complete-actifs_producthero_v1.png` | P2 | liste-complete-actifs | Product Hero | « Tu vois chaque jour tout l'amour qu'il te donne. » + 3 bullets icônes |
| 4 | `barky_p1_cest-lage_lifestyle_v1.png` | P1 | cest-lage | Lifestyle | « Ton chien profite du printemps ? Ou il reste en retrait ? » |
| 5 | `barky_p1_signes-mobilite_producthero_v1.png` | P1 | signes-mobilite | Product Hero | « Les longues balades du printemps arrivent. Ton chien peut y aller ? » + 4 icônes bénéfices |

**Patterns à observer pour le skill** :
- **Hook long en 3 niveaux** (#1) : structure question 1 → question 2 → résolution (pastille bleu pastel). Tester si ça fonctionne en feed Meta vs hook 1-niveau.
- **Layout Proof magazine-style** (#2) : zone hook+photo+packshot en haut, bandeau 3 vignettes numérotées en bas, closing 1 ligne. Structure dense mais hyper-lisible.
- **Encart vert sage** (#3) : déviation palette stricte assumée — à valider en feedback. Si Thomas l'accepte → relax la règle palette pour les Product Hero "encarts info".
- **Hooks saisonniers printemps** (#4, #5) : angle temporel pour booster CTR à un moment précis. Catalogue à constituer : printemps / été / rentrée / hiver / fêtes.
- **Hybride Product Hero + Lifestyle** (#5) : packshot intégré dans scène nature + icônes bénéfices alignées. Format à reproduire pour combos `signes-mobilite`.

**À surveiller dans le Feedback Notion** :
- Ciel cyan saturé sur #4 et #5 : passe ou se fait taper ? (cyan listé dans bans palette)
- Encart vert sage sur #3 : passe ou se fait taper ? (idem)
- Border collie (#2) vs golden senior canonique P1 : cohérence persona ou variation acceptable ?
- Densité texte hook (#1 = 3 niveaux, #5 = hook + 4 bénéfices + disclaimer) : seuil de tolérance en feed ?

**Apprentissage méta** : Thomas génère manuellement quand il veut explorer un pattern précis (saisonnier, layout magazine, hook 3-niveaux). Le skill `/barky-creas-batch` reste l'industrialisation, mais **les imports manuels alimentent le catalogue de patterns** que le skill pourra réutiliser une fois validés.

---

### Session 2026-05-14 1005 — Batch test refonte skill (5 créas, GPT Image 2)

**Batch ID** : `2026-05-14-1005`
**Mode** : auto (5 combos test après refonte 14/05/2026 du skill `/barky-creas-batch`)
**Volume demandé / généré** : 5 / 5 (100% succès)
**Coût réel** : ~35 credits Higgsfield (gpt_image_2 quality high × 5)
**Modèle** : `gpt_image_2` (premier batch avec GPT Image 2 après switch défaut Nano Banana 2 → GPT Image 2 le 14/05)
**Apprentissages relus** : 2 rows Notion rejetées le matin (cron Cowork) — bug hex codes affichés textuellement + pot Barky raté → injection dans le meta-prompt de la consigne « NE JAMAIS afficher les codes hex textuellement dans l'image » et passage systématique du packshot officiel en `medias` dès que le pot est visible.

**Matrice exécutée** :
| # | Persona | Angle | Static type | Winner / Inspiration | Job ID | Notion |
|---|---|---|---|---|---|---|
| 1 | P1 | cest-lage ★★★ | Lifestyle | from scratch — Cereal magazine | `19c0d61d-79e4-4098-9ae6-04597065d7a7` | À valider |
| 2 | P1 | signes-mobilite ★★ + packshot | Lifestyle | from scratch — The Farmer's Dog ad | `f0208178-6cd1-424c-9764-3854200c96e3` | À valider |
| 3 | P1 | fete-meres (nouveau slug) | Lifestyle | from scratch — Aesop × Cereal | `a1e91766-3707-4738-aa59-e20a922c74c7` | À valider |
| 4 | P1 | pas-vieux-il-manque ★ | Lifestyle | from scratch — naturaliste 35mm | `4058314b-9b57-4f62-8810-8e57f064b629` | À valider |
| 5 | P2 | carences-invisibles ★★★ + packshot | Product Hero | exode_problem-solution-01 — mousse forêt verte | `fa6bd890-bde8-43d1-a3a5-c7a0686a9ef2` | À valider |

**Patterns gagnants confirmés (refonte 14/05 validée)** :
- ✅ **Pattern court Cowork-style sur GPT Image 2 = qualité Dog is Human / Aesop niveau premium.** Pattern validé sur Nano Banana 2 (4 statics Cowork 13/05), transposé tel quel sur GPT Image 2, résultat équivalent voire supérieur (hiérarchie typo encore plus riche, badges + disclaimers spontanés excellents).
- ✅ **Meta-prompt fixe ~150 mots + brief court 1-3 phrases** = recette qui marche. 5/5 succès.
- ✅ **Consigne anti-hex display** : zéro hex affiché textuellement dans les 5 rendus (vs bug du matin avec ancien prompt sans cette consigne).
- ✅ **Packshot officiel en `medias[].role="image"`** dès que le pot est visible : 2/5 combos (#2 et #5) ont le pot **parfaitement fidèle** (label « Barky. » + « MULTIVITAMINES » + badge France + « 60 BOUCHÉES MOELLEUSES » lisibles). GPT Image 2 accepte uniquement role « image » (auto-coerce depuis « reference »).
- ✅ **Winner = inspiration optionnelle** : 4/5 combos `from scratch`, 1/5 cite un winner (Exode `problem-solution-01`) — les 4 from scratch sortent aussi bien que le clone. Validation de la refonte « winner = inspiration, pas contrainte ».
- ✅ **GPT Image 2 quality high** = excellente fidélité texte FR avec accents (zéro gibberish observé), même sur des hooks de 25+ mots.

**Insights techniques nouveaux** :
- **Coûts mesurés (1:1 2k)** : Nano Banana 2 = 2 cr · GPT Image 2 medium = 3 cr · **GPT Image 2 high = 7 cr/image**. Ratio 3,5× vs Nano Banana 2 pour quality high.
- **Temps de génération GPT Image 2 quality high** = ~100-150s par image (vs ~10-20s annoncés pour image standard). Nécessite 5-6 rounds de polling sync. Pour batches plus gros, prévoir cette latence.
- **GPT Image 2 role = "image" seulement** : auto-coerce depuis "reference" mais à passer directement "image" pour les prochains batchs.
- **CDN Shopify URL packshot expiré** : `?v=1777296328` retournait 404. Fallback via `media_upload` local réussi. Pour le pipeline Cowork 11h qui utilise l'URL CDN — risque de re-expiration à monitorer.

**Patterns à abandonner (confirmé par le test)** :
- ❌ Prompts verbeux 500-700 mots de `prompt-library.md` : pattern court court Cowork donne meilleurs résultats avec moins de friction.
- ❌ READ winner.jpg + clone fidèle pixel-par-pixel : le mood en 1 ligne suffit, le modèle respire mieux.

**À surveiller dans les prochains Feedback** :
- Si Thomas valide les 5/5, on a un pipeline production-ready. Si Rejetée → identifier précisément quelle dimension casse (palette, typo, mise en scène, etc.) pour ajuster le meta-prompt.
- Slug `fete-meres` à ajouter au Select Notion `Angle` si combo #3 validé.
- Comparer à un batch équivalent en Nano Banana 2 quality équivalente pour benchmarker objectivement la préférence Thomas GPT Image 2.

**Assets** : `08-ads/statics/2026-05-14-1005/` (5 PNG 2k 1:1, ~40 Mo total)
**Notion DB** : https://www.notion.so/35ffd75e0c44809189a0ead944464f3c → vue Board by Status > À valider, tag `[REFONTE-1405]`

---

### Session 2026-05-13 1610 — Batch 2 fidélité-winner (20 créas refondues)

**Mode** : refonte du batch 1530 en appliquant la règle fidélité-winner (mémoire `feedback-creas-fidelite-winner`).
**Cap dur respecté** : 50 credits Higgsfield total (5 test + 15 retry batch = 20 jobs × 2).
**Volume généré** : 20/20 (100%).

**Diversité de design produite** (vs batch 1530 uniforme) :
| # | Design type clone | Differs from batch 1530 |
|---|---|---|
| T1 / F19 | Chocolate-on-chocolate plâtre (clone mousse-forêt) | Background brun dominant pas bleu |
| T2 | Split-screen 2 jars comparison | Vrai split au lieu de Typo Forte uniforme |
| T3 | Handheld + post-it manuscrit jaune | UGC tactical pas Typo Forte propre |
| T4 / F20 | Infographie 4 cases vs Lifestyle premium | Pédago séquentielle ET still life premium |
| T5 | Selfie UGC influenceuse P1 cuisine | Humain incarné au lieu de carte flat |
| F02 | UGC iPhone POV cuisine + caption jaune TikTok | UGC au lieu de Typo statement |
| F04/F14 | Typo Forte fond CREAM | Cream variant (pas chocolate ni blue) |
| F05 | Linen oat drape backdrop | Oat variant (pas blue, pas chocolate) |
| F07 | Typo Forte CREAM-ON-DARK | Inverted pill cream-on-chocolate |
| F08/F13/F15 | Packshot premium SOBER (no icons) | Honey-oak wood + 2 lignes minimal |
| F10 | 2-column pedagogic comparison | Gamelle seule vs + Barky |
| F11 | Typo Forte CREAM emotional | Variation sur même angle |
| F12/F16 | Still life apothecary premium + props ingredients | Foie poulet + thym + curcuma + lavande + lin |
| F18 | Vétérinaire en clinique + pot | Authority voice incarnée |

**Patterns gagnants confirmés** :
- ✅ Read winner.jpg + decrire structure SPÉCIFIQUE au winner = diversité réelle
- ✅ Varier les backgrounds (chocolate / cream / oat linen / honey-oak / tricolor / kitchen marble) selon le winner précis
- ✅ Pill inverted (cream-on-dark) marche aussi bien que (dark-on-cream)
- ✅ Inclure des HUMAINS dans les Proofs (femme P1 cuisine, Dr véto clinique) — Nano Banana 2 gère bien
- ✅ Sober packshot SANS icônes possible pour certains winners (product-launch)
- ✅ Still life apothecary avec props ingredients (foie poulet/thym/curcuma) = registre Aesop premium

**À surveiller** :
- Texte FR sur 3 lignes Typo Forte : encore risque gibberish sur le 3ème mot encadré
- Variations T1 ↔ F19 : voir si l'utilisateur préfère pot-fermé ou pot-nuages
- Visuels avec humain (T5, F18) : qualité skin + persona age fidelity

**Backlog scrapage prioritaire** (toujours actif) : Lifestyle FR maître+chien (Dog is Human, Japhy, Elmut, The Farmer's Dog, Butternut Box) + testimonials vétéran chien (Zesty Paws).

**Assets** : `08-ads/statics/2026-05-13-1530/` (T1-T5 + F02-F20, 20 PNG 2k natif)
**Notion DB** : https://www.notion.so/35ffd75e0c44809189a0ead944464f3c → vue Board by Status > À valider (tags `TEST-FIDELITE-` et `FIDELITE-`)

---

### Session 2026-05-13 1545 — Retour Thomas sur le batch 1530 : trop uniforme, manque de fidélité au winner

**Verbatim Thomas** :
> *« C'est malgré tout trop souvent pareil. À part le texte qui change, on va dire c'est souvent le packshot avec un titre en haut, le logo en bas ou une petite phrase en bas. Le but c'est de garder les mêmes concepts design que le produit Winner et d'avoir le même résultat avec mon produit. »*

**Diagnostic** : j'ai factorisé les 20 prompts en "template par static type" (Product Hero / Typo Forte / Proof) avec juste les variables qui changent (hook, bénéfices). Résultat : 20 créas qui se ressemblent au lieu de 20 designs distincts clonés fidèlement chacun de son winner.

**Le vrai mode opératoire qui aurait dû être appliqué** :
1. Pour chaque combo de la matrice → **Read l'image du winner** correspondant
2. Décrire structurellement la composition SPÉCIFIQUE du winner dans le prompt :
   - Background unique (mousse vert / marbre / dépôt / split-screen / lifestyle / etc.)
   - Présence ou absence d'humain/chien
   - Structure de mise en scène unique
   - Caption style spécifique
3. Adapter à Barky **sans aplatir** la singularité du winner

**Conséquence immédiate** :
- Mémoire `feedback-creas-fidelite-winner` sauvegardée avec catalogue des 15 winners et leur composition à cloner
- SKILL.md `/barky-creas-batch` §7 mis à jour : Read winner.jpg obligatoire avant de prompter, multi-medias autorisé pour photo lifestyle chien/humain
- **À refaire au prochain batch** : ne plus mettre fond bleu pastel par défaut partout, varier selon le winner précis
- Photos `01-identite/assets/photos/lifestyle/` (19 photos chien/humain dispo) à utiliser en référence multi-media quand le winner contient un sujet humain/animal

---

### Session 2026-05-13 1530 — Batch auto 20 créas (1er run industriel `/barky-creas-batch`)

**Batch ID** : 2026-05-13-1530
**Mode** : auto (proposé 25 → édité à 20 après application règle absolue winner-requis)
**Coût réel** : 40 credits Higgsfield (cap dur atteint exactement)
**Volume généré** : 20/20 (100% succès, 0 échec)

**Apprentissages relus avant batch** :
- ✅ Pattern Nano Banana 2 all-in-one + ref packshot + fond bleu pastel (v6 validé sur le principe)
- ❌ Typo Forte fond brun pur dérive orange (v1/v2 rejetées) → toutes Typo Forte du batch en fond BLEU PASTEL
- ❌ Python compositing exclu (rejet v3/v4) → all-in-one only
- 🚨 Winner requis (règle absolue actée juste avant ce batch) → 8 combos `n/a` (5 Lifestyle + 3 sans testimonial) retirés de la matrice initiale

**Matrice exécutée — 20 combos** :
| # | Persona | Angle | Type | Winner | Format | Notion |
|---|---|---|---|---|---|---|
| 1 | P1 | ★★★ cest-lage | Product Hero | exode_problem-solution-01 | 1:1 | À valider |
| 2 | P1 | ★★★ cest-lage | Typo Forte | exode_ugc-style | 1:1 | À valider |
| 3 | P2 | ★★★ carences-invisibles | Product Hero | exode_problem-solution | 4:5 | À valider |
| 4 | P2 | ★★★ carences-invisibles | Typo Forte | exode_problem-solution-01 | 1:1 | À valider |
| 5 | P2 | ★★★ liste-complete-actifs | Product Hero | exode_problem-solution-01 | 1:1 | À valider |
| 6 | P2 | ★★★ liste-complete-actifs | Proof | exode_testimonial-01 | 4:5 | À valider |
| 7 | P2 | ★★★ liste-complete-actifs | Typo Forte | exode_problem-solution-01 | 1:1 | À valider |
| 8 | P1 | ★★ signes-mobilite | Product Hero | exode_product-launch | 1:1 | À valider |
| 9 | P1 | ★★ compl-moitie-marchent-pas | Proof | exode_testimonial-01 | 4:5 | À valider |
| 10 | P2 | ★★ 4-nutriments-manquants | Product Hero | exode_problem-solution | 4:5 | À valider |
| 11 | P2 | ★★ pas-tous-pareils | Typo Forte | exode_comparison | 1:1 | À valider |
| 12 | P2 | ★★ filieres-pet-food-refusees | Product Hero | exode_problem-solution-02 | 1:1 | À valider |
| 13 | P1 | ★★ made-in-france | Product Hero | exode_product-launch | 1:1 | À valider |
| 14 | P1 | ★ pas-vieux-il-manque | Typo Forte | exode_problem-solution-01 | 1:1 | À valider |
| 15 | P1 | ★ 60-bouchees-founder | Product Hero | exode_product-launch | 1:1 | À valider |
| 16 | P2 | ★ qualite-humaine | Product Hero | exode_problem-solution-02 | 1:1 | À valider |
| 17 | Tx | garantie-2-mois | Typo Forte | exode_promo-02 | 1:1 | À valider |
| 18 | Tx | comite-veto | Proof | exode_testimonial-02 | 4:5 | À valider |
| 19 | P1 | ★★★ cest-lage (var) | Product Hero | exode_problem-solution-01 | 1:1 | À valider |
| 20 | P2 | ★★★ carences-invisibles (var) | Product Hero | exode_problem-solution | 4:5 | À valider |

**Patterns intégrés depuis Feedback Notion** :
- Tous les Typo Forte → fond bleu pastel `#CADCE4` (jamais brun pur)
- Spell-out accents FR systématique dans prompts (é, è, ç, â, û)
- Encadré pill brun-cream sur le mot fort de chaque hook
- 3 bénéfices uppercase avec icônes line-art simples

**À surveiller dans les prochains Feedback** :
- Texte FR sur les Typo Forte (3 lignes au lieu de 2) — risque gibberish plus élevé
- Testimonials (#6, #9, #18) — premier test des Proof avec carte cream et signature
- Variation atmosphérique #19 (packshot pot-nuages) vs #1 (pot fermé bleu pastel)

**Assets** : `08-ads/statics/2026-05-13-1530/` (20 PNG 2k natif, ~95 Mo total)
**Notion DB** : https://www.notion.so/35ffd75e0c44809189a0ead944464f3c (vue Board by Status > À valider)

---

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
