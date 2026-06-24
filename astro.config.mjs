// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Canonical hub URL — currently the live Vercel deployment. When the custom
// domain nulldevelopment.co is connected in Vercel, change this one value to
// 'https://nulldevelopment.co' and redeploy; the sitemap, <link rel="canonical">
// and OG URLs all derive from it.
export default defineConfig({
  site: 'https://nulldevelopmentco.vercel.app',
  integrations: [sitemap()],
});
