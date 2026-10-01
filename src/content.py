# -*- coding: utf-8 -*-
"""Page content for 447766.com. Placeholders: {b} = relative base, {PARTNER} = partner contact URL."""

VIDEOS = [
    ("pT52hREAf18", "Chinese Lucky Numbers — Numberphile", "Numberphile"),
    ("lEdyGvq0hBI", "Why 4 is considered an evil number in China", "WION"),
    ("sr673iAqLZY", "Meanings behind Chinese numbers — what numbers are lucky?", "Chinese with Christine"),
    ("SgX9bX6xpHE", "Chinese number slang explained", "GoEast Mandarin"),
    ("8RC1PkGG4zk", "Why the number 4 is unlucky in Chinese", "Tait Lawton"),
    ("BFl8Z7xe0fs", "The superstition behind the number four in Chinese elevators", "Verasine"),
    ("oGdlfs4wcIc", "Cantonese lesson: lucky and unlucky numbers", "5 Minute Cantonese"),
    ("H9xQPJZgt5E", "Lucky, unlucky and special number phrases in Chinese (520, 38…)", "ChineseTutorYang"),
]

ROLES = [
    ("Chinese Culture Content Writer", "Freelance · Remote", "Write accurate, engaging number guides and programmatic page copy. Native or near-native Mandarin/Cantonese knowledge preferred."),
    ("Simplified & Traditional Chinese Translator", "Freelance · Remote", "Localise tools and top pages for our upcoming 中文 edition."),
    ("YouTube Shorts / TikTok Video Editor", "Freelance · Remote", "Turn one number a day into a 45-second explainer. Motion graphics a plus."),
    ("SEO & Programmatic Content Specialist", "Contract · Remote", "Grow organic traffic across thousands of number pages; schema, internal linking, Search Console."),
    ("Community & Contest Manager", "Part-time · Remote", "Run monthly challenges, moderate entries, manage winners and social channels."),
    ("Sponsorship & Ad Sales Partner", "Commission · Remote", "Sell sponsor slots to registrars, vanity-number vendors, language apps and feng shui brands."),
    ("Front-end Developer (Vanilla JS)", "Contract · Remote", "Build new interactive tools: share-card generator, lucky calendar, bilingual UI."),
    ("Numerology / Feng Shui Expert Partner", "Partner · Remote", "Receive qualified consultation leads from our Free Lucky Report funnel (revenue share)."),
]

ZOD = [("Rat", "鼠", "2, 3", "5, 9", "blue, gold, green", "2020, 2032"), ("Ox", "牛", "1, 4", "5, 6", "white, yellow, green", "2021, 2033"),
       ("Tiger", "虎", "1, 3, 4", "6, 7, 8", "blue, grey, orange", "2022, 2034"), ("Rabbit", "兔", "3, 4, 6", "1, 7, 8", "red, pink, purple, blue", "2023, 2035"),
       ("Dragon", "龙", "1, 6, 7", "3, 8", "gold, silver, grey", "2024, 2036"), ("Snake", "蛇", "2, 8, 9", "1, 6, 7", "black, red, yellow", "2025, 2037"),
       ("Horse", "马", "2, 3, 7", "1, 5, 6", "yellow, green", "2026, 2038"), ("Goat", "羊", "3, 4, 9", "6, 7, 8", "brown, red, purple", "2027, 2039"),
       ("Monkey", "猴", "1, 7, 8", "2, 5, 9", "white, blue, gold", "2028, 2040"), ("Rooster", "鸡", "5, 7, 8", "1, 3, 9", "gold, brown, yellow", "2029, 2041"),
       ("Dog", "狗", "3, 4, 9", "1, 6, 7", "red, green, purple", "2030, 2042"), ("Pig", "猪", "2, 5, 8", "1, 7", "yellow, grey, brown, gold", "2031, 2043")]

HP = '<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'
CONSENT = '<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my request and accept the <a href="{b}privacy/">privacy policy</a>. Unsubscribe anytime.</label>'
MSG = '<div class="form-msg" role="status" aria-live="polite"></div>'
AD = lambda s="inContent": f'<div class="ad" data-slot="{s}" aria-label="Advertisement"></div>'


def yt(v):
    return f'<div><div class="yt" data-id="{v[0]}" data-title="{v[1]}"></div><p class="vid-title">{v[1]}</p><p class="micro">{v[2]}</p></div>'


DIGIT_CARDS = "".join(
    f'<a class="card digit-card" href="{{b}}number/{d}/"><div class="big">{d}</div><div class="hz">{hz}</div><p class="micro" style="margin:6px 0 8px">{m}</p><span class="tag t-{k}">{lab}</span></a>'
    for d, hz, m, k, lab in [
        ("0", "零", "you · origin", "neutral", "Neutral"), ("1", "一", "want · unity", "neutral", "Neutral+"),
        ("2", "二", "easy · pairs", "lucky", "Lucky"), ("3", "三", "life · growth", "neutral", "Neutral+"),
        ("4", "四", "sounds like death", "vunlucky", "Unlucky"), ("5", "五", "me · not", "neutral", "Mixed"),
        ("6", "六", "smooth flow", "lucky", "Lucky"), ("7", "七", "rise · change", "neutral", "Mixed"),
        ("8", "八", "prosperity 发", "vlucky", "Luckiest"), ("9", "九", "long-lasting 久", "vlucky", "Very lucky")])

TOOLS_GRID = """<div class="grid g4">
<a class="card" href="{b}lookup/"><div class="ico">🔍</div><h3>Number Meaning Lookup</h3><p class="micro">Any number → Chinese meaning, luck score, angel number.</p></a>
<a class="card" href="{b}tools/#check"><div class="ico">📱</div><h3>Phone · Plate · Address</h3><p class="micro">Score your number and find a luckier version.</p></a>
<a class="card" href="{b}tools/#zodiac"><div class="ico">🐉</div><h3>Zodiac Lucky Numbers</h3><p class="micro">Birthday → zodiac, life path, numbers to avoid.</p></a>
<a class="card" href="{b}tools/#generator"><div class="ico">🎲</div><h3>Lucky Number Generator</h3><p class="micro">Chinese-lucky, avoid-4 or birthday-seeded.</p></a>
<a class="card" href="{b}tools/#name"><div class="ico">✍️</div><h3>Name Numerology</h3><p class="micro">Expression, soul urge and personality numbers.</p></a>
<a class="card" href="{b}domains/"><div class="ico">🌐</div><h3>Lucky Domain Score</h3><p class="micro">How Chinese buyers value numeric domains.</p></a>
<a class="card" href="{b}zodiac/"><div class="ico">🧧</div><h3>Zodiac Number Table</h3><p class="micro">All 12 animals: lucky numbers, colours, years.</p></a>
<a class="card" href="{b}contests/"><div class="ico">🏆</div><h3>Lucky Number Challenge</h3><p class="micro">Enter monthly contests and win prizes.</p></a>
</div>"""

LEAD_SHORT = """<form class="form" data-form="lucky-report-quick" data-subject="Lucky Report (quick)" data-success="🎉 Your free lucky report is on its way! Want it more personal? Add your birthday on the Free Report page.">
<div class="row"><div><label for="q-name">First name</label><input id="q-name" name="name" required autocomplete="given-name"></div>
<div><label for="q-email">Email</label><input id="q-email" type="email" name="email" required autocomplete="email"></div></div>
<div><label for="q-num">A number you care about (optional)</label><input id="q-num" name="number" inputmode="numeric" placeholder="phone, plate, wedding date…" data-prefill="n"></div>
""" + HP + CONSENT + """<button class="btn btn-gold btn-block" type="submit">Send My Free Lucky Report</button>""" + MSG + """
<div class="trust"><span>✓ Free</span><span>✓ No account needed</span><span>✓ No spam</span></div></form>"""

