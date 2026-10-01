#!/usr/bin/env python3
"""447766.com static site generator.
Run:  node src/gen-data.js && python3 src/build.py
Generates every HTML page from shared templates with relative URLs (works on GitHub Pages
project URLs and on the custom domain)."""
import json, os, html, datetime, hashlib, re
from content import PAGES, GUIDES, VIDEOS, ROLES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_URL = "https://447766.com/"
PARTNER = "https://web.works/contact"
TODAY = datetime.date.today().isoformat()
NUMS = json.load(open(os.path.join(ROOT, "src", "numbers.json"), encoding="utf-8"))
E = html.escape

NAV = [("numbers/", "Numbers"), ("tools/", "Tools"), ("zodiac/", "Zodiac"), ("domains/", "Domains"),
       ("videos/", "Videos"), ("guides/", "Guides"), ("contests/", "Contests"), ("support/", "Support")]
SITEMAP = []


JEKYLL = os.environ.get("JEKYLL") == "1"
SENT = "@@B@@"


def rel(depth):
    if depth < 0:
        return SENT
    return "./" if depth == 0 else "../" * depth


def head(title, desc, path, depth, schema=None, noads=False, ogtype="website"):
    b = rel(depth)
    canon = SITE_URL + path
    sch = ""
    for s in (schema or []):
        sch += '<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + "</script>\n"
    SITEMAP.append(path)
    return f"""<!doctype html>
<html lang="en" data-base="{b}"{' data-noads' if noads else ''}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#447766">
<meta property="og:type" content="{ogtype}"><meta property="og:site_name" content="447766 · The Lucky Number Lab">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE_URL}assets/img/og.png"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{b}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{b}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Serif+SC:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{b}assets/css/style.css">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
{sch}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar">Contact, if you are interested in this <a href="{PARTNER}" target="_blank" rel="noopener">website / domain name / Sponsorship / Advertisement / Partnership</a></div>
"""


def header(depth, active=""):
    b = rel(depth)
    items = "".join(
        f'<li><a href="{b}{u}"{" aria-current=page" if active == u else ""}>{n}</a></li>' for u, n in NAV)
    return f"""<header class="site-header"><div class="wrap nav">
<a class="logo" href="{b}" aria-label="447766 home"><span class="mark"><i>4</i><i>4</i><i>7</i><i>7</i><i>6</i><i>6</i></span><span>447766<small>The Lucky Number Lab</small></span></a>
<ul class="menu" id="menu">{items}<li class="m-only"><a href="{b}get-report/">Free Lucky Report</a></li></ul>
<button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button>
<a class="btn btn-red btn-sm nav-cta" href="{b}get-report/">Free Lucky Report</a>
<button class="icon-btn burger" aria-label="Menu" aria-controls="menu" aria-expanded="false">☰</button>
</div></header>
<main id="main">
"""


