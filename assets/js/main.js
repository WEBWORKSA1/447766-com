/* 447766 — site behaviour (no dependencies) */
(function () {
  "use strict";
  var C = window.SITE_CONFIG || {}, E = window.NumEngine, doc = document, html = doc.documentElement;
  var BASE = html.getAttribute("data-base") || "./";
  var INDEXED = window.NUM_INDEX || [];
  window.dataLayer = window.dataLayer || [];
  function track(ev, p) { try { window.dataLayer.push(Object.assign({ event: ev }, p || {})); if (window.gtag) window.gtag("event", ev, p || {}); } catch (e) {} }
  function $(s, r) { return (r || doc).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || doc).querySelectorAll(s)); }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  /* ---- owner inbox (never in markup) ---- */
  function inbox() { try { var k = C._k, o = C._o; return atob(o.map(function (i) { return k[i]; }).join("")).split("").reverse().join(""); } catch (e) { return ""; } }
  window.__inbox = undefined;

  /* ---- theme ---- */
  var saved = store("theme"); if (saved) html.setAttribute("data-theme", saved);
  $$("[data-theme-toggle]").forEach(function (b) {
    b.addEventListener("click", function () {
      var dark = html.getAttribute("data-theme") ? html.getAttribute("data-theme") === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
      var nv = dark ? "light" : "dark"; html.setAttribute("data-theme", nv); store("theme", nv);
    });
  });

  /* ---- mobile menu ---- */
  var burger = $(".burger"), menu = $(".menu");
  if (burger && menu) burger.addEventListener("click", function () { var o = menu.classList.toggle("open"); burger.setAttribute("aria-expanded", o); });

  /* ---- mail links: built on click only ---- */
  $$("[data-mail]").forEach(function (a) {
    a.addEventListener("click", function (e) { e.preventDefault(); var s = a.getAttribute("data-mail") || "Inquiry from 447766.com"; location.href = "mai" + "lto:" + inbox() + "?subject=" + encodeURIComponent(s); track("mail_click", { subject: s }); });
  });

  /* ---- analytics ---- */
  if (C.ga4 && store("consent") === "yes") {
    var g = doc.createElement("script"); g.async = true; g.src = "https://www.googletagmanager.com/gtag/js?id=" + C.ga4; doc.head.appendChild(g);
    window.gtag = function () { window.dataLayer.push(arguments); }; window.gtag("js", new Date()); window.gtag("config", C.ga4);
  }

  /* ---- ads: AdSense if configured, otherwise house ads ---- */
  var adsOff = html.hasAttribute("data-noads");
  $$(".ad").forEach(function (slot) {
    if (adsOff) { slot.remove(); return; }
    var type = slot.getAttribute("data-slot") || "inContent";
    if (C.adsenseClient && C.adSlots && C.adSlots[type]) {
      slot.innerHTML = '<ins class="adsbygoogle" style="display:block" data-ad-client="' + C.adsenseClient + '" data-ad-slot="' + C.adSlots[type] + '" data-ad-format="' + (type === "multiplex" ? "autorelaxed" : "auto") + '" data-full-width-responsive="true"></ins>';
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    } else {
      slot.classList.add("house");
      var msgs = ["Your brand here — reach people who pay premiums for lucky numbers.", "Sponsor a lucky-number tool. Limited slots.", "Advertise to number lovers, couples, investors and domainers."];
      slot.innerHTML = '<div><p style="margin:0 0 8px;font-weight:650">' + msgs[Math.floor(Math.random() * msgs.length)] + '</p><a href="' + BASE + 'advertise/">Advertise on 447766 →</a></div>';
    }
  });
  if (C.adsenseClient && !adsOff) { var s = doc.createElement("script"); s.async = true; s.crossOrigin = "anonymous"; s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + C.adsenseClient; doc.head.appendChild(s); }

  /* ---- lite YouTube ---- */
  $$(".yt[data-id]").forEach(function (el) {
    var id = el.getAttribute("data-id"), t = el.getAttribute("data-title") || "Video";
    el.innerHTML = '<img loading="lazy" alt="' + esc(t) + '" src="https://i.ytimg.com/vi/' + id + '/hqdefault.jpg"><button class="play" aria-label="Play: ' + esc(t) + '">▶</button>';
    el.addEventListener("click", function () {
      el.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + esc(t) + '" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
      track("video_play", { id: id });
    }, { once: true });
  });

  /* ---- forms → owner inbox via FormSubmit (AJAX) ---- */
  $$("form[data-form]").forEach(function (f) {
    var msg = $(".form-msg", f) || (function () { var d = doc.createElement("div"); d.className = "form-msg"; d.setAttribute("role", "status"); f.appendChild(d); return d; })();
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var fd = new FormData(f), data = {}, name = f.getAttribute("data-form");
      if (fd.get("_honey")) return;
      fd.forEach(function (v, k) { if (k !== "_honey") data[k] = data[k] ? data[k] + ", " + v : v; });
      var st = f.querySelector("[name=skill_test]");
      if (st && C.contest && String(st.value).trim() !== C.contest.skillTest.a) { msg.className = "form-msg err"; msg.textContent = "Please answer the skill-testing question correctly to enter."; return; }
      data._subject = "[447766] " + (f.getAttribute("data-subject") || name) + (data.name ? " — " + data.name : "");
      data._template = "table"; data._captcha = "false";
      data.form = name; data.page = location.href; data.submitted = new Date().toISOString();
      var btn = f.querySelector("[type=submit]"); if (btn) { btn.disabled = true; btn.dataset.t = btn.textContent; btn.textContent = "Sending…"; }
      fetch("https://formsubmit.co/ajax/" + inbox(), { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || j.success === "false" || j.success === false) throw new Error(j.message || "fail"); return j; }); })
        .then(function () {
          msg.className = "form-msg ok"; msg.textContent = f.getAttribute("data-success") || "Thank you! We received your submission and will reply soon.";
          f.reset(); track("lead_submit", { form: name }); store("lead", "1");
          var next = f.getAttribute("data-next"); if (next) setTimeout(function () { location.href = next; }, 1600);
        })
        .catch(function () {
          msg.className = "form-msg err";
          msg.innerHTML = "We couldn't send that automatically. <a href='#' class='mail-fallback'>Send it by email instead</a>.";
          var a = $(".mail-fallback", msg); a.addEventListener("click", function (ev) {
            ev.preventDefault(); var body = Object.keys(data).filter(function (k) { return k[0] !== "_"; }).map(function (k) { return k + ": " + data[k]; }).join("\n");
            location.href = "mai" + "lto:" + inbox() + "?subject=" + encodeURIComponent(data._subject) + "&body=" + encodeURIComponent(body);
          });
        })
        .then(function () { if (btn) { btn.disabled = false; btn.textContent = btn.dataset.t; } });
    });
  });

  /* ---- multi-step lead form ---- */
  $$("[data-steps]").forEach(function (f) {
    var steps = $$(".step", f), bars = $$(".steps span", f.parentNode), i = 0;
    function show(n) { steps.forEach(function (s, k) { s.hidden = k !== n; }); bars.forEach(function (b, k) { b.classList.toggle("on", k <= n); }); i = n; }
    $$("[data-next-step]", f).forEach(function (b) { b.addEventListener("click", function () {
      var req = $$("[required]", steps[i]).filter(function (x) { return !x.checkValidity(); }); if (req.length) { req[0].reportValidity(); return; }
      show(i + 1); track("lead_step", { step: i + 1 }); }); });
    $$("[data-prev-step]", f).forEach(function (b) { b.addEventListener("click", function () { show(i - 1); }); });
    show(0);
  });

  /* ---- prefill from query ---- */
  var qs = new URLSearchParams(location.search);
  $$("[data-prefill]").forEach(function (el) { var v = qs.get(el.getAttribute("data-prefill")); if (v) el.value = v; });

  /* ---- result renderer ---- */
  function link(n) { return INDEXED.indexOf(n) > -1 ? BASE + "number/" + n + "/" : BASE + "lookup/?n=" + n; }
  function gaugeColor(sc) { return sc >= 65 ? "var(--good)" : sc >= 45 ? "var(--gold)" : "var(--bad)"; }
  function renderResult(el, a) {
    if (!a) { el.innerHTML = '<div class="notice">Please enter a number (digits only — e.g. 168, 520, a phone number or a plate).</div>'; return; }
    var digits = a.digits.map(function (d) { return '<div class="ds ' + (d.w > 0 ? "pos" : d.w < 0 ? "neg" : "") + '"><b>' + d.d + '</b><i>' + d.hz + '</i></div>'; }).join("");
    var combos = a.combos.length ? '<h3>Hidden combos</h3><ul>' + a.combos.map(function (c) { return '<li><a href="' + link(c.n) + '"><b>' + c.n + '</b></a> <span class="hz">' + c.hz + '</span> — ' + esc(c.m) + '</li>'; }).join("") + '</ul>' : "";
    var sugg = a.suggestions.length ? '<h3>Luckier alternatives</h3><div class="chips">' + a.suggestions.map(function (s) { return '<a class="chip good" href="' + BASE + 'lookup/?n=' + s.n + '">' + s.n + ' · ' + s.score + '</a>'; }).join("") + '</div>' : "";
    var red = a.reduce ? a.reduce.steps.join(" → ") : "";
    el.innerHTML =
      '<div class="result"><div class="result-top"><div class="gauge" style="--v:' + a.score + ';--c:' + gaugeColor(a.score) + '"><div><div><b>' + a.score + '</b><small>luck score</small></div></div></div>' +
      '<div><div class="result-num">' + a.n + '</div><div class="result-hz">' + esc(a.hanzi) + ' · ' + esc(a.pinyin) + '</div>' +
      '<p style="margin:10px 0 0"><span class="tag t-' + a.verdict.key + '">' + a.verdict.label + ' · ' + a.verdict.hz + '</span> <span class="micro">Cantonese: ' + esc(a.jyutping) + '</span></p></div></div>' +
      '<div class="result-body"><div class="digit-strip">' + digits + '</div>' +
      '<div class="tabs" role="tablist"><button role="tab" aria-selected="true" data-tab="cn">Chinese meaning</button><button role="tab" aria-selected="false" data-tab="we">Western numerology</button><button role="tab" aria-selected="false" data-tab="use">Best uses</button></div>' +
      '<div data-panel="cn"><p class="quick">' + esc(a.chinese) + '</p>' + combos + '</div>' +
      '<div data-panel="we" hidden><p><b>Reduction:</b> ' + red + '</p><p>' + esc(a.angel.summary) + '</p><ul><li>' + esc(a.angel.love) + '</li><li>' + esc(a.angel.career) + '</li><li>' + esc(a.angel.spirit) + '</li></ul></div>' +
      '<div data-panel="use" hidden><ul>' + a.uses.map(function (u) { return "<li>" + esc(u) + "</li>"; }).join("") + '</ul></div>' +
      sugg +
      '<div class="share" style="margin-top:16px"><a class="btn btn-red btn-sm" href="' + BASE + 'get-report/?n=' + a.n + '">Email me the full report</a><button class="btn btn-ghost btn-sm" data-share="' + a.n + '">Share result</button>' + (INDEXED.indexOf(a.n) > -1 ? '<a class="btn btn-ghost btn-sm" href="' + link(a.n) + '">Read the full ' + a.n + ' guide</a>' : "") + '</div>' +
      '<p class="micro" style="margin-top:12px">Traditional cultural associations, for entertainment and education. Mandarin and Cantonese readings can differ.</p></div></div>';
    bindTabs(el); bindShare(el);
    track("number_lookup", { number: a.n, score: a.score });
  }
  window.renderResult = renderResult;
  function bindTabs(root) {
    $$(".tabs", root).forEach(function (t) {
      $$("button", t).forEach(function (b) { b.addEventListener("click", function () {
        $$("button", t).forEach(function (x) { x.setAttribute("aria-selected", x === b); });
        var box = t.parentNode; $$("[data-panel]", box).forEach(function (p) { p.hidden = p.getAttribute("data-panel") !== b.getAttribute("data-tab"); });
      }); });
    });
  }
  function bindShare(root) {
    $$("[data-share]", root).forEach(function (b) { b.addEventListener("click", function () {
      var n = b.getAttribute("data-share"), url = location.origin + location.pathname.replace(/[^/]*$/, "") ;
      var text = "What does " + n + " mean in Chinese numerology? Luck score " + E.score(n) + "/100 on 447766";
      var u = new URL(BASE + "lookup/?n=" + n, location.href).href;
      if (navigator.share) navigator.share({ title: "447766 · " + n, text: text, url: u }).catch(function () {});
      else { navigator.clipboard && navigator.clipboard.writeText(text + " " + u); b.textContent = "Link copied ✓"; }
      track("share", { number: n });
    }); });
  }
  bindTabs(doc); bindShare(doc);

  /* ---- lookup widgets ---- */
  $$("form[data-lookup]").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      var target = f.getAttribute("data-lookup");
      var n = E.clean($("input", f).value);
      if (target === "go") { e.preventDefault(); location.href = INDEXED.indexOf(n) > -1 ? link(n) : BASE + "lookup/?n=" + n; return; }
      e.preventDefault(); var out = $(target); renderResult(out, E.analyze(n));
      if (history.replaceState) history.replaceState(null, "", "?n=" + n);
    });
  });
  var lookupOut = $("#lookup-result");
  if (lookupOut) { var q = qs.get("n"); if (q) { $("#lookup-input").value = q; renderResult(lookupOut, E.analyze(q)); } }
  $$("[data-fill]").forEach(function (c) { c.addEventListener("click", function (e) { var f = c.closest("section,div").querySelector("form[data-lookup]"); if (!f) return; e.preventDefault(); $("input", f).value = c.getAttribute("data-fill"); f.requestSubmit ? f.requestSubmit() : f.submit(); }); });

  /* ---- tools ---- */
  var tz = $("#tool-zodiac");
  if (tz) tz.addEventListener("submit", function (e) {
    e.preventDefault(); var y = $("[name=year]", tz).value, m = $("[name=month]", tz).value, d = $("[name=day]", tz).value;
    var z = E.zodiacFor(y), lp = E.lifePath(y + ("0" + m).slice(-2) + ("0" + d).slice(-2));
    var luckyYour = E.generate("chinese", 6, y + m + d).slice(0, 3);
    $("#zodiac-out").innerHTML = '<div class="card"><h3>' + z.hz + ' ' + z.animal + ' · Life Path ' + lp + '</h3><p><b>Lucky numbers:</b> ' + z.lucky.join(", ") + ' · <b>Avoid:</b> ' + z.unlucky.join(", ") + '</p><p><b>Lucky colours:</b> ' + z.colors + '</p><p><b>Your personal lucky set:</b> ' + luckyYour.map(function (x) { return '<a class="chip" href="' + BASE + 'lookup/?n=' + x.n + '">' + x.n + '</a>'; }).join(" ") + '</p><p class="micro">Zodiac by Gregorian year — if you were born in January or early February, check the Lunar New Year date for your year. </p><a class="btn btn-red btn-sm" href="' + BASE + 'get-report/">Get my full lucky report</a></div>';
    track("tool_use", { tool: "zodiac" });
  });
  var tn = $("#tool-name");
  if (tn) tn.addEventListener("submit", function (e) {
    e.preventDefault(); var r = E.nameNumber($("input", tn).value); if (!r) return;
    $("#name-out").innerHTML = '<div class="card"><div class="grid g3"><div class="kpi"><span class="stat">' + r.expression + '</span><span class="micro">Expression</span></div><div class="kpi"><span class="stat">' + r.soulUrge + '</span><span class="micro">Soul urge</span></div><div class="kpi"><span class="stat">' + r.personality + '</span><span class="micro">Personality</span></div></div><p style="margin-top:12px">Expression ' + r.expression + ' echoes <a href="' + link(String(r.expression)) + '">the meaning of ' + r.expression + '</a>.</p></div>';
    track("tool_use", { tool: "name" });
  });
  var tg = $("#tool-gen");
  if (tg) tg.addEventListener("submit", function (e) {
    e.preventDefault(); var res = E.generate($("[name=mode]", tg).value, $("[name=len]", tg).value, $("[name=seed]", tg).value || null);
    $("#gen-out").innerHTML = '<div class="chips">' + res.map(function (x) { return '<a class="chip ' + (x.score >= 65 ? "good" : x.score < 45 ? "bad" : "") + '" href="' + BASE + 'lookup/?n=' + x.n + '">' + x.n + ' · ' + x.score + '</a>'; }).join("") + '</div>';
    track("tool_use", { tool: "generator" });
  });
  var tc = $("#tool-check");
  if (tc) tc.addEventListener("submit", function (e) {
    e.preventDefault(); var kind = $("[name=kind]", tc).value, raw = $("[name=value]", tc).value;
    var n = E.clean(raw.split(".")[0]); var a = E.analyze(n); var out = $("#check-out");
    if (!a) { out.innerHTML = '<div class="notice">No digits found — enter a number with digits.</div>'; return; }
    renderResult(out, a);
    var extra = { phone: "Phone numbers: the last 4 digits matter most. Avoid 4 at the end; 8, 6 or 9 is a strong finish.", plate: "Plates: shorter is more valuable. In Hong Kong, single- and double-digit lucky plates have sold for millions.", address: "Addresses: many Chinese buyers avoid unit and floor numbers containing 4, 14, 24 or 44.", domain: "Domains: Chinese buyers pay premiums for 8, 6 and 9 and discount 4 — digits-only domains are valued by length first." }[kind];
    out.insertAdjacentHTML("afterbegin", '<p class="notice">' + extra + ' <a href="' + BASE + (kind === "domain" ? "domains/#appraisal" : "get-report/#vanity") + '">' + (kind === "domain" ? "Get a free domain appraisal →" : "Request a luckier number →") + '</a></p>');
    track("tool_use", { tool: "check_" + kind });
  });

  /* ---- donations ---- */
  var dn = $("#donate");
  if (dn && C.donate) {
    var amt = C.donate.presets[2], box = $(".amounts", dn), custom = $("#custom-amt");
    box.innerHTML = C.donate.presets.map(function (p) { return '<button type="button" aria-pressed="' + (p === amt) + '" data-amt="' + p + '">$' + p.toFixed(2) + '</button>'; }).join("") + '<button type="button" data-amt="custom" aria-pressed="false">Custom</button>';
    $$("button", box).forEach(function (b) { b.addEventListener("click", function () { $$("button", box).forEach(function (x) { x.setAttribute("aria-pressed", x === b); }); var v = b.getAttribute("data-amt"); if (v === "custom") { custom.hidden = false; custom.focus(); } else { custom.hidden = true; amt = +v; } }); });
    var pp = $("#pay-paypal");
    if (pp) pp.addEventListener("click", function () {
      var a = custom.hidden ? amt : parseFloat(custom.value) || amt, monthly = $("#monthly") && $("#monthly").checked;
      var purpose = ($("[name=purpose]", dn) || {}).value || "General support";
      var u = "https://www.paypal.com/donate/?business=" + encodeURIComponent(inbox()) + "&amount=" + a.toFixed(2) + "&currency_code=" + C.donate.currency + "&item_name=" + encodeURIComponent("447766.com — " + purpose) + (monthly ? "&recurring=1" : "") + "&no_recurring=" + (monthly ? 0 : 1);
      track("donate_click", { amount: a, method: "paypal", purpose: purpose }); window.open(u, "_blank", "noopener");
    });
    ["kofi", "buymeacoffee", "stripe", "githubSponsors"].forEach(function (k) { var b = $("#pay-" + k); if (b) { if (C.donate[k]) { b.href = C.donate[k]; b.hidden = false; } else b.hidden = true; } });
    var g = C.donate, pct = g.goal ? Math.min(100, Math.round(g.raised / g.goal * 100)) : 0;
    var pr = $("#goal"); if (pr) pr.innerHTML = '<div class="progress"><span style="width:' + Math.max(pct, 2) + '%"></span></div><p class="micro" style="margin-top:8px"><b>$' + g.raised + '</b> raised of $' + g.goal + ' monthly goal · ' + g.supporters + ' supporters</p>';
  }

  /* ---- contest config ---- */
  if (C.contest) $$("[data-contest]").forEach(function (el) { var k = el.getAttribute("data-contest"); var v = k === "skill" ? C.contest.skillTest.q : C.contest[k]; if (v) el.textContent = v; });

  /* ---- sticky CTA (50% scroll, frequency capped) ---- */
  var sticky = $(".sticky-cta");
  if (sticky && !adsOff && store("lead") !== "1" && Date.now() - (+store("ctaClosed") || 0) > 3 * 864e5) {
    var shown = false;
    addEventListener("scroll", function () { if (!shown && scrollY > (doc.body.scrollHeight - innerHeight) * 0.5) { sticky.classList.add("show"); shown = true; } }, { passive: true });
    $(".x", sticky).addEventListener("click", function () { sticky.classList.remove("show"); store("ctaClosed", Date.now()); });
  }

  /* ---- cookie consent ---- */
  var ck = $(".cookie");
  if (ck && !store("consent")) { ck.classList.add("show"); $$("[data-consent]", ck).forEach(function (b) { b.addEventListener("click", function () { store("consent", b.getAttribute("data-consent")); ck.classList.remove("show"); if (b.getAttribute("data-consent") === "yes" && C.ga4) location.reload(); }); }); }

  /* ---- numbers search filter ---- */
  var nf = $("#num-filter");
  if (nf) nf.addEventListener("input", function () { var v = nf.value.trim(); $$(".num-grid a").forEach(function (a) { a.hidden = v && a.textContent.indexOf(v) === -1; }); });

  /* ---- year in footer ---- */
  $$("[data-year]").forEach(function (y) { y.textContent = new Date().getFullYear(); });
})();
