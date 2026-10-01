# 447766.com — The Lucky Number Lab

**Every number has two stories — East and West. Decode yours.**
A static site about number culture: Chinese number meanings (Mandarin and Cantonese), luck scores, Western numerology and angel numbers, lucky-number tools, a numeric-domain hub and programmatic number pages. It makes money from AdSense, YouTube, lead generation, sponsorships, donations and contests.

- **Live (GitHub Pages):** https://webworksa1.github.io/447766-com/
- **Custom domain:** https://447766.com (needs a DNS change, see below)
- **Research and business case:** [`docs/RESEARCH.md`](docs/RESEARCH.md)
- **Phase-wise build prompts:** [`docs/PROMPTS.md`](docs/PROMPTS.md)

## Stack
Plain HTML, CSS and vanilla JS. No frameworks and no server, so it runs on the free GitHub Pages plan.

- `src/build.py` generates every page from shared templates.
- `src/content.py` holds the page copy, guides, videos and job roles.
- `assets/js/numerology.js` is the number engine. The browser and the build share it.
- `assets/js/config.js` holds AdSense, donation, contest and social settings. Edit it live; no rebuild needed.
- GitHub Pages' built-in Jekyll renders the pages from shared layouts: `_layouts/page.html` and `_layouts/number.html`, with data in `_data/`. Each number page is a 4-line stub that the layout fills from `_data/n.json`. No Actions workflow is needed.

```bash
node src/gen-data.js            # recompute number data (add numbers to EXTRA for new pages)
JEKYLL=1 python3 src/build.py   # regenerate page bodies, _layouts/page.html, sitemap.xml, num-index.js
python3 src/jekyll.py           # regenerate _layouts/number.html, _data/*.json and the number stubs
python3 src/make_og.py          # optional: regenerate assets/img/og.png
python3 src/build.py            # alternative: fully static HTML output (no Jekyll needed)
```

## Pages
Home · Lookup · Tools (phone/plate/address/domain checker, zodiac + life path, generator, name numerology) · Numbers A–Z + 150 programmatic `/number/{n}/` pages · Zodiac · Domains (appraisal lead form) · Videos · 7 Guides · Contests + Official Rules · Support (donations) · Advertise · Careers · Free Lucky Report (two-step lead funnel + vanity-number requests) · About · Contact · Privacy · Terms · Disclaimer & Trademark · 404.

## Publishing (GitHub Pages, free plan)
GitHub Pages is enabled and publishes from the **`gh-pages`** branch, which GitHub builds with Jekyll automatically.
- To publish changes: push them to `gh-pages`. The simpler option is **Settings → Pages → Source: Deploy from branch → `main` / root**; after that, every push to `main` goes live.
- `main` and `gh-pages` currently hold the same site files.

## Go-live checklist
1. **Form activation (once).** All forms post to FormSubmit, which forwards to the owner inbox. The inbox address is stored only in obfuscated form in `config.js` and never appears in the page markup. The first submission sends an activation email to the owner inbox; click **Activate**. After that, you can optionally replace the address in the endpoint with the random alias FormSubmit gives you.
2. **PayPal.** The Support page builds a PayPal donate link at runtime from the owner inbox. That inbox must be a PayPal account. You can also add Ko-fi, Buy Me a Coffee, Stripe or GitHub Sponsors URLs in `config.js`.
3. **AdSense.** Apply with the custom domain. Then set `adsenseClient` and `adSlots` in `config.js` and put the real line in `ads.txt`. Until then, the ad slots show house ads for your own sponsorship offer.
4. **Contest.** Edit `contest` in `config.js` (prize, dates, question) before you promote it.
5. **Analytics.** Optionally set `ga4` in `config.js`. It loads only after the visitor accepts cookies.
6. **Social share image.** Upload `assets/img/og.png` (1200×630). Run `python3 src/make_og.py` to generate it.

## Custom domain (447766.com) on GitHub Pages
1. Repo **Settings → Pages → Custom domain**: enter `447766.com`. This creates the `CNAME` file.
2. At your registrar, add DNS records:
   - `A @ 185.199.108.153`, `A @ 185.199.109.153`, `A @ 185.199.110.153`, `A @ 185.199.111.153`
   - `CNAME www webworksa1.github.io`
3. Once the domain is verified, tick **Enforce HTTPS**.

Canonical URLs, `sitemap.xml` and `robots.txt` already point to `https://447766.com/`.

## Trademark & copyright
"447766" is used only as a numeric domain name and descriptive identifier. No rights to the number sequence are claimed. Third-party marks belong to their owners. Embedded videos remain the property of their creators. See `/disclaimer/`. Original content, code and design © 447766.com.

Partnership, domain, sponsorship or advertising inquiries: https://web.works/contact
