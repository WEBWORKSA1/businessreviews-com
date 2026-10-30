#!/usr/bin/env python3
"""Static site generator for BusinessReviews.com.
Run from repo root:  python3 build/build.py
Outputs HTML into the repo root so GitHub Pages (main branch, / root) serves it directly.
"""
import json, os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from categories import CATEGORIES
from guides import GUIDES
from pages import PAGES

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = "https://businessreviews.com"
ADSENSE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'
INTEREST_URL = "https://web.works/contact"
e = html.escape

LOGO = '''<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="2" y="4" width="36" height="28" rx="9" fill="#12213A"/><path d="M12 32l-2 6 8-6z" fill="#12213A"/><path d="M20 9.5l2.6 5.4 5.9.7-4.4 4.1 1.2 5.8L20 22.6l-5.3 2.9 1.2-5.8-4.4-4.1 5.9-.7z" fill="#F4A300"/></svg>'''

NAV = [("categories.html", "Categories"), ("guides/index.html", "Guides"), ("tools.html", "Tools"),
       ("for-business.html", "For business"), ("contests.html", "Contests"), ("donate.html", "Support us")]

def star_svg(on=True):
    return f'<svg class="star{" on" if on else ""}" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3l-5.9 3.3 1.3-6.6L2.5 9.4l6.6-.8z"/></svg>'

