# Static pages. Each entry: path, title, desc, body(ctx, r) -> html. Add entries to create pages.

VIDEOS = [
 ("SlhESAKF1Tk", "What is CRM and how does it work?", "Salesforce", "Software basics"),
 ("SAy2tlmqT94", "How to simplify your enterprise software selection process", "Technology Evaluation Centers", "Buying software"),
 ("1JpCL2EK5lE", "A beginner's course for generating and managing reviews", "BrightLocal", "Reputation"),
 ("5y4rK_UyIx8", "How to deal with negative reviews", "Marie Forleo", "Reputation"),
 ("POBr_I4jcCs", "Responding to negative reviews, step by step", "Simple Marketing Academy", "Reputation"),
 ("wbyfhGHX0Vg", "Inside the world of fake reviews", "CBC News", "Review literacy"),
 ("kt4oZC_Q4_Q", "Cracking down on fake 5-star reviews", "Global News", "Review literacy"),
 ("Umb8GG4bkd4", "How to manage your Google Business Profile with Gemini", "Google Business Profile", "Local marketing"),
 ("ryF5BnszqJ4", "How to market your small business", "HubSpot Marketing", "Marketing"),
]

def vid(v):
    i, t, ch, _ = v
    return f'<div><div class="vid" data-yt="{i}" aria-label="Play: {t}"></div><div class="vid-title">{t}</div><div class="muted" style="font-size:.9rem">{ch}</div></div>'

def cat_options(ctx, name="category", req=True):
    return f'<select id="f-{name}" name="{name}"{" required" if req else ""}><option value="">Choose…</option>' + "".join(f'<option>{ctx["e"](c["name"])}</option>' for c in ctx["CATEGORIES"]) + '<option>Other</option></select>'

# ---------------- Home ----------------
def home(ctx, r):
    e = ctx["e"]
    cats = "".join(f'<a class="card cat-card" href="{r}categories/{c["slug"]}.html"><span class="cat-ico" aria-hidden="true">{c["icon"]}</span><span><strong>{e(c["name"])}</strong><small>{e(c["blurb"])}</small></span></a>' for c in ctx["CATEGORIES"])
    chips = "".join(f'<a class="chip" href="{r}categories/{c["slug"]}.html">{e(c["name"])}</a>' for c in ctx["CATEGORIES"][:6])
    guides = "".join(f'<a class="card" href="{r}guides/{g["slug"]}.html"><span class="tag blue">{e(g["topic"])}</span><h3 style="margin-top:12px">{e(g["title"])}</h3><p class="muted">{e(g["desc"])}</p></a>' for g in ctx["GUIDES"][:6])
    return f'''
<section class="hero"><div class="wrap hero-grid">
<div>
<h1>Check a business before you trust it with your money.</h1>
<p class="lead">Honest reviews from real customers, plain-English buyer's guides and free tools for choosing software and service providers.</p>
<form class="search" action="{r}search.html" role="search"><label class="sr" for="hq">Search businesses, software or topics</label>
<input id="hq" name="q" type="search" placeholder="Search a business, tool or category" autocomplete="off"><button class="btn btn-primary" type="submit">Search</button></form>
<div class="chips" aria-label="Popular categories">{chips}<a class="chip" href="{r}categories.html">All categories</a></div>
</div>
<div class="rate-panel">
<h2>Worked with a business lately?</h2>
<p class="muted">Tap a star to start your review. It takes about three minutes and helps the next buyer decide.</p>
<div class="big-stars" id="heroStars" data-rate="heroRating" role="group" aria-label="Rate your experience"></div>
<div class="star-caption" aria-live="polite"></div>
<a class="btn btn-gold btn-block" id="heroGo" data-base="{r}write-review.html" href="{r}write-review.html" style="margin-top:14px">Write your review</a>
</div>
</div></section>

<section class="section tint"><div class="wrap grid g2">
<div class="card" style="padding:30px"><span class="tag gold">Free for buyers</span><h2 style="margin-top:14px">Get matched</h2><p>Tell us what you need in four short steps. We send a vendor-neutral shortlist and, only if you agree, introductions to up to three providers.</p><a class="btn btn-primary" href="{r}get-quotes.html">Get free quotes</a></div>
<div class="card" style="padding:30px"><span class="tag">Do it yourself</span><h2 style="margin-top:14px">Browse and compare</h2><p>Read category buyer's guides, check questions to ask every vendor, and score your shortlist with our weighted comparison tool.</p><a class="btn btn-ghost" href="{r}categories.html">Browse categories</a> <a class="btn btn-ghost" href="{r}tools.html#scorecard">Compare vendors</a></div>
</div></section>

<section class="section"><div class="wrap">
<div class="sec-head"><h2>Browse by category</h2><p>Software, finance and professional services that businesses buy most often.</p></div>
<div class="grid g3">{cats}</div>
</div></section>

<section class="section ink"><div class="wrap">
<div class="sec-head"><h2>How a review gets published here</h2><p style="color:#B9C3D4">Every review is checked by a person before it appears. Businesses can't pay to hide or reorder reviews.</p></div>
<ol class="steps">
<li><h3>Submitted</h3><p style="color:#B9C3D4">A reviewer shares a first-hand experience and discloses any relationship or incentive.</p></li>
<li><h3>Screened</h3><p style="color:#B9C3D4">We check for duplicates, conflicts of interest and policy breaches, and may ask for proof of use.</p></li>
<li><h3>Labelled</h3><p style="color:#B9C3D4">Reviews carry clear labels such as Verified, Invited or Incentivized, so you can weigh them.</p></li>
<li><h3>Published</h3><p style="color:#B9C3D4">The business can reply publicly. Anyone can report a review that breaks the rules.</p></li>
</ol>
<p style="margin-top:28px"><a href="{r}review-guidelines.html" style="color:#FFD36B">Read the review guidelines</a> · <a href="{r}editorial-policy.html" style="color:#FFD36B">See our methodology</a></p>
</div></section>

<section class="section"><div class="wrap"><div class="lead-band">
<div><h2>Stop comparing 40 vendors. Compare the right 3.</h2>
<ul class="checks"><li>Shortlist matched to your team size, budget and timeline</li><li>Questions to ask and red flags for each category</li><li>You choose who contacts you — or nobody at all</li></ul>
<a class="btn btn-gold" href="{r}get-quotes.html">Start the 4-step match</a></div>
<div>{ctx["quick_lead"](r, "", "Home")}</div>
</div></div></section>

<section class="section tint"><div class="wrap">
<div class="sec-head"><h2>Buyer's guides</h2><a class="btn btn-ghost btn-sm" href="{r}guides/index.html">All guides</a></div>
<div class="grid g3">{guides}</div>
</div></section>

<section class="section"><div class="wrap">
<div class="sec-head"><h2>Free tools for buyers and owners</h2><p>No sign-up. Everything runs in your browser.</p></div>
<div class="grid g3">
<a class="card" href="{r}tools.html#scorecard"><h3>Vendor scorecard</h3><p class="muted">Weight your criteria and score up to four vendors side by side.</p></a>
<a class="card" href="{r}tools.html#tco"><h3>Total cost calculator</h3><p class="muted">See the three-year cost of a SaaS tool, not just the sticker price.</p></a>
<a class="card" href="{r}tools.html#response"><h3>Review response writer</h3><p class="muted">Draft a calm, professional reply to any review in seconds.</p></a>
<a class="card" href="{r}tools.html#request"><h3>Review request builder</h3><p class="muted">Policy-compliant email and SMS templates for asking customers.</p></a>
<a class="card" href="{r}tools.html#goal"><h3>Rating goal calculator</h3><p class="muted">How many new reviews it takes to move your average.</p></a>
<a class="card" href="{r}videos.html"><h3>Video library</h3><p class="muted">Short explainers on buying software and managing your reputation.</p></a>
</div></div></section>

<section class="section tint"><div class="wrap">
<div class="sec-head"><h2>Watch and learn</h2><a class="btn btn-ghost btn-sm" href="{r}videos.html">All videos</a></div>
<div class="grid g3">{"".join(vid(v) for v in [VIDEOS[0], VIDEOS[2], VIDEOS[5]])}</div>
</div></section>

<section class="section"><div class="wrap split">
<div><h2>Own a business? Your profile is free.</h2><p class="lead">Claim your listing, reply to reviews, invite customers and show a review badge on your website.</p>
<ul class="checks"><li>Free profile with your logo, description and contact details</li><li>Public replies to every review</li><li>Review invitation links and website widgets</li><li>Optional lead program for matched buyer requests</li></ul>
<a class="btn btn-primary" href="{r}for-business.html">Claim your free profile</a> <a class="btn btn-ghost" href="{r}advertise.html">Advertise with us</a></div>
<div class="grid g2">
<a class="card" href="{r}contests.html"><span class="tag gold">Win prizes</span><h3 style="margin-top:10px">Contests</h3><p class="muted">Monthly awards for the most helpful reviews and small-business stories.</p></a>
<a class="card" href="{r}careers.html"><span class="tag blue">We're hiring</span><h3 style="margin-top:10px">Careers</h3><p class="muted">Moderators, writers, video creators and partnership roles.</p></a>
<a class="card" href="{r}donate.html"><span class="tag">Reader-supported</span><h3 style="margin-top:10px">Support us</h3><p class="muted">Help fund moderation, prizes and independent guides.</p></a>
<a class="card" href="{r}awards.html"><span class="tag gold">2027</span><h3 style="margin-top:10px">Community Choice</h3><p class="muted">Awards decided by verified reviews only. Nominations open.</p></a>
</div></div></section>'''