# ------------------------------------------------------------------ guides
GUIDES = [
    {"slug": "chinese-lucky-numbers", "short": "Chinese lucky numbers", "tag": "Essentials", "read": 9,
     "title": "Chinese Lucky Numbers: The Complete Guide (0–9, Combos & Slang)",
     "desc": "Why 8 means wealth, 4 means death and 6 means smooth success — plus 168, 520, 1314 and the number codes Chinese speakers use every day.",
     "body": """<p class="lead">In Chinese, numbers are judged less by their maths than by their <b>sound</b>. Because Mandarin and Cantonese are full of homophones, a digit borrows the meaning of the word it resembles — and that meaning moves real money.</p>
<h2>The ten digits at a glance</h2>
<div class="table-wrap"><table><thead><tr><th>Digit</th><th>Hanzi</th><th>Sounds like</th><th>Verdict</th></tr></thead><tbody>
<tr><td>0</td><td class="hz">零</td><td>你 "you" (slang), wholeness</td><td><span class="tag t-neutral">Neutral</span></td></tr>
<tr><td>1</td><td class="hz">一</td><td>要 "want", unity</td><td><span class="tag t-neutral">Neutral+</span></td></tr>
<tr><td>2</td><td class="hz">二</td><td>易 "easy" (Cantonese); pairs</td><td><span class="tag t-lucky">Lucky</span></td></tr>
<tr><td>3</td><td class="hz">三</td><td>生 "life" (Cantonese)</td><td><span class="tag t-neutral">Neutral+</span></td></tr>
<tr><td>4</td><td class="hz">四</td><td>死 "death"</td><td><span class="tag t-vunlucky">Unlucky</span></td></tr>
<tr><td>5</td><td class="hz">五</td><td>我 "me" / 唔 "not"</td><td><span class="tag t-neutral">Mixed</span></td></tr>
<tr><td>6</td><td class="hz">六</td><td>溜/流 "smooth", 禄 "fortune"</td><td><span class="tag t-lucky">Lucky</span></td></tr>
<tr><td>7</td><td class="hz">七</td><td>起 "rise", 气 "energy" / 欺 "cheat"</td><td><span class="tag t-neutral">Mixed</span></td></tr>
<tr><td>8</td><td class="hz">八</td><td>发 "prosper"</td><td><span class="tag t-vlucky">Luckiest</span></td></tr>
<tr><td>9</td><td class="hz">九</td><td>久 "long-lasting"</td><td><span class="tag t-vlucky">Very lucky</span></td></tr>
</tbody></table></div>
<h2>Why 8 is king</h2><p><a href="{b}number/8/">Eight</a> (bā) rhymes with 发 (fā), "to prosper". The Beijing Olympics opened on 8/8/2008 at 8:08:08 pm; Sichuan Airlines paid ¥2.33 million for the phone number +86 28 8888 8888; and Hong Kong licence plates with 8s routinely sell for six or seven figures.</p>
<h2>Why 4 is feared</h2><p><a href="{b}number/4/">Four</a> (sì) sounds almost exactly like 死 (sǐ), "death". Many buildings in China, Hong Kong and Singapore skip the 4th, 14th and 24th floors — one Hong Kong tower skips 43 floor numbers. Read our <a href="{b}guides/why-4-is-unlucky/">full guide to tetraphobia</a>.</p>
<h2>Famous combinations</h2><ul>
<li><a href="{b}number/168/">168</a> 一路发 — "prosperity all the way"</li><li><a href="{b}number/518/">518</a> 我要发 — "I will prosper"</li>
<li><a href="{b}number/520/">520</a> 我爱你 — "I love you" (20 May is internet Valentine's Day)</li><li><a href="{b}number/1314/">1314</a> 一生一世 — "forever"</li>
<li><a href="{b}number/666/">666</a> 溜溜溜 — "awesome!"</li><li><a href="{b}number/250/">250</a> 二百五 — "idiot" (never price a gift at 250)</li>
<li><a href="{b}number/14/">14</a> 要死 — "want to die", <a href="{b}number/74/">74</a> 去死 — "go die"</li></ul>
<h2>Mandarin vs Cantonese</h2><p>Dialect changes everything. <a href="{b}number/58/">58</a> is "I prosper" in Mandarin slang but "won't prosper" (唔发) in Cantonese; <a href="{b}number/13/">13</a> is "sure to live" in Cantonese; and in Teochew and Shanghainese, 4 can even sound like "happiness".</p>
<h2>How to use this</h2><p>Picking a phone number, plate, wedding date, price or business name for a Chinese-speaking audience? Favour 8, 6, 9 and 2, avoid 4 (especially at the end), and check combos. Our <a href="{b}lookup/">lookup tool</a> does it in one second.</p>"""},
    {"slug": "why-4-is-unlucky", "short": "Why 4 is unlucky", "tag": "Culture", "read": 7,
     "title": "Why Is 4 Unlucky? Tetraphobia in China, Hong Kong and Beyond",
     "desc": "The sound of death: how the number 4 reshapes buildings, phone numbers, plates, prices and even product names across East Asia.",
     "body": """<p class="lead">Tetraphobia — the fear of the number four — is one of the most visible superstitions in the world. It is rooted in a simple sound: 四 (sì) "four" and 死 (sǐ) "death".</p>
<h2>Where you'll see it</h2><ul><li><b>Buildings:</b> missing 4th, 14th, 24th and 40s floors. 39 Conduit Road in Hong Kong skips 43 floor numbers.</li><li><b>Hospitals and hotels:</b> rooms ending in 4 are often skipped.</li><li><b>Products:</b> some phone and camera makers have skipped "4" in model series sold in Asia.</li><li><b>Phone numbers &amp; plates:</b> numbers with 4s sell at a discount; numbers with 8s at a premium.</li><li><b>Numeric domains:</b> in the 2015 six-digit .com boom, domains with an "unlucky" 4 traded around half the price of 4-free names.</li></ul>
<h2>Deadly combinations</h2><p><a href="{b}number/14/">14</a> (要死, "want to die"), <a href="{b}number/24/">24</a> (易死, "easy death" in Cantonese), <a href="{b}number/74/">74</a> (去死, "go die"), <a href="{b}number/514/">514</a> (我要死) and <a href="{b}number/44/">44</a> (死死) are the most avoided.</p>
<h2>When 4 is lucky</h2><p>Context can redeem it. <a href="{b}number/1314/">1314</a> (一生一世, "a lifetime") and <a href="{b}number/3344/">3344</a> (生生世世, "forever") read 4 as 世 "lifetime". <a href="{b}number/54/">54</a> is "won't die" in Cantonese. Teochew speakers consider 4 lucky — Singapore's famous No. 44 Emerald Hill was chosen deliberately.</p>
<h2>East vs West</h2><p>In Western "angel number" culture, <a href="{b}number/444/">444</a> is the most-searched sequence of all and is read as protection and stability. Same digits, opposite stories — which is why 447766 shows both readings on every page.</p>"""},
    {"slug": "447766-meaning", "short": "447766 decoded", "tag": "Our story", "read": 5,
     "title": "447766 Meaning: The Comeback Code — Turn Your 4s into 6s",
     "desc": "44 is death, 77 is rising and change, 66 is smooth success. Here's why we named a lucky-number site after the unluckiest pair in Chinese.",
     "body": """<p class="lead">Ask a Mandarin speaker to read 447766 and they'll wince at the start: <span class="hz">死死</span> — "death, death". Then something interesting happens.</p>
<div class="code"><div class="dg d4">4<span>死</span></div><div class="dg d4">4<span>死</span></div><div class="dg d7">7<span>起</span></div><div class="dg d7">7<span>起</span></div><div class="dg d6">6<span>顺</span></div><div class="dg d6">6<span>顺</span></div></div>
<h2>Act 1 — 44: endings</h2><p>Four sounds like death. Doubled, it's the most avoided pair in the language. It stands for every setback, failure and bad-luck streak.</p>
<h2>Act 2 — 77: rising and change</h2><p>Seven (七 qī) echoes 起 "to rise" and 气 "vital energy"; the I Ching saying 逢七必变 holds that "on seven, things change". 77 is also <a href="{b}number/77/">Qixi</a>, the Double Seventh — Chinese Valentine's Day.</p>
<h2>Act 3 — 66: smooth success</h2><p><a href="{b}number/66/">66</a> is 六六大顺 — "everything goes smoothly", one of the most common blessings in Chinese.</p>
<h2>The point</h2><p>447766 isn't a traditional idiom — it's a story we chose: <b>from endings, to rising, to smooth success</b>. It's also a reminder that numbers only carry the meanings we give them. Our tools show you the traditional reading and the alternatives, so you can decide.</p>
<p class="notice">Fun fact: the colour <b>#447766</b> is a calm teal-green. It's our brand colour.</p>"""},
    {"slug": "lucky-numbers-by-occasion", "short": "Lucky numbers by occasion", "tag": "Practical", "read": 8,
     "title": "Lucky Numbers by Occasion: Weddings, Business, Phones, Plates & Gifts",
     "desc": "The right number for every moment — wedding dates, red-envelope amounts, shop prices, phone numbers, licence plates and house numbers.",
     "body": """<div class="table-wrap"><table><thead><tr><th>Occasion</th><th>Use</th><th>Avoid</th></tr></thead><tbody>
<tr><td>Weddings &amp; anniversaries</td><td>2, 6, 8, 9, 520, 1314, 3344, 999</td><td>4, 14, 250, odd gift amounts</td></tr>
<tr><td>Red envelopes (hongbao)</td><td>Even amounts: 66, 88, 168, 666, 888</td><td>Anything with 4; 250</td></tr>
<tr><td>Business opening / prices</td><td>8, 168, 518, 1688, prices ending in 8</td><td>4, 14, 74</td></tr>
<tr><td>Phone numbers</td><td>Last 4 digits with 8/6/9; 168, 888</td><td>Ending in 4; 514, 748</td></tr>
<tr><td>Licence plates</td><td>Short plates with 8, 18, 28, 88</td><td>4, 14, 24, 44</td></tr>
<tr><td>Addresses &amp; floors</td><td>6, 8, 9, 18, 28</td><td>4, 14, 24, 44</td></tr>
<tr><td>Gifts (quantity)</td><td>Pairs; 9 or 99 roses; 6 or 8 items</td><td>4 items; clocks (送钟 = "attend a funeral")</td></tr>
</tbody></table></div>
<h2>Weddings</h2><p>Couples love dates like 5/20 (<a href="{b}number/520/">520</a>, "I love you"), dates containing 1314, and the Qixi festival. Gifts come in pairs because 好事成双 — "good things come in pairs".</p>
<h2>Business</h2><p>Shopkeepers price items at 88 or 168, choose phone numbers ending in 8 and open on dates with 8. A memorable lucky number can be a marketing asset in itself — just look at numeric brands like 360.com, 58.com and 4399.com.</p>
<h2>Phones and plates</h2><p>The last digits carry most weight. Check yours with our <a href="{b}tools/#check">phone and plate checker</a>, then see luckier alternatives. Want help finding a vanity number? <a href="{b}get-report/#vanity">Request one</a>.</p>"""},
    {"slug": "numeric-domains-china", "short": "Numeric domains in China", "tag": "Money", "read": 8,
     "title": "Numeric Domains in China: Why Numbers Sell (and Which Ones)",
     "desc": "From 360.com's $17M sale to the six-digit .com boom — how Chinese buyers value numeric domains and how lucky digits move prices.",
     "body": """<p class="lead">For Chinese internet users, numbers are easier to remember and type than pinyin, and they cross dialect lines. That's why so many giants run on numeric domains: 163.com and 126.com (NetEase), 360.com, 58.com, 51job.com ("I want a job"), 4399.com and 7k7k.com.</p>
<h2>Landmark sales</h2><ul><li><b>360.com</b> — about $17M (2015), then a record.</li><li><b>55.com</b> — $2.3M (2011).</li><li><b>114.com</b> — $2.1M (2013).</li></ul>
<h2>The 6N.com boom</h2><p>There are exactly 1,000,000 six-digit .com domains. All of them were registered by November 2015, as Chinese demand pushed average prices from under $80 to over $170 within weeks.</p>
<h2>How digits change value</h2><div class="table-wrap"><table><thead><tr><th>Pattern (2015 6N.com market)</th><th>Typical price</th></tr></thead><tbody><tr><td>Any 6N.com (floor)</td><td>~$20</td></tr><tr><td>Contains an "unlucky" 4 or a leading 0</td><td>~$40</td></tr><tr><td>No 4s</td><td>~$80</td></tr><tr><td>Lucky patterns (88, 888)</td><td>$100–$261</td></tr></tbody></table></div>
<p>Rule of thumb: <b>shorter is better</b>, 8/6/9 add premiums, 4 subtracts, and 0 at the start hurts. Today the deepest liquidity is in 3- and 4-digit .com domains, and Chinese platforms set the price floors.</p>
<h2>Branding beats flipping</h2><p>A number with 4s may be a weak investment but a strong <b>brand</b> if it has a story — that's the bet behind 447766.com.</p>
<p><a class="btn btn-red" href="{b}domains/#appraisal">Get a free numeric-domain appraisal</a></p>"""},
    {"slug": "chinese-number-slang", "short": "Chinese number slang", "tag": "Language", "read": 6,
     "title": "Chinese Number Slang: 520, 1314, 666, 233, 886 and More",
     "desc": "Decode the number codes Chinese speakers use online — love codes, insults, laughter and goodbyes.",
     "body": """<p class="lead">Chinese internet culture runs on numbers. Because digits sound like words, a few keystrokes can say "I love you", "LOL" or "go away".</p>
<div class="table-wrap"><table><thead><tr><th>Code</th><th>Reads as</th><th>Meaning</th></tr></thead><tbody>
<tr><td><a href="{b}number/520/">520</a></td><td class="hz">我爱你</td><td>I love you</td></tr><tr><td><a href="{b}number/521/">521</a></td><td class="hz">我愿意</td><td>I do / I'm willing</td></tr>
<tr><td><a href="{b}number/1314/">1314</a></td><td class="hz">一生一世</td><td>Forever</td></tr><tr><td><a href="{b}number/5201314/">5201314</a></td><td class="hz">我爱你一生一世</td><td>I love you forever</td></tr>
<tr><td><a href="{b}number/530/">530</a></td><td class="hz">我想你</td><td>I miss you</td></tr><tr><td><a href="{b}number/9420/">9420</a></td><td class="hz">就是爱你</td><td>It's you I love</td></tr>
<tr><td><a href="{b}number/666/">666</a></td><td class="hz">溜溜溜</td><td>Awesome! Smooth!</td></tr><tr><td><a href="{b}number/233/">233</a></td><td class="hz">哈哈</td><td>LOL</td></tr>
<tr><td><a href="{b}number/88/">88</a> / <a href="{b}number/886/">886</a></td><td class="hz">拜拜(了)</td><td>Bye-bye</td></tr><tr><td><a href="{b}number/555/">555</a></td><td class="hz">呜呜呜</td><td>Boo-hoo (crying)</td></tr>
<tr><td><a href="{b}number/7456/">7456</a></td><td class="hz">气死我了</td><td>I'm furious</td></tr><tr><td><a href="{b}number/748/">748</a></td><td class="hz">去死吧</td><td>Go to hell</td></tr>
<tr><td><a href="{b}number/250/">250</a></td><td class="hz">二百五</td><td>Idiot</td></tr><tr><td><a href="{b}number/38/">38</a></td><td class="hz">三八</td><td>Gossip (insult)</td></tr>
</tbody></table></div>
<p>Note how 666 and 555 mean the opposite of their Western "angel number" or pop-culture readings. Context and audience are everything.</p>"""},
    {"slug": "angel-numbers-vs-chinese-numbers", "short": "Angel vs Chinese numbers", "tag": "East vs West", "read": 6,
     "title": "Angel Numbers vs Chinese Numerology: Same Digits, Opposite Stories",
     "desc": "444 is protection in the West and triple death in China. 666 is evil in the West and 'awesome' in China. A side-by-side guide.",
     "body": """<p class="lead">Millions of people search "angel number 444" every month. In Western spiritual culture it means angels are protecting you. In Chinese, the same digits sound like "death, death, death".</p>
<div class="table-wrap"><table><thead><tr><th>Number</th><th>Western angel number</th><th>Chinese reading</th></tr></thead><tbody>
<tr><td><a href="{b}number/444/">444</a></td><td>Protection, stability</td><td>死死死 — triple death</td></tr>
<tr><td><a href="{b}number/666/">666</a></td><td>Reflect and rebalance (and "the beast" in pop culture)</td><td>溜溜溜 — awesome, smooth</td></tr>
<tr><td><a href="{b}number/555/">555</a></td><td>Big change ahead</td><td>呜呜呜 — crying</td></tr>
<tr><td><a href="{b}number/888/">888</a></td><td>Abundance</td><td>发发发 — triple prosperity</td></tr>
<tr><td><a href="{b}number/777/">777</a></td><td>Spiritual luck</td><td>Mixed: rising vs Ghost Month</td></tr>
<tr><td><a href="{b}number/1111/">1111</a></td><td>Make a wish, alignment</td><td>Singles' Day — the biggest shopping day on Earth</td></tr>
<tr><td><a href="{b}number/13/">13</a></td><td>Unlucky</td><td>实生 — "sure to live" (Cantonese)</td></tr>
</tbody></table></div>
<h2>Which one should you follow?</h2><p>Follow your audience. A Western wellness brand can embrace 444; a restaurant serving Chinese families should not. Our <a href="{b}lookup/">lookup tool</a> shows both readings side by side for any number.</p>"""},
]

