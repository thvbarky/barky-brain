// contexte.js
// Bobby charge le Second Brain de Barky et le passe à Hermione (la stratège).
// Lecture autonome : walk les dossiers clés, applique des garde-fous, retourne
// un dictionnaire { chemin/relatif.md: contenu } prêt à injecter dans un prompt.

const fs = require('fs')
const path = require('path')

// ─── CONFIGURATION ───────────────────────────────────────────────────────────

// Fichiers chargés en priorité absolue (master + instructions).
const ALWAYS_INCLUDE = [
  'BARKY_CERVEAU.md',
  'CLAUDE.md',
]

// Dossiers thématiques scannés automatiquement.
const REPO_DIRS = [
  '01-identite',
  '02-marche',
  '03-produit',
  '04-legal',
  '14-knowledge',
]

// Sous-dossiers à exclure (rapports lourds déjà synthétisés, binaires, archives).
const EXCLUDE_SUBDIRS = new Set([
  'assets',
  'rapports',
  'archive',
  'archives',
  '.git',
])

// Profondeur max sous chaque REPO_DIR (0 = uniquement racine du dossier).
const MAX_DEPTH = 1

// Tronque les fichiers > N lignes (évite qu'un rapport oublié sature le contexte).
const MAX_LINES_PER_FILE = 500

// ─── HELPERS ─────────────────────────────────────────────────────────────────

function readFileSafe(filePath, { skipTruncation = false } = {}) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8')
    if (skipTruncation) return content
    const lines = content.split('\n')
    if (lines.length > MAX_LINES_PER_FILE) {
      return (
        lines.slice(0, MAX_LINES_PER_FILE).join('\n') +
        `\n\n[... fichier tronqué à ${MAX_LINES_PER_FILE} lignes — voir le fichier complet dans le repo ...]`
      )
    }
    return content
  } catch (err) {
    console.warn(`⚠️  Bobby n'a pas pu lire ${filePath} : ${err.message}`)
    return null
  }
}

function walkMarkdown(rootDir, currentDir = rootDir, depth = 0, results = []) {
  if (!fs.existsSync(currentDir)) return results
  if (depth > MAX_DEPTH) return results

  let entries
  try {
    entries = fs.readdirSync(currentDir, { withFileTypes: true })
  } catch (err) {
    console.warn(`⚠️  Bobby n'a pas pu lister ${currentDir} : ${err.message}`)
    return results
  }

  for (const entry of entries) {
    const fullPath = path.join(currentDir, entry.name)
    if (entry.isDirectory()) {
      if (EXCLUDE_SUBDIRS.has(entry.name)) continue
      walkMarkdown(rootDir, fullPath, depth + 1, results)
    } else if (entry.isFile() && entry.name.endsWith('.md')) {
      results.push(fullPath)
    }
  }
  return results
}

// ─── MAIN ────────────────────────────────────────────────────────────────────

async function readSecondBrain() {
  const cwd = process.cwd()
  const brain = {}

  // 1. Fichiers always-include (master + instructions, priorité absolue)
  for (const filename of ALWAYS_INCLUDE) {
    const fullPath = path.join(cwd, filename)
    if (!fs.existsSync(fullPath)) {
      console.warn(`⚠️  Fichier critique manquant : ${filename}`)
      continue
    }
    // Master + CLAUDE.md jamais tronqués (sources de vérité absolues).
    const content = readFileSafe(fullPath, { skipTruncation: true })
    if (content) brain[filename] = content
  }

  // 2. Scan auto des dossiers thématiques
  for (const dir of REPO_DIRS) {
    const root = path.join(cwd, dir)
    const files = walkMarkdown(root)
    for (const fullPath of files) {
      const relativePath = path.relative(cwd, fullPath)
      const content = readFileSafe(fullPath)
      if (content) brain[relativePath] = content
    }
  }

  // 3. Stats console
  const fileCount = Object.keys(brain).length
  const totalChars = Object.values(brain).reduce((sum, c) => sum + c.length, 0)
  const totalKChars = Math.round(totalChars / 1000)
  console.log(`📚 Bobby a chargé le Second Brain : ${fileCount} fichiers · ~${totalKChars}k caractères`)

  return brain
}

module.exports = { readSecondBrain }
