# BusinessReviews.com: phase-by-phase build prompt

This is a reusable, phased prompt for building (or rebuilding) BusinessReviews.com. Each phase is self-contained, so you can paste them one at a time into an AI coding assistant or give them to a developer. The site in this repository is the output of Phases 1–7.

> **Contact address placeholder:** wherever the prompt says `[OWNER_EMAIL]`, use the owner's private inbox. Store it **only** in obfuscated JavaScript, never as plain text in HTML, Markdown, link `href`s or metadata.

---

## The business idea (why this concept wins)

**BusinessReviews.com = a moderated review and buyer's-guide hub for B2B software, finance products and professional services, with a free "get matched" lead engine.**

| Revenue lever | Why it fits this domain | Rough economics (illustrative, not guaranteed) |
|---|---|---|
| **AdSense display ads** | B2B software, payments, insurance, loans and business services sit among the highest-CPC ad verticals | Category and guide pages are high commercial intent, so RPM tends to run well above consumer-review niches |
| **Pay-per-lead "Get matched"** | Capterra, Software Advice and Clutch all monetise this way; buyers who fill out a 4-step form are near purchase | B2B software and services leads commonly sell for tens to hundreds of dollars each |
| **Business plans** (widgets, insights) | Claimed profiles turn businesses into recurring customers (the Trustpilot and Birdeye model) | Monthly SaaS-style revenue per business |
| **Labelled sponsorships** | Category, newsletter, contest and video sponsors | Flat monthly fees |
| **Reader support** | Donations fund moderation and prizes | Small, but builds goodwill |
| **Domain/strategic exit** | The exact-match generic .com is itself an asset | The topbar routes buyers to the owner |

**Why not a pure Yelp/Trustpilot clone?** Consumer local reviews need millions of reviews before they're useful, and the incumbents are entrenched. The B2B guide + lead model earns from day one through content, AdSense and lead capture, and the reviews compound over time.

**Hard rule:** never seed fake reviews or invented ratings. Show "No verified reviews yet / write the first review" until real, moderated reviews exist. This is also what AdSense's user-generated-content policy and the FTC's 2024 rule on consumer reviews and testimonials require.

---

## Phase 1: Research and information architecture

```
Act as a product strategist. Study at least 35 leading review, comparison and reputation sites
(Trustpilot, G2, Capterra, Software Advice, GetApp, TrustRadius, Gartner Peer Insights, BBB,
Sitejabber/SmartCustomer, ConsumerAffairs, Clutch, GoodFirms, UpCity, DesignRush, Expertise.com,
Thumbtack, Angi, HomeAdvisor, Houzz, Yelp, Tripadvisor, Glassdoor, Indeed, Kununu, Product Hunt,
AlternativeTo, SourceForge, Crozdesk, SaaSworthy, Reviews.io, Feefo, Yotpo, Birdeye, Podium,
ProvenExpert, Which?, Consumer Reports, Forbes Advisor, NerdWallet, TechRadar Pro).
Produce: (1) a feature matrix, (2) lead-form field patterns, (3) review-form fields and
verification methods, (4) trust/transparency policies, (5) trust design patterns.
Then define a sitemap for BusinessReviews.com: home, categories index, one page per category,
guides index + articles, get-quotes (lead gen), write-review, for-business (claim profile),
advertise, contests, careers, donate, tools, videos, awards, about, contact, methodology,
review guidelines, privacy, terms, cookies, disclaimer, trademark & copyright, search, 404.
```

## Phase 2: Design system

```
Create a distinctive, trustworthy design system for BusinessReviews.com, avoiding lookalikes
of Trustpilot green or Yelp red.
Tokens: Ink #12213A, Mist #EEF2F7, Paper #FFFFFF, Ultramarine #2D3FE0 (actions),
Marigold #F4A300 (stars: the signature element), Jade #0E8A63 (verified/success).
Type: Bricolage Grotesque (display), Public Sans (body).
Components: sticky header, mobile drawer nav, dark mode, buttons, chips, cards, star rating
input, multi-step forms with progress bar, opt-grid radio tiles, FAQ accordions, lazy YouTube
embeds, cookie notice, sticky CTA, exit-intent modal, footer with newsletter.
Accessibility: visible focus, skip link, reduced motion, WCAG AA contrast, labelled inputs.
On EVERY page, add a top bar reading "Contact, if you are interested in this website/domain
name/Sponsorship/Advertisement/Partnership" that links to https://web.works/contact.
```

## Phase 3: Core pages and content

```
Build a static site generator in Python (build/build.py) that writes plain HTML into the repo
root. All links must be relative so it works on a GitHub Pages project URL and on the custom
domain. Data lives in build/categories.py, build/guides.py and build/pages.py.
Write original, substantive content (no thin pages):
- 16 category guides: intro, what to look for, pricing models, commonly evaluated providers
  (names and links only, no ratings), questions to ask, red flags, FAQ with FAQPage schema.
- 10+ buyer's guides (spot fake reviews, get reviews ethically, respond to negative reviews,
  7-step software buying framework, CRM guide, Google Business Profile checklist, star
  ratings explained, SaaS TCO, vetting agencies, payment fees).
- Home: search hero + interactive star "start a review" panel, two-path band ("Get matched"
  vs "Browse and compare"), categories, 4-step publication process, lead band, guides, tools,
  videos, owner CTA, community (contests/careers/donate/awards).
```

