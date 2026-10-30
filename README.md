# BusinessReviews.com

A moderated review and buyer's-guide hub for business software, finance products and professional services. It's a static site, ready for GitHub Pages and monetised with Google AdSense, a lead-generation engine, business plans, sponsorships, contests and reader support.

## Structure

| Path | Purpose |
|---|---|
| `index.html` and other root `*.html` | Page sources (front matter + body), built by GitHub Pages' Jekyll from `main` / root |
| `_layouts/`, `_includes/`, `_data/categories.yml` | Shared page chrome, the quick-match form, and category data |
| `categories/` | 16 category buyer's guides |
| `guides/` | Editorial guides |
| `assets/css/style.css` | Design system: light and dark themes, responsive |
| `assets/js/main.js` | Navigation, theme, forms, star ratings, multi-step flows, search, cookie notice, lazy video |
| `assets/js/tools.js` | Interactive tools: scorecard, TCO, response writer, request builder, rating goal |
| `build/` | Python generator and content: `categories.py`, `guides.py`, `pages.py` |
| `docs/BUILD-PROMPT.md` | Phase-by-phase build prompt and business model |
| `ads.txt`, `robots.txt`, `sitemap.xml`, `search-index.json` | SEO and ads files |

## Edit and rebuild

Content lives in `build/*.py`. After editing, regenerate the Jekyll sources and commit:

```bash
pip install pyyaml
python3 build/export_jekyll.py .                   # regenerates pages, layouts, _data
python3 build/export_jekyll.py --preview _preview  # optional plain-HTML preview (gitignored)
```

GitHub Pages builds the final HTML, `sitemap.xml` and `search-index.json` with Jekyll on every push to `main`. No Actions workflow is needed. Don't run `build/build.py` directly in the repo root; use the preview flag.

- **New category:** add a dict to `build/categories.py`.
- **New guide:** add a dict to `build/guides.py`.
- **New page:** add an entry to `PAGES` in `build/pages.py`.

## Forms

All forms post through FormSubmit to the owner's private inbox. The address is assembled at runtime and never appears in page source. The first submission sends a one-time activation email, which must be confirmed.

## Donations

To show "Give by card / PayPal / Ko-fi" buttons, set the links in `DONATE_LINKS` near the top of `assets/js/main.js`, or define `window.BR_DONATE_LINKS` before it loads. Until then, the pledge form collects pledges and a payment link is sent by email.

## Deployment

1. Go to **Settings → Pages → Build and deployment**, choose **Deploy from a branch**, then **main** and **/ (root)**. GitHub's built-in Jekyll build publishes the site at `https://webworksa1.github.io/businessreviews-com/`.
2. To use the custom domain, add a `CNAME` file containing `businessreviews.com` and point DNS to GitHub Pages:
   - A records: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - or a CNAME for `www` to `webworksa1.github.io`
3. Enforce HTTPS.

## Trademark & copyright

"Business reviews" is used as a generic, descriptive phrase. No exclusive trademark rights are claimed, and the site is not affiliated with any similarly named company or review platform. See `trademark-copyright.html`. Third-party names are the marks of their owners. Original site content © BusinessReviews.com.

For interest in this website, the domain, sponsorship, advertising or partnership, see https://web.works/contact.