def footer(depth, sticky=True):
    b = rel(depth)
    st = f"""<div class="sticky-cta" role="complementary"><p>🎁 Get your free personal lucky-number report.</p><a class="btn btn-red btn-sm" href="{b}get-report/">Get it free</a><button class="x" aria-label="Close">×</button></div>""" if sticky else ""
    return f"""</main>
<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="logo" href="{b}" style="color:#fff"><span class="mark"><i>4</i><i>4</i><i>7</i><i>7</i><i>6</i><i>6</i></span><span>447766<small style="color:#93a09a">The Lucky Number Lab</small></span></a>
<p style="margin-top:14px;font-size:.92rem">Every number has two stories — East and West. Decode yours. <span class="hz">死死 · 七七 · 顺顺</span> — turn your 4s into 6s.</p>
<form class="form" data-form="newsletter" data-subject="Newsletter signup" data-success="You're in! Watch for your first lucky number.">
<label for="nl-email" style="color:#fff">Daily lucky number, free</label>
<div style="display:flex;gap:8px"><input id="nl-email" type="email" name="email" required placeholder="you@email.com" autocomplete="email"><button class="btn btn-gold btn-sm" type="submit">Join</button></div>
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off"><span class="micro" style="color:#93a09a">No spam. Unsubscribe anytime.</span></form></div>
<div><h4>Explore</h4><ul><li><a href="{b}lookup/">Number lookup</a></li><li><a href="{b}numbers/">Numbers A–Z</a></li><li><a href="{b}tools/">Lucky tools</a></li><li><a href="{b}zodiac/">Chinese zodiac</a></li><li><a href="{b}guides/">Guides</a></li><li><a href="{b}videos/">Videos</a></li></ul></div>
<div><h4>Grow with us</h4><ul><li><a href="{b}get-report/">Free lucky report</a></li><li><a href="{b}domains/#appraisal">Domain appraisal</a></li><li><a href="{b}advertise/">Advertise</a></li><li><a href="{PARTNER}" target="_blank" rel="noopener">Partnership / buy this domain</a></li><li><a href="{b}careers/">Careers</a></li></ul></div>
<div><h4>Community</h4><ul><li><a href="{b}contests/">Contests &amp; prizes</a></li><li><a href="{b}contest-rules/">Contest rules</a></li><li><a href="{b}support/">Support 447766</a></li><li><a href="{b}contact/">Contact</a></li></ul></div>
<div><h4>Legal</h4><ul><li><a href="{b}about/">About &amp; methodology</a></li><li><a href="{b}privacy/">Privacy</a></li><li><a href="{b}terms/">Terms</a></li><li><a href="{b}disclaimer/">Disclaimer &amp; trademark</a></li><li><a href="{b}sitemap.xml">Sitemap</a></li></ul></div>
</div>
<div class="legal">
<p><b>Trademark &amp; copyright disclosure:</b> 447766.com is an independent publication. "447766" is used solely as a numeric domain name and descriptive identifier; no exclusive rights to the number sequence are claimed and none are infringed. All third-party names, trademarks and logos (including Google, AdSense, YouTube, PayPal, Ko-fi, Buy Me a Coffee, Stripe and GitHub) belong to their respective owners; their mention does not imply endorsement. Embedded videos are played through the official YouTube player and remain the property of their creators. Number readings are traditional cultural associations provided for entertainment and education only. Original text, tools and design © <span data-year>2026</span> 447766.com. All rights reserved. <a href="{b}disclaimer/">Full disclosure</a>.</p>
</div></div></footer>
{st}
<div class="cookie" role="dialog" aria-label="Cookie notice"><p style="margin:0 0 10px">We use cookies for analytics and ads (Google AdSense) to keep our tools free. See our <a href="{b}privacy/">privacy policy</a>.</p><button class="btn btn-brand btn-sm" data-consent="yes">Accept</button> <button class="btn btn-ghost btn-sm" data-consent="no">Essential only</button></div>
<script src="{b}assets/js/config.js"></script>
<script src="{b}assets/js/numerology.js"></script>
<script src="{b}assets/js/num-index.js"></script>
<script src="{b}assets/js/main.js" defer></script>
</body></html>
"""


def ad(slot="inContent", cls=""):
    return f'<div class="ad {cls}" data-slot="{slot}" aria-label="Advertisement"></div>'


def crumbs(depth, trail):
    b = rel(depth)
    parts = [f'<a href="{b}">Home</a>']
    for name, url in trail:
        parts.append(f'<a href="{b}{url}">{E(name)}</a>' if url else E(name))
    return '<nav class="crumbs" aria-label="Breadcrumb">' + " › ".join(parts) + "</nav>"


def bc_schema(trail):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL}]
    for i, (name, url) in enumerate(trail):
        items.append({"@type": "ListItem", "position": i + 2, "name": name, "item": SITE_URL + (url or "")})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def sidebar(depth):
    b = rel(depth)
    return f"""<aside class="sidebar">
<div class="card"><h3>Check any number</h3><form data-lookup="go" class="form"><input inputmode="numeric" placeholder="e.g. 168 or your phone" aria-label="Number"><button class="btn btn-red btn-block" type="submit">Reveal meaning</button></form></div>
<div class="card" style="background:var(--gold-soft)"><h3>🎁 Free lucky report</h3><p class="micro">Your personal lucky numbers, zodiac numbers to avoid, and the best dates — emailed free.</p><a class="btn btn-red btn-block" href="{b}get-report/">Get my report</a></div>
{ad("sidebar", "side")}
</aside>"""


