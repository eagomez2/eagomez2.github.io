import { load } from 'js-yaml';
import siteRaw from '../data/site.yaml?raw';
import pubsRaw from '../data/publications.yaml?raw';
import researchRaw from '../data/research.yaml?raw';
import { getCollection, type CollectionEntry } from 'astro:content';

export interface Link { label: string; href: string; short?: string }
export interface Site {
  name: string; tagline: string; url: string; googleAnalyticsId?: string; resume: string; bio: string;
  skills: { label: string; items: string }[];
  degrees: { degree: string; school: string; years: string }[];
  social: Link[];
  contact: { text: string; signoff: string; sign: string; email: string };
  githubNote: string; copyright: string;
}
export interface Publication {
  title: string; type: string; year: string | number; authors: string; venue?: string; note?: string;
  supervisors?: string; links: Link[]; keywords?: string; abstract?: string; bibtex?: string;
}

export const site = load(siteRaw) as Site;
export const publications = load(pubsRaw) as Publication[];
export const research = load(researchRaw) as { talks: string[]; teaching: string[]; articles: { title: string; href: string }[] };

export type Project = CollectionEntry<'projects'>;

export async function getProjects(category: 'software' | 'sound'): Promise<Project[]> {
  const all = await getCollection('projects', (p) => p.data.category === category);
  return all.sort((a, b) => b.data.date.getTime() - a.data.date.getTime() || a.data.order - b.data.order);
}

/** Keeps the old WordPress address: /YYYY/MM/DD/slug/ */
export function projectUrl(p: Project): string {
  const d = p.data.date;
  const pad = (n: number) => String(n).padStart(2, '0');
  return `/${d.getUTCFullYear()}/${pad(d.getUTCMonth() + 1)}/${pad(d.getUTCDate())}/${p.id}/`;
}

/** Minimal inline formatting for YAML text: **bold** only. */
export function inline(text: string): string {
  const esc = text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  return esc.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
}
