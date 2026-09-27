# Binh Huy Nguyen — academic homepage

A research-led academic portfolio built with Jekyll and hosted on GitHub Pages.
Custom Liquid layouts and plain CSS replace the original Minima presentation.
No JavaScript, client-side framework, external fonts, or custom Jekyll plugins are required.

## Structure

- `_layouts/default.html`: semantic document shell, metadata, header, and footer.
- `_layouts/home.html`: compact identity, five research streams, publications, software, and career.
- `_layouts/page.html` and `_layouts/research.html`: inner pages and illustrated research narratives.
- `_includes/`: shared navigation, profiles, figures, research showcase, selected works, publications, software, and career.
- `_research/*.md`: authoritative theme narratives, summaries, ordering, primary figures, and ordered work IDs.
- `_data/works.yml`: thematic research-output layer. One work may belong to multiple themes and may reference figures, code, or media.
- `_data/publications.yml`: verified bibliographic records used by the homepage and Publications page.
- `_data/career.yml`: homepage career summary, transcribed from `cv.md`.
- `assets/css/site.css`: responsive visual system, keyboard focus, and print styles.
- `assets/images/research/`: self-contained author-controlled research images and provenance notes.
- `assets/media/`: scientific animations and experimental media.
- `_config.yml`: identity, profile links, navigation, collections, and site-wide settings.

Canonical routes remain `/`, `/research/`, `/publications/`, `/software/`, `/cv/`,
and `/research/<theme>/`. The collection permalink and explicit page permalinks
preserve these independently of layout names. The five research streams are
ordered by each document's `order` field.

## Research content model

The site uses three levels rather than treating each research theme as a single project:

1. **Homepage:** five broad research streams, each with one main visual and up to three compact selected-work links.
2. **Research detail pages:** the theme narrative followed by the full ordered set of selected works for that theme.
3. **Publications:** the central bibliographic index.

Work IDs live in `_data/works.yml` and are referenced from each research page through
`selected_works`. Cross-listing is intentional: for example, differentiable
ferroelectric FEM belongs to both Ferroelectric MEMS and Scientific Machine Learning
& Differentiable Mechanics, while FNO homogenization bridges Scientific Machine
Learning and Multiscale Computational Mechanics.

Each work may carry a `source_figure` pointing to author-controlled source artwork in
another repository. Those paths are provenance/design inputs, not public-site links.
Web-ready animations may be recorded under `media`; the shared works component exposes
only entries with `web_ready: true`. Source formats such as AVI remain in the data model
but are not rendered until converted to a browser-ready MP4/WebM derivative.

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

## Publications

`_data/publications.yml` is the bibliographic source used by the shared publication
component. Records contain an internal `id`, title, authors, venue/status, year,
theme membership, and optional DOI/preprint/code links. Four to six records may be
marked `selected: true` for the homepage; the Publications page displays the complete
verified set.

`assets/publications.bib` remains reserved for a BibTeX export and is not automatically
parsed. If it is populated later, keep it consistent with the YAML records.

## Content maintenance

Keep scientific narratives in `_research` authoritative and keep work summaries in
`_data/works.yml` concise. A work should be defined once and cross-listed by ID rather
than duplicated between themes. Keep `cv.md` and `_data/career.yml` consistent.

Figures retain their scientific panels and legends. The detail pages and every theme
caption link to full-size assets. Navigation remains visible at every viewport without
JavaScript. The responsive layout stacks in reading order below 700px; figure dimensions
reserve layout space and lazy loading limits initial transfer.
