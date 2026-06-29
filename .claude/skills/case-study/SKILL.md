---
name: case-study
description: Create an ONDEWO customer case study, success story, or testimonial — a Challenge→Solution→Results one-pager (PDF), a web HTML story, or a social quote card. Use whenever the user asks to write/create/design/make/turn a customer win into a case study, success story, customer story, customer reference, results one-pager, win story, testimonial, or quote card for ONDEWO ("write up the <customer> case study", "make a testimonial card", "turn this result into a success story"). Produces on-brand PDF/HTML/SVG using the official logo, tokens (#004C87 blue, #BE216B magenta), and Futura/Jost type.
---

# Create an ONDEWO case study / testimonial

You are producing a finished, on-brand ONDEWO customer story. Pick one of two modes
up front:

- **`mode: case-study`** — a full Challenge → Solution → Results narrative with
  quantified metrics, a customer quote, an at-a-glance box, and the logo. Outputs:
  a **PDF one-pager** and/or a **web HTML** story.
- **`mode: testimonial`** — a short quote card for social/web: one punchy customer
  quote + attribution. Output: a **social quote-card SVG** (reuse the social-post
  template).

This skill owns the case-study-specific layer: the intake interview, the
Challenge→Solution→Results structure, and the proof/consent discipline. It **composes,
never re-implements**, two sibling skills — hand the actual rendering to
`create-brand-asset` (the SVG/HTML/PDF production + render engine) and the wording to
`brand-copy` (ONDEWO voice). Don't reinvent their work; layer this structure on top.

Follow this process exactly — it guarantees brand consistency and keeps you from
inventing facts.

## 0. Load brand context (always do this first)

Read, in order:
1. `brand-kit/README.md` — kit map.
2. `brand-kit/voice-and-tone.md` — the story must sound like ONDEWO (clear over
   clever, confident not boastful, proof points do the bragging).
3. `brand-kit/color-system.md` (60-30-10, magenta ≤10%) and `brand-kit/typography.md`
   (Futura → Jost, type scale, all-caps tracking).
4. `brand-kit/logo-guidelines.md` — variant per background, clear space, min size.
5. `brand-kit/layout-and-spacing.md` — grid, 4px spacing, §8 pre-ship checklist.
6. `brand-kit/accessibility.md` — approved text/background contrast pairs.
7. `brand-kit/tokens/ondewo.tokens.json` — exact values (use these, never raw hex).
8. `brand-kit/document-templates/PLAN.md` — **the canonical output-engine plan**
   (which renderer to use for PDF / web / SVG, and the page specs). If that file
   isn't present yet, fall back to the render commands in §3 / §4 below and
   `brand-kit/templates/README.md`.

Start every output from a template in `brand-kit/templates/` and embed the real logo
from `brand-kit/assets/logo/`. Never invent colours/fonts or redraw the swirl.

## 1. Intake (gather the story — keep it lean)

Infer what you can from the brief; only ask for what you genuinely can't. The story
is only as good as the facts — **do not fabricate a customer, a quote, or a metric.**

**Decide first:** mode (`case-study` | `testimonial`), and which outputs (PDF, web
HTML, quote-card SVG). Then collect the story with this **interview question set**:

*Customer & context*
- Who is the customer? (name, industry, region, size) — OK to anonymise: "a
  European insurer".
- Which ONDEWO product/capability did they use? (CAI, S2T/T2S, telephony, on-prem)
- What was the deployment? (on-premise / cloud, languages, channels, go-live date)

*Challenge*
- What problem were they solving? What did "before ONDEWO" look like?
- What was the cost of the status quo? (missed calls, hold times, headcount, cost)
- Why was it hard / why now?

*Solution*
- What did ONDEWO build/automate, concretely? (use cases, call flows, integrations)
- How did rollout go? What made it work? (timeline, effort, integration points)

*Results (quantified — this is the spine of a case study)*
- The headline number (the one stat for the at-a-glance box and the title).
- 2–4 supporting metrics with **before → after** values and time window.
- Soft outcomes (CSAT, agent experience, languages added, 24/7 coverage).
- For **every** metric: what's the **source** and is it **verified**? Mark any number
  you can't trace to a customer-approved source as **`‹confirm›`** (see Guardrails).

*Quote & approval*
- A usable customer quote + attribution: **name, title, company** (+ logo if cleared).
- Is the name/logo/quote **approved for publication**? (consent/GDPR — see Guardrails.)

*Logistics*
- Audience (sales leave-behind, website, LinkedIn), tone, language (EN-GB vs EN-US),
  and the CTA ("Book a demo" / "Talk to sales" / "Read the docs").

Capture metrics in a **metrics table** before you design — it is your single source
of truth and your `‹confirm›` audit:

| Metric | Before | After | Δ / result | Time window | Source | Verified? |
|--------|--------|-------|-----------|-------------|--------|-----------|
| Calls answered | 68% | 100% | +32 pts | 6 mo | Customer ops report | ✅ |
| Avg. handling time | 4m10s | 2m05s | −50% | 6 mo | — | `‹confirm›` |
| Languages live | 1 | 8 | +7 | go-live | Deployment record | ✅ |

## 2. Canonical structure

### A. Case study one-pager (PDF / web HTML)

Top-to-bottom outline — reusable for every customer:

1. **Brand frame** — ONDEWO logo (top-left, horizontal lockup) + blue/magenta top
   bar (as in `letterhead.html`).
2. **Eyebrow** — all-caps, magenta, tracked: `CASE STUDY` or `SUCCESS STORY` ·
   `‹Industry›`.
3. **Headline** — the outcome in one sentence, sentence case, blue, Bold. Lead with
   the result, e.g. "‹Customer› answers 100% of calls — in 8 languages, 24/7."
4. **At-a-glance box** — a bordered/`neutral-50` card with: Customer · Industry ·
   Region · Product · Deployment · **2–3 headline metrics** (Bold, blue/one magenta).
5. **Challenge** — H2 "The challenge" + 2–4 sentences on the before-state and its cost.
6. **Solution** — H2 "The solution" + what ONDEWO automated, concretely (call flows,
   integrations, on-prem). Keep it specific and technically credible.
7. **Results** — H2 "The results" + a row/grid of **metric cards** (big number +
   small label) drawn from the metrics table; quantified, with `‹confirm›` on anything
   unverified.
8. **Customer quote** — pull quote with a magenta opening quotation mark, then
   attribution: **Name, Title, Company** (+ customer logo if cleared).
9. **Footer / CTA** — tagline "We automate your phone calls.", one primary CTA, and
   `ondewo.com`.

Keep it to one page (A4) for the PDF; the web version may scroll but follows the
same order.

### B. Testimonial quote card (social / web SVG)

A single-focal quote card, 1080×1080 (square) or adapt to the LinkedIn banner:

1. **ONDEWO logo** (top-left) + decorative low-opacity swirl watermark (already in
   the social template).
2. **Eyebrow** — `CUSTOMER STORY` (magenta, all-caps, tracked) — optional.
3. **The quote** — large, blue, Bold/Light, sentence case. Open with a magenta
   quotation mark or a short magenta accent bar. **Aim ≤ 25 words; hard cap ~40** so
   it stays legible at the type sizes in the template.
4. **Attribution** — Name (Medium), Title · Company (muted ink). Optional small
   customer logo/avatar.
5. **Footer** — `ondewo.com` (and a soft CTA only if there's room).

One quote, one focal point — no metric soup on a testimonial card.

## 3. Build

Pick the base + output engine, then hand production to **`create-brand-asset`** rather
than re-implementing it — it already enforces logo embedding, tokens, and the render
step. Use **`brand-copy`** for the headline, section text, and any drafted quote. This
section just maps the case-study structure onto those engines.

| Output | Start from | Engine |
|--------|-----------|--------|
| **PDF one-pager** | `templates/letterhead.html` (A4 frame, top bar, footer) | HTML → PDF (print-to-PDF) |
| **Web HTML story** | `templates/web-hero.html` (+ `components.html` for metric cards) | responsive HTML |
| **Testimonial quote-card SVG** | `templates/social-post-1080.svg` | SVG → PNG |

- **Embed the logo** from `brand-kit/assets/logo/` — copy the official paths; never
  trace the swirl. Mark = two paths (`fill="#BE216B"`, `fill="#004C87"`) in
  `viewBox="30 30 157 123"`; horizontal lockup native `viewBox="26.2 26.5 543.4 130.1"`.
  Scale with a `<g transform>`. Use `ondewo-logo-horizontal.svg` on light,
  `…-mono-white.svg` on blue/dark.
- **Colours:** token values only (`--ondewo-*`). Lead blue/neutral; **magenta ≤ ~10%**
  — one eyebrow, one quotation mark / accent bar, or one hero metric. Never blue-on-
  magenta or magenta-on-blue text.
- **Type:** the Futura/Jost stack. Headlines sentence-case (Bold or Light). All-caps
  eyebrows get `letter-spacing:0.12em`. Big metric numbers are Bold, in blue (or one
  in magenta). For self-contained SVGs use
  `font-family="Jost, Futura, 'Century Gothic', sans-serif"`; on web load Jost via
  Google Fonts (see `typography.md`), not commercial Futura files.
- **Layout:** 4px-grid spacing, generous whitespace, one focal point, one primary CTA.
  Metric cards: white/`neutral-50` on `neutral-100`, 1px `neutral-100` border, soft
  blue-tinted shadow.
- **PDF engine:** keep the `letterhead.html` `@page { size:A4 }`. Render with the
  engine named in `document-templates/PLAN.md`; otherwise headless Chrome:
  `chrome --headless --print-to-pdf=out.pdf --no-pdf-header-footer "file://<abs>.html"`
  (or browser Print → Save as PDF).
- **Voice:** apply `voice-and-tone.md` throughout. Draft any missing copy (headline,
  section text, even a candidate quote) but flag a drafted quote as `‹confirm›` and
  get the customer's exact words before publishing.

## 4. Verify (before delivering)

- **Render it — don't ship unseen:**
  - SVG → PNG: `qlmanage -t -s 2000 -o ./out <file.svg>` (macOS), or
    `rsvg-convert -w 2160 <file.svg> -o out.png` / `resvg` if installed.
  - HTML → PNG preview: `chrome --headless --screenshot=out.png --window-size=1280,1600 "file://<abs>.html"`.
  - HTML → PDF: command in §3; then open the PDF and check the page fits A4.
  - View the output; fix any clipping, overflow, or off-brand detail.
- **Brand checklist** — run `brand-kit/layout-and-spacing.md` §8 (logo clear space &
  correct variant, tokens only, magenta ≤10%, Futura/Jost + scale, 4px grid, AA
  contrast, one focal point + one CTA).
- **Accessibility pairs** — every text/background pair must come from
  `accessibility.md` §2 (ink on white, white on blue/magenta). Quote text on a tinted
  card must still clear AA (4.5:1, or 3:1 for large display text).
- **Facts** — confirm every metric traces to the metrics table and that anything
  unverified is visibly marked `‹confirm›`. Confirm the quote and the customer
  name/logo are approved for publication.

## 5. Deliver

- Save source to `brand-kit/generated/` (create it if missing; never overwrite
  `templates/`, `assets/`, or `tokens/`). Naming per `assets/ASSET-INDEX.md` §D:
  - `ondewo-case-study-‹customer›-light.pdf` / `.html`
  - `ondewo-testimonial-‹customer›-light-1080.svg` (+ exported `.png`)
- Tell the user: what you made and where it is, which placeholders/`‹confirm›` items
  still need real values, how to export at final resolution (PDF size, 2× PNG), and
  which CTA/quote to confirm before publishing.

## Guardrails

- **No off-brand colours or fonts.** Token palette only; extend along the 50–900
  scales, never a new hue. Jost on public web — not commercial Futura font files.
- **Logo is fixed artwork.** Use the official SVGs; don't stretch, recolour, shadow,
  or redraw the swirl. Mono-white on blue/dark backgrounds.
- **Magenta is an accent (≤ ~10%)** — never the dominant fill of a card or page.
- **Never fabricate proof.** Don't invent customers, quotes, logos, or numbers. Mark
  any metric or fact you can't trace to a customer-approved source as **`‹confirm›`**
  (the brand kit's unverified-fact marker; same intent as a `<confirm>` flag) and tell
  the user it needs verification before publishing.
- **Consent/GDPR.** Only use a customer's real name, logo, or quote when the user
  confirms it's approved for publication; otherwise anonymise ("a European telco").
- **Voice rules.** `ONDEWO` always all-caps; headlines and CTAs sentence case; active
  voice, present tense, "we → you"; pick EN-GB or EN-US and stay consistent; avoid the
  banned words in `voice-and-tone.md` §5 (revolutionary, disruptive, magic,
  world-class without proof, …). Let the metrics brag, not the adjectives.
- **Compose, don't replace.** Production/render = `create-brand-asset`; words =
  `brand-copy`. This skill adds the case-study intake, structure, and proof discipline.
