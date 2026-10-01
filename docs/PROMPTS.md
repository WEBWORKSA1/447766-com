# 447766.com — Phase-wise Build Prompts

Copy-paste these prompts in order into any capable AI coding assistant to rebuild, extend or fork this site.
`{{OWNER_EMAIL}}` = the single owner inbox. **Never write it in plain text anywhere in the site.** Store it only as obfuscated, split, reversed base64 in `assets/js/config.js`, and decode it at runtime.

---

## Phase 0 — Strategy lock
> You are a senior product strategist. The domain is 447766.com, read as "44 77 66". In Chinese, 44 = 死死 (death), 77 = 七七 (Qixi / rising / change), 66 = 六六大顺 (smooth success). Position the brand as **"447766 · The Lucky Number Lab — every number has two stories, East and West."** The brand story is "Turn your 4s into 6s". Define: target personas (Western angel-number searchers, Chinese diaspora, couples picking wedding dates, people choosing phone or plate numbers, domain investors). Then define the core loop: search number → dual reading + luck score → share / lead → related pages. Also the revenue stack (AdSense, YouTube, lead gen, sponsorship, donations, contests, affiliate) and the KPIs: pages/session, lead CVR, RPM, email list growth. Output a one-page brief.

## Phase 1 — Foundation, design system & global chrome
> Build a static, dependency-free website (HTML5 + CSS + vanilla JS) that runs on the free GitHub Pages plan. Use relative URLs only, so it works at `user.github.io/447766-com/` and later at the custom domain. Generate the pages with a Python build script (`build.py`) from shared header and footer templates, so that hundreds of pages stay consistent.
> Design tokens: brand teal #447766, lucky red #C8102E for CTAs, imperial gold #D4A017 for scores, rice-paper #FAF7F2 background, ink #16181A. Full dark mode via `prefers-color-scheme` plus a toggle. Fonts: Inter for UI and Noto Serif SC for hanzi.
> Global chrome on EVERY page:
> (1) A slim top bar reading "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership", linked to https://web.works/contact.
> (2) A sticky header with logo "447766", nav (Numbers · Tools · Zodiac · Domains · Videos · Guides · Contests · Support) and a CTA button "Free Lucky Report".
> (3) Mobile hamburger menu.
> (4) A footer with sitemap columns, newsletter form, trademark/copyright notice, and links to Privacy, Terms, Disclaimer, Contest Rules.
> (5) A cookie/consent banner.
> Target Lighthouse ≥ 95, CLS < 0.05 (reserve ad slot heights) and WCAG AA.

## Phase 2 — Number engine (the product)
> Write `assets/js/numerology.js`. It needs:
> (a) a digit dictionary 0–9 with hanzi, Mandarin pinyin, Jyutping, homophones, meaning and a luck weight (8 = +4, 9 = +3, 6 = +3, 2 = +2, 1 = +1, 3 = +1, 0 = 0, 5 = 0, 7 = 0, 4 = −4);
> (b) a combo dictionary (168, 518, 520, 521, 1314, 5201314, 3344, 666, 888, 88, 99, 250, 38, 14, 24, 74, 94, 514, 748, 886, 55, 555, 233, 9420, 7456, 1688, 6688, 28, 18, 58, 54, 13, 77, 49, 1111, 447766…) with meaning and sentiment;
> (c) a luck scoring function from 0 to 100. It weights the last digit ×1.5, adds repeated-lucky-run bonuses, penalises 4 and the death combos, and applies combo overrides;
> (d) Western numerology: digit-sum reduction keeping master numbers 11, 22, 33, plus angel-number themes per digit, with extra emphasis when digits repeat;
> (e) Pythagorean name numerology;
> (f) the Chinese zodiac from birth year, with lucky and unlucky numbers per animal;
> (g) a lucky-number generator with modes "Chinese-lucky", "avoid-4", "random" and "birthday-seeded".
> The functions must be pure and unit-testable.

## Phase 3 — Core pages
> Build: Home (hero with animated 4-4-7-7-6-6 → 死死·七七·顺顺 story, lookup input, example chips, digit cards 0–9, tools grid, latest guides, video strip, lead CTA, sponsor strip, donation CTA). Then:
> - `/lookup/`: full result card with score gauge, digit table, Chinese and Western readings, share button, related numbers, inline lead form.
> - `/tools/`: lucky phone, plate, address and domain checker; birthday lucky numbers + zodiac; name numerology; lucky number generator; "find a luckier version" suggester.
> - `/numbers/`: dictionary hub with ranges and search.
> - `/zodiac/`: 12-animal table + year finder.
> - `/videos/`: lite YouTube facades.
> - `/guides/`: article index and long-form articles.