def layout(path, title, desc, body, active="", schema=None, scripts=(), noindex=False):
    depth = path.count("/")
    r = "../" * depth
    canonical = SITE + "/" + ("" if path == "index.html" else path)
    full_title = title if "BusinessReviews.com" in title else f"{title} | BusinessReviews.com"
    nav = "".join(f'<a href="{r}{h}"{" aria-current=\"page\"" if active == h else ""}>{t}</a>' for h, t in NAV)
    nav += f'<a href="{r}videos.html" class="mob-only" style="color:inherit;font-weight:550">Videos</a><a href="{r}write-review.html" class="mob-only">Write a review</a><a href="{r}get-quotes.html" class="mob-only">Get free quotes</a>'
    ld = [{"@context": "https://schema.org", "@type": "Organization", "name": "BusinessReviews.com", "url": SITE, "logo": SITE + "/assets/img/favicon.svg"},
          {"@context": "https://schema.org", "@type": "WebSite", "name": "BusinessReviews.com", "url": SITE,
           "potentialAction": {"@type": "SearchAction", "target": SITE + "/search.html?q={search_term_string}", "query-input": "required name=search_term_string"}}]
    if schema: ld += schema if isinstance(schema, list) else [schema]
    ldjs = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    extra = "".join(f'<script src="{r}assets/js/{s}" defer></script>' for s in scripts)
    cats_opts = "".join(f'<option>{e(c["name"])}</option>' for c in CATEGORIES)
    return f'''<!DOCTYPE html>
<html lang="en" data-root="{r}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
{'<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website"><meta property="og:site_name" content="BusinessReviews.com">
<meta property="og:title" content="{e(full_title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#12213A">
<meta name="google-adsense-account" content="ca-pub-6620975821265271">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,650;12..96,750&family=Public+Sans:ital,wght@0,400;0,550;0,600;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
{ADSENSE}
{ldjs}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><a href="{INTEREST_URL}" target="_blank" rel="noopener">Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership</a></div>
<header class="site-head"><div class="wrap head-in">
<a class="brand" href="{r}index.html" aria-label="BusinessReviews.com home">{LOGO}<span>BusinessReviews<span class="tld">.com</span></span></a>
<nav class="nav" id="nav" aria-label="Main">{nav}</nav>
<div class="head-actions">
<a class="icon-btn" href="{r}search.html" aria-label="Search"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg></a>
<button class="icon-btn" type="button" data-theme-toggle aria-label="Toggle dark mode"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/></svg></button>
<a class="btn btn-ghost btn-sm" href="{r}write-review.html">Write a review</a>
<a class="btn btn-primary btn-sm" href="{r}get-quotes.html">Get free quotes</a>
<button class="icon-btn menu-btn" id="menuBtn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div></div></header>
<div class="scrim" id="scrim"></div>
<main id="main">
{body}
</main>
<footer class="site-foot"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="{r}index.html" style="color:#fff">{LOGO}<span>BusinessReviews<span class="tld" style="color:#93A0B8">.com</span></span></a>
<p style="margin-top:14px;max-width:34ch">Independent reviews, buyer's guides and free tools for choosing business software and service providers.</p>
<form data-form="Newsletter signup" data-ok="You're subscribed. Look out for our next buyer's brief." class="news" aria-label="Newsletter">
<label class="sr" for="nl-email">Email address</label><input id="nl-email" type="email" name="email" placeholder="Your work email" required>
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<button class="btn btn-gold btn-sm" type="submit">Subscribe</button></form>
<p class="hint" style="color:#93A0B8">Monthly buyer's brief. Unsubscribe any time.</p></div>
<div><h4>Explore</h4><ul><li><a href="{r}categories.html">All categories</a></li><li><a href="{r}guides/index.html">Buyer's guides</a></li><li><a href="{r}tools.html">Free tools</a></li><li><a href="{r}videos.html">Videos</a></li><li><a href="{r}awards.html">Community Choice Awards</a></li><li><a href="{r}search.html">Search</a></li></ul></div>
<div><h4>For businesses</h4><ul><li><a href="{r}for-business.html">Claim your profile</a></li><li><a href="{r}get-quotes.html">Get free quotes</a></li><li><a href="{r}advertise.html">Advertise &amp; sponsor</a></li><li><a href="{r}review-guidelines.html">Review guidelines</a></li><li><a href="{INTEREST_URL}" target="_blank" rel="noopener">Partnerships</a></li></ul></div>
<div><h4>Community</h4><ul><li><a href="{r}write-review.html">Write a review</a></li><li><a href="{r}contests.html">Contests &amp; prizes</a></li><li><a href="{r}careers.html">Careers</a></li><li><a href="{r}donate.html">Support us</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="{r}about.html">About</a></li><li><a href="{r}editorial-policy.html">Methodology &amp; editorial policy</a></li><li><a href="{r}contact.html">Contact</a></li><li><a href="{r}privacy.html">Privacy policy</a></li><li><a href="{r}terms.html">Terms of use</a></li><li><a href="{r}cookies.html">Cookie policy</a></li><li><a href="{r}disclaimer.html">Disclaimer &amp; disclosures</a></li><li><a href="{r}trademark-copyright.html">Trademark &amp; copyright</a></li></ul></div>
</div>
<div class="foot-legal">
<p>© <span data-year>2026</span> BusinessReviews.com. Original content on this site is protected by copyright. "Business reviews" is used as a generic, descriptive phrase; no exclusive trademark rights are claimed in it, and this site is not affiliated with any other company or service using similar words. Third-party names and marks belong to their owners and are used for identification only. <a href="{r}trademark-copyright.html">Full disclosure</a>.</p>
<p>Reviews reflect the opinions of individual reviewers, not BusinessReviews.com. This site displays advertising served by Google AdSense. <a href="{r}disclaimer.html">How we make money</a>.</p>
</div>
</div></footer>
<a class="btn btn-gold sticky-cta" id="stickyCta" href="{r}get-quotes.html">Get matched free</a>
<div class="modal" id="leadModal" role="dialog" aria-modal="true" aria-labelledby="lmTitle"><div class="form-card">
<button class="icon-btn x" type="button" data-close aria-label="Close">✕</button>
<h3 id="lmTitle">Before you go: get a free shortlist</h3>
<p class="muted">Tell us what you're shopping for and we'll email you a vendor-neutral shortlist with questions to ask.</p>
<form data-form="Lead: Exit shortlist" data-ok="Done — your shortlist request is in. Check your inbox within 2 business days.">
<div class="field"><label for="lm-cat">Category</label><select id="lm-cat" name="category" required><option value="">Choose…</option>{cats_opts}</select></div>
<div class="field"><label for="lm-email">Work email</label><input id="lm-email" type="email" name="email" required autocomplete="email"></div>
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my request. <a href="{r}privacy.html">Privacy</a></label>
<button class="btn btn-primary btn-block" type="submit" style="margin-top:14px">Send my shortlist</button></form>
</div></div>
<div class="cookie" id="cookie" role="region" aria-label="Cookie notice">
<p>We use cookies for essential site functions and, with Google AdSense, to show and measure ads. Read our <a href="{r}cookies.html">cookie policy</a>.</p>
<div class="btns"><button class="btn btn-primary btn-sm" data-consent="all">Accept all</button><button class="btn btn-ghost btn-sm" data-consent="essential">Essential only</button></div></div>
<script src="{r}assets/js/main.js" defer></script>
{extra}
</body>
</html>
'''

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def page_head(title, lead, crumbs=None, r=""):
    c = ""
    if crumbs:
        c = '<nav class="crumbs" aria-label="Breadcrumb"><a href="' + r + 'index.html">Home</a> / ' + " / ".join(
            (f'<a href="{r}{h}">{e(t)}</a>' if h else e(t)) for h, t in crumbs) + "</nav>"
    return f'<section class="page-head"><div class="wrap">{c}<h1>{title}</h1><p class="lead">{lead}</p></div></section>'

HP = '<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'

