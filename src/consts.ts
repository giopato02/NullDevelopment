// ============================================================================
// NullDevelopment — site-wide constants
// ----------------------------------------------------------------------------
// ▶ EDIT ME: everything Giorgi needs to change before launch lives here (plus
//   the apps list in src/data/apps.ts and the canonical URL in astro.config.mjs).
// ============================================================================

export const SITE_TITLE = 'NullDevelopment';

export const SITE_DESCRIPTION =
  'NullDevelopment is the solo studio of Giorgi Pataridze. Small, focused apps and websites, each one carrying the Null. NullState is live on Google Play.';

// Public contact address (no backend — this opens the visitor's mail client).
export const CONTACT_EMAIL = 'nulldevelopment.co@gmail.com';

// Optional. Leave as '' to hide the GitHub link in the footer.
export const GITHUB_URL = 'https://github.com/giopato02';

// The canonical hub URL lives in astro.config.mjs (`site`) so the sitemap,
// robots.txt and <link rel="canonical"> all stay in sync from one place.
// Currently the live Vercel URL; switch it there to https://nulldevelopment.co
// once the custom domain is connected.
