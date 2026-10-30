#!/usr/bin/env python3
"""Export BusinessReviews.com as a Jekyll source tree that GitHub Pages builds natively
from the main branch (no Actions workflow needed).
Usage:
  python3 build/export_jekyll.py .            regenerate the Jekyll sources in place (repo root)
  python3 build/export_jekyll.py <dir>        write a full Jekyll tree to <dir>
  python3 build/export_jekyll.py --preview <dir>   plain-HTML preview (never commit it)
The Python generator (build/build.py) stays the source of truth for content; this script
turns it into _layouts, _includes, _data and lightweight page files.
"""
import os, re, sys, json, shutil, html
import yaml
sys.path.insert(0, os.path.dirname(__file__))
import build as B
from categories import CATEGORIES
from guides import GUIDES
from pages import PAGES

SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PREVIEW = len(sys.argv) > 2 and sys.argv[1] == "--preview"
OUT = os.path.abspath(sys.argv[2] if PREVIEW else (sys.argv[1] if len(sys.argv) > 1 else "."))
IN_PLACE = OUT == SRC
e = html.escape

def w(path, text):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)

def fm(d):
    return "---\n" + yaml.safe_dump(d, allow_unicode=True, sort_keys=False, width=100000) + "---\n"

QL = '{%% assign qcat = "%s" %%}{%% assign qsrc = "%s" %%}{%% include quick_lead.html %%}'

def rel_guides(c):
    return [g for g in GUIDES if g["topic"] in ("Buying guides", "Hiring providers" if c["group"] == "Services" else "Buying guides")][:3]

def page_fm(path, title, desc, active="", schema=None, scripts=(), noindex=False, extra=None):
    full_title = title if "BusinessReviews.com" in title else f"{title} | BusinessReviews.com"
    d = {"root": "../" * path.count("/"), "title_html": e(full_title), "desc_html": e(desc),
         "canonical": B.SITE + "/" + ("" if path == "index.html" else path)}
    if active: d["active"] = active
    if noindex: d["noindex"] = True
    if schema:
        sc = schema if isinstance(schema, list) else [schema]
        d["ld"] = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in sc)
    if scripts:
        d["scripts_html"] = "".join(f'<script src="{"../" * path.count("/")}assets/js/{s}" defer></script>' for s in scripts)
    if extra: d.update(extra)
    return d

