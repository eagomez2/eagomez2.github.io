// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://www.estebangomez.me',
  trailingSlash: 'ignore',
  integrations: [sitemap({ filter: (page) => !page.includes('/download/') })],
  redirects: {
    // Old WordPress resume link
    '/download/517': '/files/esteban-gomez-resume.pdf',
    '/download/691': '/files/sd_manual1.4br2.pdf',
    '/download/795': '/files/peq1-flexible-riaa-eq-analysis.pdf',
    '/download/798': '/files/peq1-poster-esteban-gomez-spanish.pdf',
  },
});