def write(path, content):
    full = os.path.join(ROOT, path, "index.html") if not path.endswith(".html") else os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)


def yt(vid, title):
    return f'<div><div class="yt" data-id="{vid}" data-title="{E(title)}"></div><p class="vid-title">{E(title)}</p></div>'


def honeypot():
    return '<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'


def consent():
    return '<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my request and accept the privacy policy. Unsubscribe anytime.</label>'


# ---------------------------------------------------------------- number pages
def luck_tag(w):
    if w > 0:
        return '<span class="tag t-lucky">+ lucky</span>'
    if w < 0:
        return '<span class="tag t-unlucky">− unlucky</span>'
    return '<span class="tag t-neutral">○ neutral</span>'


def related(n):
    out = []
    ds = sorted(set(n))
    for d in ds:
        for k in (d, d * 2, d * 3, d * 4):
            if k in NUMS and k != n and k not in out:
                out.append(k)
    if n.isdigit() and len(n) <= 4:
        for k in (str(int(n) - 1), str(int(n) + 1)):
            if k in NUMS and k not in out and k != n:
                out.append(k)
    for c in NUMS[n]["combos"]:
        if c["n"] in NUMS and c["n"] not in out:
            out.append(c["n"])
    for k in ("8", "168", "520", "666", "888", "1314", "447766"):
        if k != n and k not in out:
            out.append(k)
    return out[:18]


def pick_video(n):
    if "4" in n:
        return VIDEOS[1] if int(hashlib.md5(n.encode()).hexdigest(), 16) % 2 else VIDEOS[4]
    return VIDEOS[[0, 2, 3, 7][int(hashlib.md5(n.encode()).hexdigest(), 16) % 4]]