# ------------------------------------------------------------------ pages
VID_GRID = '<div class="grid g3">' + "".join(yt(v) for v in VIDEOS[:3]) + "</div>"
VID_ALL = '<div class="grid g3">' + "".join(yt(v) for v in VIDEOS) + "</div>"
GUIDE_CARDS = '<div class="grid g3">' + "".join(
    f'<a class="card" href="{{b}}guides/{g["slug"]}/"><span class="tag t-neutral">{g["tag"]}</span><h3 style="margin-top:10px">{g["title"]}</h3><p class="micro">{g["desc"]}</p></a>' for g in GUIDES[:6]) + "</div>"

HOME = """
<section class="hero"><div class="wrap hero-grid"><div>
<span class="eyebrow">The Lucky Number Lab · 幸运数字实验室</span>
<h1>Every number has two stories. <span style="color:var(--red)">Decode yours.</span></h1>
<p class="lead">Chinese meaning, luck score, Cantonese reading and Western angel-number meaning for any number — phone, plate, address, date or domain. Free, instant, no sign-up.</p>
<form class="search" data-lookup="go" role="search"><input inputmode="numeric" placeholder="Enter any number — e.g. 168" aria-label="Enter a number" autocomplete="off"><button class="btn btn-red" type="submit">Reveal</button></form>
<div class="chips"><a class="chip good" href="{b}number/8/">8 · 发</a><a class="chip good" href="{b}number/168/">168 · 一路发</a><a class="chip good" href="{b}number/520/">520 · 我爱你</a><a class="chip good" href="{b}number/1314/">1314 · 一生一世</a><a class="chip bad" href="{b}number/444/">444 · 死死死</a><a class="chip" href="{b}number/447766/">447766</a></div>
<p class="micro" style="margin-top:10px">✓ 150+ numbers decoded · ✓ Mandarin &amp; Cantonese · ✓ East + West readings</p>
</div><div>
<div class="card" style="text-align:center"><p class="eyebrow" style="margin:0 0 6px">The comeback code</p>
<div class="code" style="justify-content:center"><div class="dg d4">4<span>死</span></div><div class="dg d4">4<span>死</span></div><div class="dg d7">7<span>起</span></div><div class="dg d7">7<span>起</span></div><div class="dg d6">6<span>顺</span></div><div class="dg d6">6<span>顺</span></div></div>
<div class="story" style="justify-content:center"><b>Endings</b><span class="arr">→</span><b>Rising</b><span class="arr">→</span><b>Smooth success</b></div>
<p class="micro" style="margin:12px 0">44 sounds like death, 77 like rising, 66 like "everything goes smoothly". Turn your 4s into 6s.</p>
<a class="btn btn-ghost btn-sm" href="{b}guides/447766-meaning/">Read the story</a></div>
</div></div></section>

<div class="wrap">""" + AD("top") + """</div>

<section class="block"><div class="wrap"><div class="section-head"><h2>The ten digits, decoded</h2><a href="{b}numbers/">All numbers →</a></div>
<div class="grid g5">""" + DIGIT_CARDS + """</div></div></section>

<section class="block alt"><div class="wrap"><div class="section-head"><h2>Free lucky-number tools</h2><a href="{b}tools/">All tools →</a></div>""" + TOOLS_GRID + """</div></section>

<section class="block"><div class="wrap grid g2" style="align-items:center">
<div><span class="eyebrow">Free personal report</span><h2 style="margin-top:0">Your lucky numbers, chosen for <em>you</em></h2>
<p class="lead">Tell us your name and a number you care about. We'll email your personal lucky-number report: your zodiac numbers, numbers to avoid, the best endings for your phone or plate, and lucky dates.</p>
<ul><li>Built on Chinese homophones and Western numerology</li><li>Phone, plate, wedding date, business name or domain</li><li>Optional expert consultation if you want one</li></ul></div>
<div class="lead-box"><div class="steps"><span class="on"></span><span></span></div><h3>Get my free lucky report</h3>""" + LEAD_SHORT + """</div>
</div></section>

<section class="block alt"><div class="wrap"><div class="section-head"><h2>Guides</h2><a href="{b}guides/">All guides →</a></div>""" + GUIDE_CARDS + """</div></section>

<section class="block"><div class="wrap"><div class="section-head"><h2>Watch &amp; learn</h2><a href="{b}videos/">All videos →</a></div>""" + VID_GRID + "</div></section>" + """

<section class="block alt"><div class="wrap grid g3">
<div class="card"><div class="ico">🏆</div><h3>Win in the Lucky Number Challenge</h3><p data-contest="prize">Monthly prizes for the best lucky-number picks.</p><a class="btn btn-red btn-sm" href="{b}contests/">Enter now</a></div>
<div class="card"><div class="ico">🧧</div><h3>Support free tools</h3><p>Chip in a lucky $6.66 or $8.88 to keep 447766 free, fund new tools and grow the prize pool.</p><a class="btn btn-brand btn-sm" href="{b}support/">Support us</a></div>
<div class="card"><div class="ico">🤝</div><h3>Sponsor · Advertise · Partner</h3><p>Reach people who pay premiums for lucky numbers. Sponsor a tool, a contest or the whole domain.</p><a class="btn btn-ghost btn-sm" href="{PARTNER}" target="_blank" rel="noopener">Let's talk</a></div>
</div></section>

<section class="block"><div class="wrap"><p class="micro" style="text-align:center;letter-spacing:.1em;text-transform:uppercase">Sponsor slots available</p>
<div class="sponsor-strip"><a class="sponsor-slot" href="{b}advertise/">Your logo here</a><a class="sponsor-slot" href="{b}advertise/">Tool sponsor</a><a class="sponsor-slot" href="{b}advertise/">Contest prize sponsor</a><a class="sponsor-slot" href="{b}advertise/">Newsletter sponsor</a></div>
<div class="faq" style="max-width:820px;margin:36px auto 0"><h2 style="text-align:center">FAQ</h2>
<details><summary>What is the luckiest number in Chinese culture?</summary><p>8 (八, bā), because it sounds like 发 (fā), "to prosper". Combinations like 168, 888 and 8888 are especially prized.</p></details>
<details><summary>Why is 4 unlucky?</summary><p>四 (sì) sounds like 死 (sǐ), "death". See <a href="{b}guides/why-4-is-unlucky/">our guide to tetraphobia</a>.</p></details>
<details><summary>What does 447766 mean?</summary><p>44 sounds like "death, death", 77 like "rising", 66 like "everything goes smoothly" — we read it as a comeback story. <a href="{b}guides/447766-meaning/">Full story</a>.</p></details>
<details><summary>Is this fortune-telling?</summary><p>No. We explain traditional cultural associations and numerology conventions for entertainment and education. Make real decisions on real information.</p></details>
</div></div></section>
<div class="wrap">""" + AD("multiplex") + "</div>"