# ---------------- Categories ----------------
def categories(ctx, r):
    e = ctx["e"]; out = ""
    for grp in ("Software", "Finance", "Services"):
        items = "".join(f'<a class="card cat-card" data-cat="{e((c["name"]+" "+c["blurb"]+" "+" ".join(n for n,_ in c["providers"])).lower())}" href="{r}categories/{c["slug"]}.html"><span class="cat-ico" aria-hidden="true">{c["icon"]}</span><span><strong>{e(c["name"])}</strong><small>{e(c["blurb"])}</small></span></a>' for c in ctx["CATEGORIES"] if c["group"] == grp)
        out += f'<h2 style="margin-top:1.4em">{grp}</h2><div class="grid g3">{items}</div>'
    return ctx["page_head"]("All categories", "Choose a category for a buyer's guide, pricing models, questions to ask and the providers people evaluate most.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap">
<div class="field" style="max-width:440px"><label for="catFilter">Filter categories</label><input id="catFilter" type="search" placeholder="Try “payroll” or “Shopify”"></div>
{out}
<div class="notice" style="margin-top:36px">Don't see your category? <a href="{r}contact.html?topic=Suggest%20a%20category">Suggest one</a> — new categories are added every month.</div>
</div></section>'''

# ---------------- Guides index ----------------
def guides_index(ctx, r):
    e = ctx["e"]
    cards = "".join(f'<a class="card" href="{r}guides/{g["slug"]}.html"><span class="tag blue">{e(g["topic"])}</span><h3 style="margin-top:12px">{e(g["title"])}</h3><p class="muted">{e(g["desc"])}</p><p class="muted" style="font-size:.88rem">{g["minutes"]} min read</p></a>' for g in ctx["GUIDES"])
    return ctx["page_head"]("Buyer's guides", "Vendor-neutral guides for choosing software and providers, reading reviews critically and managing your reputation.", None, r) + f'<section class="section" style="padding-top:36px"><div class="wrap"><div class="grid g3">{cards}</div></div></section>'

# ---------------- Get quotes (lead generation) ----------------
def get_quotes(ctx, r):
    e = ctx["e"]
    opts = "".join(f'<label class="opt"><input type="radio" name="category" value="{e(c["name"])}" required><span>{c["icon"]} {e(c["name"])}</span></label>' for c in ctx["CATEGORIES"])
    def radios(name, vals):
        return "".join(f'<label class="opt"><input type="radio" name="{name}" value="{v}" required><span>{v}</span></label>' for v in vals)
    feats = ["Easy to use", "Mobile app", "Integrations with current tools", "Automation", "Reporting & dashboards", "Strong security & compliance", "Local support / time zone", "Fast setup", "Scales with growth", "Lowest total cost"]
    return ctx["page_head"]("Get free, vendor-neutral quotes", "Four quick steps. A shortlist matched to your needs. You decide who — if anyone — contacts you.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap layout">
<div class="form-card">
<form data-form="LEAD: Get matched (full)" data-ok="Your request is in. Expect your shortlist by email within 2 business days — sooner for urgent timelines." novalidate>
<div style="display:flex;justify-content:space-between;align-items:center"><strong data-step-label>Step 1 of 4</strong><span class="muted" style="font-size:.9rem">About 90 seconds</span></div>
<div class="progress" aria-hidden="true"><span></span></div>

<div class="step-pane"><h2>What are you looking for?</h2>
<div class="opt-grid" data-require-one>{opts}<label class="opt"><input type="radio" name="category" value="Other"><span>Something else</span></label></div>
<div class="field" style="margin-top:18px"><label>Where are you in the process?</label><div class="opt-grid" data-require-one>{radios("stage", ["Buying for the first time", "Replacing a current tool or provider", "Adding to what we have", "Just researching"])}</div></div>
<div class="step-nav"><span></span><button class="btn btn-primary" type="button" data-next>Continue</button></div></div>

<div class="step-pane"><h2>About your business</h2>
<div class="row"><div class="field"><label for="gq-size">Company size</label><select id="gq-size" name="company_size" required><option value="">Choose…</option><option>Just me</option><option>2–10</option><option>11–50</option><option>51–200</option><option>201–1,000</option><option>1,000+</option></select></div>
<div class="field"><label for="gq-users">People who will use it</label><input id="gq-users" type="number" min="1" name="users" required placeholder="e.g. 8"></div></div>
<div class="row"><div class="field"><label for="gq-budget">Monthly budget (USD)</label><select id="gq-budget" name="budget" required><option value="">Choose…</option><option>Under $100</option><option>$100–$500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option><option>Not sure yet</option></select></div>
<div class="field"><label for="gq-time">When do you want to decide?</label><select id="gq-time" name="timeline" required><option value="">Choose…</option><option>As soon as possible</option><option>Within 1 month</option><option>1–3 months</option><option>3–6 months</option><option>Just researching</option></select></div></div>
<div class="row"><div class="field"><label for="gq-cur">Current tool or provider (optional)</label><input id="gq-cur" type="text" name="current_solution" placeholder="e.g. spreadsheets, QuickBooks"></div>
<div class="field"><label for="gq-reg">Country / region</label><input id="gq-reg" type="text" name="region" required placeholder="e.g. Canada – Quebec" autocomplete="country-name"></div></div>
<div class="field"><label for="gq-ind">Industry</label><input id="gq-ind" type="text" name="industry" required placeholder="e.g. construction, retail, SaaS"></div>
<div class="step-nav"><button class="btn btn-ghost" type="button" data-prev>Back</button><button class="btn btn-primary" type="button" data-next>Continue</button></div></div>

<div class="step-pane"><h2>What matters most?</h2><p class="muted">Pick your must-haves. We match on these first.</p>
<div class="opt-grid">{"".join(f'<label class="opt"><input type="checkbox" name="must_haves" value="{f}"><span>{f}</span></label>' for f in feats)}</div>
<div class="field" style="margin-top:18px"><label for="gq-notes">Anything else we should know? (optional)</label><textarea id="gq-notes" name="details" placeholder="Problems you're solving, integrations you need, deal-breakers…"></textarea></div>
<div class="step-nav"><button class="btn btn-ghost" type="button" data-prev>Back</button><button class="btn btn-primary" type="button" data-next>Continue</button></div></div>

<div class="step-pane"><h2>Where should we send your shortlist?</h2>
<div class="row"><div class="field"><label for="gq-name">Full name</label><input id="gq-name" type="text" name="name" required autocomplete="name"></div>
<div class="field"><label for="gq-email">Work email</label><input id="gq-email" type="email" name="email" required autocomplete="email"></div></div>
<div class="row"><div class="field"><label for="gq-co">Company</label><input id="gq-co" type="text" name="company" required autocomplete="organization"></div>
<div class="field"><label for="gq-phone">Phone (optional)</label><input id="gq-phone" type="tel" name="phone" autocomplete="tel"></div></div>
<div class="field"><label for="gq-contact">How would you like to hear back?</label><select id="gq-contact" name="contact_preference"><option>Email only</option><option>Email, then a short call</option><option>Phone call</option></select></div>
<label class="check" style="margin-bottom:10px"><input type="checkbox" name="consent_contact" value="yes" required> BusinessReviews.com may contact me about this request.</label>
<label class="check"><input type="checkbox" name="consent_share" value="yes"> I also agree that BusinessReviews.com may share my request with up to 3 matched providers, who may contact me by email or phone. (Optional — leave unticked to receive the shortlist only.)</label>
{ctx["HP"]}
<div class="step-nav"><button class="btn btn-ghost" type="button" data-prev>Back</button><button class="btn btn-gold" type="submit">Send my request</button></div>
<p class="hint">We never sell your details. See our <a href="{r}privacy.html">privacy policy</a>.</p></div>
</form></div>
<aside><div class="aside-stick">
<div class="card"><h3>What happens next</h3><ol style="padding-left:20px;margin:0"><li>We review your needs against our category research.</li><li>You get a shortlist of 3–5 options with questions to ask each.</li><li>If you opted in, up to 3 providers reach out. Otherwise, nobody does.</li></ol></div>
<div class="card"><h3>Always free for buyers</h3><p class="muted">Providers may pay us when they join our lead program. That never changes the order of reviews or what our guides say. <a href="{r}disclaimer.html">How we make money</a>.</p></div>
<div class="card"><h3>Prefer to talk?</h3><p class="muted">For partnerships or large projects, <a href="{r}contact.html?topic=Enterprise%20buying%20help">contact our team</a>.</p></div>
</div></aside></div></section>'''

# ---------------- Write review ----------------
def write_review(ctx, r):
    def sub(name, label):
        return f'<div class="field"><label for="wr-{name}">{label}</label><select id="wr-{name}" name="{name}"><option value="">Not applicable</option><option>5 – Excellent</option><option>4 – Great</option><option>3 – Average</option><option>2 – Poor</option><option>1 – Bad</option></select></div>'
    return ctx["page_head"]("Write a review", "Share a first-hand experience with a business, software product or service provider. Every review is checked before it's published.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap layout"><div class="form-card">
<form data-form="REVIEW submission" data-ok="Thank you. Your review is in the moderation queue — we'll email you when it's published or if we need anything." novalidate>
<div style="display:flex;justify-content:space-between"><strong data-step-label>Step 1 of 3</strong><span class="muted" style="font-size:.9rem">About 3 minutes</span></div>
<div class="progress" aria-hidden="true"><span></span></div>
<div class="step-pane"><h2>Which business are you reviewing?</h2>
<div class="row"><div class="field"><label for="wr-biz">Business or product name</label><input id="wr-biz" type="text" name="business" required></div>
<div class="field"><label for="wr-site">Website (optional)</label><input id="wr-site" type="url" name="website" placeholder="https://"></div></div>
<div class="field"><label for="f-category">Category</label>{cat_options(ctx)}</div>
<div class="field"><label>Your overall rating</label><div class="rate-input" data-rate="reviewRating" role="group" aria-label="Overall rating"></div><div class="star-caption" aria-live="polite"></div><input type="hidden" id="reviewRating" name="rating" required></div>
<div class="field"><label for="wr-title">Review title</label><input id="wr-title" type="text" name="title" required maxlength="100" placeholder="Sum up your experience in one line"></div>
<div class="step-nav"><span></span><button class="btn btn-primary" type="button" data-next>Continue</button></div></div>

<div class="step-pane"><h2>Tell us what happened</h2>
<div class="field"><label for="wr-text">Your review</label><textarea id="wr-text" name="review" required minlength="100" placeholder="What did you buy or use? What went well, what didn't, and would you choose them again?"></textarea><div class="hint">At least 100 characters. Specific details help other buyers most.</div></div>
<div class="row"><div class="field"><label for="wr-pros">What did you like?</label><textarea id="wr-pros" name="pros" style="min-height:90px"></textarea></div>
<div class="field"><label for="wr-cons">What could be better?</label><textarea id="wr-cons" name="cons" style="min-height:90px"></textarea></div></div>
<div class="row">{sub("rating_value","Value for money")}{sub("rating_support","Customer support")}</div>
<div class="row">{sub("rating_ease","Ease of use / working with them")}<div class="field"><label for="wr-nps">How likely are you to recommend them? (0–10)</label><input id="wr-nps" type="number" min="0" max="10" name="recommend_0_10"></div></div>
<div class="row"><div class="field"><label for="wr-date">Date of experience</label><input id="wr-date" type="date" name="date_of_experience" required></div>
<div class="field"><label for="wr-dur">How long have you used them?</label><select id="wr-dur" name="usage_duration" required><option value="">Choose…</option><option>One-time purchase or project</option><option>Less than 6 months</option><option>6–12 months</option><option>1–2 years</option><option>More than 2 years</option><option>Free trial only</option></select></div></div>
<div class="step-nav"><button class="btn btn-ghost" type="button" data-prev>Back</button><button class="btn btn-primary" type="button" data-next>Continue</button></div></div>

<div class="step-pane"><h2>About you</h2><p class="muted">Your email is never published. We use it to confirm your review.</p>
<div class="row"><div class="field"><label for="wr-name">Display name</label><input id="wr-name" type="text" name="display_name" required placeholder="e.g. Priya S."></div>
<div class="field"><label for="wr-email">Email</label><input id="wr-email" type="email" name="email" required autocomplete="email"></div></div>
<div class="row"><div class="field"><label for="wr-role">Your role (optional)</label><input id="wr-role" type="text" name="role" placeholder="e.g. Operations manager"></div>
<div class="field"><label for="wr-size">Company size (optional)</label><select id="wr-size" name="company_size"><option value="">Choose…</option><option>Just me</option><option>2–10</option><option>11–50</option><option>51–200</option><option>201–1,000</option><option>1,000+</option></select></div></div>
<div class="field"><label for="wr-rel">Your relationship with this business</label><select id="wr-rel" name="relationship" required><option value="">Choose…</option><option>Current customer</option><option>Former customer</option><option>Trial user</option><option>Employee, owner or relative (not eligible to review)</option><option>Competitor (not eligible to review)</option></select></div>
<div class="field"><label for="wr-inc">Did you receive anything for writing this review?</label><select id="wr-inc" name="incentive" required><option value="">Choose…</option><option>No</option><option>Yes — I was invited by the business</option><option>Yes — I received a gift, discount or payment (will be labelled Incentivized)</option></select></div>
<div class="field"><label for="wr-proof">Order, invoice or account reference (optional, kept private)</label><input id="wr-proof" type="text" name="proof_reference"><div class="hint">Helps us apply the Verified label. Never published.</div></div>
<label class="check" style="margin-bottom:10px"><input type="checkbox" name="confirm_genuine" value="yes" required> This review is based on my own genuine experience, and I've disclosed any relationship or incentive.</label>
<label class="check"><input type="checkbox" name="agree_terms" value="yes" required> I agree to the <a href="{r}review-guidelines.html" target="_blank">review guidelines</a> and <a href="{r}terms.html" target="_blank">terms</a>, and grant BusinessReviews.com a licence to publish this review.</label>
{ctx["HP"]}
<div class="step-nav"><button class="btn btn-ghost" type="button" data-prev>Back</button><button class="btn btn-gold" type="submit">Submit review for moderation</button></div></div>
</form></div>
<aside><div class="aside-stick">
<div class="card"><h3>What makes a helpful review</h3><ul class="checks"><li>Specific: what you bought and when</li><li>Balanced: what worked and what didn't</li><li>Honest: your own experience only</li><li>Respectful: no personal attacks or private data</li></ul></div>
<div class="card"><h3>Labels we apply</h3><p><span class="tag">Verified</span> proof of purchase or use checked</p><p><span class="tag blue">Invited</span> the business asked you to review</p><p><span class="tag gold">Incentivized</span> you received something of value</p><p style="margin:0"><a href="{r}review-guidelines.html">Full guidelines</a></p></div>
</div></aside></div></section>'''

# ---------------- For business ----------------
def for_business(ctx, r):
    tiers = [("Free profile", "$0", "For every business", ["Claim and verify your listing", "Logo, description and contact details", "Public replies to reviews", "Review invitation link"], "Free profile", False),
             ("Growth", "Founding rate on request", "For businesses that want more reviews", ["Everything in Free", "Website review widgets and badge", "Monthly review insights", "Bulk email review invitations", "Priority moderation of disputes"], "Growth", True),
             ("Partner", "Custom", "For providers who want matched buyers", ["Everything in Growth", "Matched buyer requests in your category", "Clearly labelled sponsored placement options", "Dedicated partner manager"], "Partner / lead program", False)]
    cards = "".join(f'''<div class="card tier{" feature" if f else ""}"><h3>{n}</h3><div class="amt">{p}</div><p class="muted">{d}</p><ul class="checks">{"".join(f"<li>{x}</li>" for x in li)}</ul><a class="btn {"btn-gold" if f else "btn-ghost"} btn-block" href="#claim" onclick="var s=document.getElementById('fb-plan');if(s)s.value='{v}'">Choose {n}</a></div>''' for n, p, d, li, v, f in tiers)
    return ctx["page_head"]("For business owners", "Claim your free profile, respond to reviews and turn your reputation into new customers.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap">
<div class="grid g3">{cards}</div>
<p class="muted" style="margin-top:14px;font-size:.92rem">No plan lets a business remove, edit or reorder reviews. Sponsored placements are always labelled. See our <a href="{r}review-guidelines.html#business">rules for businesses</a>.</p>
</div></section>
<section class="section tint" id="claim"><div class="wrap split">
<div><h2>Claim your profile</h2><p class="lead">We verify that you represent the business, usually by a code sent to an email address on your website's domain.</p>
<ul class="checks"><li>Respond publicly to every review</li><li>Keep hours, services and contact details accurate</li><li>Invite customers with your own review link</li><li>Get notified about new reviews</li></ul>
<h3 style="margin-top:28px">Rules that protect your reputation too</h3><p class="muted">Ask every customer — not only happy ones. Never offer rewards for positive reviews. Report reviews you believe break our guidelines instead of disputing them publicly.</p></div>
<div class="form-card"><form data-form="BUSINESS: Claim profile" data-ok="Thanks — we'll verify your business and email next steps within 2 business days.">
<div class="row"><div class="field"><label for="fb-biz">Business name</label><input id="fb-biz" name="business" type="text" required></div>
<div class="field"><label for="fb-site">Website</label><input id="fb-site" name="website" type="url" required placeholder="https://"></div></div>
<div class="field"><label for="f-category">Category</label>{cat_options(ctx)}</div>
<div class="row"><div class="field"><label for="fb-name">Your name</label><input id="fb-name" name="name" type="text" required autocomplete="name"></div>
<div class="field"><label for="fb-role">Your role</label><input id="fb-role" name="role" type="text" required placeholder="Owner, marketing lead…"></div></div>
<div class="row"><div class="field"><label for="fb-email">Work email</label><input id="fb-email" name="email" type="email" required><div class="hint">Use an address on your business domain for faster verification.</div></div>
<div class="field"><label for="fb-phone">Phone</label><input id="fb-phone" name="phone" type="tel"></div></div>
<div class="row"><div class="field"><label for="fb-plan">Plan of interest</label><select id="fb-plan" name="plan"><option>Free profile</option><option>Growth</option><option>Partner / lead program</option><option>Not sure yet</option></select></div>
<div class="field"><label for="fb-loc">Locations served</label><input id="fb-loc" name="locations" type="text" placeholder="City, region or 'online'"></div></div>
{ctx["HP"]}<label class="check"><input type="checkbox" name="authorised" value="yes" required> I'm authorised to represent this business and agree to the <a href="{r}review-guidelines.html#business">business rules</a>.</label>
<button class="btn btn-primary btn-block" type="submit" style="margin-top:14px">Claim my free profile</button></form></div>
</div></section>
<section class="section"><div class="wrap"><h2>Free tools for owners</h2><div class="grid g3">
<a class="card" href="{r}tools.html#response"><h3>Review response writer</h3><p class="muted">Professional replies in your tone.</p></a>
<a class="card" href="{r}tools.html#request"><h3>Review request builder</h3><p class="muted">Compliant email and SMS templates.</p></a>
<a class="card" href="{r}tools.html#goal"><h3>Rating goal calculator</h3><p class="muted">Plan how many reviews you need.</p></a></div></div></section>'''

# ---------------- Advertise ----------------
def advertise(ctx, r):
    pk = [("Category sponsorship", "A labelled sponsor slot on a category page and its buyer's guide."), ("Sponsored guide", "A clearly marked sponsored article written to our editorial standards."), ("Newsletter sponsorship", "A labelled placement in our monthly buyer's brief."),
          ("Contest & prize sponsorship", "Fund a monthly prize and get credited on the contest page and announcement."), ("Video sponsorship", "A sponsor mention on explainer videos in our library."), ("Domain, acquisition or partnership", "Interested in the BusinessReviews.com domain or a strategic partnership.")]
    cards = "".join(f'<div class="card"><h3>{n}</h3><p class="muted">{d}</p></div>' for n, d in pk)
    opts = "".join(f"<option>{n}</option>" for n, _ in pk)
    return ctx["page_head"]("Advertise, sponsor or partner", "Reach people who are actively choosing business software and service providers — with placements that are always clearly labelled.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap">
<div class="notice" style="margin-bottom:28px"><strong>Interested in this website, the domain name, sponsorship, advertising or a partnership?</strong> <a href="{ctx["INTEREST_URL"]}" target="_blank" rel="noopener">Contact the owner directly</a>, or use the form below.</div>
<div class="grid g3">{cards}</div></div></section>
<section class="section tint"><div class="wrap split">
<div><h2>Our advertising principles</h2><ul class="checks"><li>Every paid placement is labelled Sponsored or Advertisement</li><li>Sponsors never see or influence reviews before they're published</li><li>Sponsorship never changes ratings, review order or editorial verdicts</li><li>We decline advertisers with credible evidence of review manipulation</li></ul></div>
<div class="form-card"><form data-form="ADVERTISE / Sponsorship inquiry" data-ok="Thanks — our partnerships team will reply within 2 business days.">
<div class="row"><div class="field"><label for="ad-name">Name</label><input id="ad-name" name="name" required></div><div class="field"><label for="ad-co">Company</label><input id="ad-co" name="company" required></div></div>
<div class="row"><div class="field"><label for="ad-email">Work email</label><input id="ad-email" type="email" name="email" required></div><div class="field"><label for="ad-site">Website</label><input id="ad-site" type="url" name="website" placeholder="https://"></div></div>
<div class="field"><label for="ad-pk">Interested in</label><select id="ad-pk" name="package" required><option value="">Choose…</option>{opts}</select></div>
<div class="field"><label for="ad-bud">Budget range (USD)</label><select id="ad-bud" name="budget"><option>Under $1,000</option><option>$1,000–$5,000</option><option>$5,000–$25,000</option><option>$25,000+</option><option>Discuss</option></select></div>
<div class="field"><label for="ad-msg">Goals and timing</label><textarea id="ad-msg" name="message" required></textarea></div>
{ctx["HP"]}<button class="btn btn-primary btn-block" type="submit">Send inquiry</button></form></div>
</div></section>'''

# ---------------- Contests ----------------
def contests(ctx, r):
    cs = [("Most Helpful Review of the Month", "Judged on specificity, balance and usefulness to other buyers — never on whether the review is positive or negative.", "Monthly", "Featured spotlight + sponsor-funded prize"),
          ("Small Business Story", "Tell us how a tool, provider or decision changed your business — good or bad. Winners are published as interviews.", "Quarterly", "Feature interview + prize"),
          ("Tool Tips Challenge", "Share your best workflow tip for a business tool you use daily. Short video or written entries.", "Monthly", "Featured in our video library + prize")]
    cards = "".join(f'<div class="card"><span class="tag gold">{f}</span><h3 style="margin-top:12px">{n}</h3><p class="muted">{d}</p><p><strong>Prize:</strong> {p}</p></div>' for n, d, f, p in cs)
    opts = "".join(f"<option>{n}</option>" for n, *_ in cs)
    return ctx["page_head"]("Contests &amp; prizes", "Monthly and quarterly contests that reward the most useful contributions to our community.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap"><div class="grid g3">{cards}</div>
<p class="muted" style="margin-top:14px">Prize values are announced at the start of each round and funded by sponsors and supporters. <a href="{r}advertise.html">Sponsor a prize</a> · <a href="{r}donate.html">Support the prize fund</a></p></div></section>
<section class="section tint"><div class="wrap split">
<div class="form-card"><h2>Enter a contest</h2><form data-form="CONTEST entry" data-ok="Entry received. Winners are notified by email and announced on this page.">
<div class="field"><label for="ct-c">Contest</label><select id="ct-c" name="contest" required><option value="">Choose…</option>{opts}</select></div>
<div class="row"><div class="field"><label for="ct-n">Name</label><input id="ct-n" name="name" required></div><div class="field"><label for="ct-e">Email</label><input id="ct-e" type="email" name="email" required></div></div>
<div class="row"><div class="field"><label for="ct-cty">Country</label><input id="ct-cty" name="country" required></div><div class="field"><label for="ct-link">Link to entry (optional)</label><input id="ct-link" type="url" name="entry_link" placeholder="Video or document link"></div></div>
<div class="field"><label for="ct-txt">Your entry</label><textarea id="ct-txt" name="entry" required minlength="80"></textarea></div>
{ctx["HP"]}<label class="check" style="margin-bottom:8px"><input type="checkbox" name="age" value="yes" required> I am 18 or older (or the age of majority where I live).</label>
<label class="check"><input type="checkbox" name="rules" value="yes" required> I have read and accept the official rules below.</label>
<button class="btn btn-gold btn-block" type="submit" style="margin-top:14px">Submit my entry</button></form></div>
<div class="article"><h2 id="rules" style="margin-top:0">Official rules (summary)</h2>
<ol><li><strong>No purchase necessary.</strong> A purchase does not improve your chances of winning.</li>
<li><strong>Eligibility:</strong> open to individuals who have reached the age of majority where they live. Employees of BusinessReviews.com, sponsors and their immediate families are not eligible. Void where prohibited.</li>
<li><strong>Judging:</strong> entries are judged by our editorial team on helpfulness, originality and clarity. For review contests, the star rating and sentiment play no part in judging.</li>
<li><strong>Disclosure:</strong> reviews entered into a contest are labelled "Contest entry" when published, in line with consumer-protection rules on incentivised reviews.</li>
<li><strong>Prizes:</strong> announced per round; non-transferable; winners may need to answer a skill-testing question where required by law (for example, in Canada).</li>
<li><strong>Winners</strong> are notified by email and must respond within 14 days, or an alternate is chosen.</li>
<li><strong>Privacy:</strong> entry data is used only to run the contest. See our <a href="{r}privacy.html">privacy policy</a>.</li></ol></div>
</div></section>'''

# ---------------- Careers ----------------
def careers(ctx, r):
    roles = [("Review moderator", "Remote · Part-time", "Screen submitted reviews against our guidelines, request proof of use and handle disputes fairly."),
             ("B2B software writer", "Remote · Freelance", "Research and write vendor-neutral buyer's guides with clear sourcing."),
             ("SEO & content strategist", "Remote · Contract", "Plan category coverage, internal linking and search performance."),
             ("Video creator", "Remote · Freelance", "Produce short explainers on buying software and managing reputation."),
             ("Community & contests manager", "Remote · Part-time", "Run monthly contests, spotlight contributors and grow the reviewer community."),
             ("Partnerships lead", "Remote · Commission + base", "Build the provider lead program and sponsorship partnerships.")]
    cards = "".join(f'<div class="card"><span class="tag blue">{m}</span><h3 style="margin-top:10px">{n}</h3><p class="muted">{d}</p><a class="btn btn-ghost btn-sm" href="#apply" onclick="document.getElementById(\'cr-role\').value=\'{n}\'">Apply for this role</a></div>' for n, m, d in roles)
    opts = "".join(f"<option>{n}</option>" for n, *_ in roles)
    return ctx["page_head"]("Careers", "Help build the most trustworthy place to research business purchases. Remote-first roles, flexible hours.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap"><div class="grid g3">{cards}</div></div></section>
<section class="section tint" id="apply"><div class="wrap split">
<div><h2>How we work</h2><ul class="checks"><li>Remote-first, asynchronous by default</li><li>Clear editorial standards and independence from advertisers</li><li>Paid trial projects for writing and moderation roles</li></ul><p class="muted">Don't see your role? Apply anyway and tell us what you'd build.</p></div>
<div class="form-card"><form data-form="CAREERS application" data-ok="Application received. If there's a fit, we'll be in touch within 10 business days.">
<div class="field"><label for="cr-role">Role</label><select id="cr-role" name="role" required><option value="">Choose…</option>{opts}<option>Open application</option></select></div>
<div class="row"><div class="field"><label for="cr-n">Full name</label><input id="cr-n" name="name" required autocomplete="name"></div><div class="field"><label for="cr-e">Email</label><input id="cr-e" type="email" name="email" required></div></div>
<div class="row"><div class="field"><label for="cr-loc">Location / time zone</label><input id="cr-loc" name="location" required></div><div class="field"><label for="cr-av">Availability</label><select id="cr-av" name="availability"><option>Under 10 hrs/week</option><option>10–20 hrs/week</option><option>20–40 hrs/week</option><option>Full-time</option></select></div></div>
<div class="field"><label for="cr-pf">Portfolio, LinkedIn or CV link</label><input id="cr-pf" type="url" name="portfolio" required placeholder="https://"></div>
<div class="field"><label for="cr-m">Why you, in a few sentences</label><textarea id="cr-m" name="message" required></textarea></div>
{ctx["HP"]}<button class="btn btn-primary btn-block" type="submit">Send application</button></form></div>
</div></section>'''

# ---------------- Donate ----------------
def donate(ctx, r):
    tiers = [("Supporter", "$5", "Covers moderation of about ten reviews.", "5"), ("Backer", "$25", "Funds research for a new category guide.", "25"), ("Champion", "$100", "Sponsors part of a monthly contest prize.", "100"), ("Patron", "$500", "Helps us hire moderators and creators.", "500")]
    cards = "".join(f'<div class="card tier{" feature" if a=="25" else ""}"><h3>{n}</h3><div class="amt">{p}</div><p class="muted">{d}</p><button class="btn {"btn-gold" if a=="25" else "btn-ghost"} btn-block" type="button" data-amount="{a}">Give {p}</button></div>' for n, p, d, a in tiers)
    return ctx["page_head"]("Support independent reviews", "BusinessReviews.com is free for everyone. Reader support keeps moderation human, guides independent and contest prizes funded.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap"><div class="grid g4">{cards}</div></div></section>
<section class="section tint"><div class="wrap split">
<div><h2>Where your support goes</h2>
<table class="matrix"><tr><td><strong>Operations</strong></td><td>Hosting, moderation tools and human review screening</td></tr><tr><td><strong>Promotions &amp; marketing</strong></td><td>Reaching more buyers so more honest reviews get written</td></tr><tr><td><strong>Hiring talent</strong></td><td>Moderators, writers and video creators</td></tr><tr><td><strong>Contests &amp; prizes</strong></td><td>Rewarding the community's most helpful contributions</td></tr></table>
<p class="muted" style="margin-top:16px">Supporting us never affects any review or rating. Businesses cannot donate to influence content; such offers are declined. Donations are not tax-deductible unless stated on your receipt.</p>
<div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:14px"><a class="btn btn-primary" data-donate="stripe" hidden href="#">Give by card</a><a class="btn btn-ghost" data-donate="paypal" hidden href="#">Give with PayPal</a><a class="btn btn-ghost" data-donate="kofi" hidden href="#">Ko-fi</a></div></div>
<div class="form-card"><h2>Pledge your support</h2><p class="muted">Choose an amount and purpose. We'll email a secure payment link and a receipt.</p>
<form data-form="DONATION pledge" data-ok="Thank you! A secure payment link is on its way to your inbox.">
<div class="row"><div class="field"><label for="pledgeAmount">Amount (USD)</label><input id="pledgeAmount" type="number" min="1" name="amount" required></div>
<div class="field"><label for="dn-f">Frequency</label><select id="dn-f" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<div class="field"><label for="dn-p">Put it towards</label><select id="dn-p" name="purpose"><option>Where it's needed most</option><option>Operations</option><option>Promotions &amp; marketing</option><option>Hiring talent</option><option>Contests &amp; prizes</option></select></div>
<div class="row"><div class="field"><label for="dn-n">Name</label><input id="dn-n" name="name" required></div><div class="field"><label for="dn-e">Email</label><input id="dn-e" type="email" name="email" required></div></div>
<label class="check"><input type="checkbox" name="public_thanks" value="yes"> Thank me publicly on the supporters list.</label>
{ctx["HP"]}<button class="btn btn-gold btn-block" type="submit" style="margin-top:14px">Send my pledge</button></form></div>
</div></section>'''

# ---------------- Tools ----------------
def tools(ctx, r):
    vend = "".join(f'<th><input aria-label="Vendor {chr(65+i)} name" value="Vendor {chr(65+i)}"></th>' for i in range(4))
    crit = [("Fit to must-haves", 5), ("Ease of use", 4), ("Integrations", 3), ("Total cost", 4), ("Support quality", 3), ("Vendor stability & exit terms", 2)]
    rows = "".join(f'<tr><td>{c}</td><td><input data-w type="number" min="0" max="5" value="{w}" aria-label="Weight for {c}"></td>' + "".join(f'<td><input data-s type="number" min="0" max="10" value="{[7,6,8,5][i]}" aria-label="{c} score, vendor {chr(65+i)}"></td>' for i in range(4)) + '</tr>' for c, w in crit)
    return ctx["page_head"]("Free tools", "Practical calculators and writers for buyers comparing vendors and owners managing reviews. Nothing to install, nothing stored.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap">
<div class="chips" style="margin:0 0 30px"><a class="chip" href="#scorecard">Vendor scorecard</a><a class="chip" href="#tco">Total cost calculator</a><a class="chip" href="#response">Review response writer</a><a class="chip" href="#request">Review request builder</a><a class="chip" href="#goal">Rating goal calculator</a></div>

<div class="card tool" id="scorecard" style="margin-bottom:24px"><h2>Vendor scorecard</h2><p class="muted">Set a weight (0–5) for each criterion, then score each vendor 0–10. Agree weights before demos.</p>
<div style="overflow-x:auto"><table class="matrix" id="scTable"><thead><tr><th>Criterion</th><th>Weight</th>{vend}</tr></thead><tbody>{rows}</tbody></table></div>
<div id="scOut" style="margin-top:18px" aria-live="polite"></div></div>

<div class="card tool" id="tco" style="margin-bottom:24px"><div class="split"><form id="tcForm" onsubmit="return false"><h2>SaaS total cost of ownership</h2>
<div class="row"><div class="field"><label for="tcSeats">Users today</label><input id="tcSeats" type="number" min="1" value="10"></div><div class="field"><label for="tcPrice">Price per user / month ($)</label><input id="tcPrice" type="number" min="0" value="45"></div></div>
<div class="row"><div class="field"><label for="tcMonths">Period (months)</label><input id="tcMonths" type="number" min="1" value="36"></div><div class="field"><label for="tcAddons">Add-ons per month ($)</label><input id="tcAddons" type="number" min="0" value="100"></div></div>
<div class="row"><div class="field"><label for="tcSetup">Implementation ($)</label><input id="tcSetup" type="number" min="0" value="3000"></div><div class="field"><label for="tcTrain">Training &amp; change ($)</label><input id="tcTrain" type="number" min="0" value="1500"></div></div>
<div class="row"><div class="field"><label for="tcGrowth">Headcount growth per year (%)</label><input id="tcGrowth" type="number" value="20"></div><div class="field"><label for="tcHike">Price increase per year (%)</label><input id="tcHike" type="number" value="5"></div></div></form>
<div id="tcOut" aria-live="polite"></div></div></div>

<div class="card tool" id="response" style="margin-bottom:24px"><div class="split"><form id="rrForm"><h2>Review response writer</h2>
<div class="row"><div class="field"><label for="rrName">Reviewer's first name</label><input id="rrName" value="Sam"></div><div class="field"><label for="rrBiz">Your business</label><input id="rrBiz" value="Northside Plumbing"></div></div>
<div class="row"><div class="field"><label for="rrStars">Star rating</label><select id="rrStars"><option>5</option><option>4</option><option>3</option><option selected>2</option><option>1</option></select></div><div class="field"><label for="rrIssue">What was it about?</label><select id="rrIssue"><option value="service">Service</option><option value="product">Product</option><option value="price">Price</option><option value="wait" selected>Wait time</option><option value="billing">Billing</option><option value="staff">Staff</option><option value="other">Other</option></select></div></div>
<div class="row"><div class="field"><label for="rrTone">Tone</label><select id="rrTone"><option value="pro">Professional</option><option value="warm">Warm</option><option value="brief">Brief</option></select></div><div class="field"><label for="rrSign">Sign off as</label><input id="rrSign" placeholder="e.g. Dana, Owner"></div></div>
<div class="field"><label for="rrDetail">Specific detail to mention (optional)</label><input id="rrDetail" placeholder="e.g. the technician arrived two hours late"></div></form>
<div><div class="out" id="rrOut" aria-live="polite"></div><button class="btn btn-ghost btn-sm" id="rrCopy" type="button" style="margin-top:10px">Copy text</button><p class="hint">Always personalise before posting. Never offer compensation in exchange for changing a review.</p></div></div></div>

<div class="card tool" id="request" style="margin-bottom:24px"><div class="split"><form id="rqForm" onsubmit="return false"><h2>Review request builder</h2>
<div class="row"><div class="field"><label for="rqChannel">Channel</label><select id="rqChannel"><option value="email">Email</option><option value="sms">SMS</option></select></div><div class="field"><label for="rqBiz">Business name</label><input id="rqBiz" value="Northside Plumbing"></div></div>
<div class="row"><div class="field"><label for="rqCust">Customer first name</label><input id="rqCust" value="Alex"></div><div class="field"><label for="rqWhat">What they bought</label><input id="rqWhat" value="your water-heater installation"></div></div>
<div class="field"><label for="rqLink">Your review link</label><input id="rqLink" type="url" placeholder="https://"></div></form>
<div><div class="out" id="rqOut" aria-live="polite"></div><button class="btn btn-ghost btn-sm" id="rqCopy" type="button" style="margin-top:10px">Copy text</button><p class="hint">Send to every customer, not only happy ones. Get SMS consent where the law requires it.</p></div></div></div>

<div class="card tool" id="goal"><div class="split"><form id="rgForm" onsubmit="return false"><h2>Rating goal calculator</h2>
<div class="row"><div class="field"><label for="rgAvg">Current average</label><input id="rgAvg" type="number" step="0.01" min="1" max="5" value="4.1"></div><div class="field"><label for="rgCount">Current number of reviews</label><input id="rgCount" type="number" min="1" value="86"></div></div>
<div class="field"><label for="rgTarget">Target average</label><input id="rgTarget" type="number" step="0.01" min="1" max="4.99" value="4.5"></div></form>
<div id="rgOut" aria-live="polite"></div></div></div>
</div></section>
<section class="section tint"><div class="wrap">{ctx["quick_lead"](r, "", "Tools page")}</div></section>'''

# ---------------- Videos ----------------
def videos(ctx, r):
    groups = {}
    for v in VIDEOS: groups.setdefault(v[3], []).append(v)
    out = "".join(f'<h2 style="margin-top:1.2em">{g}</h2><div class="grid g3">{"".join(vid(v) for v in vs)}</div>' for g, vs in groups.items())
    return ctx["page_head"]("Video library", "Short explainers from respected channels on choosing software, managing reviews and spotting fakes. Videos load only when you press play.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap">{out}
<p class="muted" style="margin-top:30px;font-size:.92rem">Videos are embedded from YouTube in privacy-enhanced mode and belong to their creators. Inclusion is not an endorsement by or of BusinessReviews.com. <a href="{r}contact.html?topic=Suggest%20a%20video">Suggest a video</a> · <a href="{r}advertise.html">Sponsor the library</a></p></div></section>'''

# ---------------- Awards ----------------
def awards(ctx, r):
    return ctx["page_head"]("Community Choice Awards", "Annual awards decided only by verified reviews — not by fees, sponsorship or editorial favourites.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap split"><div class="article">
<h2 style="margin-top:0">Eligibility</h2><ul><li>At least 10 published reviews in the 12 months before the cut-off, with at least half labelled Verified.</li><li>No upheld manipulation findings during the period.</li><li>Ranked within category by our published score (see <a href="{r}editorial-policy.html#score">methodology</a>).</li></ul>
<h2>Timeline</h2><p>Reviews submitted through the year count toward the next edition. Winners are announced each January; the first edition will be announced once enough verified reviews exist to make results meaningful.</p>
<h2>Badges</h2><p>Winners receive a free badge they may display on their website. Badges link back to the live profile so anyone can check the evidence.</p></div>
<div class="form-card"><h2>Nominate a business</h2><p class="muted">Nominations tell us where to focus outreach. They do not count as votes.</p>
<form data-form="AWARDS nomination" data-ok="Nomination received — thank you.">
<div class="field"><label for="aw-b">Business or product</label><input id="aw-b" name="business" required></div>
<div class="field"><label for="f-category">Category</label>{cat_options(ctx)}</div>
<div class="field"><label for="aw-w">Why they deserve it</label><textarea id="aw-w" name="reason" required></textarea></div>
<div class="field"><label for="aw-e">Your email</label><input id="aw-e" type="email" name="email" required></div>
<label class="check"><input type="checkbox" name="no_conflict" value="yes" required> I'm not an employee or owner of this business.</label>
{ctx["HP"]}<button class="btn btn-gold btn-block" style="margin-top:14px" type="submit">Submit nomination</button></form></div>
</div></section>'''

# ---------------- About ----------------
def about(ctx, r):
    return ctx["page_head"]("About BusinessReviews.com", "We help people choose business software and service providers with honest reviews, clear guides and free tools.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap layout"><article class="article">
<h2 style="margin-top:0">Why we exist</h2><p>Buying the wrong software or hiring the wrong provider is expensive: wasted licences, lost months and painful migrations. Yet much of the information buyers rely on is either vendor marketing or reviews that are hard to trust. BusinessReviews.com exists to make that research faster and more honest.</p>
<h2>What we do</h2><ul><li><strong>Moderated reviews</strong> from people with first-hand experience, labelled so you can weigh them.</li><li><strong>Buyer's guides</strong> that explain what to look for, how pricing works and what to ask — written to our <a href="{r}editorial-policy.html">editorial policy</a>.</li><li><strong>Free tools</strong> for comparing vendors and managing reviews.</li><li><strong>Free matching</strong> for buyers who want a shortlist.</li></ul>
<h2>How we make money</h2><p>We are funded by display advertising (Google AdSense), optional paid tools for businesses, a provider lead program, labelled sponsorships and reader support. None of these can buy a better rating, remove a review or change what our guides say. Read the full <a href="{r}disclaimer.html">disclosure</a>.</p>
<h2>Our commitments</h2><ul><li>Businesses can never pay to remove or reorder reviews.</li><li>Every sponsored placement is labelled.</li><li>We publish our moderation rules and scoring method.</li><li>We correct errors quickly and say so.</li></ul>
<h2>Get in touch</h2><p>Questions, corrections or partnership ideas: <a href="{r}contact.html">contact us</a>. For interest in this website, domain, sponsorship, advertising or partnership: <a href="{ctx["INTEREST_URL"]}" target="_blank" rel="noopener">contact the owner</a>.</p>
</article><aside><div class="aside-stick">{ctx["quick_lead"](r, "", "About")}</div></aside></div></section>'''

# ---------------- Contact ----------------
def contact(ctx, r):
    topics = ["General question", "Report a review", "Correction to a guide", "Business profile help", "Advertising & sponsorship", "Partnership", "Press", "Suggest a category", "Suggest a video", "Enterprise buying help", "Privacy request", "Other"]
    return ctx["page_head"]("Contact us", "We read every message and reply within two business days.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap split">
<div class="form-card"><form data-form="CONTACT form" data-ok="Message sent. We'll reply within 2 business days.">
<div class="row"><div class="field"><label for="ct-name">Name</label><input id="ct-name" name="name" required autocomplete="name"></div><div class="field"><label for="ct-email">Email</label><input id="ct-email" type="email" name="email" required autocomplete="email"></div></div>
<div class="field"><label for="ct-topic">Topic</label><select id="ct-topic" name="topic" required>{"".join(f"<option>{t}</option>" for t in topics)}</select></div>
<div class="field"><label for="ct-msg">Message</label><textarea id="ct-msg" name="message" required></textarea></div>
{ctx["HP"]}<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree that my message will be processed as described in the <a href="{r}privacy.html">privacy policy</a>.</label>
<button class="btn btn-primary btn-block" style="margin-top:14px" type="submit">Send message</button></form></div>
<div><div class="card" style="margin-bottom:18px"><h3>Website, domain, sponsorship or partnership?</h3><p class="muted">If you're interested in this website, the BusinessReviews.com domain name, sponsorship, advertising or a partnership, contact the owner directly.</p><a class="btn btn-gold" href="{ctx["INTEREST_URL"]}" target="_blank" rel="noopener">Contact the owner</a></div>
<div class="card" style="margin-bottom:18px"><h3>Prefer email?</h3><p class="muted">Open a pre-addressed message in your email app.</p><a class="btn btn-ghost" href="#" data-mail="Inquiry from BusinessReviews.com">Email us</a></div>
<div class="card"><h3>Reporting a review?</h3><p class="muted">Include the business name, the reviewer's display name and which guideline you believe it breaks.</p><a href="{r}review-guidelines.html#report">Read how reports are handled</a></div></div>
</div></section>'''

# ---------------- Editorial policy / methodology ----------------
def editorial(ctx, r):
    return ctx["page_head"]("Methodology &amp; editorial policy", "How we write guides, moderate reviews, calculate scores and keep advertising separate from content.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap narrow article">
<h2 id="independence" style="margin-top:0">Editorial independence</h2><p>Guides are written by our editorial team. Advertisers, sponsors and lead-program partners do not review, approve or influence editorial content before publication. When a page contains sponsored content, it is labelled at the top.</p>
<h2 id="guides">How we write guides</h2><ul><li>We research vendor documentation, public pricing pages, independent sources and reviews.</li><li>We prefer criteria and questions that stay true over time to claims that go stale quickly.</li><li>Every guide shows the date it was last updated. Pricing and features change, so we ask readers to verify with vendors.</li><li>Errors are corrected promptly; material corrections are noted at the end of the page.</li></ul>
<h2 id="moderation">How reviews are moderated</h2><ol><li><strong>Automated checks</strong> for duplicates, spam patterns and prohibited content.</li><li><strong>Human review</strong> of every submission against our <a href="{r}review-guidelines.html">guidelines</a>.</li><li><strong>Verification</strong> where possible — proof of purchase or use, which is never published.</li><li><strong>Publication with labels</strong>, or rejection with a reason sent to the reviewer.</li></ol>
<h2 id="labels">Review labels</h2><table><thead><tr><th>Label</th><th>Meaning</th></tr></thead><tbody><tr><td>Verified</td><td>We confirmed proof of purchase, subscription or engagement.</td></tr><tr><td>Invited</td><td>The business invited this customer to leave a review.</td></tr><tr><td>Organic</td><td>The reviewer came to us without an invitation.</td></tr><tr><td>Incentivized</td><td>The reviewer received something of value, not conditioned on sentiment.</td></tr><tr><td>Contest entry</td><td>Submitted as part of a community contest.</td></tr></tbody></table>
<h2 id="score">How the BR Score works</h2><p>Simple averages reward businesses with a handful of five-star reviews. Our BR Score blends a business's ratings with the category average, weights recent reviews more heavily and gives Verified reviews more weight:</p>
<blockquote>BR Score = (C × m + Σ wᵢ·rᵢ) ÷ (C + Σ wᵢ), where m is the category average, C is a confidence constant of 10 reviews, rᵢ is each rating, and wᵢ = recency weight (1.0 in the last 12 months, 0.5 for 12–24 months, 0.25 older) × verification weight (1.25 Verified, 1.0 otherwise).</blockquote>
<p>Scores are shown only after a business has at least three published reviews. Payment, sponsorship and plan level are never inputs.</p>
<h2 id="transparency">Transparency reporting</h2><p>Once reviews are live we will publish a quarterly report covering reviews submitted, published and rejected (with reasons), reports received and actions taken against businesses for manipulation.</p>
<h2 id="ai">Use of AI</h2><p>We may use AI tools to help detect spam or draft outlines. Published guides are reviewed and edited by people, and we never publish AI-generated reviews.</p>
</div></section>'''

# ---------------- Review guidelines ----------------
def guidelines(ctx, r):
    return ctx["page_head"]("Review guidelines", "The rules for reviewers and businesses that keep reviews here useful and fair. These also serve as our user-generated content policy.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap layout"><article class="article">
<h2 id="reviewers" style="margin-top:0">For reviewers</h2><h3>You may review if</h3><ul><li>You have a genuine, first-hand experience with the business or product in the last 24 months.</li><li>You are not an employee, owner, contractor, relative or competitor of the business.</li><li>You disclose any incentive or invitation.</li></ul>
<h3>Not allowed</h3><ul><li>Fake, copied, purchased or AI-generated reviews.</li><li>Reviews written for, or on behalf of, someone else.</li><li>Hate speech, harassment, threats, sexual content or profanity aimed at individuals.</li><li>Personal data: phone numbers, home addresses, health or financial details of anyone.</li><li>Promotional content, links to competitors, or spam.</li><li>Allegations of criminal conduct presented as fact, or content that breaks the law.</li><li>Multiple reviews of the same experience.</li></ul>
<h2 id="business">For businesses</h2><ul><li>Invite all customers equally. Selectively asking only satisfied customers ("review gating") is not allowed.</li><li>Do not offer incentives conditioned on a positive review, and disclose any incentive you offer.</li><li>Do not write, buy or commission reviews of your own business or competitors.</li><li>Do not use threats, legal pressure or non-disparagement clauses to suppress reviews.</li><li>Reply publicly and respectfully. Do not reveal customers' private information.</li></ul>
<p>Breaches may lead to removal of affected reviews, a public notice on the business profile and loss of plan benefits. Payment never buys removal.</p>
<h2 id="moderation">Moderation and appeals</h2><p>Every review is checked before publication. If we reject or remove a review, we tell the reviewer why. Reviewers and businesses can appeal once by contacting us; a different moderator decides the appeal.</p>
<h2 id="report">Report a review</h2><p>If a published review breaks these guidelines, report it below. Reports are reviewed within 5 business days.</p>
<div class="form-card"><form data-form="REPORT a review" data-ok="Report received. We'll review it within 5 business days and email you the outcome.">
<div class="row"><div class="field"><label for="rp-b">Business</label><input id="rp-b" name="business" required></div><div class="field"><label for="rp-r">Reviewer display name</label><input id="rp-r" name="reviewer" required></div></div>
<div class="field"><label for="rp-why">Reason</label><select id="rp-why" name="reason" required><option value="">Choose…</option><option>Not a genuine experience</option><option>Conflict of interest</option><option>Harassment or hate speech</option><option>Contains personal information</option><option>Spam or promotion</option><option>Illegal content</option><option>Other</option></select></div>
<div class="field"><label for="rp-d">Details</label><textarea id="rp-d" name="details" required></textarea></div>
<div class="row"><div class="field"><label for="rp-e">Your email</label><input id="rp-e" type="email" name="email" required></div><div class="field"><label for="rp-rel">You are</label><select id="rp-rel" name="reporter_type"><option>A member of the public</option><option>The business owner or representative</option><option>The reviewer</option></select></div></div>
{ctx["HP"]}<button class="btn btn-primary" type="submit">Submit report</button></form></div>
<h2 id="legal">Legal notices</h2><p>To report content you believe is unlawful or infringes your rights, use the form above or <a href="{r}contact.html?topic=Report%20a%20review">contact us</a> with the URL, the content and the legal basis for your request.</p>
</article><aside><div class="aside-stick"><div class="card toc"><h4>On this page</h4><a href="#reviewers">For reviewers</a><a href="#business">For businesses</a><a href="#moderation">Moderation &amp; appeals</a><a href="#report">Report a review</a></div></div></aside></div></section>'''

# ---------------- Legal ----------------
UPDATED = "October 30, 2026"
def legal_wrap(ctx, r, title, lead, inner):
    return ctx["page_head"](title, lead, None, r) + f'<section class="section" style="padding-top:36px"><div class="wrap narrow article"><p class="muted">Last updated: {UPDATED}</p>{inner}</div></section>'

def privacy(ctx, r):
    return legal_wrap(ctx, r, "Privacy policy", "What we collect, why, and the choices you have.", f'''
<h2>Who we are</h2><p>BusinessReviews.com ("we", "us") operates this website. Questions about privacy can be sent through our <a href="{r}contact.html?topic=Privacy%20request">contact form</a>.</p>
<h2>Information we collect</h2><ul><li><strong>Information you submit</strong> in forms: name, email, phone, company details, reviews, contest entries, applications, pledges and messages.</li><li><strong>Technical data</strong> collected automatically by our hosting provider and advertising partners, such as IP address, browser type, device and pages visited.</li><li><strong>Preferences</strong> stored in your browser (theme, cookie choice) using local storage.</li></ul>
<h2>How we use it</h2><ul><li>To publish and moderate reviews and respond to your requests.</li><li>To send you a shortlist and, only where you opt in, share your request with up to three matched providers.</li><li>To run contests, process applications and send pledge payment links.</li><li>To send the newsletter if you subscribe (unsubscribe at any time).</li><li>To keep the site secure and understand how it is used.</li></ul>
<h2>Form processing</h2><p>Form submissions are delivered to us by email through FormSubmit (formsubmit.co), which acts as a processor. We do not sell personal information.</p>
<h2>Advertising and Google AdSense</h2><p>We use Google AdSense to display ads. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this website or other websites. Google's use of advertising cookies enables it and its partners to serve ads to you based on your visits to this and/or other sites on the internet.</p><p>You may opt out of personalised advertising by visiting <a href="https://adssettings.google.com" rel="noopener" target="_blank">Google Ads Settings</a>. You can also opt out of some third-party vendors' use of cookies for personalised advertising at <a href="https://www.aboutads.info/choices/" rel="noopener" target="_blank">www.aboutads.info</a>, or in the EU at <a href="https://www.youronlinechoices.eu/" rel="noopener" target="_blank">youronlinechoices.eu</a>. Learn <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">how Google uses information from sites that use its services</a>.</p><p>Where required (including the EEA, UK and Switzerland), we ask for your consent through a Google-certified consent management platform before personalised ads are shown.</p>
<h2>Embedded content</h2><p>Videos are embedded from YouTube in privacy-enhanced mode and load only when you press play. Fonts are served by Google Fonts. These services may receive your IP address.</p>
<h2>Retention</h2><p>We keep submissions only as long as needed for the purpose collected — for example, published reviews while the profile exists, and leads for up to 24 months — unless the law requires longer.</p>
<h2>Your rights</h2><p>Depending on where you live (including under the GDPR, UK GDPR, Canada's PIPEDA and Quebec's Law 25, and U.S. state laws such as the CCPA/CPRA), you may have rights to access, correct, delete or port your data, to withdraw consent and to object to certain processing. We do not sell or share personal information for cross-context behavioural advertising except through the advertising cookies described above, which you can control. To exercise your rights, <a href="{r}contact.html?topic=Privacy%20request">contact us</a>.</p>
<h2>Children</h2><p>This site is intended for adults and is not directed to children under 16. We do not knowingly collect their data.</p>
<h2>Changes</h2><p>We will post changes on this page and update the date above.</p>''')

def terms(ctx, r):
    return legal_wrap(ctx, r, "Terms of use", "The rules for using BusinessReviews.com.", f'''
<h2>Acceptance</h2><p>By using this website you agree to these terms. If you do not agree, please do not use the site.</p>
<h2>Content you submit</h2><p>You are responsible for reviews and other content you submit. You confirm it reflects your genuine experience, is accurate to the best of your knowledge and complies with our <a href="{r}review-guidelines.html">review guidelines</a>. You keep ownership of your content and grant us a worldwide, non-exclusive, royalty-free licence to host, display, adapt (for formatting and moderation) and distribute it in connection with the service. We may decline, label or remove content at our discretion.</p>
<h2>Information only</h2><p>Guides, tools and reviews are for general information. They are not legal, financial, tax or professional advice. Calculator results are estimates. Always verify pricing, features and terms with providers before you buy.</p>
<h2>Matching and introductions</h2><p>When you request quotes, we may share your request with providers only if you opt in. We are not a party to any agreement between you and a provider and do not guarantee their services.</p>
<h2>Acceptable use</h2><p>Do not scrape, overload or attempt to disrupt the site; submit fake or manipulated reviews; impersonate others; or use the site for unlawful purposes.</p>
<h2>Intellectual property</h2><p>Site design, text, graphics and code are protected by copyright. See our <a href="{r}trademark-copyright.html">trademark &amp; copyright disclosure</a>.</p>
<h2>Third-party links</h2><p>Links to other sites are provided for convenience. We are not responsible for their content or practices.</p>
<h2>Disclaimer of warranties and limitation of liability</h2><p>The site is provided "as is". To the fullest extent permitted by law, we disclaim all warranties and are not liable for indirect or consequential losses arising from your use of the site or reliance on its content.</p>
<h2>Changes</h2><p>We may update these terms; continued use means you accept the updated terms.</p>
<h2>Contact</h2><p>Questions about these terms: <a href="{r}contact.html">contact us</a>.</p>''')

def cookies(ctx, r):
    return legal_wrap(ctx, r, "Cookie policy", "How this site uses cookies and similar technologies.", f'''
<h2>Essential storage</h2><p>We store your theme and cookie-notice choice in your browser's local storage. These are needed for the site to work as you expect.</p>
<h2>Advertising cookies</h2><p>Google AdSense and its partners may set cookies to show and measure ads, including personalised ads based on your browsing. In the EEA, UK and Switzerland these require your consent, collected through a Google-certified consent platform.</p>
<h2>Embedded media</h2><p>YouTube videos load in privacy-enhanced mode only after you press play.</p>
<h2>Your choices</h2><ul><li>Clear or block cookies in your browser settings.</li><li>Manage Google ad personalisation at <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a>.</li><li>Opt out of participating vendors at <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener">aboutads.info</a>.</li></ul>
<p>See also our <a href="{r}privacy.html">privacy policy</a>.</p>''')

def disclaimer(ctx, r):
    return legal_wrap(ctx, r, "Disclaimer &amp; disclosures", "How we make money and what that means for what you read.", f'''
<h2 id="money">How we make money</h2><ul><li><strong>Display advertising</strong> through Google AdSense. Ads are labelled and selected by Google, not by our editors.</li><li><strong>Business plans</strong> for optional tools such as widgets and review insights.</li><li><strong>Lead program</strong>: providers may pay when a buyer who opted in is introduced to them.</li><li><strong>Sponsorships</strong>, always labelled as Sponsored.</li><li><strong>Reader support</strong> through voluntary donations.</li><li><strong>Affiliate links</strong>: we do not currently use affiliate links. If we add them, the affected pages will say so.</li></ul>
<h2 id="independence">What money can't buy</h2><p>No payment can remove a review, change a rating or score, alter review order or change the conclusions of a guide.</p>
<h2 id="reviews">Reviews disclaimer</h2><p>Reviews are the opinions of individual reviewers and do not represent the views of BusinessReviews.com. We moderate reviews but cannot guarantee the accuracy of every statement.</p>
<h2 id="info">General information</h2><p>Content is for general information and is not professional advice. Vendor pricing and features change; verify with the vendor. Listing a vendor is not an endorsement.</p>
<h2 id="external">External links and videos</h2><p>We link to and embed third-party content we believe is useful. We do not control it and are not responsible for it.</p>''')

def trademark(ctx, r):
    return legal_wrap(ctx, r, "Trademark &amp; copyright disclosure", "How we use names, marks and content — ours and other people's.", f'''
<h2>Our name</h2><p>"Business reviews" is a generic, descriptive phrase meaning reviews of businesses. BusinessReviews.com uses it descriptively as the name of this website and domain. We do not claim exclusive trademark rights in the phrase "business reviews", and we do not use it to suggest any connection with another organisation.</p>
<h2>No affiliation</h2><p>BusinessReviews.com is an independent website. It is not affiliated with, endorsed by or sponsored by any other company, publication, directory, app or service that uses the words "business reviews" or similar words in its name, nor by any review platform such as Trustpilot, Yelp, G2, Capterra, the Better Business Bureau, Google or others.</p>
<h2>Third-party trademarks</h2><p>Product names, company names, logos and brands mentioned on this site are trademarks or registered trademarks of their respective owners. We use them only to identify the products and services being discussed (nominative use). Their use does not imply endorsement or any relationship with us.</p>
<h2>Copyright</h2><p>© 2026 BusinessReviews.com. The site's original text, design, graphics, code and tools are protected by copyright and may not be reproduced without permission, except for brief quotations with attribution and a link. Reviews remain the property of their authors, licensed to us for display. Embedded videos remain the property of their creators.</p>
<h2>Infringement notices</h2><p>If you believe content on this site infringes your copyright or trademark, <a href="{r}contact.html?topic=Other">contact us</a> with: identification of the work or mark, the URL of the material, your contact details, a statement of good-faith belief that the use is not authorised, and a statement that the information is accurate and that you are the owner or authorised to act for the owner. We respond promptly and remove infringing material where appropriate.</p>''')

def search(ctx, r):
    return ctx["page_head"]("Search", "Find categories, providers, guides and tools.", None, r) + f'''
<section class="section" style="padding-top:36px"><div class="wrap narrow">
<form class="search" action="{r}search.html" role="search" style="margin-bottom:24px"><label class="sr" for="q">Search</label><input id="q" name="q" type="search" placeholder="Search a business, tool or topic"><button class="btn btn-primary" type="submit">Search</button></form>
<div id="results" aria-live="polite"></div></div></section>'''

def notfound(ctx, r):
    return f'''<section class="section"><div class="wrap narrow" style="text-align:left">
<h1>This page isn't here.</h1><p class="lead">It may have moved, or the link may be mistyped. Try searching, or start from a category.</p>
<form class="search" action="search.html" role="search" style="margin:24px 0"><label class="sr" for="nfq">Search</label><input id="nfq" name="q" type="search" placeholder="Search a business, tool or topic"><button class="btn btn-primary" type="submit">Search</button></form>
<a class="btn btn-ghost" href="index.html">Go to the homepage</a> <a class="btn btn-ghost" href="categories.html">Browse categories</a></div></section>'''

PAGES = [
 {"path": "index.html", "title": "BusinessReviews.com — Honest reviews & buyer's guides for business software and services", "desc": "Read moderated reviews, vendor-neutral buyer's guides and use free tools to choose business software and service providers. Get free matched quotes.", "body": home, "priority": "1.0"},
 {"path": "categories.html", "title": "All categories", "desc": "Browse buyer's guides for CRM, accounting, payroll, payments, insurance, loans, agencies, IT services and more.", "body": categories, "active": "categories.html", "priority": "0.9"},
 {"path": "guides/index.html", "title": "Buyer's guides", "desc": "Vendor-neutral guides for choosing business software and providers, spotting fake reviews and managing your reputation.", "body": guides_index, "active": "guides/index.html", "priority": "0.9"},
 {"path": "get-quotes.html", "title": "Get free quotes — matched business software & providers", "desc": "Answer four quick questions and get a free, vendor-neutral shortlist of software or service providers matched to your needs.", "body": get_quotes, "priority": "0.9", "keywords": "lead quote match shortlist"},
 {"path": "write-review.html", "title": "Write a review", "desc": "Share an honest, first-hand review of a business, software product or service provider.", "body": write_review, "priority": "0.8", "keywords": "review submit rate"},
 {"path": "for-business.html", "title": "For business owners — claim your free profile", "desc": "Claim your free business profile, reply to reviews, invite customers and get matched buyer requests.", "body": for_business, "active": "for-business.html", "priority": "0.8", "keywords": "claim profile owner widgets"},
 {"path": "advertise.html", "title": "Advertise, sponsor or partner", "desc": "Labelled sponsorships, newsletter placements, contest sponsorships and partnership opportunities on BusinessReviews.com.", "body": advertise, "priority": "0.6", "keywords": "advertising sponsorship partnership domain"},
 {"path": "contests.html", "title": "Contests & prizes", "desc": "Win prizes for the most helpful reviews, small-business stories and tool tips. Official rules inside.", "body": contests, "active": "contests.html", "priority": "0.6", "keywords": "contest prize giveaway"},
 {"path": "careers.html", "title": "Careers", "desc": "Remote roles for review moderators, writers, SEO, video creators, community and partnerships.", "body": careers, "priority": "0.5", "keywords": "jobs hiring"},
 {"path": "donate.html", "title": "Support independent reviews", "desc": "Help fund moderation, independent guides, hiring and contest prizes on BusinessReviews.com.", "body": donate, "active": "donate.html", "priority": "0.5", "keywords": "donate support"},
 {"path": "tools.html", "title": "Free tools — vendor scorecard, TCO calculator, review response writer", "desc": "Free calculators and writers: weighted vendor scorecard, SaaS total cost of ownership, review response writer, review request builder and rating goal calculator.", "body": tools, "active": "tools.html", "scripts": ("tools.js",), "priority": "0.8", "keywords": "calculator scorecard compare response template"},
 {"path": "videos.html", "title": "Video library", "desc": "Short videos on choosing business software, managing reviews, responding to criticism and spotting fake reviews.", "body": videos, "active": "videos.html", "priority": "0.6", "keywords": "youtube video"},
 {"path": "awards.html", "title": "Community Choice Awards", "desc": "Annual awards decided only by verified reviews. Eligibility, methodology and nominations.", "body": awards, "priority": "0.5", "keywords": "awards badge"},
 {"path": "about.html", "title": "About us", "desc": "Why BusinessReviews.com exists, what we do and how we make money.", "body": about, "priority": "0.5"},
 {"path": "contact.html", "title": "Contact us", "desc": "Contact BusinessReviews.com for questions, corrections, partnerships or to report a review.", "body": contact, "priority": "0.5"},
 {"path": "editorial-policy.html", "title": "Methodology & editorial policy", "desc": "How we write guides, moderate and label reviews, calculate the BR Score and separate advertising from content.", "body": editorial, "priority": "0.5", "keywords": "methodology score transparency"},
 {"path": "review-guidelines.html", "title": "Review guidelines", "desc": "Rules for reviewers and businesses, moderation and appeals, and how to report a review.", "body": guidelines, "priority": "0.5", "keywords": "rules policy report"},
 {"path": "privacy.html", "title": "Privacy policy", "desc": "How BusinessReviews.com collects, uses and protects personal information, including Google AdSense cookies.", "body": privacy, "priority": "0.3"},
 {"path": "terms.html", "title": "Terms of use", "desc": "Terms governing use of BusinessReviews.com and content you submit.", "body": terms, "priority": "0.3"},
 {"path": "cookies.html", "title": "Cookie policy", "desc": "How BusinessReviews.com uses cookies and local storage.", "body": cookies, "priority": "0.3"},
 {"path": "disclaimer.html", "title": "Disclaimer & disclosures", "desc": "How BusinessReviews.com makes money and what money can't buy.", "body": disclaimer, "priority": "0.3"},
 {"path": "trademark-copyright.html", "title": "Trademark & copyright disclosure", "desc": "Trademark and copyright disclosure for BusinessReviews.com, including non-affiliation and third-party marks.", "body": trademark, "priority": "0.3"},
 {"path": "search.html", "title": "Search", "desc": "Search BusinessReviews.com.", "body": search, "noindex": True},
 {"path": "404.html", "title": "Page not found", "desc": "The page you're looking for isn't here.", "body": notfound, "noindex": True},
]
