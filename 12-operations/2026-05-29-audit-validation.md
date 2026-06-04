# Audit site — Validation Thomas
## Vendredi 29 mai 2026 · session Thomas + Elias + Claude

> **Mode d'emploi**
> Pour chaque reco : remplacer `[ ]` par `[x]` devant **OK** si tu valides, devant **CHANGE** si tu veux qu'on modifie/discute.
> Tu peux écrire tes notes libres sous chaque reco (objection, contre-proposition, "à voir avec Elias", etc.).
> Quand t'as fini, dis-moi et je relis le doc + j'applique les modifs validées.
>
> Légende : ✅ = quick win · 🟡 = réflexion · 🔴 = décision business

---

## SECTION A — FICHE PRODUIT (sélecteur 3 étapes)

### A.1 — Remplacer "Mon toutou pèse" → "Mon chien pèse" ✅
> Raison : "toutou" est explicitement banni voice-of-brand §4.1.
- [X] **OK**
- [ ] **CHANGE**
- Notes :

### A.2 — Réécrire le tip Étape 2 + retirer emoji 💡 ✅
> Avant : *« 💡 Les vétérinaires recommandent un traitement d'au moins 2 mois pour observer 100% des bienfaits. »*
> Après : *« Les vétérinaires recommandent une cure d'**au moins 2 mois** pour observer les premiers signes durables. »*
> Raison : "traitement" sonne médical (risque DGCCRF), "100%" est un chiffre non sourcé, emoji 💡 banni voice-of-brand.
- [X] **OK**
- [ ] **CHANGE**
- Notes :

### A.3 — Vouvoiement Étape 3 + reformulations 🟡
> Avant : *« Choisis ta cadence de livraison »* / *« Idéal moyens & grands chiens »*
> Après : *« Choisissez votre cadence de livraison »* / *« Recommandée petits chiens »* / *« Recommandée moyens & grands chiens »*
> Raison : voice-of-brand impose le vouvoiement sur le site (tutoiement réservé aux ads + emails marketing).
- [X] **OK**
- [ ] **CHANGE**
- Notes :

### A.4 — Ajouter bannière LANCEMENT10 au-dessus du CTA 🔴
> Bannière fine (style brun ambré) : *« Code `LANCEMENT10` appliqué automatiquement — 10 % de remise supplémentaire offerte. Plus que XX places sur 100. »*
> Raison : on a tranché que l'offre stack -25% abo + -10% LANCEMENT10. Si on ne le rend pas visible, l'urgence ne se voit pas.
- [X] **OK**
- [ ] **CHANGE**
- Notes :

### A.5 — Pill "Recommandé" sur l'option Abonnement 🟡
> Petit pill brun ambré à côté du label "Abonnement" → ancre cognitive que c'est le bon choix par défaut.
> Raison : aujourd'hui les 2 options (one-off vs abo) sont à plat visuellement. L'abo est l'enjeu business n°1.
- [X] **OK**
- [ ] **CHANGE**
- Notes :

### A.6 — Prix-jour dans le CTA 🟡
> Sous le prix CTA, en petit : *« Soit X,XX € par jour »* (calculé dynamiquement selon bundle + cadence).
> Raison : la LP joue déjà cet ancrage (0,93€/jour). La PDP ne le reprend pas → on perd un argument de réassurance prix.
- [X] **OK**
- [ ] **CHANGE**
- Notes :

---

## SECTION B — LANDING PAGE / Critiques bloquantes

### B.1 — JSON-LD : corriger le domaine + slug 🔴
> Avant (ligne 38) : `"@id": "https://barky.fr/pages/multivitamine-daily"`
> Après : `"@id": "https://barky.pet/pages/barky-daily-journal"`
> Raison : mauvais TLD (`.fr` au lieu de `.pet`) ET mauvais slug. Casse le SEO + le partage social.
- [X] **OK**
- [ ] **CHANGE**
- Notes :

### B.2 — Aligner l'offre LP sur la décision du jour 🔴
> Avant (CTA light, ligne 1308) : *« -30 % sur le premier mois d'abonnement »*
> Après :
> - *« Abonnement à −25 %. Premier mois à −32 % avec le code `LANCEMENT10`. »*
> - *« 22,95 € la première box. 25,50 € ensuite. Sans engagement, annulable en 1 clic. »*
> Raison : décision actée stack (-25% abo permanent + -10% LANCEMENT10 single-use sur les 100 premières commandes).
- [X] **OK**
- [ ] **CHANGE**
- Notes :

### B.3 — Recalculer le prix-jour partout sur la LP 🔴
> Avant : *« 0,93 €/jour »* (basé sur 28 €/mois)
> Après : *« 0,85 €/jour · 0,76 € le premier mois »* (basé sur 25,50 € abo + 22,95 € 1re box)
> Raison : tous les prix doivent matcher la nouvelle offre. Aujourd'hui la LP ment au visiteur.
- [X] **OK**
- [ ] **CHANGE**
- Notes :