LOOKUP = """<div class="wrap"><h1>Number Meaning Lookup</h1>
<p class="lead">Type any number — a phone, plate, date, price, address or domain — to see its Chinese meaning, Cantonese reading, luck score and angel-number meaning.</p>
<section><form class="search" data-lookup="#lookup-result" role="search" style="margin:18px 0"><input id="lookup-input" inputmode="numeric" placeholder="e.g. 13800138000 or 520" aria-label="Number" autocomplete="off"><button class="btn btn-red" type="submit">Reveal meaning</button></form>
<div class="chips"><a class="chip" href="#" data-fill="168">168</a><a class="chip" href="#" data-fill="520">520</a><a class="chip" href="#" data-fill="888">888</a><a class="chip" href="#" data-fill="444">444</a><a class="chip" href="#" data-fill="1314">1314</a><a class="chip" href="#" data-fill="447766">447766</a></div></section>
<div class="content" style="margin-top:24px"><div><div id="lookup-result"><div class="notice">Your result will appear here. Try one of the examples above.</div></div>
""" + AD("top") + """
<div class="lead-box" style="margin-top:24px"><h3>Get the full report by email</h3>""" + LEAD_SHORT + """</div></div>
<aside class="sidebar"><div class="card"><h3>Popular lookups</h3><div class="chips"><a class="chip" href="{b}number/8/">8</a><a class="chip" href="{b}number/6/">6</a><a class="chip" href="{b}number/9/">9</a><a class="chip" href="{b}number/4/">4</a><a class="chip" href="{b}number/14/">14</a><a class="chip" href="{b}number/666/">666</a><a class="chip" href="{b}number/1111/">1111</a><a class="chip" href="{b}number/5201314/">5201314</a></div></div>""" + AD("sidebar").replace('class="ad"', 'class="ad side"') + "</aside></div></div>"

TOOLS = """<div class="wrap"><h1>Free Lucky Number Tools</h1><p class="lead">Instant, private and free — everything runs in your browser.</p>""" + AD("top") + """
<section class="block" id="check" style="padding-top:12px"><h2>Phone · Plate · Address · Domain checker</h2>
<form id="tool-check" class="form card"><div class="row"><div><label for="ck-kind">What are you checking?</label><select id="ck-kind" name="kind"><option value="phone">Phone number</option><option value="plate">Licence plate</option><option value="address">Address / unit / floor</option><option value="domain">Numeric domain</option></select></div>
<div><label for="ck-val">Number</label><input id="ck-val" name="value" required placeholder="e.g. 416 555 0168 or 888.com"></div></div><button class="btn btn-red" type="submit">Check my number</button></form>
<div id="check-out" style="margin-top:16px"></div></section>
<section class="block" id="zodiac"><h2>Birthday → zodiac lucky numbers &amp; life path</h2>
<form id="tool-zodiac" class="form card"><div class="row"><div><label for="z-y">Birth year</label><input id="z-y" name="year" type="number" min="1900" max="2100" required placeholder="1990"></div>
<div class="row"><div><label for="z-m">Month</label><select id="z-m" name="month">""" + "".join(f'<option value="{m}">{m}</option>' for m in range(1, 13)) + """</select></div><div><label for="z-d">Day</label><select id="z-d" name="day">""" + "".join(f'<option value="{d}">{d}</option>' for d in range(1, 32)) + """</select></div></div></div>
<button class="btn btn-red" type="submit">Reveal my lucky numbers</button></form><div id="zodiac-out" style="margin-top:16px"></div></section>
""" + AD() + """
<section class="block" id="generator"><h2>Lucky number generator</h2>
<form id="tool-gen" class="form card"><div class="row"><div><label for="g-mode">Style</label><select id="g-mode" name="mode"><option value="chinese">Chinese-lucky (8, 6, 9)</option><option value="lucky">Ultra-lucky (8, 6, 9 only)</option><option value="avoid4">Avoid 4</option><option value="random">Pure random</option></select></div>
<div class="row"><div><label for="g-len">Digits</label><input id="g-len" name="len" type="number" min="1" max="12" value="6"></div><div><label for="g-seed">Seed (optional)</label><input id="g-seed" name="seed" placeholder="birthday or name"></div></div></div>
<button class="btn btn-red" type="submit">Generate lucky numbers</button></form><div id="gen-out" style="margin-top:16px"></div>
<p class="micro">For fun and inspiration only — not for lotteries or gambling.</p></section>
<section class="block" id="name"><h2>Name numerology</h2>
<form id="tool-name" class="form card"><div><label for="n-name">Full name</label><input id="n-name" required placeholder="Your full birth name"></div><button class="btn btn-red" type="submit">Calculate</button></form><div id="name-out" style="margin-top:16px"></div></section>
""" + AD("multiplex") + "</div>"

ZODIAC = """<div class="wrap"><h1>Chinese Zodiac Lucky Numbers</h1><p class="lead">Each of the 12 animals carries its own lucky and unlucky numbers and colours in traditional Chinese astrology. Associations vary between sources — use them as inspiration.</p>""" + AD("top") + """
<div class="table-wrap"><table><thead><tr><th>Animal</th><th>Lucky numbers</th><th>Avoid</th><th>Lucky colours</th><th>Next years</th></tr></thead><tbody>""" + "".join(
    f"<tr><td><b class='hz'>{hz}</b> {a}</td><td>{l}</td><td>{u}</td><td>{c}</td><td>{y}</td></tr>" for a, hz, l, u, c, y in ZOD) + """</tbody></table></div>
<p class="notice">The zodiac year starts at Lunar New Year (late January – mid February), not 1 January. <a href="{b}tools/#zodiac">Find your animal and lucky numbers →</a></p>
<h2>2026: Year of the Fire Horse 🐎</h2><p>The Horse's traditional lucky numbers are 2, 3 and 7; numbers to avoid are 1, 5 and 6. 2027 is the Year of the Goat (lucky 3, 4, 9).</p>
""" + AD() + """<div class="lead-box"><h3>Get your personal zodiac number report</h3>""" + LEAD_SHORT + "</div></div>"