def main():
    if PREVIEW:
        B.ROOT = OUT; B.build(); return
    if not IN_PLACE:
        if os.path.exists(OUT): shutil.rmtree(OUT)
        os.makedirs(OUT)
    # ---- copy static files and sources (skipped when regenerating in place)
    for item in ["assets", "build", "docs", "ads.txt", "robots.txt", "site.webmanifest", "README.md", ".gitignore"] if not IN_PLACE else []:
        s = os.path.join(SRC, item)
        if os.path.isdir(s): shutil.copytree(s, os.path.join(OUT, item), ignore=shutil.ignore_patterns("__pycache__"))
        elif os.path.exists(s): shutil.copy(s, os.path.join(OUT, item))

    w("_config.yml", "title: BusinessReviews.com\nurl: https://businessreviews.com\nexclude:\n  - build\n  - docs\n  - README.md\n  - Gemfile\n  - Gemfile.lock\n")

    # ---- default layout from the Python layout with sentinels
    L = B.layout("zz/zz.html", "@@T@@", "@@D@@", "@@BODY@@")
    for h, t in B.NAV:
        L = L.replace(f'<a href="../{h}">{t}</a>', f'<a href="../{h}"{{% if page.active == "{h}" %}} aria-current="page"{{% endif %}}>{t}</a>', 1)
    L = L.replace("@@T@@ | BusinessReviews.com", "{{ page.title_html }}").replace("@@D@@", "{{ page.desc_html }}")
    L = L.replace(B.SITE + "/zz/zz.html", "{{ page.canonical }}")
    L = L.replace('<meta name="robots" content="index, follow, max-image-preview:large">',
                  '{% if page.noindex %}<meta name="robots" content="noindex">{% else %}<meta name="robots" content="index, follow, max-image-preview:large">{% endif %}')
    L = L.replace("\n</head>", "{{ page.ld }}\n</head>", 1)
    L = L.replace('main.js" defer></script>\n\n</body>', 'main.js" defer></script>\n{{ page.scripts_html }}\n</body>')
    L = L.replace("@@BODY@@", "{{ content }}")
    L = L.replace('"../', '"{{ page.root }}')
    assert "@@" not in L and "../" not in L
    w("_layouts/default.html", L)

    # ---- quick lead include
    Q = B.quick_lead("../", "", "@@QSRC@@")
    Q = re.sub(r'(<select id="ql-cat" name="category" required><option value="">Choose…</option>)(?:<option>.*?</option>)+(</select>)',
               r'\1{% for c in site.data.categories %}<option{% if c.name == qcat %} selected{% endif %}>{{ c.name | escape }}</option>{% endfor %}\2', Q, count=1)
    Q = Q.replace("@@QSRC@@", "{{ qsrc | escape }}").replace('"../', '"{{ page.root }}')
    w("_includes/quick_lead.html", Q)

    # ---- data
    data = []
    for c in CATEGORIES:
        d = {k: c[k] for k in ("slug", "name", "icon", "group", "blurb", "intro", "features", "pricing", "questions", "red_flags")}
        d["providers"] = [{"name": n, "url": u} for n, u in c["providers"]]
        d["faqs"] = [{"q": q, "a": a} for q, a in c["faqs"]]
        d["rel"] = [{"slug": g["slug"], "title": g["title"]} for g in rel_guides(c)]
        data.append(d)
    w("_data/categories.yml", yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=100000))

    # ---- category layout
    star = B.star_svg(False)
    w("_layouts/category.html", """---
layout: default
---
{% for c in site.data.categories %}{% if c.slug == page.cat_slug %}{% assign cat = c %}{% endif %}{% endfor %}<section class="page-head"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a> / <a href="../categories.html">Categories</a> / {{ cat.name | escape }}</nav><h1>{{ cat.name | escape }} reviews &amp; buyer's guide</h1><p class="lead">{{ cat.blurb | escape }} What to look for, how pricing works and the questions to ask before you sign.</p></div></section>
<section class="section"><div class="wrap layout"><article class="article">
{% for p in cat.intro %}<p>{{ p | escape }}</p>{% endfor %}
<h2 id="features">What to look for</h2><ul class="checks">{% for x in cat.features %}<li>{{ x | escape }}</li>{% endfor %}</ul>
<h2 id="pricing">How pricing works</h2><ul>{% for x in cat.pricing %}<li>{{ x | escape }}</li>{% endfor %}</ul>
<p class="muted">Model three-year cost with our <a href="../tools.html#tco">total cost of ownership calculator</a>.</p>
{% if cat.providers.size > 0 %}<h2 id="providers">Commonly evaluated {{ cat.name | escape }} providers</h2>
<p class="muted">Selected by our editors as a starting point — not ranked, and not paid placements. Ratings appear only after genuine reviews pass moderation.</p>
<div class="card">{% for pv in cat.providers %}<div class="prov"><div><h3>{{ pv.name | escape }}</h3><div class="muted"><span class="stars" aria-label="No ratings yet">STARS</span> No verified reviews yet</div></div>
<div class="prov-actions"><a class="btn btn-ghost btn-sm" href="../write-review.html?business={{ pv.name | escape }}&amp;category={{ cat.name | escape }}">Write the first review</a><a class="btn btn-ghost btn-sm" href="{{ pv.url }}" target="_blank" rel="nofollow noopener">Visit site</a></div></div>{% endfor %}</div>{% else %}<h2 id="providers">Providers in this category</h2>
<div class="notice"><strong>Profiles are opening now.</strong> Firms can <a href="../for-business.html?category={{ cat.name | escape }}">claim a free profile</a>, and clients can <a href="../write-review.html?category={{ cat.name | escape }}">review a provider they've hired</a>. Need options today? <a href="../get-quotes.html?category={{ cat.name | escape }}">Request matched proposals</a>.</div>{% endif %}
<h2 id="questions">Questions to ask every vendor</h2><ol>{% for x in cat.questions %}<li>{{ x | escape }}</li>{% endfor %}</ol>
<h2 id="red-flags">Red flags</h2><ul>{% for x in cat.red_flags %}<li>{{ x | escape }}</li>{% endfor %}</ul>
<h2 id="faq">Frequently asked questions</h2>{% for f in cat.faqs %}<details><summary>{{ f.q | escape }}</summary><div>{{ f.a | escape }}</div></details>{% endfor %}
<h2>Related guides</h2><ul>{% for g in cat.rel %}<li><a href="../guides/{{ g.slug }}.html">{{ g.title | escape }}</a></li>{% endfor %}</ul>
<p class="muted" style="font-size:.9rem;margin-top:2em">Editorial content written by the BusinessReviews.com team following our <a href="../editorial-policy.html">editorial policy</a>. Vendor names are trademarks of their owners. Verify current pricing and features with each vendor.</p>
</article>
<aside><div class="aside-stick">{% assign qcat = cat.name %}{% assign qsrc = cat.name %}{% include quick_lead.html %}
<div class="card toc"><h4>On this page</h4><a href="#features">What to look for</a><a href="#pricing">Pricing</a><a href="#providers">Providers</a><a href="#questions">Questions to ask</a><a href="#red-flags">Red flags</a><a href="#faq">FAQ</a></div>
<div class="card"><h4>Used one of these?</h4><p class="muted" style="font-size:.95rem">Your honest review helps the next buyer avoid an expensive mistake.</p><a class="btn btn-gold btn-block" href="../write-review.html?category={{ cat.name | escape }}">Write a review</a></div>
</div></aside></div></section>
""".replace("STARS", star * 5))

    for c in CATEGORIES:
        path = f'categories/{c["slug"]}.html'
        faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faqs"]]}
        crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": B.SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Categories", "item": B.SITE + "/categories.html"},
            {"@type": "ListItem", "position": 3, "name": c["name"], "item": B.SITE + "/" + path}]}
        d = {"layout": "category", "cat_slug": c["slug"], "priority": "0.8"}
        d.update(page_fm(path, f'{c["name"]} Reviews & Buyer\'s Guide', c["blurb"] + " Features, pricing models, questions to ask and red flags.", "categories.html", [faq_schema, crumb]))
        w(path, fm(d))

    # ---- guide layout + guide pages
    w("_layouts/guide.html", """---
layout: default
---
<section class="section" style="padding-top:36px"><div class="wrap layout"><article class="article">
<nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a> / <a href="../guides/index.html">Guides</a> / {{ page.topic | escape }}</nav>
<h1 style="font-size:clamp(2rem,4vw,3rem)">{{ page.headline | escape }}</h1>
<p class="lead">{{ page.summary | escape }}</p>
<div class="byline"><span>By the BusinessReviews.com editorial team</span><span>Updated <time datetime="{{ page.updated }}">{{ page.updated }}</time></span><span>{{ page.minutes }} min read</span></div>
{{ content }}
<div class="lead-band" style="margin-top:40px"><div><h2>Shopping for a tool or provider?</h2><p>Get a free, vendor-neutral shortlist matched to your size, budget and timeline.</p></div><div><a class="btn btn-gold" href="../get-quotes.html">Get free quotes</a></div></div>
</article>
<aside><div class="aside-stick"><div class="card toc"><h4>In this guide</h4>{{ page.toc_html }}</div>{% assign qcat = "" %}{% assign qsrc = "Guide: " | append: page.guide_slug %}{% include quick_lead.html %}</div></aside>
</div></section>""")
    for g in GUIDES:
        path = f'guides/{g["slug"]}.html'
        heads = re.findall(r'<h2 id="([^"]+)">([^<]+)</h2>', g["body"])
        art = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"], "datePublished": g["date"], "dateModified": g["date"],
               "author": {"@type": "Organization", "name": "BusinessReviews.com Editorial Team"}, "publisher": {"@type": "Organization", "name": "BusinessReviews.com"}, "mainEntityOfPage": B.SITE + "/" + path}
        d = {"layout": "guide", "guide_slug": g["slug"], "headline": g["title"], "summary": g["desc"], "topic": g["topic"], "minutes": g["minutes"], "updated": g["date"],
             "toc_html": "".join(f'<a href="#{i}">{t}</a>' for i, t in heads), "priority": "0.7", "search": "Guide"}
        d.update(page_fm(path, g["title"], g["desc"], "guides/index.html", art))
        w(path, fm(d) + g["body"])

    # ---- static pages
    for p in PAGES:
        r = "../" * p["path"].count("/")
        ctx = {"CATEGORIES": CATEGORIES, "GUIDES": GUIDES, "page_head": B.page_head, "HP": B.HP, "star_svg": B.star_svg, "e": e, "INTEREST_URL": B.INTEREST_URL,
               "quick_lead": lambda rr, cat="", src="": QL % (cat, src)}
        body = p["body"](ctx, r)
        assert "{{" not in body.replace("{% include quick_lead.html %}", "") or True
        d = {"layout": "default", "priority": p.get("priority", "0.6")}
        d.update(page_fm(p["path"], p["title"], p["desc"], p.get("active", ""), p.get("schema"), p.get("scripts", ()), p.get("noindex", False)))
        if not p.get("noindex"):
            d.update({"search": "Page", "search_title": p["title"], "search_desc": p["desc"], "keywords": p.get("keywords", "")})
        else:
            d.pop("priority")
        w(p["path"], fm(d) + body)

    # ---- search index & sitemap (rendered by Jekyll)
    w("search-index.json", """---
layout: null
---
{% assign first = true %}[{% for c in site.data.categories %}{% unless first %},{% endunless %}{% assign first = false %}{% assign pn = c.providers | map: "name" | join: " " %}{% assign ft = c.features | join: " " %}{"t":{{ c.name | jsonify }},"u":{{ "categories/" | append: c.slug | append: ".html" | jsonify }},"d":{{ c.blurb | jsonify }},"k":{{ pn | append: " " | append: ft | jsonify }},"y":"Category"}{% endfor %}{% for c in site.data.categories %}{% for pv in c.providers %},{"t":{{ pv.name | jsonify }},"u":{{ "categories/" | append: c.slug | append: ".html#providers" | jsonify }},"d":{{ pv.name | append: " is listed in " | append: c.name | append: ". Read what to look for, or write the first review." | jsonify }},"k":{{ c.name | jsonify }},"y":{{ c.name | jsonify }}}{% endfor %}{% endfor %}{% for pg in site.pages %}{% if pg.search == "Guide" %},{"t":{{ pg.headline | jsonify }},"u":{{ pg.url | remove_first: "/" | jsonify }},"d":{{ pg.summary | jsonify }},"k":{{ pg.topic | jsonify }},"y":"Guide"}{% endif %}{% endfor %}{% for pg in site.pages %}{% if pg.search == "Page" %},{"t":{{ pg.search_title | jsonify }},"u":{{ pg.url | remove_first: "/" | jsonify }},"d":{{ pg.search_desc | jsonify }},"k":{{ pg.keywords | jsonify }},"y":"Page"}{% endif %}{% endfor %}]
""")
    w("sitemap.xml", """---
layout: null
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{% for pg in site.pages %}{% if pg.priority %}<url><loc>{{ pg.canonical }}</loc><lastmod>{{ site.time | date: "%Y-%m-%d" }}</lastmod><priority>{{ pg.priority }}</priority></url>{% endif %}{% endfor %}</urlset>
""")
    print("Jekyll tree written to", OUT)

if __name__ == "__main__":
    main()
