// @ts-check
import { defineConfig } from 'astro/config';
// Preview build — configurable for a GitHub Pages subpath:
//   SITE_URL=https://user.github.io BASE_PATH=/fv-peinture npm run build
export default defineConfig({
  output: 'static',
  site: process.env.SITE_URL || 'http://localhost:4321',
  base: process.env.BASE_PATH || '/',
  trailingSlash: 'ignore',
  build: { inlineStylesheets: 'auto' },
  devToolbar: { enabled: false },
});