DOMAINS = """<div class="wrap"><h1>Numeric Domains: Lucky Numbers Online</h1>
<p class="lead">Numbers are a language of their own on the Chinese internet. Learn what drives numeric-domain value, score any numeric domain, and get a free appraisal.</p>""" + AD("top") + """
<div class="grid g3"><div class="card"><div class="stat">1,000,000</div><p class="micro">possible 6-digit .com domains — all registered by Nov 2015</p></div><div class="card"><div class="stat">$17M</div><p class="micro">reported price of 360.com (2015)</p></div><div class="card"><div class="stat">~2×</div><p class="micro">price gap between 4-free and "unlucky 4" six-digit .coms in 2015</p></div></div>
<h2>How Chinese buyers value numeric domains</h2><ul><li><b>Length first:</b> 2–3 digits are premium, 4 digits are liquid, 5–6 digits are a volume market.</li><li><b>Lucky digits</b> 8, 6 and 9 add value; <b>4</b> subtracts; a leading <b>0</b> hurts.</li><li><b>Meaning</b> beats randomness: 168, 518, 520 and repeating patterns carry stories.</li><li><b>Brandability:</b> a story can rescue an "unlucky" number — see <a href="{b}guides/447766-meaning/">447766</a>.</li></ul>
<h2>Score a numeric domain</h2><form class="search" data-lookup="#dom-out" style="margin:12px 0"><input inputmode="numeric" placeholder="e.g. 168888 (without .com)" aria-label="Domain digits"><button class="btn btn-red" type="submit">Score it</button></form><div id="dom-out"></div>
""" + AD() + """
<section id="appraisal" class="block"><div class="grid g2" style="align-items:start"><div><h2 style="margin-top:0">Free lucky-domain appraisal</h2><p>Buying or selling a numeric or Chinese-market domain? Get a free, human-reviewed estimate with comparables and the best marketplaces to list on.</p><ul><li>Number-meaning analysis (Mandarin &amp; Cantonese)</li><li>Comparable sales and liquidity notes</li><li>Optional brokerage or partnership introduction</li></ul>
<p class="notice">Interested in <b>447766.com</b> itself? <a href="{PARTNER}" target="_blank" rel="noopener">Contact us about the website, domain or partnership</a>.</p></div>
<div class="lead-box"><h3>Request my appraisal</h3><form class="form" data-form="domain-appraisal" data-subject="Domain appraisal request" data-success="Thanks! Your appraisal request is in. Expect a reply within 2 business days.">
<div><label for="da-dom">Domain(s)</label><input id="da-dom" name="domain" required placeholder="e.g. 168888.com"></div>
<div class="row"><div><label for="da-goal">I want to</label><select id="da-goal" name="goal"><option>Sell</option><option>Buy</option><option>Lease / partner</option><option>Just curious</option></select></div><div><label for="da-budget">Budget / asking (USD)</label><select id="da-budget" name="budget"><option>Under $1k</option><option>$1k–$10k</option><option>$10k–$100k</option><option>$100k+</option></select></div></div>
<div class="row"><div><label for="da-name">Name</label><input id="da-name" name="name" required></div><div><label for="da-email">Email</label><input id="da-email" type="email" name="email" required></div></div>
""" + HP + CONSENT + """<button class="btn btn-gold btn-block" type="submit">Get My Free Appraisal</button>""" + MSG + "</form></div></div></section></div>"

VIDEOS_PAGE = """<div class="wrap"><h1>Videos: Chinese Numbers Explained</h1><p class="lead">Hand-picked explainers on lucky and unlucky numbers, number slang and tetraphobia. Videos play through the official YouTube player and belong to their creators.</p>""" + AD("top") + VID_ALL + """
<div class="card" style="margin-top:28px;display:flex;gap:16px;align-items:center;flex-wrap:wrap"><div style="flex:1;min-width:240px"><h3>📺 447766 on YouTube</h3><p class="micro" style="margin:0">One number a day in under 60 seconds. Subscribe for daily Shorts.</p></div><a class="btn btn-red" id="yt-sub" href="https://www.youtube.com/results?search_query=chinese+lucky+numbers" target="_blank" rel="noopener">Watch more</a></div>
<p class="micro" style="margin-top:14px">Are you a creator? <a href="{b}careers/">Make videos with us</a> or <a href="{b}contact/">suggest a video</a>.</p>""" + AD("multiplex") + "</div>"

CONTESTS = """<div class="wrap"><h1>Contests &amp; Prizes</h1><p class="lead">Show off your number sense, win prizes and get featured on 447766.</p>
<div class="grid g2" style="align-items:start;margin-top:20px"><div>
<div class="card"><span class="tag t-lucky">Now open</span><h2 style="margin-top:12px" data-contest="title">The Lucky Number Challenge</h2>
<p><b>Prize:</b> <span data-contest="prize">US$88</span></p><p><b>Opens:</b> <span data-contest="opens">On launch</span> · <b>Closes:</b> <span data-contest="closes">TBA</span></p>
<p><b>Challenge:</b> <span data-contest="question">Pick the luckiest 4-digit number and tell us why.</span></p>
<h3>How to win</h3><ol><li>Submit your entry with the form.</li><li>Answer the skill-testing question.</li><li>Get <b>bonus entries</b>: share your result card (+1), follow us on YouTube (+1), refer a friend who enters (+3).</li><li>Winners are picked by a judging panel on creativity and cultural accuracy, then announced here.</li></ol>
<p class="micro">No purchase necessary. See the <a href="{b}contest-rules/">official rules</a>.</p></div>
<h3 style="margin-top:28px">Upcoming contests</h3><ul><li><b>Qixi Love Code</b> — the most creative love message in numbers.</li><li><b>Lucky Plate Design</b> — design the luckiest licence plate.</li><li><b>Number Story Shorts</b> — a 60-second video about a number in your life.</li></ul>
<h3>Winners' hall</h3><p class="micro">Our first winners will be listed here.</p>
<p class="notice">Want to sponsor a prize? <a href="{b}advertise/">Become a contest sponsor</a>.</p></div>
<div class="lead-box"><h3>Enter the challenge</h3><form class="form" data-form="contest-entry" data-subject="Contest entry" data-success="You're entered! Good luck — we'll email you if you win.">
<div class="row"><div><label for="ce-name">Full name</label><input id="ce-name" name="name" required></div><div><label for="ce-email">Email</label><input id="ce-email" type="email" name="email" required></div></div>
<div class="row"><div><label for="ce-country">Country / province</label><input id="ce-country" name="region" required></div><div><label for="ce-num">Your number</label><input id="ce-num" name="number" required inputmode="numeric"></div></div>
<div><label for="ce-why">Why is it lucky? (max 300 characters)</label><textarea id="ce-why" name="answer" maxlength="300" required></textarea></div>
<div><label for="ce-ref">Referred by (optional)</label><input id="ce-ref" name="referred_by" placeholder="friend's email" data-prefill="ref"></div>
<div><label for="ce-skill" data-contest="skill">Skill-testing question</label><input id="ce-skill" name="skill_test" required inputmode="numeric"></div>
""" + HP + """<label class="check"><input type="checkbox" name="rules" value="accepted" required> I am of the age of majority where I live and accept the <a href="{b}contest-rules/">official rules</a>.</label>
""" + CONSENT + """<button class="btn btn-gold btn-block" type="submit">Submit My Entry</button>""" + MSG + "</form></div></div></div>"

RULES = """<div class="wrap prose"><h1>Official Contest Rules</h1><p class="micro">Applies to every 447766.com contest unless a contest page says otherwise. Last updated <span data-year>2026</span>.</p>
<ol><li><b>Sponsor.</b> 447766.com ("Sponsor"). Contact through the <a href="{b}contact/">contact page</a>.</li>
<li><b>No purchase necessary.</b> A purchase or donation will not increase your chances of winning.</li>
<li><b>Eligibility.</b> Open to individuals who have reached the age of majority where they live, except where prohibited. Void where prohibited or restricted by law. Employees and contractors of the Sponsor and their households are not eligible.</li>
<li><b>Entry period.</b> As shown on the contest page. Late, incomplete or automated entries are void.</li>
<li><b>How to enter.</b> Submit the online form. Limit: one base entry per person and email. Bonus entries (shares, follows, referrals) are listed on the contest page and verified manually.</li>
<li><b>Selection.</b> Skill-based contests are judged by a panel on creativity (50%), cultural accuracy (30%) and clarity (20%). Draw-based contests use a random draw among eligible entries. Odds depend on the number of eligible entries.</li>
<li><b>Skill-testing question.</b> Canadian residents must correctly answer a mathematical skill-testing question before being declared a winner.</li>
<li><b>Québec residents.</b> Any dispute about the running of a publicity contest may be submitted to the Régie des alcools, des courses et des jeux for a ruling. Any dispute about awarding a prize may be submitted to the Régie only to help the parties reach a settlement.</li>
<li><b>Prizes.</b> As described on the contest page. No substitution except at the Sponsor's discretion for a prize of equal or greater value. Cash prizes are paid by PayPal or bank transfer. Winners are responsible for any taxes.</li>
<li><b>Notification.</b> Winners are contacted by email and must reply within 7 days, or an alternate winner may be selected.</li>
<li><b>Publicity.</b> Winners agree that their first name, region and entry may be published on 447766.com and our social channels.</li>
<li><b>Conduct.</b> Entries must be original and lawful, and must not infringe anyone's rights. We may disqualify fraudulent, abusive or duplicate entries.</li>
<li><b>Privacy.</b> Entry data is used to run the contest, as described in our <a href="{b}privacy/">privacy policy</a>.</li>
<li><b>Platforms.</b> Contests are not sponsored, endorsed or administered by, or associated with, YouTube, Google, Meta, TikTok or any other platform.</li>
<li><b>Gambling.</b> Our contests and tools never predict lottery numbers or encourage gambling.</li></ol></div>"""

