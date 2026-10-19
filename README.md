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

Products: TOODA (existing repository material), Paper Hero (user-supplied YouTube video, title verified through YouTube oEmbed), and Kalimour (official Steam listing). External product images load from YouTube and Steam. Product destinations remain usable if those image services are unavailable.

Sources:
- https://www.youtube.com/watch?v=pX-UymX0gXg
- https://store.steampowered.com/app/2402460/Kalimour/

The previous template's unused CSS, scripts and media remain in the repository for reference but are no longer loaded by the pages.

## Sharing previews

Every page has server-rendered Open Graph and Twitter card metadata, canonical URL, locale and a localized 1200×630 JPEG under `assets/share-*-v1.jpg`. To rebuild the social images from the site's SVG mark, run `python3 scripts/build_social_images.py` (requires librsvg and ImageMagick). Then regenerate pages with `python3 scripts/build_pages.py`. Version image filenames when replacing them to avoid stale image caches. Metadata follows https://ogp.me/.
