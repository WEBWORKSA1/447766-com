// Regenerates src/numbers.json from the shared engine. Add numbers to EXTRA to create new pages.
const E = require("../assets/js/numerology.js"), fs = require("fs"), path = require("path");
const EXTRA = ["000","123","1234","12345","123456","1314","5201314","447766","2024","2025","2026","2027","1688","6688","8848","9420","168","518","520","521","530","250","514","748","886","555","233","3344","6868","2828","168888","1666","7456","1111"];
const set = new Set();
for (let i = 0; i < 100; i++) set.add(String(i));
for (let d = 1; d <= 9; d++) { set.add(String(d).repeat(3)); set.add(String(d).repeat(4)); }
EXTRA.forEach(x => set.add(x)); Object.keys(E.COMBOS).forEach(k => set.add(k));
const out = {}; [...set].forEach(n => out[n] = E.analyze(n));
fs.writeFileSync(path.join(__dirname, "numbers.json"), JSON.stringify(out));
console.log(Object.keys(out).length, "numbers");
