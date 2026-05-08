// analyste.js — Ron, le chasseur de tendances
// Appelle l'API Claude avec le MCP Trendtrack attaché.
// Mission : dénicher les pépites créatives qui scalent sur Meta cette semaine,
// dans le petfood ET dans les autres verticales DTC (wellness, beauty, food,
// subscription, lifestyle) — pour donner à Hermione un éventail d'inspiration
// transférable vers Barky.

const ANTHROPIC_API = 'https://api.anthropic.com/v1/messages'
const TRENDTRACK_MCP_URL = 'https://api.trendtrack.io/v1/mcp'

// Sonnet 4.6 — analyse + JSON, suffisant pour Ron (Hermione utilisera Opus 4.7).
const MODEL = 'claude-sonnet-4-6'

// Réponse vide en cas d'échec — l'agent doit pouvoir continuer sans Ron.
const EMPTY_PAYLOAD = {
  top_ads_pet: [],
  top_ads_inspiration: [],
  patterns: {
    dominant_hooks: [],
    dominant_formats: [],
    transferable_structures: [],
    what_to_avoid_this_week: [],
  },
  week_signal: null,
  error: null,
}

const RON_PROMPT = `Tu es Ron, chasseur de tendances créatives du pôle créa Barky.

Contexte Barky : friandises fonctionnelles multivitaminées pour chiens, 28€/mois en abonnement DTC. Identité "apothicaire moderne / wellness premium" — palette bleu pastel #CADCE4 + brun ambré #463432, typo Recoleta. Tagline : "Nourri comme il le mérite."

Ta mission : dénicher des PÉPITES créatives qui scalent fort sur Meta cette semaine. Pas seulement du petfood — toutes les catégories DTC où le créatif performe et où le pattern peut être adapté pour Barky.

CONTRAINTE BUDGET : maximum 7 appels MCP au total. Sois efficace.

INSTRUCTIONS :

ÉTAPE 1 — search_ads FR
- Appelle search_ads avec country="FR", trend_signal="reach_growth_7d", limit=25
- Dans les 25 résultats, sélectionne :
  · 2-3 ads pet/dog/animal/friandise/chien (les plus pertinentes pour Barky)
  · 2-3 ads dans les verticales transférables vers Barky :
    – Wellness/supplements humains (AG1, Ritual, Huel-style daily product)
    – Beauty/skincare premium (Typology, Glossier-style)
    – Food/snacks fonctionnels
    – Subscription DTC (peu importe la catégorie — la mécanique de récurrence)
    – Lifestyle/habitudes daily (rituel matinal, routine)

ÉTAPE 2 — Fallback pet US/UK (DÉCLENCHÉ UNIQUEMENT SI 0 ad pet trouvée en France)
- Si l'étape 1 n'a remonté AUCUNE ad pet en FR, lance search_ads avec country="US"
  ou country="GB", trend_signal="reach_growth_7d", limit=15, et garde 1-2 ads
  pet/dog/animal pour avoir au moins une référence niche dans le rapport.
- Si l'étape 1 a déjà 1+ ad pet : SKIP cette étape, ne consomme pas de crédit.

ÉTAPE 3 — scan_ad() sur 4 max (les plus prometteuses)
- Choisis les 4 ads les plus intéressantes (mix pet + inspiration)
- Lance scan_ad() sur chacune pour obtenir le détail créatif et l'URL source

ÉTAPE 4 — Extraction de patterns
- Identifie les hooks, formats, structures et angles narratifs qui reviennent.
- Pense "transférabilité" : qu'est-ce qu'Hermione peut adapter pour Barky ?

URLS SOURCES (très important pour la traçabilité) :
- Inclus l'URL Trendtrack si elle est présente dans la réponse de scan_ad (champ
  source_url, trendtrack_url, ou équivalent — utilise ce que le MCP te renvoie).
- Inclus aussi meta_ad_library_url construit comme :
  https://www.facebook.com/ads/library/?id=<ad_numeric_id>
  où <ad_numeric_id> est extrait de id (ex: "facebook_807231749125366" → "807231749125366").
- Inclus country : "FR", "US", "GB" — selon la passe d'origine de l'ad.

RETOURNE UNIQUEMENT CE JSON — pas de markdown, pas de texte avant/après :

{
  "top_ads_pet": [
    {
      "id": "string",
      "brand": "string",
      "country": "FR|US|GB",
      "hook_text": "string",
      "hook_visual": "string",
      "format": "static|carousel|video",
      "angle": "string",
      "structure": ["string", "string", "string"],
      "cta": "string",
      "reach_growth_7d": number,
      "duration_seconds": number,
      "trendtrack_url": "string|null",
      "meta_ad_library_url": "string",
      "why_it_works": "string"
    }
  ],
  "top_ads_inspiration": [
    {
      "id": "string",
      "brand": "string",
      "country": "FR|US|GB",
      "vertical": "wellness|beauty|food|subscription|lifestyle|other",
      "hook_text": "string",
      "hook_visual": "string",
      "format": "static|carousel|video",
      "angle": "string",
      "structure": ["string", "string", "string"],
      "cta": "string",
      "reach_growth_7d": number,
      "duration_seconds": number,
      "trendtrack_url": "string|null",
      "meta_ad_library_url": "string",
      "transferable_pattern": "string (comment Hermione peut l'adapter pour Barky)"
    }
  ],
  "patterns": {
    "dominant_hooks": ["string"],
    "dominant_formats": ["string"],
    "transferable_structures": ["string"],
    "what_to_avoid_this_week": ["string"]
  },
  "week_signal": "string (1 phrase qui résume ce qui scale cette semaine cross-vertical)"
}`

