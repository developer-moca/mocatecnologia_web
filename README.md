# Moca Tecnologia

Static bilingual company website. English: `/`. Portuguese: `/pt/`.

## Preview

```sh
python3 -m http.server 8080
```

Open `http://localhost:8080/pt/`. Serve the repository root: assets use root-relative URLs.

## Editing

- `scripts/build_pages.py`: localized content and shared page templates.
- `assets/site.css`: responsive navy / matte gold visual system.
- `assets/site.js`: accessible mobile navigation.
- `assets/moca-mark.svg`: vector interpretation of the approved mountain and sun concept.
- `assets/favicon.svg`: small-format brand symbol.

After changing content, run `python3 scripts/build_pages.py` and commit the generated HTML too. Hosting does not require a build or third-party scripts. Existing English/Portuguese routes, TOODA documents, and CNAME remain supported.

## Content and contact

Verified contact links: `developer@mocatecnologia.com` and WhatsApp `+55 21 96604-5167`. Links open the visitor’s email client or WhatsApp; no messages are sent by this site.

Products: Dungeon Fighters (official game website), TOODA (existing repository material), Paper Hero (user-supplied YouTube video, title verified through YouTube oEmbed), and Kalimour (official Steam listing). External product images load from YouTube and Steam. Product destinations remain usable if those image services are unavailable.

Sources:
- https://dungeonfighters.github.io/Web/
- https://www.youtube.com/watch?v=pX-UymX0gXg
- https://store.steampowered.com/app/2402460/Kalimour/

The previous template's unused CSS, scripts and media remain in the repository for reference but are no longer loaded by the pages.

## Sharing previews

Every page has server-rendered Open Graph and Twitter card metadata, canonical URL, locale and a localized 1200×630 JPEG under `assets/share-*-v1.jpg`. To rebuild the social images from the site's SVG mark, run `python3 scripts/build_social_images.py` (requires librsvg and ImageMagick). Then regenerate pages with `python3 scripts/build_pages.py`. Version image filenames when replacing them to avoid stale image caches. Metadata follows https://ogp.me/.

## Product detail pages

Four bilingual product pages live at `/products/<slug>/` and `/pt/products/<slug>/`: `dungeon-fighters`, `tooda`, `paper-hero`, `kalimour`. Edit factual product content in `scripts/product_content.py`, then regenerate the 14 pages. Homepage cards link to these pages; original TOODA project routes remain available. Product descriptions use the public sources above.

TOODA Carnival 2026: partnership with FIA-RJ confirmed by the company owner. The supplied one-minute FIA-RJ video is served locally with manual playback and credit. The Tupi article covers the broader SOS Folia initiative; its 60,000-wristband figure is not attributed to TOODA deliveries.
- https://www.tupi.fm/rio/carnaval-2026-tera-60-mil-pulseiras-para-criancas-no-rj/
- https://www.instagram.com/p/DVJw0mWFM-b/

## SEO and services

`python3 scripts/build_pages.py` generates 18 pages plus `sitemap.xml` and
`robots.txt`. Service copy lives in `scripts/service_content.py`. All routes
include canonical URLs, reciprocal language alternatives, an English x-default,
and JSON-LD; home pages describe the organization and service pages describe
services. The generator is the source of truth for generated HTML.

Service pages: `/pt/services/custom-software/` and `/pt/services/metabase-bi/`,
with corresponding English routes under `/services/`. Public case descriptions
avoid operational details and do not claim measured outcomes or production
status based on repository code alone. Metabase is presented as a third-party
tool used in service delivery.

Search Console follow-up: verify the domain property, submit
`https://www.mocatecnologia.com/sitemap.xml`, inspect the service URLs and monitor
indexing and search queries. Publishing these files does not itself confirm
Google indexing or Search Console setup.

## Responsive images

`python3 scripts/build_images.py` builds lossless WebP variants with ImageMagick
at widths up to 480, 800, 1200 and the original width (never upscaled). Original
files remain available; remote sources are listed in the script and downloaded
into the ignored `.image-cache/` directory. Smaller JPEG originals remain in use
when lossless conversion would increase their size. Generated filenames include
a content hash. Commit `assets/optimized/` and `scripts/image_manifest.json`.
Then run `python3 scripts/build_pages.py` to refresh both languages.

`scripts/responsive_images.py` adds `srcset`, `sizes`, original aspect dimensions
and asynchronous decoding, and optimizes the video poster. Full-resolution WebP
versions were checked against originals with ImageMagick's absolute pixel error
metric (zero differing pixels). Smaller variants are resized for their display
size; original-resolution variants remain available for high-density screens.

## Brand identity in search

Use **Moca Tecnologia** as the brand name in both languages; translate service
copy, not the company name. `scripts/build_pages.py` defines the shared identity.
Home pages include one `WebSite` entity for the root domain, published by the
`Organization`. Every `WebPage` references that website and organization.
Canonical URLs and language alternatives remain separate for each translation.

Only confirmed company profiles belong in `OFFICIAL_PROFILES` / `sameAs`.
The existing GitHub account is https://github.com/developer-moca; product
websites and client accounts are not alternate identities of Moca.
The GitHub profile should use the name “Moca Tecnologia”, website
https://www.mocatecnologia.com/ and a description such as
“Software sob medida, produtos digitais e jogos. Conheça nossos projetos.”
Changing that account requires its owner's access.

These signals help communicate identity; they do not guarantee ranking or
disable Google's automatic spelling corrections. Reference:
https://developers.google.com/search/docs/appearance/site-names