def quick_lead(r, cat_name="", src="Category page"):
    opts = "".join(f'<option{" selected" if c["name"] == cat_name else ""}>{e(c["name"])}</option>' for c in CATEGORIES)
    return f'''<div class="form-card"><h3>Get matched for free</h3><p class="muted" style="font-size:.95rem">Answer three questions and get a vendor-neutral shortlist, typically within 2 business days.</p>
<form data-form="Lead: Quick match ({e(src)})" data-ok="Request received. A shortlist is on its way within 2 business days.">
<div class="field"><label for="ql-cat">What do you need?</label><select id="ql-cat" name="category" required><option value="">Choose…</option>{opts}</select></div>
<div class="field"><label for="ql-size">Company size</label><select id="ql-size" name="company_size" required><option value="">Choose…</option><option>Just me</option><option>2–10</option><option>11–50</option><option>51–200</option><option>201–1,000</option><option>1,000+</option></select></div>
<div class="field"><label for="ql-email">Work email</label><input id="ql-email" type="email" name="email" required autocomplete="email"></div>
{HP}<label class="check"><input type="checkbox" name="consent" value="yes" required> Contact me about this request.</label>
<button class="btn btn-primary btn-block" style="margin-top:12px" type="submit">Get my shortlist</button>
<p class="hint">Free for buyers. No obligation. <a href="{r}privacy.html">Privacy</a></p></form></div>'''