SUPPORT = """<div class="wrap"><div class="grid g2" style="align-items:start"><div>
<span class="eyebrow">Support 447766</span><h1>Keep the lucky numbers flowing 🧧</h1>
<p class="lead">447766 is free — no paywalls, no sign-ups. Your support pays for operations, new tools, promotion, talented contributors and contest prizes.</p>
<h2>Where your support goes</h2><div class="grid g2">
<div class="card"><h3>⚙️ Operations</h3><p class="micro">Hosting, tools, data and research.</p></div><div class="card"><h3>📣 Promotion &amp; marketing</h3><p class="micro">Reaching more number lovers worldwide.</p></div>
<div class="card"><h3>👩‍💻 Hiring talent</h3><p class="micro">Writers, translators, video editors, developers.</p></div><div class="card"><h3>🏆 Contests &amp; prizes</h3><p class="micro">Growing the monthly prize pool.</p></div></div>
<h2>Supporter perks</h2><ul><li><b>$6.66+/month — Smooth (顺):</b> name in our supporters list and early access to new tools.</li><li><b>$16.80+/month — Prosper (一路发):</b> plus a personal lucky-number calendar each month.</li><li><b>$88+/month — Patron (发发):</b> plus a sponsor credit and a quarterly 1-on-1 number consult.</li></ul>
<h2>Supporters wall</h2><p class="micro">Be one of our founding supporters — your name and lucky wish will appear here (with your permission).</p>
</div>
<div class="card" id="donate"><h2 style="margin-top:0">Choose a lucky amount</h2><div id="goal" style="margin-bottom:16px"></div>
<div class="amounts"></div><input id="custom-amt" type="number" min="1" step="0.01" placeholder="Custom amount (USD)" hidden style="margin-top:10px" aria-label="Custom amount">
<div style="margin-top:14px"><label for="purpose">Direct my support to</label><select id="purpose" name="purpose"><option>General support</option><option>Operations</option><option>Promotions &amp; marketing</option><option>Hiring talent</option><option>Contest prizes</option></select></div>
<label class="check" style="margin-top:12px"><input type="checkbox" id="monthly"> Make it monthly</label>
<button class="btn btn-red btn-block" id="pay-paypal" type="button" style="margin-top:14px">Support with PayPal</button>
<div class="grid g2" style="margin-top:10px"><a class="btn btn-ghost" id="pay-kofi" hidden target="_blank" rel="noopener">Ko-fi</a><a class="btn btn-ghost" id="pay-buymeacoffee" hidden target="_blank" rel="noopener">Buy Me a Coffee</a><a class="btn btn-ghost" id="pay-stripe" hidden target="_blank" rel="noopener">Card (Stripe)</a><a class="btn btn-ghost" id="pay-githubSponsors" hidden target="_blank" rel="noopener">GitHub Sponsors</a></div>
<p class="micro" style="margin-top:12px">Secure checkout by the payment provider. 447766.com is not a registered charity, so support is not tax-deductible.</p>
<hr style="border:0;border-top:1px solid var(--line);margin:18px 0">
<h3>Leave a lucky wish</h3><form class="form" data-form="supporter-wish" data-subject="Supporter wish / pledge" data-success="Thank you! Your wish has been received 🧧">
<div class="row"><div><label for="sw-name">Name (or "Anonymous")</label><input id="sw-name" name="name" required></div><div><label for="sw-email">Email</label><input id="sw-email" type="email" name="email" required></div></div>
<div><label for="sw-msg">Your lucky wish</label><input id="sw-msg" name="wish" maxlength="140" placeholder="May your 4s become 6s!"></div>
<label class="check"><input type="checkbox" name="show_on_wall" value="yes"> Show my name and wish on the supporters wall</label>""" + HP + """
<button class="btn btn-brand btn-block" type="submit">Send my wish</button>""" + MSG + "</form></div></div></div>"

ADVERTISE = """<div class="wrap"><span class="eyebrow">Advertise · Sponsor · Partner</span><h1>Reach people who pay premiums for lucky numbers</h1>
<p class="lead">Our audience chooses phone numbers, plates, wedding dates, business names and domains — and acts on what the numbers say. Put your brand in front of them, in context.</p>
<div class="grid g3" style="margin-top:20px"><div class="card"><h3>👥 Who visits</h3><p class="micro">Chinese-diaspora families, couples planning weddings, small-business owners, domain investors, numerology and angel-number fans, and language learners.</p></div>
<div class="card"><h3>🎯 Contextual intent</h3><p class="micro">Every page is about a decision: which number, which date, which name. Your offer appears at that moment.</p></div>
<div class="card"><h3>📈 Media kit</h3><p class="micro">Traffic, audience regions, email list and YouTube stats are available on request.</p></div></div>
<h2>Sponsorship slots</h2><div class="table-wrap"><table><thead><tr><th>Slot</th><th>Placement</th><th>Ideal for</th></tr></thead><tbody>
<tr><td>Tool sponsor ("presented by")</td><td>Lookup, phone/plate checker, generator</td><td>Telecoms, vanity numbers, auto dealers</td></tr>
<tr><td>Featured lucky domains</td><td>Domains hub + number pages</td><td>Registrars, marketplaces, brokers, escrow</td></tr>
<tr><td>Contest prize sponsor</td><td>Contest page, entry emails, social</td><td>Any brand seeking engagement</td></tr>
<tr><td>Newsletter sponsor</td><td>Daily lucky-number email</td><td>Language apps, feng shui, jewellery, travel</td></tr>
<tr><td>Category takeover</td><td>Weddings / business / zodiac clusters</td><td>Wedding vendors, banks, real estate</td></tr>
<tr><td>Display (programmatic)</td><td>Site-wide ad slots</td><td>Self-serve via Google Ads</td></tr>
<tr><td>Whole-site partnership</td><td>Co-brand, joint venture or acquisition</td><td><a href="{PARTNER}" target="_blank" rel="noopener">Talk to us</a></td></tr>
</tbody></table></div>
<div class="grid g2" style="align-items:start;margin-top:24px"><div><h2 style="margin-top:0">Our principles</h2><ul><li>Every placement is clearly labelled.</li><li>No ads inside tools or results.</li><li>No gambling, lottery, crypto-scheme or deceptive offers.</li><li>Sponsors never change our readings.</li></ul>
<p class="notice">For partnership, domain acquisition or whole-site deals, use our <a href="{PARTNER}" target="_blank" rel="noopener">partnership contact</a>.</p></div>
<div class="lead-box"><h3>Request the rate card</h3><form class="form" data-form="advertise-inquiry" data-subject="Advertising / sponsorship inquiry" data-success="Thanks! We'll send the rate card and availability within 2 business days.">
<div class="row"><div><label for="ad-co">Company</label><input id="ad-co" name="company" required></div><div><label for="ad-name">Your name</label><input id="ad-name" name="name" required></div></div>
<div class="row"><div><label for="ad-email">Work email</label><input id="ad-email" type="email" name="email" required></div><div><label for="ad-site">Website</label><input id="ad-site" name="website" type="url" placeholder="https://"></div></div>
<div class="row"><div><label for="ad-slot">Interested in</label><select id="ad-slot" name="slot"><option>Tool sponsor</option><option>Featured lucky domains</option><option>Contest prize sponsor</option><option>Newsletter sponsor</option><option>Category takeover</option><option>Partnership / acquisition</option></select></div>
<div><label for="ad-budget">Monthly budget</label><select id="ad-budget" name="budget"><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option></select></div></div>
<div><label for="ad-msg">Goals</label><textarea id="ad-msg" name="message"></textarea></div>""" + HP + CONSENT + """
<button class="btn btn-gold btn-block" type="submit">Send Me the Rate Card</button>""" + MSG + "</form></div></div></div>"

CAREERS = """<div class="wrap"><span class="eyebrow">Careers</span><h1>Build the world's home for number culture</h1><p class="lead">We're a remote-first team of writers, linguists, creators and builders. Freelance, contract and partner roles — work from anywhere.</p>
<div class="grid g2" style="margin-top:20px">""" + "".join(
    f'<div class="card"><h3>{t}</h3><p class="micro"><b>{k}</b></p><p>{d}</p><a class="btn btn-ghost btn-sm" href="#apply" onclick="document.getElementById(\'ap-role\').value=\'{t}\'">Apply</a></div>' for t, k, d in ROLES) + """</div>
<section id="apply" class="block"><div class="lead-box" style="max-width:760px;margin:0 auto"><h2>Apply / join our talent pool</h2>
<form class="form" data-form="job-application" data-subject="Job application" data-success="Application received — thank you! We review every application and reply within 7 days.">
<div class="row"><div><label for="ap-name">Full name</label><input id="ap-name" name="name" required></div><div><label for="ap-email">Email</label><input id="ap-email" type="email" name="email" required></div></div>
<div class="row"><div><label for="ap-role">Role</label><select id="ap-role" name="role">""" + "".join(f"<option>{t}</option>" for t, _, _ in ROLES) + """<option>Other / open application</option></select></div><div><label for="ap-loc">Location &amp; time zone</label><input id="ap-loc" name="location"></div></div>
<div class="row"><div><label for="ap-port">Portfolio / LinkedIn / CV link</label><input id="ap-port" name="portfolio" type="url" required placeholder="https://"></div><div><label for="ap-lang">Languages</label><input id="ap-lang" name="languages" placeholder="English, 普通话, 粤语…"></div></div>
<div><label for="ap-why">Why you? (short)</label><textarea id="ap-why" name="message" required></textarea></div>""" + HP + CONSENT + """
<button class="btn btn-gold btn-block" type="submit">Submit Application</button>""" + MSG + "</form></div></section></div>"