## Phase 4: Lead generation and forms

```
Implement every form with no backend: on submit, POST JSON to
https://formsubmit.co/ajax/[OWNER_EMAIL], building the address at runtime from an obfuscated
char-code array in assets/js/main.js. The address must never appear in page source.
Include a honeypot field, inline success/error states, and a mailto: fallback built at runtime.
Forms: 4-step Get Matched (category + stage → company size, users, budget, timeline, current
tool, region, industry → must-haves + notes → name, work email, company, phone, contact
preference, required contact consent + OPTIONAL consent to share with up to 3 providers);
quick-match sidebar form on category/guide pages; exit-intent shortlist modal; newsletter;
3-step review submission (business, category, star rating, title → review ≥100 chars, pros,
cons, sub-ratings, 0–10 recommend, date of experience, usage duration → display name, email,
role, company size, relationship, incentive disclosure, private proof reference, genuine-
experience and terms consent); claim profile; advertise; contest entry; careers; donation
pledge; awards nomination; report a review; contact.
Support query-string prefill (?category=, ?business=, ?rating=, ?amount=).
```

## Phase 5: Monetisation and community

```
- Put the AdSense loader in <head> on every page:
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>
  plus <meta name="google-adsense-account" content="ca-pub-6620975821265271">. Use Auto ads.
  Keep ads away from form buttons and never style ads like navigation.
- ads.txt: google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0
- Donations page: tiers ($5/$25/$100/$500), allocation (operations, promotions & marketing,
  hiring talent, contests & prizes), pledge form, optional payment-link buttons configured
  in main.js (DONATE_LINKS: stripe, paypal, kofi). They stay hidden until filled in.
- Contests: Most Helpful Review (judged sentiment-neutrally; entries labelled "Contest entry"),
  Small Business Story, Tool Tips Challenge, plus official rules (no purchase necessary, age of
  majority, skill-testing question where required).
- Careers: moderator, writer, SEO, video, community, partnerships roles + application form.
- For business: Free / Growth / Partner tiers + claim form. Advertise: 6 labelled packages.
- Videos: verified YouTube IDs, lazy-loaded via youtube-nocookie.
- Tools (assets/js/tools.js): vendor weighted scorecard, SaaS TCO calculator, review
  response writer, review request builder, rating goal calculator.
```

## Phase 6: Trust, compliance and legal

```
Write: methodology & editorial policy (independence, moderation steps, labels: Verified,
Invited, Organic, Incentivized, Contest entry; published BR Score formula; quarterly
transparency report commitment; AI use), review guidelines that double as the UGC policy
(reviewer rules, business rules: no gating, no sentiment-conditioned incentives, no
suppression; appeals; report form), privacy policy with the required Google AdSense cookie
disclosure and opt-out links, terms, cookie policy, disclaimer ("how we make money"),
and a trademark & copyright disclosure stating that "business reviews" is a generic,
descriptive phrase with no exclusive rights claimed, plus non-affiliation with any similarly
named company or review platform. Add a cookie notice and recommend enabling Google's
certified CMP (AdSense → Privacy & messaging) for EEA/UK/CH visitors.
```

## Phase 7: SEO, performance and deployment

```
Add unique titles/descriptions, canonical URLs (https://businessreviews.com/...), Open Graph,
JSON-LD (Organization, WebSite+SearchAction, BreadcrumbList, FAQPage, Article), sitemap.xml,
robots.txt, a client-side search index (search-index.json), 404.html, .nojekyll, a web
manifest, an SVG favicon and an OG image. Push to GitHub repo WEBWORKSA1/businessreviews-com
on main, enable GitHub Pages (Deploy from branch → main → / root), then connect the custom
domain businessreviews.com (add a CNAME file plus DNS A/AAAA records or a CNAME to
webworksa1.github.io) and enforce HTTPS.
```

## Phase 8: Growth roadmap (after launch)

1. Activate FormSubmit (the first submission triggers a confirmation email) and swap the address for FormSubmit's random alias string.
2. Apply to AdSense once the custom domain resolves. Enable Auto ads and Google's CMP.
3. Publish 2 guides a week. Target "best [category] for [industry]", "[vendor] alternatives" and "[vendor] vs [vendor]" pages once you have first-hand data.
4. Recruit the first 200 reviews through contests, owner invitations and LinkedIn outreach. Turn on BR Scores at 3+ reviews.
5. Sign the first lead-program partners per category; route the full Get Matched form to a CRM via Zapier or Make.
6. Add provider profile pages only once each has real reviews, so there are no thin pages.
7. Launch a YouTube channel that repurposes the guides, and embed it in the video library.
