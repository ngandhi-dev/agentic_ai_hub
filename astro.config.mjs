// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  // Replace with your custom domain
  site: 'https://www.agentsicworld.com',

  outDir: 'dist',

  vite: {
    plugins: [tailwindcss()],
  },
});