def build():
    pages_out = []
    # Category pages
    for c in CATEGORIES:
        path = f'categories/{c["slug"]}.html'; r = "../"
        prov = ""
        if c["providers"]:
            rows = "".join(f'''<div class="prov"><div><h3>{e(n)}</h3><div class="muted"><span class="stars" aria-label="No ratings yet">{"".join(star_svg(False) for _ in range(5))}</span> No verified reviews yet</div></div>
<div class="prov-actions"><a class="btn btn-ghost btn-sm" href="{r}write-review.html?business={e(n)}&amp;category={e(c["name"])}">Write the first review</a><a class="btn btn-ghost btn-sm" href="{u}" target="_blank" rel="nofollow noopener">Visit site</a></div></div>''' for n, u in c["providers"])
            prov = f'''<h2 id="providers">Commonly evaluated {e(c["name"])} providers</h2>
<p class="muted">Selected by our editors as a starting point — not ranked, and not paid placements. Ratings appear only after genuine reviews pass moderation.</p>
<div class="card">{rows}</div>'''
        else:
            prov = f'''<h2 id="providers">Providers in this category</h2>
<div class="notice"><strong>Profiles are opening now.</strong> Firms can <a href="{r}for-business.html?category={e(c["name"])}">claim a free profile</a>, and clients can <a href="{r}write-review.html?category={e(c["name"])}">review a provider they've hired</a>. Need options today? <a href="{r}get-quotes.html?category={e(c["name"])}">Request matched proposals</a>.</div>'''
        faq_html = "".join(f"<details><summary>{e(q)}</summary><div>{e(a)}</div></details>" for q, a in c["faqs"])
        rel = [g for g in GUIDES if g["topic"] in ("Buying guides", "Hiring providers" if c["group"] == "Services" else "Buying guides")][:3]
        rel_html = "".join(f'<li><a href="{r}guides/{g["slug"]}.html">{e(g["title"])}</a></li>' for g in rel)
        body = page_head(e(c["name"]) + " reviews &amp; buyer's guide", e(c["blurb"]) + " What to look for, how pricing works and the questions to ask before you sign.", [("categories.html", "Categories"), ("", c["name"])], r) + f'''
<section class="section"><div class="wrap layout"><article class="article">
{"".join(f"<p>{e(p)}</p>" for p in c["intro"])}
<h2 id="features">What to look for</h2><ul class="checks">{"".join(f"<li>{e(x)}</li>" for x in c["features"])}</ul>
<h2 id="pricing">How pricing works</h2><ul>{"".join(f"<li>{e(x)}</li>" for x in c["pricing"])}</ul>
<p class="muted">Model three-year cost with our <a href="{r}tools.html#tco">total cost of ownership calculator</a>.</p>
{prov}
<h2 id="questions">Questions to ask every vendor</h2><ol>{"".join(f"<li>{e(x)}</li>" for x in c["questions"])}</ol>
<h2 id="red-flags">Red flags</h2><ul>{"".join(f"<li>{e(x)}</li>" for x in c["red_flags"])}</ul>
<h2 id="faq">Frequently asked questions</h2>{faq_html}
<h2>Related guides</h2><ul>{rel_html}</ul>
<p class="muted" style="font-size:.9rem;margin-top:2em">Editorial content written by the BusinessReviews.com team following our <a href="{r}editorial-policy.html">editorial policy</a>. Vendor names are trademarks of their owners. Verify current pricing and features with each vendor.</p>
</article>
<aside><div class="aside-stick">{quick_lead(r, c["name"], c["name"])}
<div class="card toc"><h4>On this page</h4><a href="#features">What to look for</a><a href="#pricing">Pricing</a><a href="#providers">Providers</a><a href="#questions">Questions to ask</a><a href="#red-flags">Red flags</a><a href="#faq">FAQ</a></div>
<div class="card"><h4>Used one of these?</h4><p class="muted" style="font-size:.95rem">Your honest review helps the next buyer avoid an expensive mistake.</p><a class="btn btn-gold btn-block" href="{r}write-review.html?category={e(c["name"])}">Write a review</a></div>
</div></aside></div></section>'''
        faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faqs"]]}
        crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Categories", "item": SITE + "/categories.html"},
            {"@type": "ListItem", "position": 3, "name": c["name"], "item": SITE + "/" + path}]}
        write(path, layout(path, f'{c["name"]} Reviews & Buyer\'s Guide', c["blurb"] + " Features, pricing models, questions to ask and red flags.", body, "categories.html", [faq_schema, crumb]))
        pages_out.append((path, "0.8"))

    # Guides
    for g in GUIDES:
        path = f'guides/{g["slug"]}.html'; r = "../"
        import re
        heads = re.findall(r'<h2 id="([^"]+)">([^<]+)</h2>', g["body"])
        toc = "".join(f'<a href="#{i}">{t}</a>' for i, t in heads)
        body = f'''<section class="section" style="padding-top:36px"><div class="wrap layout"><article class="article">
<nav class="crumbs" aria-label="Breadcrumb"><a href="{r}index.html">Home</a> / <a href="{r}guides/index.html">Guides</a> / {e(g["topic"])}</nav>
<h1 style="font-size:clamp(2rem,4vw,3rem)">{e(g["title"])}</h1>
<p class="lead">{e(g["desc"])}</p>
<div class="byline"><span>By the BusinessReviews.com editorial team</span><span>Updated <time datetime="{g["date"]}">{g["date"]}</time></span><span>{g["minutes"]} min read</span></div>
{g["body"]}
<div class="lead-band" style="margin-top:40px"><div><h2>Shopping for a tool or provider?</h2><p>Get a free, vendor-neutral shortlist matched to your size, budget and timeline.</p></div><div><a class="btn btn-gold" href="{r}get-quotes.html">Get free quotes</a></div></div>
</article>
<aside><div class="aside-stick"><div class="card toc"><h4>In this guide</h4>{toc}</div>{quick_lead(r, "", "Guide: " + g["slug"])}</div></aside>
</div></section>'''
        art = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"], "datePublished": g["date"], "dateModified": g["date"],
               "author": {"@type": "Organization", "name": "BusinessReviews.com Editorial Team"}, "publisher": {"@type": "Organization", "name": "BusinessReviews.com"}, "mainEntityOfPage": SITE + "/" + path}
        write(path, layout(path, g["title"], g["desc"], body, "guides/index.html", art))
        pages_out.append((path, "0.7"))

    # Static pages from pages.py
    ctx = {"CATEGORIES": CATEGORIES, "GUIDES": GUIDES, "page_head": page_head, "quick_lead": quick_lead, "HP": HP, "star_svg": star_svg, "e": e, "INTEREST_URL": INTEREST_URL}
    for p in PAGES:
        body = p["body"](ctx, "../" * p["path"].count("/"))
        write(p["path"], layout(p["path"], p["title"], p["desc"], body, p.get("active", ""), p.get("schema"), p.get("scripts", ()), p.get("noindex", False)))
        if not p.get("noindex"): pages_out.append((p["path"], p.get("priority", "0.6")))

    # Search index
    idx = [{"t": c["name"], "u": f'categories/{c["slug"]}.html', "d": c["blurb"], "k": " ".join(n for n, _ in c["providers"]) + " " + " ".join(c["features"]), "y": "Category"} for c in CATEGORIES]
    for c in CATEGORIES:
        for n, _ in c["providers"]:
            idx.append({"t": n, "u": f'categories/{c["slug"]}.html#providers', "d": f'{n} is listed in {c["name"]}. Read what to look for, or write the first review.', "k": c["name"], "y": c["name"]})
    idx += [{"t": g["title"], "u": f'guides/{g["slug"]}.html', "d": g["desc"], "k": g["topic"], "y": "Guide"} for g in GUIDES]
    idx += [{"t": p["title"], "u": p["path"], "d": p["desc"], "k": p.get("keywords", ""), "y": "Page"} for p in PAGES if not p.get("noindex")]
    write("search-index.json", json.dumps(idx, ensure_ascii=False))

    # Sitemap
    from datetime import date
    today = date.today().isoformat()
    urls = "".join(f'<url><loc>{SITE}/{"" if pth == "index.html" else pth}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>' for pth, pr in sorted(pages_out, key=lambda x: (x[0] != "index.html", x[0])))
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    print(f"Built {len(pages_out)} indexable pages + search index + sitemap")

if __name__ == "__main__":
    build()
