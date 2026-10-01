/* 447766.com — site configuration. Edit values here; no rebuild needed. */
window.SITE_CONFIG = {
  siteName: "447766",
  tagline: "The Lucky Number Lab",
  partnerUrl: "https://web.works/contact",

  /* Owner inbox: stored obfuscated (split + reversed base64). Never write it in plain text anywhere. */
  _k: ["YW1nQDFh", "bW9jLmxp", "ZXc=", "c2tyb3di"],
  _o: [1, 0, 3, 2],

  /* Google AdSense — paste your publisher ID (ca-pub-XXXXXXXXXXXXXXXX) and slot IDs after approval.
     While empty, ad slots show "Advertise here" house ads. Also update /ads.txt. */
  adsenseClient: "",
  adSlots: { top: "", inContent: "", sidebar: "", multiplex: "" },

  /* Analytics (optional): GA4 measurement ID e.g. G-XXXXXXX */
  ga4: "",

  /* Social / YouTube */
  youtubeChannel: "https://www.youtube.com/results?search_query=chinese+lucky+numbers",
  social: { youtube: "", x: "", instagram: "", tiktok: "", pinterest: "", facebook: "" },

  /* Donations — PayPal donate link is generated at runtime from the owner inbox.
     Optionally add Ko-fi / Buy Me a Coffee / Stripe Payment Link / GitHub Sponsors URLs. */
  donate: {
    currency: "USD",
    presets: [1.68, 6.66, 8.88, 18.88, 66.88],
    paypal: true,
    kofi: "",
    buymeacoffee: "",
    stripe: "",
    githubSponsors: "",
    goal: 888,      // monthly goal (USD)
    raised: 0,      // update manually
    supporters: 0   // update manually
  },

  /* Contest — edit before promoting */
  contest: {
    id: "LNC-01",
    title: "The Lucky Number Challenge #1",
    status: "open",              // "upcoming" | "open" | "closed"
    prize: "US$88 cash prize (PayPal) + a featured spot on 447766.com",
    opens: "On launch",
    closes: "Announced on this page and by email to entrants",
    question: "Pick the number you think is the luckiest 4-digit number and tell us why in one sentence.",
    skillTest: { q: "Skill-testing question: (8 × 6) + 18 − 6 = ?", a: "60" }
  }
};