def number_page(n):
    a = NUMS[n]
    depth = 2
    b = rel(depth)
    path = f"number/{n}/"
    v = a["verdict"]
    title = f"{n} Meaning in Chinese, Numerology & Angel Numbers — Lucky or Not? | 447766"
    one = a["chinese"].split(". ")[0].rstrip(".") + "."
    desc = f"Is {n} lucky? {v['label']} ({a['score']}/100). {n} in Chinese is {a['hanzi']} ({a['pinyin']}). {one}"[:300]
    faq = [
        (f"Is {n} a lucky number in Chinese culture?", f"{v['label']} — {n} scores {a['score']}/100 on our Chinese luck scale. {a['chinese']}"),
        (f"What does {n} mean in Chinese?", f"{n} is written {a['digitsHz']} and read “{a['pinyin']}” in Mandarin. " + " ".join(f"{d['d']} ({d['hz']}) sounds like {d['sounds']}." for d in a['digits'][:4])),
        (f"What is the angel number {n} meaning?", a["angel"]["summary"] + " " + a["angel"]["love"]),
        (f"Is {n} good for a phone number, licence plate or address?", "Best uses: " + "; ".join(a["uses"]) + "."),
        (f"What does {n} reduce to in numerology?", f"Adding the digits gives {' → '.join(a['reduce']['steps'])}. The root number is {a['reduce']['root']}."),
        (f"How do you say {n} in Mandarin and Cantonese?", f"Mandarin: {a['pinyin']}. Cantonese (Jyutping): {a['jyutping']}."),
    ]
    schema = [
        {"@context": "https://schema.org", "@type": "Article", "headline": f"{n} Meaning in Chinese, Numerology & Angel Numbers",
         "dateModified": TODAY, "datePublished": "2026-10-01", "author": {"@type": "Organization", "name": "447766 Editorial"},
         "publisher": {"@type": "Organization", "name": "447766.com"}, "mainEntityOfPage": SITE_URL + path},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in faq]},
        bc_schema([("Numbers", "numbers/"), (n, path)]),
    ]
    digits_rows = "".join(
        f"<tr><td><b>{d['d']}</b></td><td class='hz'>{d['hz']}</td><td>{d['py']}</td><td>{d['jp']}</td><td>{E(d['sounds'])}</td><td>{luck_tag(d['w'])}</td></tr>"
        for d in a["digits"])
    combos = ""
    if a["combos"]:
        combos = "<h3>Hidden combinations inside " + n + "</h3><ul>" + "".join(
            f"<li><a href='{b}number/{c['n']}/'><b>{c['n']}</b></a> <span class='hz'>{c['hz']}</span> — {E(c['m'])}</li>" if c['n'] in NUMS else f"<li><b>{c['n']}</b> <span class='hz'>{c['hz']}</span> — {E(c['m'])}</li>"
            for c in a["combos"]) + "</ul>"
    sugg = ""
    if a["suggestions"]:
        sugg = "<h3>Luckier alternatives to " + n + "</h3><div class='chips'>" + "".join(
            f"<a class='chip good' href='{b}lookup/?n={s['n']}'>{s['n']} · {s['score']}</a>" for s in a["suggestions"]) + "</div>"
    rel_links = "".join(
        f"<a class='{'g' if NUMS[k]['score'] >= 65 else ('b' if NUMS[k]['score'] < 45 else 'n')}' href='{b}number/{k}/'>{k}</a>" for k in related(n))
    vid = pick_video(n)
    gc = "var(--good)" if a["score"] >= 65 else ("var(--gold)" if a["score"] >= 45 else "var(--bad)")
    known = f"<p class='notice'><b>Known meaning:</b> <span class='hz'>{a['known']['hz']}</span> — {E(a['known']['m'])}</p>" if a.get("known") else ""
    body = f"""
<div class="wrap page-hero">{crumbs(depth, [("Numbers", "numbers/"), (n, None)])}
<h1>{n} Meaning in Chinese, Numerology &amp; Angel Numbers</h1>
<div class="byline"><span>By 447766 Editorial</span>·<span>Updated {TODAY}</span>·<a href="{b}about/#methodology">How we score numbers</a></div></div>
<div class="wrap content"><article class="prose" style="max-width:none">
<div class="result"><div class="result-top"><div class="gauge" style="--v:{a['score']};--c:{gc}"><div><div><b>{a['score']}</b><small>luck score</small></div></div></div>
<div><div class="result-num">{n}</div><div class="result-hz">{E(a['hanzi'])} · {E(a['pinyin'])}</div>
<p style="margin:10px 0 0"><span class="tag t-{v['key']}">{v['label']} · {v['hz']}</span> <span class="micro">Cantonese: {E(a['jyutping'])}</span></p></div></div>
<div class="result-body"><p class="quick"><b>Quick answer:</b> {E(a['chinese'])}</p>
<div class="share"><a class="btn btn-red btn-sm" href="{b}get-report/?n={n}">Email me my lucky report</a><button class="btn btn-ghost btn-sm" data-share="{n}">Share</button></div></div></div>
{ad("top")}
{known}
<h2>Digit-by-digit breakdown of {n}</h2>
<div class="table-wrap"><table><thead><tr><th>Digit</th><th>Hanzi</th><th>Mandarin</th><th>Cantonese</th><th>Sounds like</th><th>Luck</th></tr></thead><tbody>{digits_rows}</tbody></table></div>
<h2>What {n} means in Chinese culture</h2>
<p>{E(a['chinese'])}</p>
{combos}
<h2>{n} in Western numerology</h2>
<p>Adding the digits: <b>{' → '.join(a['reduce']['steps'])}</b>. {E(a['angel']['summary'])}</p>
{ad("inContent")}
<h2>Angel number {n}: love, career and spirit</h2>
<ul><li>{E(a['angel']['love'])}</li><li>{E(a['angel']['career'])}</li><li>{E(a['angel']['spirit'])}</li></ul>
<p class="notice"><b>East vs West:</b> {('Western angel-number readers treat 4 as stability and protection, while Chinese tradition hears 死 (death). Same digits, opposite stories — which one you follow depends on your audience.' if '4' in n else ('In both traditions ' + n + ' leans positive.' if a['score'] >= 65 else 'Chinese and Western readings weigh this number differently, so consider who will see it.'))}</p>
<h2>Best uses for {n}</h2>
<ul>{''.join('<li>' + E(u) + '</li>' for u in a['uses'])}</ul>
{sugg}
<div class="lead-box" style="margin:28px 0"><h3>Want a number that works for <em>you</em>?</h3><p>Get a free personal report: your lucky numbers by birthday and zodiac, numbers to avoid, and how to pick a phone, plate or wedding date.</p><a class="btn btn-gold" href="{b}get-report/?n={n}">Get my free report →</a></div>
<h2>Watch: Chinese lucky numbers explained</h2>
{yt(vid[0], vid[1])}
<h2>FAQ about {n}</h2>
<div class="faq">{''.join(f'<details><summary>{E(q)}</summary><p>{E(ans)}</p></details>' for q, ans in faq)}</div>
{ad("inContent")}
<h2>Related numbers</h2>
<div class="num-grid">{rel_links}</div>
<p class="micro" style="margin-top:18px">Readings reflect traditional Chinese homophones and Western numerology conventions. They're for entertainment and education, not financial, legal or medical advice. Dialects differ — <a href="{b}contact/">suggest a correction</a>.</p>
{ad("multiplex")}
</article>{sidebar(depth)}</div>"""
    write(path, head(title, desc, path, depth, schema, ogtype="article") + header(depth, "numbers/") + body + footer(depth))


