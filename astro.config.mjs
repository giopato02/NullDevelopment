// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Canonical hub URL. Domain not yet registered — placeholder for Giorgi to keep
// or swap once the real domain is live. The /privacy page resolves under this.
export default defineConfig({
  site: 'https://nulldevelopmentco.vercel.app',
  integrations: [sitemap()],
});
