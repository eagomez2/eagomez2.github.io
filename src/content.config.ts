import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// One Markdown file per project in src/content/projects/.
// category decides the page it is listed on; newer dates come first,
// and `order` breaks ties between projects with the same date.
const projects = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(),
    heading: z.string().optional(),
    subtitle: z.string(),
    category: z.enum(['software', 'sound']),
    date: z.coerce.date(),
    order: z.number().default(0),
    cover: z.string(),
    tags: z.array(z.string()).default([]),
  }),
});

export const collections = { projects };
