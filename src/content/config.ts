import { defineCollection, z } from 'astro:content';

const pulse = defineCollection({
  schema: z.object({
    title: z.string(),
    // This tells Astro to convert strings like "2025-05-28" into Date objects
    date: z.date(), 
    excerpt: z.string(),
    tag: z.string(),
    readTime: z.string(),
  }),
});

export const collections = { pulse };