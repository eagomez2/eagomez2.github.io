# estebangomez.me

My personal website, built with [Astro](https://astro.build) and published for free with GitHub Pages. All content lives in plain text files: edit one on github.com (pencil icon) or locally, commit to `main`, and the site rebuilds and goes live in about a minute.

## Table of contents

- [Structure of this repository](#structure-of-this-repository)
- [Adding content](#adding-content)
  - [Where everything lives](#where-everything-lives)
  - [About page, skills and social links](#about-page-skills-and-social-links)
  - [Publications](#publications)
  - [Talks, teaching and articles](#talks-teaching-and-articles)
  - [Projects](#projects)
  - [Images and files](#images-and-files)
  - [Resume](#resume)
- [Publishing on GitHub Pages](#publishing-on-github-pages)
- [Using a custom domain](#using-a-custom-domain)
- [Google Analytics](#google-analytics)
- [Search engines](#search-engines)
- [Working locally](#working-locally)
- [Copyright](#copyright)

## Structure of this repository

```text
.
├── .github/workflows/deploy.yml   # builds the site and publishes it to GitHub Pages on every push to main
├── astro.config.mjs               # site address, sitemap and redirects from old addresses
├── package.json                   # dependencies and npm scripts
├── public/                        # copied as-is to the website
│   ├── files/                     # PDFs (resume, manuals, posters…)
│   ├── images/                    # portrait and project images, one folder per project
│   ├── favicon.png
│   └── robots.txt
├── src/
│   ├── data/                      # content of the About and Research & Talks pages (YAML)
│   │   ├── site.yaml
│   │   ├── publications.yaml
│   │   └── research.yaml
│   ├── content/projects/          # one Markdown file per project
│   ├── content.config.ts          # the fields a project file can have
│   ├── pages/                     # one file per page; [year]/[month]/[day]/[slug].astro renders every project
│   ├── layouts/Base.astro         # shared frame: sidebar, menu, footer, theme toggle
│   ├── components/                # project list, picture enlarger, icons, analytics banner…
│   ├── lib/                       # helpers: data loading, tag colours, BibTeX formatting
│   └── styles/global.css          # colours, fonts and layout for the light and dark themes
└── tools/                         # one-off helper scripts, not used to build the site
```

You normally only need to touch `src/data/`, `src/content/projects/` and `public/`.

## Adding content

### Where everything lives

| What | Where |
| --- | --- |
| Bio, skills, degrees, social links, contact text, analytics ID | `src/data/site.yaml` |
| Publications (order on the page = order in the file) | `src/data/publications.yaml` |
| Talks, teaching, articles | `src/data/research.yaml` |
| Software & Hardware and Sound & Music projects | `src/content/projects/*.md` (one file per project) |
| Images | `public/images/` |
| PDFs (resume, manuals…) | `public/files/` |
| Colours of programming-language tags | `src/lib/tags.ts` |

### About page, skills and social links

Edit `src/data/site.yaml`. The comments at the top of the file explain each field. Text in `bio` can use `**bold**`. Each skills group is one comma-separated line; programming languages get a coloured dot, with colours set in `src/lib/tags.ts`.

### Publications

Copy an entry in `src/data/publications.yaml`, paste it at the top and change the fields. `abstract` and `bibtex` use `|` so you can paste several lines. The BibTeX is indented and aligned automatically on the page.

### Talks, teaching and articles

Add a line to the matching list in `src/data/research.yaml`. Lists are shown in the order of the file.

### Projects

1. Put a cover image in `public/images/projects/<slug>/cover.jpg`. Covers look best at 16:10 (for example 800×500 pixels). Any other shape also works: the whole image is always shown, never cropped, and the empty space around it is filled automatically with a blurred copy of the same image.
2. Copy any file in `src/content/projects/`, rename it to `<slug>.md` and edit the top block:

```yaml
---
title: "Project name"            # shown in the project list
heading: "Longer page title"     # optional, shown on the project page
subtitle: "One line"             # shown under the title in the list
category: "software"             # or "sound"
date: "2026-11-07"               # newest first; also used in the address /2026/11/07/<slug>/
order: 1                         # only breaks ties between projects with the same date
tags: ["Open source", "Python"]  # optional, shown as small tags in the list
cover: "/images/projects/<slug>/cover.jpg"
---
```

3. Write the page below it in Markdown (or HTML).

Useful snippets for the page:

- **Image beside text:** `<div class="cols"><div class="col col-1-3">…</div><div class="col col-2-3">…</div></div>`
- **Section heading:** `<h3>Pictures</h3>`
- **Video:**

  ```html
  <div class="video"><iframe src="https://www.youtube-nocookie.com/embed/VIDEO_ID" title="Video player" loading="lazy" allowfullscreen></iframe></div>
  ```

Every picture inside a `<figure>` can be clicked (or tapped) to see it larger; nothing extra is needed. Give every image a short description in `alt="…"`: it helps image search and people using screen readers. The page's search-result description is taken from its first paragraph automatically.

### Images and files

Anything in `public/` is published at the same path, so `public/files/poster.pdf` becomes `/files/poster.pdf`. Keep project images in `public/images/projects/<slug>/`.

### Resume

Overwrite `public/files/esteban-gomez-resume.pdf` with the new file and keep the same name. The Resume menu item links to it.

## Publishing on GitHub Pages

1. In the repository go to **Settings → Pages** and set **Source** to **GitHub Actions**.
2. Push to `main`. The workflow in `.github/workflows/deploy.yml` builds and publishes the site. Progress is shown in the **Actions** tab.

## Using a custom domain

1. Add a file `public/CNAME` that contains only your domain, for example `www.example.com`.
2. Set the same address in `site` in `astro.config.mjs` and in `url` in `src/data/site.yaml`.
3. At your DNS provider, follow GitHub's guide to [managing a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site): a `CNAME` record for `www` pointing to `<your-user>.github.io`, and `A` records for the bare domain pointing to GitHub's Pages servers. Leave any existing email (`MX`) records as they are.
4. Once the domain works, tick **Enforce HTTPS** in **Settings → Pages**.

If a page used to live at a different address, add a redirect under `redirects` in `astro.config.mjs` so old links keep working.

## Google Analytics

Paste your GA4 Measurement ID (`G-XXXXXXXXXX`) into `googleAnalyticsId` in `src/data/site.yaml`. This ID is public by design, so it is safe to commit. Analytics only loads after a visitor clicks **Allow** on a small banner, which keeps the site in line with GDPR, and it never loads while working locally. Leave the value empty to turn analytics off.

## Search engines

The site already includes a sitemap (`/sitemap-index.xml`), `robots.txt`, a description for every page, and structured data that tells search engines who you are and links your profiles. After publishing:

1. Add the site in [Google Search Console](https://search.google.com/search-console) and submit `<your-site>/sitemap-index.xml` under **Sitemaps**.
2. Do the same in [Bing Webmaster Tools](https://www.bing.com/webmasters) (it can import from Search Console).
3. Link to the site from your academic and social profiles.

## Working locally

You need [Node.js](https://nodejs.org) 22 or newer.

```sh
npm install
npm run dev      # live preview at http://localhost:4321
npm run build    # production build in dist/
npm run preview  # serve the production build
```

## Copyright

© Esteban Gómez. All rights reserved.
