/* 447766 Number Engine — pure functions shared by the browser and the build script.
   Readings are traditional/cultural associations, for entertainment and education. */
(function (root) {
  "use strict";

  var DIGITS = {
    "0": { hz: "零", py: "líng", jp: "ling4", sounds: "你 (nǐ, 'you') in text slang; 灵 'spirit'", meaning: "Wholeness, origin, potential. In number slang 0 often stands for 'you' (520 = I love you).", w: 0, angel: "infinite potential and a fresh start", theme: "Potential" },
    "1": { hz: "一", py: "yī", jp: "jat1", sounds: "要 (yào, 'want/will'); 一 'one, unity'", meaning: "Unity and leadership; the 'single' of 1314 (一生一世, a whole lifetime).", w: 1, angel: "new beginnings and leadership", theme: "Beginnings" },
    "2": { hz: "二", py: "èr", jp: "ji6", sounds: "易 (Cantonese ji6, 'easy'); 爱 'love' in slang (520)", meaning: "'Good things come in pairs' (好事成双). Favoured for weddings and gifts.", w: 2, angel: "balance, partnership and trust", theme: "Harmony" },
    "3": { hz: "三", py: "sān", jp: "saam1", sounds: "生 (Cantonese saang1, 'life, birth'); 散 'scatter' in Mandarin", meaning: "Life and growth, especially in Cantonese. Three is also the number of heaven, earth and humanity.", w: 1, angel: "creativity, expression and growth", theme: "Life" },
    "4": { hz: "四", py: "sì", jp: "sei3", sounds: "死 (sǐ / sei2, 'death')", meaning: "Widely avoided (tetraphobia): floors, phone numbers and plates skip it. In Teochew and Shanghainese it can sound like 'happiness'.", w: -4, angel: "stability, foundations and protection", theme: "Endings" },
    "5": { hz: "五", py: "wǔ", jp: "ng5", sounds: "我 (wǒ, 'me') in slang; 唔/无 'not / none' in Cantonese", meaning: "The Five Elements (五行) — balance. Mixed: 'me' in love codes, 'not' in Cantonese.", w: 0, angel: "change, freedom and adventure", theme: "Change" },
    "6": { hz: "六", py: "liù", jp: "luk6", sounds: "溜/流 (liū, 'smooth, flowing'); 禄 (luk6, 'prosperity')", meaning: "Smooth progress — 六六大顺 'everything goes smoothly'. Loved by businesses and online as 666 ('awesome').", w: 3, angel: "home, care and responsibility", theme: "Smoothness" },
    "7": { hz: "七", py: "qī", jp: "cat1", sounds: "起 'rise', 齐 'together', 气 'vital energy' — also 欺 'deceive'", meaning: "Change and rising. The 7th day of the 7th month is Qixi (Chinese Valentine's Day); the 7th month is also Ghost Month.", w: 0, angel: "spiritual insight and inner wisdom", theme: "Rising" },
    "8": { hz: "八", py: "bā", jp: "baat3", sounds: "发 (fā / faat3, 'prosper, get rich')", meaning: "The luckiest digit — wealth and success. The Beijing Olympics opened 8/8/08 at 8:08 pm.", w: 4, angel: "abundance, power and achievement", theme: "Prosperity" },
    "9": { hz: "九", py: "jiǔ", jp: "gau2", sounds: "久 (jiǔ, 'long-lasting')", meaning: "Longevity and eternity; the emperor's number. Popular for weddings and anniversaries.", w: 3, angel: "completion, wisdom and service", theme: "Longevity" }
  };

  /* Known combos: s = sentiment (+2 very lucky, +1 lucky, 0 neutral, -1 unlucky, -2 very unlucky) */
  var COMBOS = {
    "447766": { hz: "死死·七七·顺顺", s: 1, m: "The comeback code: 44 (endings) → 77 (rising, change) → 66 (smooth success). Read as a whole, it is a story of turning bad luck into good — 'turn your 4s into 6s'." },
    "168": { hz: "一路发", s: 2, m: "'Prosperity all the way' (yī lù fā). A favourite for shop phone numbers, prices and business openings." },
    "518": { hz: "我要发", s: 2, m: "'I will prosper' (wǒ yào fā). Popular in business numbers and opening dates." },
    "520": { hz: "我爱你", s: 2, m: "'I love you' (wǔ èr líng ≈ wǒ ài nǐ). 20 May (5/20) is China's internet Valentine's Day." },
    "521": { hz: "我愿意", s: 2, m: "'I do / I'm willing' — the answer to 520." },
    "530": { hz: "我想你", s: 1, m: "'I miss you'." },
    "1314": { hz: "一生一世", s: 2, m: "'One life, one lifetime' — forever. Hugely popular in weddings; 4 here is read as 世 'lifetime', not death." },
    "5201314": { hz: "我爱你一生一世", s: 2, m: "'I love you for a lifetime.' Couples transfer ¥520 or ¥1,314 as love tokens." },
    "3344": { hz: "生生世世", s: 2, m: "'Life after life, forever' — another wedding favourite where 4 escapes its curse." },
    "9420": { hz: "就是爱你", s: 2, m: "'It's just you I love.'" },
    "88": { hz: "发发 / 拜拜", s: 2, m: "Double prosperity (发发). In chat it also means 'bye-bye'." },
    "888": { hz: "发发发", s: 2, m: "Triple prosperity — wealth on wealth." },
    "8888": { hz: "发发发发", s: 2, m: "Ultimate prosperity. Sichuan Airlines paid ¥2.33M for +86 28 8888 8888." },
    "666": { hz: "溜溜溜", s: 2, m: "'Smooth!' / 'Awesome!' — praise in Chinese gaming and internet slang. Unlike the West, no devilish meaning." },
    "6666": { hz: "六六六六", s: 2, m: "Super smooth — an amplified 666." },
    "66": { hz: "六六大顺", s: 2, m: "'Everything goes smoothly' — one of the most common blessings." },
    "99": { hz: "久久", s: 2, m: "'Forever and ever' — 9/9 is the Double Ninth (Chongyang) Festival honouring elders." },
    "999": { hz: "久久久", s: 2, m: "Eternal — popular for 999 roses and long-lasting love." },
    "9999": { hz: "久久久久", s: 2, m: "Everlasting." },
    "1688": { hz: "一路发发", s: 2, m: "'Prosperity all the way, doubled.'" },
    "6688": { hz: "顺顺发发", s: 2, m: "Smooth and prosperous." },
    "6868": { hz: "顺发顺发", s: 2, m: "Smooth prosperity, repeated." },
    "28": { hz: "易发", s: 2, m: "'Easy prosperity' (Cantonese ji6 faat3). Hong Kong plate '28' sold for HK$18.1M." },
    "18": { hz: "要发 / 实发", s: 2, m: "'Will prosper' / 'surely prosper'. Hong Kong plate '18' sold for HK$16.5M." },
    "168888": { hz: "一路发发发发", s: 2, m: "Prosperity all the way, multiplied." },
    "1666": { hz: "一路顺顺顺", s: 2, m: "Smooth all the way." },
    "58": { hz: "我发 / 唔发", s: 0, m: "'I prosper' in Mandarin slang, but 'won't prosper' in Cantonese — a classic dialect split (58.com)." },
    "54": { hz: "唔死", s: 1, m: "'Won't die' in Cantonese — a 4 that turns lucky." },
    "51": { hz: "我要", s: 1, m: "'I want' — hence 51job.com ('I want a job')." },
    "13": { hz: "实生", s: 0, m: "Unlucky in the West, but 'sure to live' (实生) in Cantonese." },
    "14": { hz: "要死 / 实死", s: -2, m: "'Want to die' / 'sure death'. Many buildings skip floor 14." },
    "24": { hz: "易死", s: -2, m: "'Easy death' in Cantonese." },
    "74": { hz: "气死 / 去死", s: -2, m: "'Furious to death' / 'go die'." },
    "94": { hz: "就是 / 九死", s: 0, m: "Internet slang for 'exactly' (就是), but also 'nine deaths' (九死一生)." },
    "514": { hz: "我要死", s: -2, m: "'I'm going to die' — avoided." },
    "748": { hz: "去死吧", s: -2, m: "'Go to hell' — an insult in chat slang." },
    "7456": { hz: "气死我了", s: -1, m: "'I'm so angry!' — chat slang." },
    "250": { hz: "二百五", s: -1, m: "'Idiot / half-wit' — a famous insult. Never price a gift at 250." },
    "38": { hz: "三八", s: -1, m: "An insult for a gossipy woman — though 3/8 is also International Women's Day." },
    "886": { hz: "拜拜了", s: 0, m: "'Bye-bye!' in chat slang." },
    "55": { hz: "呜呜", s: 0, m: "Crying sound 'boo-hoo'." },
    "555": { hz: "呜呜呜", s: 0, m: "Crying sound — sad in chat slang (the opposite of the West's 'angel number 555')." },
    "233": { hz: "哈哈", s: 1, m: "LOL — from emoticon #233 on the Mop forum (a laughing face)." },
    "77": { hz: "七七 / 七夕", s: 0, m: "Qixi (Double Seventh) — Chinese Valentine's Day — but 七七 is also the 49-day mourning rite." },
    "49": { hz: "七七四十九", s: -1, m: "The 49th-day mourning period; 'four-nine' also sounds like 死久 'dead for long'." },
    "44": { hz: "死死", s: -2, m: "'Death, death' — the most avoided pair. Teochew speakers are the exception." },
    "444": { hz: "死死死", s: -2, m: "Triple death in Chinese tradition — the opposite of the West, where 444 is a popular 'angel number' of protection." },
    "4444": { hz: "死死死死", s: -2, m: "Extremely avoided in Chinese culture; a 'protection' angel number in the West." },
    "1111": { hz: "光棍节 / 双十一", s: 1, m: "Singles' Day (11/11) — now the world's biggest shopping festival." },
    "8848": { hz: "珠峰", s: 1, m: "The height of Mount Everest (8,848 m) — a symbol of peak achievement (and a phone brand)." },
    "2828": { hz: "易发易发", s: 2, m: "'Easy prosperity, easy prosperity' (Cantonese)." },
    "8": { hz: "发", s: 2, m: "Prosperity — the luckiest single digit in Chinese culture." },
    "4": { hz: "死", s: -2, m: "Sounds like death — the most avoided digit in Chinese culture." },
    "6": { hz: "顺", s: 2, m: "Smooth progress and prosperity." },
    "9": { hz: "久", s: 2, m: "Long-lasting — longevity and eternal love." },
    "7": { hz: "起", s: 0, m: "Rising and change — Qixi romance, but also Ghost Month." }
  };

  var ZODIAC = [
    { a: "Rat", hz: "鼠", lucky: [2, 3], unlucky: [5, 9], colors: "blue, gold, green" },
    { a: "Ox", hz: "牛", lucky: [1, 4], unlucky: [5, 6], colors: "white, yellow, green" },
    { a: "Tiger", hz: "虎", lucky: [1, 3, 4], unlucky: [6, 7, 8], colors: "blue, grey, orange" },
    { a: "Rabbit", hz: "兔", lucky: [3, 4, 6], unlucky: [1, 7, 8], colors: "red, pink, purple, blue" },
    { a: "Dragon", hz: "龙", lucky: [1, 6, 7], unlucky: [3, 8], colors: "gold, silver, grey" },
    { a: "Snake", hz: "蛇", lucky: [2, 8, 9], unlucky: [1, 6, 7], colors: "black, red, yellow" },
    { a: "Horse", hz: "马", lucky: [2, 3, 7], unlucky: [1, 5, 6], colors: "yellow, green" },
    { a: "Goat", hz: "羊", lucky: [3, 4, 9], unlucky: [6, 7, 8], colors: "brown, red, purple" },
    { a: "Monkey", hz: "猴", lucky: [1, 7, 8], unlucky: [2, 5, 9], colors: "white, blue, gold" },
    { a: "Rooster", hz: "鸡", lucky: [5, 7, 8], unlucky: [1, 3, 9], colors: "gold, brown, yellow" },
    { a: "Dog", hz: "狗", lucky: [3, 4, 9], unlucky: [1, 6, 7], colors: "red, green, purple" },
    { a: "Pig", hz: "猪", lucky: [2, 5, 8], unlucky: [1, 7], colors: "yellow, grey, brown, gold" }
  ];

  var ANGEL_LIFE = {
    "0": { love: "an open heart and room for something new", career: "a blank canvas — the right moment to start", spirit: "connection to the whole" },
    "1": { love: "taking the first step and being honest about what you want", career: "initiative, launching, leading", spirit: "your thoughts shaping reality" },
    "2": { love: "patience, partnership and mutual trust", career: "collaboration and diplomacy", spirit: "faith that things are aligning" },
    "3": { love: "playfulness and open communication", career: "creative projects and self-expression", spirit: "growth and encouragement" },
    "4": { love: "building something steady and loyal", career: "discipline, systems and hard work paying off", spirit: "protection and solid foundations" },
    "5": { love: "change, excitement and honest freedom", career: "pivoting, travel and new opportunities", spirit: "letting go of what no longer fits" },
    "6": { love: "nurturing, home and family", career: "service, responsibility and balance", spirit: "care for yourself and others" },
    "7": { love: "deeper understanding and soul connection", career: "research, study and specialised expertise", spirit: "intuition and inner wisdom" },
    "8": { love: "confident, equal partnership", career: "money, power and earned success", spirit: "karma — what you give returns" },
    "9": { love: "compassion and closing old chapters", career: "finishing projects and mentoring", spirit: "completion and humanitarian purpose" }
  };

  function clean(n) { return String(n == null ? "" : n).replace(/[^0-9]/g, ""); }

  function reduce(n) {
    var s = clean(n); if (!s) return null;
    var steps = [s];
    var v = s.split("").reduce(function (a, d) { return a + +d; }, 0);
    steps.push(String(v));
    while (v > 9 && v !== 11 && v !== 22 && v !== 33) {
      v = String(v).split("").reduce(function (a, d) { return a + +d; }, 0);
      steps.push(String(v));
    }
    return { root: v, steps: steps };
  }

  function findCombos(s) {
    var found = [];
    Object.keys(COMBOS).forEach(function (k) {
      if (k.length >= 2 && k !== s && s.indexOf(k) !== -1) found.push(k);
    });
    found.sort(function (a, b) { return b.length - a.length; });
    // drop combos fully contained in a longer found combo
    var out = [];
    found.forEach(function (k) { if (!out.some(function (o) { return o.indexOf(k) !== -1; })) out.push(k); });
    return out.slice(0, 6);
  }

  function score(n) {
    var s = clean(n); if (!s) return null;
    if (COMBOS[s] && s.length > 1) {
      var base = { "2": 92, "1": 76, "0": 55, "-1": 30, "-2": 12 }[String(COMBOS[s].s)];
      if (s === "447766") base = 74;
      return base;
    }
    var total = 0, max = 0;
    for (var i = 0; i < s.length; i++) {
      var w = DIGITS[s[i]].w, mult = (i === s.length - 1) ? 1.5 : 1;
      total += w * mult; max += 4 * mult;
    }
    // runs of lucky digits
    var runs = s.match(/(8{2,}|6{2,}|9{2,})/g); if (runs) runs.forEach(function (r) { total += r.length * 1.5; max += r.length * 1.5; });
    var fours = s.match(/4{2,}/g); if (fours) fours.forEach(function (r) { total -= r.length * 1.5; });
    findCombos(s).forEach(function (k) { total += COMBOS[k].s * 2.5; max += 5; });
    var min = -max;
    var pct = Math.round(((total - min) / (max - min)) * 100);
    if (s.indexOf("4") === -1) pct = Math.max(pct, 50);
    return Math.max(3, Math.min(99, pct));
  }

  function verdict(sc) {
    if (sc >= 85) return { label: "Very lucky", key: "vlucky", hz: "大吉" };
    if (sc >= 65) return { label: "Lucky", key: "lucky", hz: "吉" };
    if (sc >= 45) return { label: "Neutral", key: "neutral", hz: "平" };
    if (sc >= 25) return { label: "Unlucky", key: "unlucky", hz: "凶" };
    return { label: "Very unlucky", key: "vunlucky", hz: "大凶" };
  }

  function counts(s) { var c = {}; s.split("").forEach(function (d) { c[d] = (c[d] || 0) + 1; }); return c; }

  function dominant(s) {
    var c = counts(s), best = s[0];
    Object.keys(c).forEach(function (d) { if (c[d] > c[best]) best = d; });
    return best;
  }

  function hanzi(s) { return s.split("").map(function (d) { return DIGITS[d].hz; }).join(""); }
  function pinyin(s) { return s.split("").map(function (d) { return DIGITS[d].py; }).join(" "); }
  function jyutping(s) { return s.split("").map(function (d) { return DIGITS[d].jp; }).join(" "); }

  function chineseReading(s) {
    if (COMBOS[s]) return COMBOS[s].m;
    if (s.length === 1) return DIGITS[s].meaning;
    var c = counts(s), parts = [];
    var combos = findCombos(s);
    if (combos.length) parts.push("It contains " + combos.map(function (k) { return k + " (" + COMBOS[k].hz + ")"; }).join(", ") + ".");
    if (c["8"]) parts.push(c["8"] > 1 ? "Multiple 8s (发) amplify prosperity." : "The 8 (发) brings a prosperity boost.");
    if (c["6"]) parts.push("6 (顺) adds smooth progress.");
    if (c["9"]) parts.push("9 (久) adds longevity.");
    if (c["4"]) parts.push(c["4"] > 1 ? "The repeated 4s (死) are a red flag for traditional Chinese buyers — expect a discount on phone numbers, plates or domains." : "The 4 (死) is a minus for many Chinese speakers, especially in the final position.");
    if (s[s.length - 1] === "8" || s[s.length - 1] === "6" || s[s.length - 1] === "9") parts.push("Ending on " + s[s.length - 1] + " is considered a strong finish.");
    if (s[s.length - 1] === "4") parts.push("Ending on 4 is the weakest possible finish.");
    if (!parts.length) parts.push("A balanced, low-risk number with no strong lucky or unlucky signals.");
    return parts.join(" ");
  }

  function angelReading(s) {
    var d = dominant(s), c = counts(s), uniq = Object.keys(c).length;
    var r = reduce(s);
    var intro = (uniq === 1 && s.length > 1)
      ? "A repeating sequence of " + d + " amplifies its message of " + DIGITS[d].angel + "."
      : "Led by " + d + " (" + DIGITS[d].angel + ")" + (uniq > 1 ? ", blended with " + Object.keys(c).filter(function (x) { return x !== d; }).slice(0, 3).map(function (x) { return x + " (" + DIGITS[x].theme.toLowerCase() + ")"; }).join(", ") : "") + ".";
    var root = r && r.root < 10 ? " It reduces to " + r.root + ", the number of " + DIGITS[String(r.root)].angel + "." : (r ? " It reduces to the master number " + r.root + " — heightened intuition and purpose." : "");
    var L = ANGEL_LIFE[d], R = (r && r.root < 10) ? ANGEL_LIFE[String(r.root)] : ANGEL_LIFE[d];
    return { summary: intro + root, love: "In love: " + L.love + "; at its core, " + R.love + ".", career: "In work and money: " + L.career + ", with an undertone of " + R.career + ".", spirit: "Spiritually: " + L.spirit + " — and " + R.spirit + "." };
  }

  function bestUses(s, sc) {
    var u = [];
    if (sc >= 80) u.push("Business phone numbers, shop prices and opening dates", "Licence plates and house numbers", "Domain names for Chinese-speaking audiences");
    else if (sc >= 60) u.push("Personal phone numbers and passwords you want to remember", "Prices and promotions", "Apartment or unit numbers");
    else if (sc >= 45) u.push("Everyday use — neutral for most audiences", "Western branding where Chinese numerology matters less");
    else u.push("Avoid for gifts, prices, plates or business numbers aimed at Chinese customers", "Fine for Western audiences, where 4 is often read as stability");
    if (/520|1314|521|3344|9420|99/.test(s)) u.unshift("Weddings, anniversaries, proposals and love gifts");
    return u;
  }

  function suggest(n) {
    // find a luckier variant by swapping 4s and weak digits
    var s = clean(n); if (!s) return [];
    var map = { "4": ["6", "8", "9"], "0": ["8"], "5": ["6", "8"], "7": ["9", "8"], "3": ["8"], "1": ["6"], "2": ["8"] };
    var out = {};
    for (var i = s.length - 1; i >= 0 && Object.keys(out).length < 8; i--) {
      (map[s[i]] || []).forEach(function (r) { var v = s.slice(0, i) + r + s.slice(i + 1); out[v] = score(v); });
    }
    if (s.indexOf("4") !== -1) { var all = s.replace(/4/g, "6"); out[all] = score(all); var all8 = s.replace(/4/g, "8"); out[all8] = score(all8); }
    return Object.keys(out).map(function (k) { return { n: k, score: out[k] }; }).filter(function (x) { return x.score > score(s); })
      .sort(function (a, b) { return b.score - a.score; }).slice(0, 5);
  }

  function analyze(n) {
    var s = clean(n); if (!s) return null;
    if (s.length > 20) s = s.slice(0, 20);
    var sc = score(s);
    return {
      n: s, score: sc, verdict: verdict(sc), hanzi: COMBOS[s] ? COMBOS[s].hz : hanzi(s), digitsHz: hanzi(s), pinyin: pinyin(s), jyutping: jyutping(s),
      digits: s.split("").map(function (d, i) { var x = DIGITS[d]; return { d: d, hz: x.hz, py: x.py, jp: x.jp, sounds: x.sounds, w: x.w, pos: i }; }),
      combos: findCombos(s).map(function (k) { return { n: k, hz: COMBOS[k].hz, s: COMBOS[k].s, m: COMBOS[k].m }; }),
      known: COMBOS[s] || null,
      chinese: chineseReading(s), reduce: reduce(s), angel: angelReading(s), uses: bestUses(s, sc), suggestions: suggest(s)
    };
  }

  function zodiacFor(year) {
    var y = parseInt(year, 10); if (!y) return null;
    var i = ((y - 4) % 12 + 12) % 12; var z = ZODIAC[i];
    return { animal: z.a, hz: z.hz, lucky: z.lucky, unlucky: z.unlucky, colors: z.colors, index: i };
  }

  function nameNumber(name) {
    var t = String(name || "").toLowerCase().replace(/[^a-z]/g, ""); if (!t) return null;
    var sum = 0, v = 0, c = 0, vowels = "aeiou";
    for (var i = 0; i < t.length; i++) { var x = ((t.charCodeAt(i) - 97) % 9) + 1; sum += x; if (vowels.indexOf(t[i]) > -1) v += x; else c += x; }
    function r(k) { while (k > 9 && k !== 11 && k !== 22 && k !== 33) k = String(k).split("").reduce(function (a, d) { return a + +d; }, 0); return k; }
    return { expression: r(sum), soulUrge: r(v), personality: r(c) };
  }

  function lifePath(dateStr) {
    var s = clean(dateStr); if (s.length < 8) return null;
    return reduce(s).root;
  }

  function generate(mode, len, seed) {
    len = Math.max(1, Math.min(12, parseInt(len, 10) || 6));
    var rnd = seed ? mulberry(hash(String(seed))) : Math.random;
    var pools = { chinese: "8889966621", avoid4: "012356789", random: "0123456789", lucky: "8869" };
    var pool = pools[mode] || pools.chinese, out = [];
    for (var k = 0; k < 6; k++) {
      var s = ""; for (var i = 0; i < len; i++) s += pool[Math.floor(rnd() * pool.length)];
      if (mode === "chinese" || mode === "lucky") s = s.slice(0, -1) + "8689"[Math.floor(rnd() * 4)];
      out.push({ n: s, score: score(s) });
    }
    return out.sort(function (a, b) { return b.score - a.score; });
  }
  function hash(str) { var h = 1779033703 ^ str.length; for (var i = 0; i < str.length; i++) { h = Math.imul(h ^ str.charCodeAt(i), 3432918353); h = h << 13 | h >>> 19; } return h >>> 0; }
  function mulberry(a) { return function () { a |= 0; a = a + 0x6D2B79F5 | 0; var t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }

  var API = { DIGITS: DIGITS, COMBOS: COMBOS, ZODIAC: ZODIAC, clean: clean, reduce: reduce, score: score, verdict: verdict, analyze: analyze, zodiacFor: zodiacFor, nameNumber: nameNumber, lifePath: lifePath, generate: generate, suggest: suggest, hanzi: hanzi, pinyin: pinyin };
  if (typeof module !== "undefined" && module.exports) module.exports = API; else root.NumEngine = API;
})(typeof window !== "undefined" ? window : this);