### B.4 — Fusionner Topbar + Urgency bar 🟡
> Avant : 3 bandeaux sticky empilés (urgency / topbar / masthead) qui mangent 100-130px en mobile.
> Après : 1 seule barre brun ambré : *« Offre de lancement — code `LANCEMENT10` actif · Livraison offerte »*. Sticky uniquement le masthead.
> Raison : friction lourde sur mobile, surtout au scroll vertical de lecture éditoriale.
- [X] **OK**
- [ ] **CHANGE**
- Notes :

---

## SECTION C — LANDING PAGE / Nice-to-have

### C.1 — Réécrire le deck sous le headline 🟡
> Avant : *« Une fois par jour. Ce que les croquettes du commerce oublient depuis cinquante ans — formulé par quatre vétérinaires français, fabriqué en France, transparent sur ses dosages. »*
> Après : *« 12 actifs aux doses biodisponibles. Formulée avec 4 vétérinaires français. Fabriquée en France. »*
> Raison : le deck actuel rejoue le reframe du headline. La preuve frappe plus fort que la répétition.
- [X] **OK**
- [ ] **CHANGE**
- Notes :

### C.2 — Section "12 actifs en détail" en accordéon 🟡
> Garder l'architecture 5 clusters mais collapser par défaut (clic pour ouvrir chaque cluster).
> Raison : risque "wall of science" en milieu de page après la timeline + posologie + témoignages.
- [X] **OK**
- [ ] **CHANGE**
- Notes :

### C.3 — Audit tutoiement/vouvoiement section par section 🟡
> Voice-of-brand : site = vouvoiement. Aujourd'hui la LP mixe les deux. À harmoniser : vouvoyer côté Barky-qui-parle, garder le tutoiement uniquement dans les verbatim clients.
> Raison : cohérence de marque. Le mix donne un sentiment d'amateur.
- [X] **OK**
- [ ] **CHANGE**
- Notes :

---

## SECTION D — DÉCISIONS BUSINESS à trancher (réponse libre)

### D.1 — Dr. Camille Berton (signature LP) : réelle ou placeholder ? 🔴
La byline + le JSON-LD attribuent la rédaction à Dr. Camille Berton (Nutritionniste ENV Alfort). Si c'est une véto fictive : risque Google "ghost article" + risque réputation si on monte un blog réel.

**3 options** :
1. Réelle (contrat signé) → on garde tel quel.
2. Placeholder en attendant de signer une vraie véto → on retire la byline + on retire `author` du JSON-LD, on signe "Comité scientifique Barky".
3. Placeholder mais on assume le concept "véto fictive de marque" → on garde, on accepte le risque.

- [ ] Option 1 (réelle)
- [X] Option 2 (retirer byline + author JSON-LD)
- [ ] Option 3 (assumer fictive)
- Notes :

### D.2 — Nom de la garantie : "Chien en forme — 60 jours" ou "Queue Remuante — 60 jours" ? 🟡
Aujourd'hui la LP utilise *« Garantie chien en forme — 60 jours »*. Voice-of-brand §3.2 prescrit *« Garantie Queue Remuante — 60 jours »* (notre nom propriétaire, chaleureux + drôle juste).

- [ ] Garder "Chien en forme" (sobre)
- [X] Basculer sur "Queue Remuante" (voice-of-brand officielle)
- Notes :

### D.3 — Livraison gratuite à 34 € one-off : vrai ou seuil minimum ? 🔴
La PDP affiche "Livraison gratuite" en trust signal sur tous les cas. Si on offre vraiment à 34 € = OK. Sinon il faut un seuil affiché ou retirer le claim sur le one-off.

- [ ] Gratuite dès 34 € (assumé, on ajuste la marge)
- [ ] Seuil à préciser (ex : "Livraison offerte dès 40 € · 4,90 € en dessous")
- [X] Gratuite uniquement sur abonnement
- Notes :

---

## SECTION E — CE QUE J'AI BESOIN DE VOIR AVANT LE BLOC 2 (Meta)

Pour l'instant je n'ai pas pu auditer :
- [ ] Le **corps des sections Témoignages** de la LP (lignes 1142-1298) — c'est probablement là que se joue 30 % du taux de conversion.
- [ ] La **FAQ** de la LP (lignes 1365-1395) — 7-10 questions probables, à vérifier si on couvre les vraies objections.
- [ ] Le **reste de la fiche produit** (galerie, description, social proof, FAQ produit) — la description Shopify est vide, donc tout doit être dans des sections custom du thème dev que je n'ai pas encore lues.

**Suggestion** : tu ouvres le thème dev en preview avec Elias, vous me dictez les sections que vous voyez et je code en parallèle. Ou je continue à lire le code en parallèle de tes validations.

- [ ] J'ouvre la preview avec Elias et je te raconte
- [X] Tu continues à lire le code du thème dev en parallèle

---

## Fin du doc
Quand tu as coché → tu me dis "doc OK" + je relis + j'applique toutes les modifs validées.
