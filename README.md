# Binh Huy Nguyen — academic homepage

A research-led academic portfolio built with Jekyll and hosted on GitHub Pages.
Custom Liquid layouts and plain CSS replace the original Minima presentation.
No JavaScript, client-side framework, external fonts, or custom Jekyll plugins are required.

## Structure

- `_layouts/default.html`: semantic document shell, metadata, header, and footer.
- `_layouts/home.html`: compact identity, five research streams, publications, software, and career.
- `_layouts/page.html` and `_layouts/research.html`: inner pages and illustrated research narratives.
- `_includes/`: shared navigation, profiles, figures, showcase, publications, software, and career.
- `_research/*.md`: scientific narratives, summaries, ordering, and figure metadata.
- `_data/career.yml`: homepage career summary, transcribed from `cv.md`.
- `_data/publications.yml`: verified publication records; deliberately empty for now.
- `assets/css/site.css`: responsive visual system, keyboard focus, and print styles.
- `assets/images/research/`: self-contained author-controlled research images and provenance notes.
- `_config.yml`: identity, profile links, navigation, collections, and site-wide settings.

Canonical routes remain `/`, `/research/`, `/publications/`, `/software/`, `/cv/`,
and `/research/<theme>/`. The collection permalink and explicit page permalinks
preserve these independently of layout names. The five research streams are
ordered by each document's `order` field.

## Local build and GitHub Pages

Use Ruby and Bundler, then:

```sh
bundle install
bundle exec jekyll serve
# Production parity / link review:
JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter
```

The Gemfile uses the `github-pages` dependency set. The only enabled plugin is
GitHub Pages-supported `jekyll-seo-tag`. Publish from the root of `main` in the
repository's existing Pages settings. No theme dependency or build-time asset
pipeline is needed. Never commit `_site`, caches, or installed dependencies.
Asset provenance documentation is excluded from the generated site.

## Adding publications

The shared publication component supports title, authors, venue, year, and
optional DOI URL, preprint URL, code URL, related research URL, and `selected`.
Add only verified records to `_data/publications.yml`; mark four to six as
`selected: true` for the homepage. The homepage caps the list at six; the
publications page displays all records. Until records exist, both surfaces
provide a concise Google Scholar link, without fabricated entries or empty cards.
`assets/publications.bib` remains reserved for a verified BibTeX export; it is
not automatically parsed and should be kept consistent when populated.

## Content maintenance

Keep scientific narratives in `_research` authoritative; summaries are concise
presentation text. Keep `cv.md` and `_data/career.yml` consistent. A PDF CV is
not supplied, so no download link is shown. DiffFEM is linked at its supplied
repository URL and explicitly marked as a public release in preparation;
no private implementation details have been imported.

Figures retain their scientific panels and legends. The detail pages and every
caption link to full-size assets. See the image README for sources and exports.
Navigation remains visible at every viewport without JavaScript. The responsive
layout stacks in reading order below 700px; figure dimensions reserve layout
space and lazy loading limits initial transfer.