## Phase 4 — Programmatic SEO
> Generate `/number/{n}/` for 0–99, the repeating families (111–999, 1111–9999), the curated combos and 447766. Page order:
> 1. H1 "{n} Meaning in Chinese, Numerology & Angel Numbers";
> 2. a quick-answer box (verdict, score, hanzi, pinyin, one-line meaning);
> 3. a digit-by-digit table;
> 4. the Chinese cultural reading (with the combo story if known);
> 5. the Western reduction;
> 6. angel-number meaning for Love / Career / Spiritual;
> 7. best uses (phone, plate, wedding, price, domain);
> 8. a lead CTA;
> 9. an FAQ with FAQPage JSON-LD;
> 10. related numbers (repeating family, ±1, digit pages);
> 11. byline + "Updated" date.
>
> Add BreadcrumbList and Article schema, canonical tags, OG/Twitter cards, `sitemap.xml`, `robots.txt` and range hubs. Never put ads inside the tool or result card.

## Phase 5 — Lead generation engine
> Build `/get-report/` as a dedicated, distraction-free landing page (no nav ads). Its form is a two-step progressive form. Step 1: first name + email + "number you care about". Step 2 (optional): birthday dropdowns, WhatsApp/WeChat, interest (phone number, plate, wedding date, business name, domain, consult). Add consent checkboxes.
> Also build three secondary lead forms:
> - Lucky Domain Appraisal (domain, buy/sell, budget);
> - Vanity Number Request (country, phone or plate, digits wanted, budget);
> - Expert Consult (topic, preferred contact).
>
> Submit all forms over AJAX to FormSubmit (`formsubmit.co/ajax/{email}`). Build the email at runtime from the obfuscated config, and include a honeypot, `_subject` tags per form, a success state and a mailto fallback built at runtime. Add an exit-intent / 50%-scroll sticky CTA bar with a frequency cap in localStorage. Track conversions with `dataLayer` events.

## Phase 6 — Monetisation
> AdSense: `config.js` holds `ADSENSE_CLIENT` and slot IDs. When it is empty, each slot shows an "Advertise here" house ad linking to `/advertise/`. Placements: below the answer box, in-content after every 2nd H2 (max 3), sticky desktop sidebar, multiplex before the footer. No ads on `/get-report/`, `/support/` or form success states. Add `ads.txt`.
> YouTube: a lite-embed component on number pages and `/videos/`, plus a channel subscribe CTA.
> Sponsorship: `/advertise/` with a media-kit outline, slot catalogue (featured lucky domains, "tool presented by", newsletter, contest prize) and an inquiry form.

## Phase 7 — Community: donations, contests, hiring
> `/support/`: lucky preset amounts ($1.68, $6.66, $8.88, $18.88, custom), a "lucky wish" message, a goal progress bar from config, use-of-funds breakdown (operations, promotions/marketing, hiring talent, contest prizes) and payment buttons (PayPal donate URL built at runtime + configurable Ko-fi / Buy Me a Coffee / Stripe / GitHub Sponsors).
> `/contests/`: current challenge, prize, how to enter, bonus entries for sharing/referral, skill-testing question, winners archive.
> `/contest-rules/`: official rules (no purchase necessary, eligibility, Québec clause, odds, draw method, privacy).
> `/careers/`: open roles (writer, zh translator, Shorts editor, SEO, community, sponsorship sales, frontend dev) and an application form.

## Phase 8 — Trust, legal, compliance
> `/about/` (mission, methodology, editorial standards, corrections), `/privacy/` (forms, cookies, AdSense/YouTube third parties, GDPR/CCPA/Law 25 Québec), `/terms/`, `/disclaimer/` (entertainment-only readings; trademark & copyright disclosure: "447766" is used as a descriptive numeric domain name, with no claim to the number itself; third-party marks belong to their owners; YouTube videos are embedded via the official player and remain the property of their creators), `/contact/` (forms only, no visible email), `404.html`.

## Phase 9 — Deploy on GitHub Pages (free)
> Push to `github.com/WEBWORKSA1/447766-com`, branch `main`. Add a `.nojekyll` file. Publish from the `gh-pages` branch (or Settings → Pages → Deploy from branch → main / root). Custom domain: add a `CNAME` file containing `447766.com`. At the registrar, set apex A records to 185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153, and `www` CNAME → `webworksa1.github.io`. Then enable "Enforce HTTPS".

## Phase 10 — Growth & expansion
> Weekly: 3 new guides, 7 YouTube Shorts (one number each), and 1 contest post. Monthly: expand programmatic pages to all of 0–9999 (noindex the thin ones), add a 中文 version (`/zh/`), add daily lucky number emails (Mailchimp or Brevo free tier), and add a Pinterest share-card generator (canvas → PNG). Quarterly: sell lead packages, onboard 3 sponsors and review RPM and conversion rate per page type.
