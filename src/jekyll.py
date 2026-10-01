#!/usr/bin/env python3
"""Emits the Jekyll pieces GitHub Pages renders server-side for the programmatic number pages:
_layouts/number.html, _data/n.json, _data/digits.json and one tiny stub per number.
Keeps the repo small: ~150 stubs + one data file instead of 150 full HTML pages.
Run after `node src/gen-data.js`:  python3 src/jekyll.py"""
import json, os, re, shutil
import build as B

ROOT, NUMS = B.ROOT, B.NUMS
DIG = {}
for a in NUMS.values():
    for d in a["digits"]:
        DIG[d["d"]] = {"hz": d["hz"], "py": d["py"], "jp": d["jp"], "s": d["sounds"], "w": d["w"]}


EW = ["Western angel-number readers treat 4 as stability and protection, while Chinese tradition hears 死 (death). Same digits, opposite stories — which one you follow depends on your audience.",
      "In both traditions {n} leans positive.",
      "Chinese and Western readings weigh this number differently, so consider who will see it."]
VERD = {"vlucky": ["Very lucky", "大吉"], "lucky": ["Lucky", "吉"], "neutral": ["Neutral", "平"], "unlucky": ["Unlucky", "凶"], "vunlucky": ["Very unlucky", "大凶"]}
USES = [["Business phone numbers, shop prices and opening dates", "Licence plates and house numbers", "Domain names for Chinese-speaking audiences"],
        ["Personal phone numbers and passwords you want to remember", "Prices and promotions", "Apartment or unit numbers"],
        ["Everyday use — neutral for most audiences", "Western branding where Chinese numerology matters less"],
        ["Avoid for gifts, prices, plates or business numbers aimed at Chinese customers", "Fine for Western audiences, where 4 is often read as stability"]]
LOVE_USE = "Weddings, anniversaries, proposals and love gifts"
ENG = json.loads(os.popen("node -e \"const E=require('" + ROOT + "/assets/js/numerology.js');console.log(JSON.stringify(E.DIGITS))\"").read())
LIFE = {}
_src = open(os.path.join(ROOT, "assets/js/numerology.js"), encoding="utf-8").read()
import re as _re
for m in _re.finditer(r'"(\d)": \{ love: "([^"]*)", career: "([^"]*)", spirit: "([^"]*)" \}', _src):
    LIFE[m.group(1)] = [m.group(2), m.group(3), m.group(4)]
assert len(LIFE) == 10
for k, x in ENG.items():
    DIG[k].update({"an": x["angel"], "th": x["theme"].lower(), "lf": LIFE[k]})


def tier(sc):
    return 0 if sc >= 80 else 1 if sc >= 60 else 2 if sc >= 45 else 3


def dominant(n):
    c = {}
    for ch in n:
        c[ch] = c.get(ch, 0) + 1
    best = n[0]
    for ch in c:
        if c[ch] > c[best]:
            best = ch
    return best, c


data = {}
for n, a in NUMS.items():
    vi = B.VIDEOS.index(B.pick_video(n))
    d, c = dominant(n)
    uniq = len(c)
    bl = "".join([x for x in sorted(c) if x != d][:3])
    ewi = 0 if "4" in n else (1 if a["score"] >= 65 else 2)
    love = 1 if re.search(r"520|1314|521|3344|9420|99", n) else 0
    rec = {
        "s": a["score"], "vk": a["verdict"]["key"],
        "hz": a["hanzi"], "py": a["pinyin"], "jp": a["jyutping"], "ch": a["chinese"],
        "one": a["chinese"].split(". ")[0].rstrip(".") + ".",
        "cb": [[c2["n"], c2["hz"], c2["m"], 1 if c2["n"] in NUMS else 0] for c2 in a["combos"]],
        "rs": " → ".join(a["reduce"]["steps"]), "rr": a["reduce"]["root"],
        "ad": d, "rep": 1 if (uniq == 1 and len(n) > 1) else 0, "bl": bl,
        "ut": tier(a["score"]), "ul": love, "sg": [[s2["n"], s2["score"]] for s2 in a["suggestions"]],
        "rl": B.related(n), "v": vi, "ew": ewi,
    }
    if a.get("known"):
        rec["kn"] = [a["known"]["hz"], a["known"]["m"]]
    # sanity: recompose angel + uses in python exactly as Liquid will and compare to engine output
    L = LIFE[d]; r = a["reduce"]["root"]; R = LIFE[str(r)] if r < 10 else L
    intro = (f"A repeating sequence of {d} amplifies its message of {DIG[d]['an']}." if rec["rep"] else
             f"Led by {d} ({DIG[d]['an']})" + ((", blended with " + ", ".join(f"{x} ({DIG[x]['th']})" for x in bl)) if uniq > 1 else "") + ".")
    root = f" It reduces to {r}, the number of {DIG[str(r)]['an']}." if r < 10 else f" It reduces to the master number {r} — heightened intuition and purpose."
    assert intro + root == a["angel"]["summary"], (n, intro + root, a["angel"]["summary"])
    assert f"In love: {L[0]}; at its core, {R[0]}." == a["angel"]["love"], n
    uses = ([LOVE_USE] if love else []) + USES[rec["ut"]]
    assert uses == a["uses"], (n, uses, a["uses"])
    data[n] = rec

# The Liquid templates live in _layouts/number.html (committed). This script regenerates that file from
# PRE + HEAD + header + body + sidebar + footer when present below; see the committed layout for the source of truth.
LAYOUT = os.path.join(ROOT, "_layouts", "number.html")


def main():
    os.makedirs(os.path.join(ROOT, "_data"), exist_ok=True)
    with open(os.path.join(ROOT, "_data/n.json"), "w", encoding="utf-8") as f:
        f.write("{\n" + ",\n".join(json.dumps(k) + ":" + json.dumps(v, ensure_ascii=False, separators=(",", ":")) for k, v in data.items()) + "\n}\n")
    json.dump(DIG, open(os.path.join(ROOT, "_data/digits.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    K = {"verd": VERD, "uses": USES, "love": [LOVE_USE], "ew": EW, "videos": [[v[0], v[1]] for v in B.VIDEOS]}
    json.dump(K, open(os.path.join(ROOT, "_data/k.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    for n in NUMS:
        d = os.path.join(ROOT, "number", n)
        if os.path.isdir(d):
            shutil.rmtree(d)
        os.makedirs(d)
        open(os.path.join(d, "index.html"), "w").write(f'---\nlayout: number\nn: "{n}"\n---\n')
    print("jekyll: data + stubs for", len(data), "numbers (layout: _layouts/number.html)")


if __name__ == "__main__":
    main()