// ─── HELPERS ────────────────────────────────────────────────────────────────

function extractJson(text) {
  if (!text) return null
  // Cherche le plus grand bloc {...} dans le texte (Claude peut bavarder autour).
  const objMatch = text.match(/\{[\s\S]*\}/)
  if (!objMatch) return null
  try {
    return JSON.parse(objMatch[0])
  } catch (err) {
    console.warn(`⚠️  Ron a renvoyé du JSON invalide : ${err.message}`)
    return null
  }
}

// Lit un stream SSE Anthropic et reconstruit le texte final + log les tool calls.
async function consumeStream(response, agentName = 'Agent') {
  const reader = response.body.getReader()
  const decoder = new TextDecoder()
  let textOutput = ''
  let buffer = ''
  let toolCallCount = 0

  while (true) {
    const { done, value } = await reader.read()
    if (done) break
    buffer += decoder.decode(value, { stream: true })

    // SSE : lignes séparées par \n, events séparés par \n\n
    let nlIdx
    while ((nlIdx = buffer.indexOf('\n')) !== -1) {
      const line = buffer.slice(0, nlIdx).trim()
      buffer = buffer.slice(nlIdx + 1)
      if (!line.startsWith('data: ')) continue

      let event
      try {
        event = JSON.parse(line.slice(6))
      } catch {
        continue
      }

      if (event.type === 'content_block_start') {
        const block = event.content_block
        if (block?.type === 'mcp_tool_use') {
          toolCallCount++
          const toolName = block.name || 'unknown'
          process.stdout.write(`   ${agentName} → MCP call #${toolCallCount} : ${toolName}()\n`)
        }
      } else if (event.type === 'content_block_delta') {
        if (event.delta?.type === 'text_delta') {
          textOutput += event.delta.text
        }
      } else if (event.type === 'message_stop') {
        // Fin du message — on sort proprement
      } else if (event.type === 'error') {
        throw new Error(`Stream error: ${JSON.stringify(event.error)}`)
      }
    }
  }

  return { text: textOutput, toolCallCount }
}

// ─── MAIN ───────────────────────────────────────────────────────────────────

async function fetchTrendtrackInsights() {
  const apiKey = process.env.ANTHROPIC_API_KEY
  const ttKey = process.env.TRENDTRACK_API_KEY

  if (!apiKey || !ttKey) {
    console.warn('⚠️  Ron en sommeil : ANTHROPIC_API_KEY ou TRENDTRACK_API_KEY manquante.')
    return { ...EMPTY_PAYLOAD, error: 'missing_keys' }
  }

  console.log('🔍 Ron part en chasse de pépites créatives...')

  const body = {
    model: MODEL,
    max_tokens: 8000,
    stream: true, // OBLIGATOIRE pour MCP — sinon timeout 5min côté Anthropic
    mcp_servers: [
      {
        type: 'url',
        url: TRENDTRACK_MCP_URL,
        name: 'trendtrack',
        authorization_token: ttKey,
      },
    ],
    messages: [{ role: 'user', content: RON_PROMPT }],
  }

  let response
  try {
    response = await fetch(ANTHROPIC_API, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': apiKey,
        'anthropic-version': '2023-06-01',
        'anthropic-beta': 'mcp-client-2025-04-04',
      },
      body: JSON.stringify(body),
    })
  } catch (err) {
    console.warn(`⚠️  Ron a perdu le réseau : ${err.message}`)
    return { ...EMPTY_PAYLOAD, error: `network: ${err.message}` }
  }

  if (!response.ok) {
    const errText = await response.text().catch(() => '')
    console.warn(`⚠️  Ron a reçu un ${response.status} : ${errText.slice(0, 300)}`)
    return { ...EMPTY_PAYLOAD, error: `http_${response.status}` }
  }

  let stream
  try {
    stream = await consumeStream(response, 'Ron')
  } catch (err) {
    console.warn(`⚠️  Ron : erreur stream : ${err.message}`)
    return { ...EMPTY_PAYLOAD, error: `stream: ${err.message}` }
  }

  const parsed = extractJson(stream.text)

  if (!parsed) {
    console.warn("⚠️  Ron n'a pas trouvé de JSON exploitable dans la réponse.")
    return { ...EMPTY_PAYLOAD, error: 'no_json' }
  }

  const petCount = parsed.top_ads_pet?.length ?? 0
  const inspoCount = parsed.top_ads_inspiration?.length ?? 0
  console.log(`✅ Ron rapporte ${petCount} ads pet + ${inspoCount} inspiration (${stream.toolCallCount} MCP calls)`)
  if (parsed.week_signal) console.log(`   Signal de la semaine : "${parsed.week_signal}"`)

  return { ...parsed, error: null }
}

module.exports = { fetchTrendtrackInsights, consumeStream }
