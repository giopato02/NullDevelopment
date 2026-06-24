# NullDevelopment — studio hub

The marketing hub for **NullDevelopment**, the solo app & web studio from me, Giorgi
Pataridze. Built with [Astro](https://astro.build) as a fully static site — no
runtime, no backend, deploys anywhere.

**Live:** <https://nulldevelopmentco.vercel.app>
**Studio app:** [NullState on Google Play](https://play.google.com/store/apps/details?id=app.nulldevelopment.nullstate) · **Code:** [github.com/giopato02](https://github.com/giopato02)

> **Custom domain:** `nulldevelopment.co` is the intended home. To move off the
> Vercel subdomain: add the domain under **Vercel → Project → Settings → Domains**,
> then change `site` in `astro.config.mjs` to `https://nulldevelopment.co` and push.
> The sitemap, `<link rel="canonical">`, and OG URLs all derive from that one value.

## Pages

- **Home** (`/`) — hero, apps grid, about, contact.
- **Privacy** (`/privacy`) — honest, editable policy used as the Google Play
  "privacy policy URL" (live at `/privacy` on the URL above).
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

## Deploy

This repo **auto-deploys to Vercel** — it auto-detects Astro (build `npm run build`,
output `dist`), so every push to `main` ships a new version. Other static hosts work
identically:

- **Cloudflare Pages** — preset *Astro*, build `npm run build`, output `dist`.
- **Netlify** — build `npm run build`, publish `dist`.

> `dist/` is generated build output — Vercel rebuilds it on every deploy, so it
> doesn't need to be committed. Consider adding `dist/` to `.gitignore`.

## Configure

Everything you'd change is marked with `▶ EDIT` / `[INSERT …]`:

| What | Where |
| --- | --- |
| Canonical site URL (sitemap, canonical, OG) | `astro.config.mjs` → `site` |
| Contact email + GitHub link | `src/consts.ts` |
| The apps grid (incl. NullState's Play Store URL) | `src/data/apps.ts` |
| Privacy policy specifics (analytics, dates, etc.) | `src/pages/privacy.astro` |
| Hero tagline | `src/pages/index.astro` |
| Colours, type & spacing tokens | `src/styles/global.css` (`:root`) |

Adding a new app is a one-line change: append an object to the array in
`src/data/apps.ts`. The `icon` field accepts either an image path under
`/public` (e.g. `/icons/nullstate.svg`) or a single glyph/emoji.

## Design tokens

All colours, type, and spacing live as CSS custom properties at the top of
`src/styles/global.css` (`:root`). Change a value once; it propagates site-wide.
Current palette: parchment / oxblood / sienna / cypress / brass / ink (warm,
vintage). Contrast pairings were checked against WCAG 2.1 AA (notes are inline).
*(Palette + logo are currently being revised.)*

## Fonts & images

- **JetBrains Mono** (the "Null" wordmark, status labels) is self-hosted from
  `public/fonts/` — no Google Fonts, no external requests. Body/UI uses the
  system grotesque (`system-ui`).
- **`public/og-image.png`** (1200×630) is the social-share card. To regenerate
  it from `public/og-image.svg`, see `scripts/og-image.py` (a dev-only Python
  helper — it is **not** part of `npm run build`).
- **`public/favicon.svg`** and the app-icon tiles use the ∅ (empty-set / "null")
  mark — the brand's recurring motif.