# ---------------------------------------------------------------- generic pages
def simple(path, title, desc, inner, active="", noads=False, trail=None, schema=None, side=False, sticky=True, bare=False):
    depth = path.count("/")
    b = rel(depth)
    inner = inner.replace("{b}", b).replace("{PARTNER}", PARTNER)
    tr = trail if trail is not None else [(title.split(" | ")[0].split(" — ")[0], None)]
    sch = (schema or []) + ([] if bare else [bc_schema([(n, u or path) for n, u in tr])])
    top = '' if bare else f'<div class="wrap page-hero">{crumbs(depth, tr)}</div>'
    if side:
        main = f'{top}<div class="wrap content"><div class="prose" style="max-width:none">{inner}</div>{sidebar(depth)}</div>'
    else:
        main = top + inner
    if JEKYLL:
        SITEMAP.append(path)
        assert "{{" not in main and "{%" not in main, path
        fm = {"layout": "page", "title": title, "desc": desc, "canon": path, "b": b, "active": active,
              "noads": noads, "nosticky": not (sticky and not noads)}
        js = "".join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + "</script>" for x in sch)
        front = "---\n" + "".join(f"{k}: {json.dumps(v, ensure_ascii=False)}\n" for k, v in fm.items()) + "---\n"
        write(path, front + js + "\n" + main + "\n")
        return
    write(path, head(title, desc, path, depth, sch, noads) + header(depth, active) + main + footer(depth, sticky and not noads))


def page_layout():
    """Jekyll layout equivalent of head()+header()+footer() driven by front matter."""
    h = head("@@TITLE@@", "@@DESC@@", "@@PATH@@", -1)
    SITEMAP.pop()
    h = h.replace('data-base="@@B@@">', 'data-base="@@B@@"{% if page.noads %} data-noads{% endif %}>')
    h = h.replace("@@TITLE@@", "{{ page.title | escape }}").replace("@@DESC@@", "{{ page.desc | escape }}").replace("@@PATH@@", "{{ page.canon }}")
    hd = header(-1)
    for u, _ in NAV:
        hd = hd.replace(f'href="{SENT}{u}">', f'href="{SENT}{u}"{{% if page.active == "{u}" %}} aria-current=page{{% endif %}}>')
    ft = footer(-1, True)
    i = ft.index('<div class="sticky-cta"'); j = ft.index("</div>", ft.index('class="x"')) + len("</div>")
    ft = ft[:i] + "{% unless page.nosticky %}" + ft[i:j] + "{% endunless %}" + ft[j:]
    pre = '{%- assign B = page.b -%}{%- if page.abs -%}{%- assign B = site.baseurl | append: "/" -%}{%- endif -%}\n'
    out = pre + (h + hd + "{{ content }}" + ft).replace(SENT, "{{ B }}")
    os.makedirs(os.path.join(ROOT, "_layouts"), exist_ok=True)
    open(os.path.join(ROOT, "_layouts/page.html"), "w", encoding="utf-8").write(out)


