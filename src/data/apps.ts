// ============================================================================
// NullDevelopment — apps grid data (SINGLE SOURCE OF TRUTH)
// ----------------------------------------------------------------------------
// Adding a future app is a ONE-LINE change: append an object to the array
// below. The home page maps over it automatically — no other file to touch.
//
// `icon` can be either:
//   • a path to an image in /public  (e.g. '/icons/nullstate.svg'), or
//   • a short glyph/emoji            (e.g. '∅')  — rendered in a tile.
// ============================================================================

export interface App {
  /** Product name — keep the "Null" prefix per brand. */
  name: string;
  /** Drives the badge + actions. */
  status: 'live' | 'soon';
  /** 1–2 sentences for the card body. */
  description: string;
  /** Image path under /public, or a single glyph/emoji. */
  icon: string;
  /** Store / landing link. Omit (or '') for "coming soon" concepts. */
  link?: string;
}

export const apps: App[] = [
  {
    name: 'NullState',
    status: 'live',
    // ▶ CONFIRM this matches the live listing copy.
    description:
      'A distraction-free focus timer and journal in one — a custom timer with Strict Mode, weekly stats, and a clean journal. Fully offline, no account, no subscription: your data never leaves your phone.',
    icon: '/icons/nullstate.png',
    // Real Google Play package id (app.nulldevelopment.nullstate). ▶ Confirm the
    // listing is published before relying on this link in marketing.
    link: 'https://play.google.com/store/apps/details?id=app.nulldevelopment.nullstate',
  },

  // ── Coming-soon CONCEPTS ─────────────────────────────────────────────────
  // These three are invented placeholders to show the "every product carries
  // Null" naming quirk. Rename / replace / delete freely.
  {
    name: 'NullPoint',
    status: 'soon',
    description:
      'A distraction-free writing surface that clears itself once you are done — so a blank page never feels heavy again.',
    icon: '/icons/nullpoint.svg',
  },
  {
    name: 'NullTrace',
    status: 'soon',
    description:
      'Private, on-device habit tracking. Watch your streaks build without a single byte of your data ever leaving your phone.',
    icon: '/icons/nulltrace.svg',
  },
  {
    name: 'NullFlow',
    status: 'soon',
    description:
      'Lightweight automations for the small, repetitive tasks you keep forgetting to do. Set it once, then forget it on purpose.',
    icon: '/icons/nullflow.svg',
  },
];

export default apps;
