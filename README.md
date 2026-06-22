# NullDevelopment — studio hub

The marketing hub for **NullDevelopment**, the solo app & web studio of Giorgi
Pataridze. Built with [Astro](https://astro.build) as a fully static site — no
runtime, no backend, deploys anywhere.

- **Home** (`/`) — hero, apps grid, about, contact.
- **Privacy** (`/privacy`) — honest, editable policy usable as the Google Play
  "privacy policy URL".
- **404** — on-brand "value is null" page.

## Develop

```bash
npm install
npm run dev      # http://localhost:4321
```

## Build

```bash
npm install
npm run build    # static output → ./dist
npm run preview  # serve ./dist locally to check the production build
```

## Deploy (zero config)

The build is plain static files in `dist/`. Any static host works.

**Cloudflare Pages**
- Framework preset: **Astro**
- Build command: `npm run build`
- Build output directory: `dist`

**Vercel**
- Import the repo — Vercel auto-detects Astro. Defaults are correct
  (build `npm run build`, output `dist`). No config needed.

**Netlify**
- Build command: `npm run build`
- Publish directory: `dist`

## What to edit before launch

Everything you need to change is marked with `▶ EDIT` / `[INSERT …]`:

| What | Where |
| --- | --- |
| Canonical site URL (sitemap, canonical, OG) | `astro.config.mjs` → `site` |
| Contact email + optional GitHub link | `src/consts.ts` |
| The apps grid (incl. NullState's Play Store URL) | `src/data/apps.ts` |
| Privacy policy specifics (analytics, dates, etc.) | `src/pages/privacy.astro` |
| Hero tagline (2 alternatives are commented in) | `src/pages/index.astro` |

Adding a new app is a one-line change: append an object to the array in
`src/data/apps.ts`. The `icon` field accepts either an image path under
`/public` (e.g. `/icons/nullstate.svg`) or a single glyph/emoji.

## Design tokens

All colours, type, and spacing live as CSS custom properties at the top of
`src/styles/global.css` (`:root`). Change a value once; it propagates site-wide.
Palette: parchment / oxblood / sienna / cypress / brass / ink. Contrast pairings
were checked against WCAG 2.1 AA (notes are inline in that file).

## Fonts & images

- **JetBrains Mono** (the "Null" wordmark, status labels) is self-hosted from
  `public/fonts/` — no Google Fonts, no external requests. Body/UI uses the
  system grotesque (`system-ui`).
- **`public/og-image.png`** (1200×630) is the social-share card. To regenerate
  it from `public/og-image.svg`, see `scripts/og-image.py` (a dev-only Python
  helper — it is **not** part of `npm run build`).
- **`public/favicon.svg`** and the app-icon tiles use the ∅ (empty-set / "null")
  mark — the brand's recurring motif.