GET_REPORT = """<div class="wrap" style="max-width:980px"><div class="grid g2" style="align-items:start;padding:24px 0 48px"><div>
<span class="eyebrow">Free · personal · 2 minutes</span><h1>Your Free Lucky Number Report</h1>
<p class="lead">Find the numbers that work for you — and the ones to avoid — based on Chinese homophones, your zodiac and Western numerology.</p>
<ul><li>✅ Your personal lucky numbers and zodiac numbers to avoid</li><li>✅ A luck check of any number you choose (phone, plate, address, domain)</li><li>✅ The best endings for phone numbers and plates</li><li>✅ Auspicious dates for weddings, launches and moves</li><li>✅ Optional: a consultation with a numerology or feng shui expert</li></ul>
<p class="micro">We never sell your email address. Reports are for entertainment and education.</p></div>
<div class="lead-box"><div class="steps"><span class="on"></span><span></span></div>
<form class="form" data-form="lucky-report" data-steps data-subject="Lucky Report request (full)" data-success="🎉 Done! Your personal lucky-number report is on its way. Check your inbox (and spam folder).">
<div class="step"><h3>Step 1 — where should we send it?</h3>
<div><label for="r-name">First name</label><input id="r-name" name="name" required autocomplete="given-name"></div>
<div><label for="r-email">Email</label><input id="r-email" name="email" type="email" required autocomplete="email"></div>
<div><label for="r-num">Number to check (optional)</label><input id="r-num" name="number" inputmode="numeric" data-prefill="n" placeholder="phone, plate, date…"></div>
<button class="btn btn-gold btn-block" type="button" data-next-step>Continue →</button></div>
<div class="step" hidden><h3>Step 2 — personalise it</h3>
<div class="row"><div><label for="r-by">Birth year</label><input id="r-by" name="birth_year" type="number" min="1900" max="2100"></div><div><label for="r-bd">Birth date (optional)</label><input id="r-bd" name="birth_date" type="date"></div></div>
<div><label for="r-int">I'm choosing a…</label><select id="r-int" name="interest"><option>Phone number</option><option>Licence plate</option><option>Wedding / event date</option><option>Business name or price</option><option>Domain name</option><option>House / apartment</option><option>Just curious</option></select></div>
<div class="row"><div><label for="r-wa">WhatsApp / WeChat (optional)</label><input id="r-wa" name="whatsapp_wechat"></div><div><label for="r-cons">Expert consult?</label><select id="r-cons" name="consult"><option>No, just the report</option><option>Yes — numerology</option><option>Yes — feng shui</option><option>Yes — vanity number / plate sourcing</option></select></div></div>
""" + HP + CONSENT + """<label class="check"><input type="checkbox" name="daily_number" value="yes" checked> Also send me the free daily lucky number</label>
<div style="display:flex;gap:8px"><button class="btn btn-ghost" type="button" data-prev-step style="color:#fff;border-color:rgba(255,255,255,.4)">← Back</button><button class="btn btn-gold" type="submit" style="flex:1">Send My Free Report</button></div></div>
""" + MSG + """<div class="trust"><span>🔒 Private</span><span>✓ Free forever</span><span>✓ Unsubscribe anytime</span></div></form></div></div>
<section id="vanity" class="block" style="padding-top:0"><div class="card"><h2 style="margin-top:0">Request a lucky phone number, plate or address</h2><p>Tell us what you need — we'll connect you with vetted vanity-number and plate specialists in your region.</p>
<form class="form" data-form="vanity-request" data-subject="Vanity number / plate request" data-success="Got it! We'll match you with a specialist and reply within 2 business days.">
<div class="row"><div><label for="v-type">Type</label><select id="v-type" name="type"><option>Phone number</option><option>Licence plate</option><option>Toll-free / business number</option><option>Address / unit</option></select></div><div><label for="v-country">Country / region</label><input id="v-country" name="region" required></div></div>
<div class="row"><div><label for="v-want">Digits or pattern wanted</label><input id="v-want" name="pattern" placeholder="e.g. ends in 8888, contains 168"></div><div><label for="v-budget">Budget</label><select id="v-budget" name="budget"><option>Under $100</option><option>$100–$1,000</option><option>$1,000–$10,000</option><option>$10,000+</option></select></div></div>
<div class="row"><div><label for="v-name">Name</label><input id="v-name" name="name" required></div><div><label for="v-email">Email</label><input id="v-email" type="email" name="email" required></div></div>""" + HP + CONSENT + """
<button class="btn btn-red" type="submit">Find My Lucky Number</button>""" + MSG + "</form></div></section></div>"

ABOUT = """<div class="wrap prose"><h1>About 447766</h1><p class="lead">447766 is The Lucky Number Lab — an independent publication that explains how numbers carry meaning across cultures, starting with Chinese numerology and Western angel numbers.</p>
<h2>Our story</h2><p>In Chinese, 447766 reads as 死死·七七·顺顺: endings → rising → smooth success. We chose it as a reminder that numbers are stories, and that stories can change. <a href="{b}guides/447766-meaning/">Read the full story</a>.</p>
<h2 id="methodology">How we score numbers</h2><ul><li><b>Digit weights</b> come from traditional homophones: 8 (+4), 6 and 9 (+3), 2 (+2), 1 and 3 (+1), 0, 5 and 7 (neutral), 4 (−4).</li><li><b>Position:</b> the final digit counts 1.5×, because endings matter most for phone numbers and prices.</li><li><b>Patterns:</b> repeated lucky digits earn bonuses; repeated 4s cost extra.</li><li><b>Known combinations</b> (168, 520, 1314, 14, 250…) override the arithmetic with their established meaning.</li><li><b>Western numerology</b> uses standard digit-sum reduction, keeping the master numbers 11, 22 and 33.</li></ul>
<h2>Editorial standards</h2><p>We cite cultural sources, note Mandarin vs Cantonese differences, and correct mistakes quickly. Native speakers review sensitive topics. Sponsors never influence readings.</p>
<h2>Corrections</h2><p>Spotted an error or a dialect nuance we missed? <a href="{b}contact/">Tell us</a>.</p>
<h2>Partnerships</h2><p>Interested in this website, the domain name, sponsorship, advertising or a partnership? <a href="{PARTNER}" target="_blank" rel="noopener">Contact us here</a>.</p></div>"""

CONTACT = """<div class="wrap"><h1>Contact 447766</h1><p class="lead">We read every message. For website, domain, sponsorship, advertising or partnership inquiries, you can also use our <a href="{PARTNER}" target="_blank" rel="noopener">partnership contact</a>.</p>
<div class="grid g2" style="align-items:start;margin-top:20px"><div class="lead-box"><form class="form" data-form="contact" data-subject="Contact form" data-success="Message sent — thank you! We reply within 2 business days.">
<div class="row"><div><label for="c-name">Name</label><input id="c-name" name="name" required></div><div><label for="c-email">Email</label><input id="c-email" type="email" name="email" required></div></div>
<div><label for="c-topic">Topic</label><select id="c-topic" name="topic"><option>General question</option><option>Correction / cultural note</option><option>Advertising / sponsorship</option><option>Partnership / domain inquiry</option><option>Press</option><option>Contest question</option><option>Privacy request</option></select></div>
<div><label for="c-msg">Message</label><textarea id="c-msg" name="message" required></textarea></div>""" + HP + CONSENT + """
<button class="btn btn-gold btn-block" type="submit">Send Message</button>""" + MSG + """</form></div>
<div class="grid"><a class="card" href="{b}advertise/"><h3>📣 Advertise</h3><p class="micro">Rate card and sponsor slots.</p></a><a class="card" href="{PARTNER}" target="_blank" rel="noopener"><h3>🤝 Website / domain / partnership</h3><p class="micro">Acquisition, joint venture or co-branding.</p></a><a class="card" href="{b}careers/"><h3>💼 Careers</h3><p class="micro">Join the team.</p></a><a class="card" href="#" data-mail="Inquiry from 447766.com"><h3>✉️ Email us</h3><p class="micro">Opens your email app.</p></a></div></div></div>"""

