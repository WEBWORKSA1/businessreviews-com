# Category data for BusinessReviews.com. Add a dict to CATEGORIES to create a new category page.
# Provider lists are factual names of commonly evaluated vendors — no ratings are invented;
# star ratings appear only once genuine, moderated reviews exist.

CATEGORIES = [
 {
  "slug": "crm-software", "name": "CRM Software", "icon": "🤝", "group": "Software",
  "blurb": "Track leads, deals and customer conversations in one place.",
  "intro": [
   "Customer relationship management (CRM) software is the system of record for everyone your business sells to: contacts, companies, deals, emails, calls and the next step on each. Done well, it replaces scattered spreadsheets and inboxes with a single pipeline everyone trusts.",
   "Most small teams outgrow a spreadsheet at around three salespeople or a few hundred active leads. The right CRM is the one your team actually updates, so adoption and ease of data entry matter more than the length of the feature list."
  ],
  "features": ["Visual deal pipeline with custom stages", "Email and calendar sync (Gmail, Outlook)", "Contact and company records with activity timeline", "Task reminders and automated follow-ups", "Reporting on win rate, cycle length and forecast", "Integrations with your marketing, billing and support tools"],
  "pricing": ["Free tiers with limited users or features are common for very small teams", "Per-user, per-month subscriptions are the norm; annual billing usually discounts 10–20%", "Advanced automation, forecasting and AI features are often reserved for higher tiers", "Watch for paid add-ons: extra contacts, marketing seats, onboarding packages"],
  "questions": ["How long does a typical team our size take to go live?", "Which features in the demo are only on a higher tier?", "Can we export all data, including activity history, if we leave?", "What does the price become at renewal, and is there a cap on increases?", "Which integrations are native versus built through a third-party connector?"],
  "red_flags": ["Contracts that auto-renew with long notice periods", "Contact-based pricing that jumps sharply as your list grows", "No sandbox or trial with your own data", "Mandatory paid onboarding for basic setup"],
  "providers": [("HubSpot CRM","https://www.hubspot.com/products/crm"),("Salesforce Sales Cloud","https://www.salesforce.com/sales/"),("Zoho CRM","https://www.zoho.com/crm/"),("Pipedrive","https://www.pipedrive.com/"),("Freshsales","https://www.freshworks.com/crm/sales/"),("monday CRM","https://monday.com/crm")],
  "faqs": [("What is the difference between a CRM and a marketing automation platform?","A CRM manages sales relationships and deals one-to-one; marketing automation manages campaigns one-to-many. Many vendors bundle both, but you can buy them separately and integrate."),("How much should a small business budget for CRM?","Plan for licences per user plus 20–50% of first-year licence cost for setup, data import and training. The total-cost calculator on our Tools page models this."),("Do I need a CRM if I only have one salesperson?","If you lose track of follow-ups or rely on memory, yes — a free tier is usually enough to start.")]
 },
 {
  "slug": "accounting-software", "name": "Accounting & Invoicing", "icon": "📒", "group": "Software",
  "blurb": "Bookkeeping, invoices, expenses and tax-ready reports.",
  "intro": [
   "Accounting software records every transaction, reconciles your bank feeds and produces the profit-and-loss, balance-sheet and tax reports your accountant needs. For most small businesses it is the second system they buy after a payment tool.",
   "The decision usually comes down to three things: whether your accountant already works in the product, how well it handles your local tax rules, and whether it scales into inventory, multi-currency or payroll when you need them."
  ],
  "features": ["Automatic bank and card feeds with reconciliation", "Branded invoices, quotes and online payment links", "Expense capture from receipts", "Sales-tax / VAT / GST tracking for your jurisdiction", "Accountant or bookkeeper access", "Standard financial statements and cash-flow reports"],
  "pricing": ["Monthly subscription tiers, often limited by number of users or invoices", "Payroll, inventory and multi-currency are frequently paid add-ons", "Payment processing fees apply on top when customers pay invoices online", "Introductory discounts are common; check the price after the promo period"],
  "questions": ["Is the product fully supported for tax rules in our country and province or state?", "What happens to historical data if we downgrade or cancel?", "How many bank accounts and users are included?", "Can our accountant access it at no extra cost?", "Which payment processors integrate natively?"],
  "red_flags": ["Promo pricing without a clear post-promo rate", "No audit trail on edits and deletions", "Weak local tax support outside the vendor's home market", "Export limited to PDFs rather than raw data"],
  "providers": [("QuickBooks Online","https://quickbooks.intuit.com/"),("Xero","https://www.xero.com/"),("FreshBooks","https://www.freshbooks.com/"),("Wave","https://www.waveapps.com/"),("Zoho Books","https://www.zoho.com/books/"),("Sage Accounting","https://www.sage.com/")],
  "faqs": [("Can I switch accounting software mid-year?","Yes, but it is cleanest at a fiscal year-end or quarter-end. Bring opening balances and open invoices across, and keep read-only access to the old system."),("Do I still need an accountant?","Software automates bookkeeping; an accountant handles tax strategy, filings and judgement calls. Most businesses use both.")]
 },
 {
  "slug": "payroll-hr-software", "name": "Payroll & HR", "icon": "🧾", "group": "Software",
  "blurb": "Pay people correctly, file taxes and manage employee records.",
  "intro": [
   "Payroll and HR platforms calculate wages, withhold and remit payroll taxes, issue year-end tax forms and store employee records. Mistakes here carry penalties, so accuracy and compliance support outweigh almost every other factor.",
   "Small employers often start with payroll only and add benefits administration, time tracking, onboarding and performance tools as headcount grows. If you hire internationally, compare employer-of-record (EOR) providers separately."
  ],
  "features": ["Automated payroll runs and direct deposit", "Payroll tax filing and year-end forms", "Employee self-service portal", "Time-off tracking and timesheets", "Onboarding documents and e-signature", "Benefits and retirement plan administration"],
  "pricing": ["Typically a monthly base fee plus a per-employee fee", "Tax filing in additional states or provinces may cost extra", "HR, benefits and time tracking are often bundled into higher tiers", "Off-cycle payroll runs and amendments can carry fees"],
  "questions": ["Does the provider guarantee tax filing accuracy and pay penalties caused by its errors?", "Which jurisdictions do you file in automatically?", "How are contractors handled versus employees?", "What is the cut-off time for direct deposit?", "Can we export full payroll history if we leave?"],
  "red_flags": ["No tax-accuracy guarantee", "Per-run fees not disclosed upfront", "Support only by email during payroll week", "Limited multi-state or multi-province filing"],
  "providers": [("Gusto","https://gusto.com/"),("ADP","https://www.adp.com/"),("Paychex","https://www.paychex.com/"),("Rippling","https://www.rippling.com/"),("BambooHR","https://www.bamboohr.com/"),("Deel","https://www.deel.com/")],
  "faqs": [("When should a business move from manual payroll to software?","At the first hire. Payroll tax deadlines and calculations become error-prone quickly, and penalties usually exceed the software cost."),("What is an employer of record?","An EOR legally employs workers on your behalf in countries where you have no entity, handling local payroll and compliance.")]
 },
 {
  "slug": "project-management-software", "name": "Project Management", "icon": "🗂️", "group": "Software",
  "blurb": "Plan work, assign tasks and hit deadlines together.",
  "intro": [
   "Project management software turns plans into tasks with owners, due dates and status. Teams use it to see who is doing what, spot blocked work early and stop managing projects through long email threads.",
   "The market splits roughly into simple boards for small teams, flexible work-management platforms for cross-functional work, and specialised tools for software development. Match the tool to how your team already works rather than forcing a new methodology on day one."
  ],
  "features": ["Boards, lists, timelines and calendar views", "Task dependencies and milestones", "Workload and capacity views", "Templates for repeat projects", "Automations for status changes and reminders", "Guest access for clients and contractors"],
  "pricing": ["Generous free plans for small teams are common", "Per-seat pricing, often sold in seat bundles rather than single seats", "Timeline/Gantt, automations and reporting typically require paid tiers", "Guest and viewer seats may be free or discounted"],
  "questions": ["Are seats sold individually or in fixed bundles?", "How many automation runs are included per month?", "Can clients view progress without a paid seat?", "How are permissions handled for confidential projects?", "Does it integrate with our chat and file storage tools?"],
  "red_flags": ["Seat bundles that force you to pay for unused seats", "Automation limits that throttle you mid-month", "No offline or mobile editing", "Hard-to-export task history"],
  "providers": [("Asana","https://asana.com/"),("Trello","https://trello.com/"),("monday.com","https://monday.com/"),("ClickUp","https://clickup.com/"),("Jira","https://www.atlassian.com/software/jira"),("Basecamp","https://basecamp.com/")],
  "faqs": [("Kanban or Gantt — which do I need?","Kanban boards suit continuous work with changing priorities; Gantt timelines suit projects with fixed dates and dependencies. Most modern tools offer both views on the same data.")]
 },
 {
  "slug": "email-marketing-software", "name": "Email Marketing", "icon": "✉️", "group": "Software",
  "blurb": "Newsletters, automations and campaigns that land in the inbox.",
  "intro": [
   "Email marketing platforms manage your subscriber list, design and send campaigns, and automate sequences such as welcome series and abandoned-cart reminders. Email remains one of the highest-return channels because you own the list.",
   "Deliverability — whether your mail reaches the inbox — matters more than template galleries. Look at authentication support (SPF, DKIM, DMARC), list hygiene tools and how the vendor handles compliance with anti-spam laws such as CAN-SPAM and Canada's CASL."
  ],
  "features": ["Drag-and-drop editor and responsive templates", "Automation workflows and triggers", "Segmentation and personalisation", "A/B testing of subject lines and content", "Signup forms and landing pages", "Deliverability and authentication tools"],
  "pricing": ["Pricing usually scales with contacts or monthly sends", "Free plans often cap contacts and add vendor branding", "Automation, A/B testing and advanced segmentation tend to sit in higher tiers", "Dedicated IP addresses and SMS are typically extra"],
  "questions": ["Are unsubscribed contacts counted in our billable total?", "What is your average inbox placement and how do you monitor it?", "Can we import double-opt-in records with consent timestamps?", "How do you handle CASL and GDPR consent records?", "What happens to automations if we exceed our plan?"],
  "red_flags": ["Billing for unsubscribed or bounced contacts", "No DKIM or custom sending domain support", "Weak consent and audit records", "Steep price jumps at contact thresholds"],
  "providers": [("Mailchimp","https://mailchimp.com/"),("Klaviyo","https://www.klaviyo.com/"),("Brevo","https://www.brevo.com/"),("Constant Contact","https://www.constantcontact.com/"),("ActiveCampaign","https://www.activecampaign.com/"),("Kit","https://kit.com/")],
  "faqs": [("How often should a small business email its list?","Consistency beats volume: weekly or every two weeks is common. Watch unsubscribe and spam-complaint rates as your guide.")]
 },
 {
  "slug": "website-builders-hosting", "name": "Website Builders & Hosting", "icon": "🌐", "group": "Software",
  "blurb": "Launch and host a fast, secure business website.",
  "intro": [
   "Website builders bundle design templates, hosting and maintenance into one subscription, while web hosts give you server space to run software such as WordPress yourself. Builders trade flexibility for convenience; hosting trades convenience for control.",
   "Prioritise speed, uptime, security updates and how easily you can move away later. Your domain name should always be registered in your own account, never only through a designer or agency."
  ],
  "features": ["Templates and visual editing", "Free SSL certificates", "Uptime monitoring and backups", "Built-in SEO controls and sitemaps", "Forms, bookings and basic e-commerce", "Custom domain and professional email"],
  "pricing": ["Builders: monthly plans, with e-commerce features on higher tiers", "Hosting: low introductory rates on multi-year terms that renew higher", "Domains, email and premium themes or plugins are often separate", "Managed WordPress hosting costs more but includes updates and caching"],
  "questions": ["What is the renewal price after the introductory term?", "Can we export the site if we leave?", "Where are backups stored and how quickly can you restore?", "Is staging included for testing changes?", "What uptime guarantee is offered, and what is the remedy?"],
  "red_flags": ["Introductory pricing that triples at renewal", "Domain registered in the vendor's or agency's name", "No site export", "Upsell-heavy checkout with pre-ticked add-ons"],
  "providers": [("Wix","https://www.wix.com/"),("Squarespace","https://www.squarespace.com/"),("WordPress.com","https://wordpress.com/"),("Hostinger","https://www.hostinger.com/"),("SiteGround","https://www.siteground.com/"),("Bluehost","https://www.bluehost.com/")],
  "faqs": [("Should I use a website builder or WordPress?","Choose a builder if you want minimal maintenance and a standard site. Choose WordPress if you need deep customisation, many plugins or full ownership of the code.")]
 },
 {
  "slug": "ecommerce-platforms", "name": "E-commerce Platforms", "icon": "🛒", "group": "Software",
  "blurb": "Sell online with storefronts, checkout and inventory.",
  "intro": [
   "E-commerce platforms provide your online store, product catalogue, checkout, payments and order management. The platform you choose shapes your conversion rate, fees and how easily you can sell across marketplaces and social channels.",
   "Compare total cost per order — subscription plus payment processing plus transaction fees plus apps — rather than headline plan prices. Apps and themes can add more cost than the plan itself."
  ],
  "features": ["Hosted checkout with multiple payment methods", "Inventory and variant management", "Shipping rates and label printing", "Tax calculation", "Multichannel selling (marketplaces, social, POS)", "App ecosystem and APIs"],
  "pricing": ["Monthly plans plus payment processing fees", "Extra transaction fees may apply if you use a third-party payment gateway", "Paid themes and apps add recurring costs", "Enterprise plans often move to revenue-based pricing"],
  "questions": ["What transaction fee applies if we use our own payment processor?", "Which features we need require paid apps?", "How are taxes calculated for cross-border orders?", "Can we migrate products, customers and order history out?", "What checkout customisation is allowed on our plan?"],
  "red_flags": ["Hidden transaction fees on external gateways", "Core features only available via paid apps", "Limited export of customer data", "Checkout you cannot customise or test"],
  "providers": [("Shopify","https://www.shopify.com/"),("BigCommerce","https://www.bigcommerce.com/"),("WooCommerce","https://woocommerce.com/"),("Squarespace Commerce","https://www.squarespace.com/ecommerce-website"),("Wix eCommerce","https://www.wix.com/ecommerce/website"),("Ecwid","https://www.ecwid.com/")],
  "faqs": [("Hosted platform or self-hosted store?","Hosted platforms handle security, updates and PCI scope for you. Self-hosted (such as WooCommerce) gives more control but you manage hosting, updates and security.")]
 },
 {
  "slug": "payment-processing", "name": "Payment Processing", "icon": "💳", "group": "Finance",
  "blurb": "Accept cards and digital wallets online and in person.",
  "intro": [
   "Payment processors let you accept credit and debit cards, digital wallets and bank payments. Fees are the largest ongoing cost for many small businesses, so understanding pricing models is worth an hour of your time.",
   "Flat-rate processors are simple and predictable; interchange-plus pricing is more transparent and often cheaper at higher volume. Contract terms, payout speed and how disputes are handled matter as much as the rate."
  ],
  "features": ["Online checkout and payment links", "In-person card readers and POS", "Digital wallets (Apple Pay, Google Pay)", "Recurring billing and invoicing", "Fraud screening and chargeback tools", "Fast or instant payouts"],
  "pricing": ["Flat rate: one percentage plus a fixed fee per transaction", "Interchange-plus: card network cost plus a disclosed markup", "Tiered pricing bundles rates into qualified/non-qualified buckets — the least transparent model", "Watch for monthly minimums, PCI fees, chargeback fees and early-termination fees"],
  "questions": ["Is pricing flat-rate, interchange-plus or tiered?", "Is there a contract term or early-termination fee?", "What are the chargeback and refund fees?", "When are funds paid out, and can reserves be held?", "Do we own our card-vault data if we switch?"],
  "red_flags": ["Tiered pricing with vague rate tables", "Equipment leases you cannot cancel", "Liquidated-damages clauses", "No clear process for account holds or reserves"],
  "providers": [("Stripe","https://stripe.com/"),("Square","https://squareup.com/"),("PayPal Business","https://www.paypal.com/business"),("Adyen","https://www.adyen.com/"),("Helcim","https://www.helcim.com/"),("Clover","https://www.clover.com/")],
  "faqs": [("What is interchange?","Interchange is the fee set by card networks and paid to the card-issuing bank. It varies by card type and transaction method and forms the base of every processing fee.")]
 },
 {
  "slug": "business-phone-voip", "name": "Business Phone & VoIP", "icon": "☎️", "group": "Software",
  "blurb": "Cloud phone systems, call routing and team messaging.",
  "intro": [
   "Cloud phone (VoIP) systems give your team business numbers that work on desk phones, laptops and mobiles, with call routing, voicemail-to-email and analytics. They have largely replaced on-premise phone systems for small and mid-sized businesses.",
   "Call quality depends on your internet connection as much as on the vendor. Ask for a trial, test from your real locations and confirm number porting timelines before you sign."
  ],
  "features": ["Auto-attendant and call routing", "Mobile and desktop apps", "Call recording and voicemail transcription", "Business SMS", "CRM and helpdesk integrations", "Call analytics and queues"],
  "pricing": ["Per-user, per-month plans; call recording and analytics often in higher tiers", "International calling and toll-free minutes may be metered", "Hardware desk phones are bought or leased separately", "Regulatory fees and taxes are added on top of the plan price"],
  "questions": ["How long does porting our existing numbers take?", "What taxes and regulatory fees will appear on the bill?", "Is business SMS registered for compliance (e.g., A2P 10DLC in the US)?", "What is the uptime guarantee?", "Are there contract minimums on users?"],
  "red_flags": ["Long contracts with user minimums", "Number porting fees or delays", "Surprise regulatory surcharges", "No trial on your own network"],
  "providers": [("RingCentral","https://www.ringcentral.com/"),("Nextiva","https://www.nextiva.com/"),("Dialpad","https://www.dialpad.com/"),("8x8","https://www.8x8.com/"),("Zoom Phone","https://www.zoom.com/en/products/voip-phone/"),("Vonage Business","https://www.vonage.com/unified-communications/")],
  "faqs": [("Can I keep my current business number?","In most cases yes, through number porting. Your new provider submits the request; keep the old service active until the port completes.")]
 },
 {
  "slug": "cybersecurity-software", "name": "Cybersecurity", "icon": "🛡️", "group": "Software",
  "blurb": "Protect devices, passwords, email and data.",
  "intro": [
   "Small businesses are frequent targets of phishing, ransomware and account takeover because their defences are often thinner than larger firms'. A basic stack — password manager, multi-factor authentication, endpoint protection, email filtering and backups — removes most common risk.",
   "Buy for coverage and manageability, not fear. A tool nobody configures does not protect anyone; prefer products with sensible defaults and central management, or a managed service provider who runs them for you."
  ],
  "features": ["Password management with sharing controls", "Multi-factor authentication", "Endpoint detection and response (EDR)", "Email filtering and phishing protection", "Backup and recovery", "Security awareness training"],
  "pricing": ["Per-user or per-device subscriptions", "Managed detection and response (MDR) adds a service fee", "Business password managers usually price per user per month", "Training platforms price per learner"],
  "questions": ["What is the time to detect and respond, and who responds after hours?", "Can we manage all devices from one console?", "How are backups protected from ransomware?", "What compliance reports can you provide?", "What happens to our data if we cancel?"],
  "red_flags": ["Fear-based sales without a clear threat model", "No independent testing results", "Backups stored with the same credentials as production", "No incident-response support included"],
  "providers": [("1Password Business","https://1password.com/business"),("Bitwarden","https://bitwarden.com/"),("CrowdStrike Falcon","https://www.crowdstrike.com/"),("Malwarebytes for Teams","https://www.malwarebytes.com/business"),("Proofpoint","https://www.proofpoint.com/"),("Cloudflare Zero Trust","https://www.cloudflare.com/zero-trust/")],
  "faqs": [("What is the single most effective security step for a small business?","Turn on multi-factor authentication for email, banking and admin accounts. It blocks the large majority of automated account-takeover attempts.")]
 },
 {
  "slug": "business-insurance", "name": "Business Insurance", "icon": "☂️", "group": "Finance",
  "blurb": "General liability, professional, property and cyber cover.",
  "intro": [
   "Business insurance protects you from the costs of lawsuits, property damage, injuries and data breaches. Common policies include general liability, professional liability (errors and omissions), commercial property, workers' compensation, commercial auto and cyber liability.",
   "Many small businesses buy a business owner's policy (BOP), which bundles general liability and property cover at a lower price. Compare exclusions and limits carefully — the cheapest quote is often the narrowest cover."
  ],
  "features": ["Online quotes and instant certificates of insurance", "Bundled business owner's policies", "Claims filed online or by phone", "Add-on cyber and professional liability", "Monthly or annual payment options", "Licensed agent support"],
  "pricing": ["Premiums depend on industry risk, revenue, payroll, location and claims history", "Higher deductibles lower premiums", "Bundling policies usually reduces total cost", "Annual payment is often cheaper than monthly"],
  "questions": ["What exactly is excluded from this policy?", "Is cover on an occurrence or claims-made basis?", "What are the per-claim and aggregate limits?", "How quickly can you issue a certificate of insurance for a client?", "Who handles claims — the carrier or a third party?"],
  "red_flags": ["Vague exclusions or definitions", "Pressure to bind before you see the full policy wording", "Unlicensed sellers", "Limits lower than your client contracts require"],
  "providers": [("Hiscox","https://www.hiscox.com/"),("NEXT Insurance","https://www.nextinsurance.com/"),("The Hartford","https://www.thehartford.com/"),("Travelers","https://www.travelers.com/business-insurance"),("Chubb","https://www.chubb.com/"),("biBERK","https://www.biberk.com/")],
  "faqs": [("Is general liability insurance legally required?","Usually not by law, but leases, client contracts and licensing bodies often require it. Workers' compensation is mandatory in most places once you have employees.")]
 },
 {
  "slug": "business-loans-financing", "name": "Business Loans & Financing", "icon": "🏦", "group": "Finance",
  "blurb": "Term loans, lines of credit, invoice financing and more.",
  "intro": [
   "Business financing ranges from bank term loans and government-backed loans to online lines of credit, invoice factoring and merchant cash advances. The cost of capital varies enormously between products, so compare the annual percentage rate (APR) and total repayment, not just the monthly payment.",
   "Faster approval usually means higher cost. If you can wait a few weeks, bank and government-guaranteed programmes are typically cheapest; online lenders trade higher rates for speed and lighter paperwork."
  ],
  "features": ["Online application with soft credit check", "Lines of credit you draw as needed", "Invoice financing against receivables", "Equipment financing", "Government-backed loan programmes", "Transparent APR and repayment schedules"],
  "pricing": ["Interest rate or factor rate plus origination fees", "Merchant cash advances use factor rates that can equal very high APRs", "Prepayment penalties or fees on some products", "Personal guarantees and collateral are common"],
  "questions": ["What is the APR and total repayment amount, including all fees?", "Is there a prepayment penalty?", "Is a personal guarantee or lien required?", "Does checking my rate affect my credit score?", "How often are payments taken — daily, weekly or monthly?"],
  "red_flags": ["Quoting a factor rate without an APR", "Upfront fees before approval", "Daily repayments that strain cash flow", "Pressure to sign the same day"],
  "providers": [("Bluevine","https://www.bluevine.com/"),("OnDeck","https://www.ondeck.com/"),("Funding Circle","https://www.fundingcircle.com/"),("Fundbox","https://fundbox.com/"),("Lendio","https://www.lendio.com/"),("U.S. SBA loan programmes","https://www.sba.gov/funding-programs/loans")],
  "faqs": [("What credit score do I need for a business loan?","It depends on the product. Banks and government-backed loans typically expect stronger credit and time in business; online lenders accept lower scores at higher cost.")]
 },
 {
  "slug": "marketing-agencies", "name": "Marketing Agencies", "icon": "📣", "group": "Services",
  "blurb": "SEO, paid ads, social media and content partners.",
  "intro": [
   "Marketing agencies run campaigns you lack the time or skills to manage in-house: search engine optimisation, paid search and social ads, content, email and analytics. A good agency becomes an extension of your team; a poor one burns budget on activity rather than results.",
   "Hire for proof of results in businesses like yours, clear reporting and contract terms that let you leave. Insist that ad accounts, analytics and content are owned by your business, not the agency."
  ],
  "features": ["Discovery and strategy before execution", "Transparent monthly reporting tied to revenue or leads", "Named account manager", "Your ownership of ad accounts and assets", "Case studies with verifiable references", "Clear scope of work and deliverables"],
  "pricing": ["Monthly retainers for ongoing work", "Project fees for audits, launches or websites", "Percentage of ad spend for paid media management", "Performance-based pricing is rare and usually combined with a base fee"],
  "questions": ["Who exactly will work on our account day to day?", "Can we speak to two current clients in our industry?", "Do we own the ad accounts, analytics and creative?", "What will you report monthly, and what counts as success?", "What is the notice period to end the contract?"],
  "red_flags": ["Guaranteed first-page rankings", "Ad accounts created under the agency's ownership", "Long lock-in contracts with no performance exit", "Reports full of vanity metrics only"],
  "providers": [],
  "faqs": [("How much should a small business spend with a marketing agency?","Budgets vary by goal and market. Start with a defined project or 3-month pilot with measurable targets before committing to a long retainer.")]
 },
 {
  "slug": "web-design-agencies", "name": "Web Design & Development", "icon": "🧩", "group": "Services",
  "blurb": "Studios and freelancers who design and build websites and apps.",
  "intro": [
   "Web design and development partners plan, design and build websites, online stores and web applications. Quality varies widely, from template resellers to studios with strong engineering and UX teams.",
   "Define your goals, must-have pages and integrations before requesting quotes so proposals are comparable. Make sure you will own the domain, hosting account, design files and code at the end."
  ],
  "features": ["Discovery and sitemap planning", "UX and visual design with revision rounds", "Responsive, accessible build", "Content migration and SEO redirects", "Testing across devices and browsers", "Training and post-launch support"],
  "pricing": ["Fixed-price projects for defined scopes", "Hourly or day rates for open-ended work", "Monthly care plans for hosting, updates and small changes", "Milestone payments tied to deliverables"],
  "questions": ["Who owns the code, design files and accounts at the end?", "How many revision rounds are included?", "How will you handle SEO redirects from our current site?", "What accessibility standard will the build meet?", "What does post-launch support cost?"],
  "red_flags": ["Domain or hosting registered in the agency's name", "No written scope or milestones", "Proprietary CMS that locks you in", "100% payment upfront"],
  "providers": [],
  "faqs": [("How long does a small business website take to build?","A brochure site often takes 4–8 weeks; e-commerce or custom functionality can take several months. Content readiness is the most common cause of delay.")]
 },
 {
  "slug": "it-managed-services", "name": "IT & Managed Services", "icon": "🖥️", "group": "Services",
  "blurb": "Outsourced IT support, cloud, security and helpdesk.",
  "intro": [
   "Managed service providers (MSPs) run your IT: devices, networks, cloud accounts, backups, security and helpdesk support, usually for a predictable monthly fee. For businesses without an in-house IT team, an MSP is often cheaper than one full-time hire.",
   "Compare service-level agreements (response and resolution times), what is included versus billed hourly, and the provider's security practices — an MSP holds the keys to your systems."
  ],
  "features": ["Helpdesk with defined response times", "Device management and patching", "Backup and disaster recovery", "Security monitoring", "Microsoft 365 / Google Workspace administration", "Strategic IT planning and budgeting"],
  "pricing": ["Per-user or per-device monthly fees", "Projects (migrations, hardware rollouts) quoted separately", "After-hours and on-site visits may carry extra charges", "Some MSPs bundle security tools; others resell them separately"],
  "questions": ["What are your guaranteed response and resolution times?", "What is included in the monthly fee and what is billed hourly?", "How do you secure your own access to our systems?", "Who holds admin credentials if we part ways?", "Do you carry cyber and professional liability insurance?"],
  "red_flags": ["No written SLA", "Admin credentials held only by the provider", "No offboarding or handover process", "Unclear billing for after-hours work"],
  "providers": [],
  "faqs": [("When should a business hire an MSP?","When IT issues regularly interrupt work, when no one owns security and backups, or when you are about to grow past around ten staff.")]
 },
 {
  "slug": "accountants-bookkeepers", "name": "Accountants & Bookkeepers", "icon": "🧮", "group": "Services",
  "blurb": "Bookkeeping, tax preparation and financial advice.",
  "intro": [
   "Bookkeepers keep your records accurate month to month; accountants handle tax returns, planning and financial statements; fractional CFOs help with forecasting and funding. Many firms offer all three in packages for small businesses.",
   "Look for relevant credentials in your country (for example CPA designations), experience with businesses of your size and industry, and fluency in the accounting software you use."
  ],
  "features": ["Monthly bookkeeping and reconciliation", "Year-end financial statements", "Business and personal tax filings", "Payroll and sales-tax filings", "Cash-flow forecasting", "Audit and tax-notice support"],
  "pricing": ["Monthly packages based on transaction volume", "Fixed fees for annual returns", "Hourly rates for advisory work", "Catch-up bookkeeping quoted per month of backlog"],
  "questions": ["What credentials and licences do you hold?", "How many clients like us do you serve?", "Which accounting software do you work in?", "What is the turnaround time on monthly books?", "Who handles notices from tax authorities?"],
  "red_flags": ["No engagement letter", "Promises of guaranteed refunds", "Unclear scope of monthly package", "Slow or no response during tax season"],
  "providers": [],
  "faqs": [("Do I need a bookkeeper and an accountant?","Small businesses often hire one firm that does both. Very small businesses may do their own bookkeeping in software and use an accountant only for tax filings.")]
 },
]
