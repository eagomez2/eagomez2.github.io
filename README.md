# estebangomez.me

Personal website of Esteban Gómez, built with [Astro](https://astro.build) and published for free with GitHub Pages.

## Adding or changing content

All text lives in plain files. Edit them on github.com (pencil icon) and commit: the site rebuilds and goes live in about a minute.

| What | Where |
| --- | --- |
| Bio, skills, degrees, social links, contact text, analytics ID | `src/data/site.yaml` |
| Publications (order on the page = order in the file) | `src/data/publications.yaml` |
| Talks, teaching, Medium articles | `src/data/research.yaml` |
| Software & Hardware and Sound & Music projects | `src/content/projects/*.md` (one file per project) |
| Images | `public/images/` |
| PDFs (resume, manuals…) | `public/files/` |
| Colours of programming-language tags | `src/lib/tags.ts` |

### Add a publication

Copy an entry in `src/data/publications.yaml`, paste it at the top and change the fields. `abstract` and `bibtex` use `|` so you can paste several lines.

### Add a project

1. Put a square-ish cover image in `public/images/projects/<slug>/cover.jpg`.
2. Copy any file in `src/content/projects/`, rename it to `<slug>.md` and edit the top block:

```yaml
---
title: "Project name"          # shown in the project list
heading: "Longer page title"   # optional, shown on the project page
subtitle: "One line"            # shown under the title in the list
category: "software"           # or "sound"
date: "2026-11-07"             # newest first; also used in the address /2026/11/07/<slug>/
order: 1                       # only breaks ties between projects with the same date
tags: ["Open source", "Python"] # optional, shown as small tags in the list
cover: "/images/projects/<slug>/cover.jpg"
---
```

3. Write the page below it in Markdown (or HTML). To embed a video use:

```html
<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/VIDEO_ID" title="Video player" loading="lazy" allowfullscreen></iframe></div>
```

Give every image a short description in `alt="…"`. It helps image search and people using screen readers. The page's search-result description is taken from its first paragraph automatically.

To put an image beside text, wrap them in `<div class="cols"><div class="col col-1-3">…</div><div class="col col-2-3">…</div></div>`.

### Replace the resume

Overwrite `public/files/esteban-gomez-resume.pdf` with the new file (keep the name).

## Google Analytics

Paste your GA4 Measurement ID (`G-XXXXXXXXXX`) into `googleAnalyticsId` in `src/data/site.yaml`. This ID is public by design, so it is safe to commit. Analytics only loads after a visitor clicks **Allow** on a small banner, which keeps the site in line with GDPR. Leave the value empty to turn analytics off.

## Search engines

The site already includes a sitemap (`/sitemap-index.xml`), `robots.txt`, a description for every page, and hidden structured data that tells Google who you are and links your profiles. After launch:

1. Add the site in [Google Search Console](https://search.google.com/search-console) (choose **Domain** and verify with the DNS record it gives you), then submit `https://www.estebangomez.me/sitemap-index.xml` under **Sitemaps**.
2. Do the same in [Bing Webmaster Tools](https://www.bing.com/webmasters) (it can import from Search Console).
3. Link to the site from your Google Scholar, GitHub, LinkedIn, ORCID and university profiles.

## First-time setup on GitHub

1. In the repository go to **Settings → Pages** and set **Source** to **GitHub Actions**.
2. Push to `main`. The workflow in `.github/workflows/deploy.yml` builds and publishes the site.
3. Custom domain (when you are ready to switch from WordPress): add a file `public/CNAME` containing `www.estebangomez.me`. At your DNS provider, point `www` to `<your-user>.github.io` with a CNAME record, and the bare domain to GitHub's four A records (185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153). Then tick **Enforce HTTPS** in Settings → Pages.

Old WordPress addresses keep working: page and project URLs are the same, and the old `/download/…` links redirect to the PDFs.

## Working locally (optional)

```sh
npm install
npm run dev      # http://localhost:4321
npm run build    # output in dist/
```

`tools/import_wordpress.py` is the one-time script that copied the project pages from the old WordPress site. It is not needed any more.