PRIVACY = """<div class="wrap prose"><h1>Privacy Policy</h1><p class="micro">Last updated <span data-year>2026</span>.</p>
<p>447766.com ("we") respects your privacy. This policy explains what we collect, why we collect it, and your choices.</p>
<h2>What we collect</h2><ul><li><b>Form submissions</b> (report requests, appraisals, contest entries, applications, messages): the details you enter, such as your name, email, numbers and preferences.</li><li><b>Tool inputs:</b> numbers you type into our tools are processed in your browser and are not sent to us unless you submit a form.</li><li><b>Usage data:</b> if you accept cookies, analytics records pages visited, device type and approximate location.</li></ul>
<h2>How forms are delivered</h2><p>Forms are sent through FormSubmit, a third-party form-forwarding service, to our private inbox. Payments are handled entirely by PayPal or the other payment provider you choose; we never see your card details.</p>
<h2>Advertising &amp; cookies</h2><p>We may use Google AdSense. Google and its partners use cookies to serve ads based on your visits to this and other sites. You can opt out of personalised advertising at Google's <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Ads Settings</a> or at <a href="https://www.aboutads.info" target="_blank" rel="noopener">aboutads.info</a>. Embedded YouTube videos load through the privacy-enhanced youtube-nocookie.com player, and only when you press play.</p>
<h2>How we use data</h2><p>We use your data to deliver what you asked for (your report, a reply, contest administration), to send emails you opted into, and to improve the site. We do not sell your personal information. With your explicit consent, we may introduce you to a vetted partner (for example a consultant or broker) about your request.</p>
<h2>Your rights</h2><p>Depending on where you live (for example under GDPR, the CCPA/CPRA, PIPEDA or Québec's Law 25), you may access, correct, delete or port your data, and withdraw consent. Make a request through our <a href="{b}contact/">contact page</a>.</p>
<h2>Retention &amp; security</h2><p>We keep data only as long as needed for the purposes above. The site is served over HTTPS.</p>
<h2>Children</h2><p>The site is not directed at children under 13. Contests require the age of majority.</p>
<h2>Changes</h2><p>We will post updates on this page.</p></div>"""

TERMS = """<div class="wrap prose"><h1>Terms of Use</h1><p class="micro">Last updated <span data-year>2026</span>.</p>
<ol><li><b>Acceptance.</b> By using 447766.com you agree to these terms.</li>
<li><b>Entertainment and education.</b> Number readings, scores and generated numbers reflect cultural traditions and numerology conventions. They are not financial, legal, medical or investment advice, and they are not lottery or gambling predictions.</li>
<li><b>Your content.</b> When you submit entries, wishes or messages, you grant us a non-exclusive licence to use them as described (for example, publishing contest winners). You confirm you have the right to submit them.</li>
<li><b>Acceptable use.</b> No scraping that harms performance, no spam, no abuse of forms or contests, and no unlawful content.</li>
<li><b>Intellectual property.</b> Original text, tools, code and design are © 447766.com. Third-party marks and embedded content belong to their owners. See our <a href="{b}disclaimer/">disclaimer and trademark notice</a>.</li>
<li><b>Third-party services.</b> Links, embeds, ads and payment providers are governed by their own terms.</li>
<li><b>Donations.</b> Support is voluntary, non-refundable except where the law requires otherwise, and not tax-deductible.</li>
<li><b>Disclaimer of warranties.</b> The site is provided "as is", without warranties.</li>
<li><b>Limitation of liability.</b> To the extent the law permits, we are not liable for decisions made based on the site's content.</li>
<li><b>Governing law.</b> The laws of the Province of Québec and the federal laws of Canada that apply there.</li>
<li><b>Contact.</b> Through our <a href="{b}contact/">contact page</a>.</li></ol></div>"""

DISCLAIMER = """<div class="wrap prose"><h1>Disclaimer, Trademark &amp; Copyright Disclosure</h1>
<h2>Trademark disclosure</h2><p>447766.com is an independent publication. The number sequence "447766" is used solely as a numeric domain name and descriptive identifier. We claim no exclusive rights to the number sequence itself, and we do not intend to infer or suggest any affiliation with any company, product, phone number or mark that may contain these digits. Our logo — six digits on a teal tile — is original.</p>
<p>All third-party names, trademarks, service marks and logos mentioned on this site — including but not limited to Google, AdSense, YouTube, PayPal, Ko-fi, Buy Me a Coffee, Stripe, GitHub, NetEase, Qihoo 360, 58.com, 4399, Alibaba, Sedo and Afternic — are the property of their respective owners. They are mentioned for identification, commentary and reporting purposes only, and their mention does not imply endorsement, sponsorship or affiliation.</p>
<h2>Copyright</h2><p>Original articles, number data compilations, scoring methodology, tools, code and site design © <span data-year>2026</span> 447766.com. All rights reserved. You may quote short excerpts with a link back. Embedded YouTube videos are displayed with the official YouTube player under YouTube's Terms of Service and remain the property of their creators. Facts about public sales and events are cited from public reporting.</p>
<p>If you believe content on this site infringes your rights, contact us through the <a href="{b}contact/">contact page</a> (choose "Privacy request" or "Correction"). We respond promptly to valid notices, including DMCA notices.</p>
<h2>Content disclaimer</h2><p>Readings and scores are for entertainment and educational purposes. Cultural interpretations vary by dialect, region and family tradition. Nothing here is financial, investment, legal or medical advice, or a prediction of future events. Domain market figures are historical, sourced from public reports, and may not reflect current prices.</p>
<h2>Advertising &amp; affiliate disclosure</h2><p>This site may display advertising (including Google AdSense) and may earn from sponsorships, affiliate links and referrals. Sponsored content and ads are labelled. Compensation never changes our readings.</p></div>"""

PAGES = [
    dict(path="", title="447766 · The Lucky Number Lab — Chinese Number Meanings, Lucky Numbers & Angel Numbers", desc="Decode any number: Chinese meaning, luck score, Cantonese reading and angel-number meaning. Free lucky-number tools, zodiac numbers, guides and contests.", inner=HOME, bare=True),
    dict(path="lookup/", title="Number Meaning Lookup — Is My Number Lucky? | 447766", desc="Enter any number to see its Chinese meaning, luck score, Mandarin and Cantonese reading, and Western numerology. Free and instant.", inner=LOOKUP, trail=[("Number lookup", None)]),
    dict(path="tools/", title="Free Lucky Number Tools: Phone, Plate, Zodiac, Generator | 447766", desc="Free lucky-number tools: phone, plate and address checker, zodiac lucky numbers, life path, lucky number generator and name numerology.", inner=TOOLS, active="tools/", trail=[("Tools", None)]),
    dict(path="zodiac/", title="Chinese Zodiac Lucky Numbers & Colours for All 12 Animals | 447766", desc="Lucky and unlucky numbers, colours and years for the Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog and Pig.", inner=ZODIAC, active="zodiac/", trail=[("Zodiac", None)]),
    dict(path="domains/", title="Numeric Domains & Lucky Numbers: Values, Sales, Free Appraisal | 447766", desc="How Chinese buyers value numeric domains — lucky digits, the 6N.com boom, record sales — plus a free lucky-domain appraisal.", inner=DOMAINS, active="domains/", trail=[("Domains", None)]),
    dict(path="videos/", title="Videos: Chinese Lucky & Unlucky Numbers Explained | 447766", desc="The best videos explaining Chinese lucky numbers, the unlucky 4, number slang and Cantonese number meanings.", inner=VIDEOS_PAGE, active="videos/", trail=[("Videos", None)]),
    dict(path="contests/", title="Lucky Number Challenge — Contests & Prizes | 447766", desc="Enter the monthly Lucky Number Challenge: pick a lucky number, tell us why, and win prizes. No purchase necessary.", inner=CONTESTS, active="contests/", trail=[("Contests", None)]),
    dict(path="contest-rules/", title="Official Contest Rules | 447766", desc="Official rules for 447766.com contests, including eligibility, the skill-testing question and the Québec clause.", inner=RULES, trail=[("Contest rules", None)]),
    dict(path="support/", title="Support 447766 — Donate a Lucky Amount | 447766", desc="Keep 447766 free. Donate $1.68, $6.66 or $8.88 to fund operations, new tools, promotion, talent and contest prizes.", inner=SUPPORT, active="support/", noads=True, trail=[("Support", None)]),
    dict(path="advertise/", title="Advertise & Sponsor — Reach Lucky-Number Buyers | 447766", desc="Sponsor tools, contests, newsletters and lucky-domain listings on 447766.com. Request the rate card.", inner=ADVERTISE, trail=[("Advertise", None)]),
    dict(path="careers/", title="Careers at 447766 — Writers, Translators, Creators, Developers", desc="Remote freelance and partner roles: Chinese culture writers, translators, Shorts editors, SEO, community, sponsorship sales and developers.", inner=CAREERS, trail=[("Careers", None)]),
    dict(path="get-report/", title="Free Lucky Number Report — Personalised to You | 447766", desc="Get your free personal lucky-number report: zodiac numbers, numbers to avoid, the best phone and plate endings, and lucky dates.", inner=GET_REPORT, noads=True, trail=[("Free lucky report", None)]),
    dict(path="about/", title="About 447766 & How We Score Numbers", desc="Who we are, the 447766 story, our number-scoring methodology and editorial standards.", inner=ABOUT, trail=[("About", None)]),
    dict(path="contact/", title="Contact 447766", desc="Contact 447766.com — questions, corrections, advertising, partnerships and press.", inner=CONTACT, noads=True, trail=[("Contact", None)]),
    dict(path="privacy/", title="Privacy Policy | 447766", desc="How 447766.com collects, uses and protects your information.", inner=PRIVACY, noads=True, trail=[("Privacy", None)]),
    dict(path="terms/", title="Terms of Use | 447766", desc="Terms of use for 447766.com.", inner=TERMS, noads=True, trail=[("Terms", None)]),
    dict(path="disclaimer/", title="Disclaimer, Trademark & Copyright Disclosure | 447766", desc="Trademark and copyright disclosure, content disclaimer and advertising disclosure for 447766.com.", inner=DISCLAIMER, noads=True, trail=[("Disclaimer", None)]),
]