def build():
    # number pages (in Jekyll mode they are rendered by GitHub Pages from _layouts/number.html — see jekyll.py)
    if JEKYLL:
        page_layout()
        for n in NUMS:
            SITEMAP.append(f"number/{n}/")
    else:
        for n in NUMS:
            number_page(n)
    # num index js
    open(os.path.join(ROOT, "assets/js/num-index.js"), "w").write("window.NUM_INDEX=" + json.dumps(list(NUMS.keys())) + ";")
    # content pages
    for p in PAGES:
        simple(**p)
    # guides
    for g in GUIDES:
        path = f"guides/{g['slug']}/"
        sch = [{"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"],
                "datePublished": "2026-10-01", "dateModified": TODAY, "author": {"@type": "Organization", "name": "447766 Editorial"},
                "publisher": {"@type": "Organization", "name": "447766.com"}}]
        inner = f'<h1>{E(g["title"])}</h1><div class="byline"><span>By 447766 Editorial</span>·<span>{g["read"]} min read</span>·<span>Updated {TODAY}</span></div>' + g["body"] + \
            '<div class="lead-box" style="margin:28px 0"><h3>Make your numbers work for you</h3><p>Free personal lucky-number report — birthday, zodiac, numbers to avoid.</p><a class="btn btn-gold" href="{b}get-report/">Get my free report →</a></div>'
        simple(path, g["title"] + " | 447766", g["desc"], inner, "guides/", trail=[("Guides", "guides/"), (g["short"], None)], schema=sch, side=True)
    # numbers hub
    def cls(k):
        s = NUMS[k]["score"]; return "g" if s >= 65 else ("b" if s < 45 else "n")
    def grid(keys):
        return '<div class="num-grid">' + "".join(f"<a class='{cls(k)}' href='{{b}}number/{k}/'>{k}</a>" for k in keys) + "</div>"
    two = [str(i) for i in range(100)]
    rep = [k for k in NUMS if len(set(k)) == 1 and len(k) >= 3]
    combos = [k for k in NUMS if k not in two and k not in rep]
    top_lucky = sorted(NUMS, key=lambda k: -NUMS[k]["score"])[:12]
    top_bad = sorted(NUMS, key=lambda k: NUMS[k]["score"])[:12]
    inner = f"""<div class="wrap"><h1>Chinese Number Meanings, A–Z</h1><p class="lead">{len(NUMS)} numbers decoded with Chinese homophones, Cantonese readings, Western numerology and angel-number meanings. Green = lucky, gold = neutral, red = unlucky.</p>
<div class="search" style="margin:18px 0"><input id="num-filter" inputmode="numeric" placeholder="Filter numbers…" aria-label="Filter numbers"><a class="btn btn-red" href="{{b}}lookup/">Look up any number</a></div>
{ad("top")}
<h2>The ten digits</h2><div class="grid g5">""" + "".join(
        f"<a class='card digit-card' href='{{b}}number/{d}/'><div class='big'>{d}</div><div class='hz'>{NUMS[d]['digitsHz']}</div><span class='tag t-{NUMS[d]['verdict']['key']}'>{NUMS[d]['verdict']['label']}</span></a>" for d in "0123456789") + \
        f"""</div><h2>Luckiest numbers</h2>{grid(top_lucky)}<h2>Most avoided numbers</h2>{grid(top_bad)}
<h2>Famous combinations &amp; slang codes</h2>{grid(combos)}{ad("inContent")}<h2>Repeating numbers (angel numbers)</h2>{grid(rep)}<h2>0–99</h2>{grid(two)}
<p class="notice" style="margin-top:24px">Can't find your number? <a href="{{b}}lookup/">Our lookup tool decodes any number</a> — phone numbers, plates, dates and domains.</p></div>"""
    simple("numbers/", "Chinese Number Meanings A–Z: Lucky & Unlucky Numbers | 447766", f"{len(NUMS)} numbers decoded: Chinese meaning, pinyin, Cantonese, luck score, numerology and angel number meanings.", inner, "numbers/", trail=[("Numbers", None)])
    # guides index
    cards = "".join(f'<a class="card" href="{{b}}guides/{g["slug"]}/"><span class="tag t-neutral">{g["tag"]}</span><h3 style="margin-top:10px">{E(g["title"])}</h3><p class="micro">{E(g["desc"])}</p></a>' for g in GUIDES)
    simple("guides/", "Guides: Chinese Lucky Numbers, Tetraphobia, Numeric Domains | 447766", "In-depth guides to Chinese number culture, lucky numbers by occasion, number slang, numeric domains and angel numbers.",
           f'<div class="wrap"><h1>Guides</h1><p class="lead">Deep dives into the culture, money and psychology of numbers.</p>{ad("top")}<div class="grid g3">{cards}</div></div>', "guides/", trail=[("Guides", None)])
    if JEKYLL:  # 404 is served at any path -> links resolved from site.baseurl
        body404 = ('<div class="wrap page-hero" style="text-align:center;padding:80px 16px"><div class="code" style="justify-content:center"><div class="dg d4">4<span>死</span></div><div class="dg d4">0<span>零</span></div><div class="dg d4">4<span>死</span></div></div>'
                   '<h1>Unlucky! Page not found.</h1><p class="lead" style="margin:0 auto 20px">404 is about as unlucky as numbers get in Chinese. Let us turn it into a 6.</p>'
                   '<a class="btn btn-red" href="{{ site.baseurl }}/">Go home</a> <a class="btn btn-ghost" href="{{ site.baseurl }}/lookup/">Look up a number</a></div>')
        fm = {"layout": "page", "title": "Page not found | 447766", "desc": "This number doesn't exist… yet.", "canon": "404.html", "b": "/", "abs": True,
              "active": "", "noads": True, "nosticky": True, "permalink": "/404.html"}
        open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write("---\n" + "".join(f"{k}: {json.dumps(v, ensure_ascii=False)}\n" for k, v in fm.items()) + "---\n" + body404 + "\n")
        SITEMAP.append("404.html")
    # 404 (served at any path on GitHub Pages -> absolute URLs)
    GH = "https://webworksa1.github.io/447766-com/"
    page404 = head("Page not found | 447766", "This number doesn't exist… yet.", "404.html", 0, noads=True) + header(0) + \
        '<div class="wrap page-hero" style="text-align:center;padding:80px 16px"><div class="code" style="justify-content:center"><div class="dg d4">4<span>死</span></div><div class="dg d4">0<span>零</span></div><div class="dg d4">4<span>死</span></div></div><h1>Unlucky! Page not found.</h1><p class="lead" style="margin:0 auto 20px">404 is about as unlucky as numbers get in Chinese. Let us turn it into a 6.</p><a class="btn btn-red" href="./">Go home</a> <a class="btn btn-ghost" href="./lookup/">Look up a number</a></div>' + footer(0, False)
    page404 = page404.replace('href="./', 'href="' + GH).replace('src="./', 'src="' + GH).replace('data-base="./"', 'data-base="' + GH + '"')
    if not JEKYLL:
        write("404.html", page404)
    # sitemap
    if JEKYLL:
        sm = ('---\nlayout: null\n---\n<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
              '{% for p in site.pages %}{% if p.name == "index.html" %}<url><loc>https://447766.com{{ p.url }}</loc><lastmod>{{ site.time | date: "%Y-%m-%d" }}</lastmod></url>\n{% endif %}{% endfor %}</urlset>\n')
        open(os.path.join(ROOT, "sitemap.xml"), "w").write(sm)
    else:
        urls = "".join(f"<url><loc>{SITE_URL}{p}</loc><lastmod>{TODAY}</lastmod></url>" for p in SITEMAP if p != "404.html")
        open(os.path.join(ROOT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    print("pages:", len(SITEMAP))


if __name__ == "__main__":
    build()
