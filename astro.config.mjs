import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
  markdown: {
    shikiConfig: {
      // You can choose from Shiki's built-in themes
      // 'github-dark' is excellent for "Blueprint" aesthetic
        themes: {
          light: 'github-light',
          dark: 'github-dark',
        },      
      // Optional: Add custom languages if you use them in snippets
      langs: ['javascript', 'typescript', 'python', 'json', 'yaml'],
      
      // Enable word wrap so code doesn't break your mobile layout
      wrap: true,
    },
  },
});