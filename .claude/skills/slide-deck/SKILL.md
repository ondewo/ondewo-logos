---
name: slide-deck
description: Build an ONDEWO-branded slide deck — investor pitch deck, company presentation/overview, sales deck, or webinar deck — as 16:9 SVG slides and/or PPTX (python-pptx), Google Slides, or PDF. Use when the user asks to create, write, design, make, build, or mock up a pitch deck, investor deck, fundraising/seed/Series-A deck, company presentation, company overview deck, sales deck, customer-meeting slides, demo deck, or webinar deck for ONDEWO ("make a slide deck", "design our pitch", "build a sales presentation", "put together overview slides", "deck for the webinar"). Renders on-brand using the official swirl logo, design tokens (#004C87 blue, #BE216B magenta accent ≤10%), and Futura/Jost type.
---

# Build an ONDEWO slide deck

You are producing a finished, on-brand ONDEWO presentation. This is a **modal**
skill — pick one `mode` and follow its narrative arc, then apply the shared brand
build. One idea per slide, big type, magenta only for the single key number.

This skill **composes**, it does not replace, the base skills: it builds each SVG
slide with the shared `create-brand-asset` brand build (logo embedding, token
colours, contrast, render-before-ship) and audits the result with `brand-check`.
It adds the deck-specific narrative arcs and the presentation output engines
(PPTX / Google Slides / PDF) on top. Don't re-derive the brand rules — reuse them.

`mode: pitch | company | sales | webinar`

| mode | Deck | Audience | Default length |
|------|------|----------|----------------|
| `pitch` | Company presentation / pitch deck | Investors | 10–12 slides |
| `company` | Company overview deck | Prospects, partners, press, recruiting | 10–14 slides |
| `sales` | Sales deck | A customer in a meeting | 10–12 slides |
| `webinar` | Webinar deck | Live/recorded audience | 12–20 slides |

## 0. Load the brand context (always do this first)

Read, in order:
1. `CLAUDE.md` (repo root) — brand TL;DR and the hard rules that govern everything below.
2. `brand-kit/README.md` — kit map.
3. `brand-kit/voice-and-tone.md` — every headline, sub, and speaker note uses this.
4. `brand-kit/brand-foundation.md` — mission, positioning, audience, messaging
   pillars, proof points (the raw material for the narrative). Facts tagged
   `‹confirm›` are inferred — flag, don't assert.
5. `brand-kit/typography.md`, `color-system.md`, `layout-and-spacing.md`,
   `logo-guidelines.md`, `accessibility.md` — design rules.
6. `brand-kit/tokens/ondewo.tokens.json` — exact colour/type/space values. Use
   token values only; never raw guesses.
7. `brand-kit/document-templates/PLAN.md` — the document-template **output-engine
   plan** (which engine produces PPTX / Google Slides / PDF, the reference files,
   and how to invoke each). This is the authority for *how* to emit a chosen
   format. **If it isn't present, fall back to the inline engine guidance in §4.**
8. `brand-kit/templates/slide-title.svg` — the canonical 16:9 frame to reuse.

Never invent colours, fonts, or redraw the logo — reuse tokens and the official
SVG paths from `brand-kit/assets/logo/`.

## 1. Intake (ask only what you can't infer)

Confirm or infer, then proceed — don't interrogate:
- **mode** (pitch / company / sales / webinar) — usually obvious from the request.
- **Audience & occasion** — which investor/customer/event; what they care about.
- **The one takeaway** — if they remember a single slide, which is it?
- **Real numbers** — traction, ARR, customers, languages, latency, % uplift. Keep
  anything you don't have as a `‹confirm›` placeholder; never fabricate metrics.
- **Output format** — SVG slides, PPTX, Google Slides, or PDF (default: SVG set
  + offer PPTX).
- **Length & branding** — slide count, presenter name/role, date, light vs. brand
  theme for the title/section dividers.

If copy is missing, draft it per `voice-and-tone.md` and offer it. Default to
British English for EU-facing decks, US English for US-facing (`‹confirm›`).

## 2. Structure — the canonical arc per mode

One idea per slide. Each slide = an **eyebrow** (all-caps label, magenta, +0.12em),
a **sentence-case headline** (the point, Futura/Jost Bold), and minimal support
(≤3 bullets or one stat or one visual). Open with a title slide and close with a
CTA slide built from `slide-title.svg`.

### mode: pitch (investor deck)
1. **Title / hook** — ONDEWO + tagline *We automate your phone calls.* + one-line positioning.
2. **Problem** — the pain, made vivid (e.g. "97% of callers hang up after 2 min on hold"). One stat.
3. **Solution** — what ONDEWO does in one sentence; the "after" state.
4. **Product / how it works** — speech-to-text → dialogue → text-to-speech → telephony, on-premise. One simple flow diagram (arcs/soundwave motif), not a wall of features.
5. **Why now** — market timing / shift that makes this inevitable.
6. **Market size** — TAM/SAM/SOM; the single key number in magenta. `‹confirm›`
7. **Traction** — customers, calls automated, ARR, growth curve. Proof, not adjectives.
8. **Business model** — how ONDEWO makes money (licence / usage / on-prem); unit economics.
9. **Competition / moat** — why ONDEWO wins: on-premise, multilingual, modular, engineering-led.
10. **Team** — founders + key hires; why this team.
11. **The ask** — round size, use of funds, milestones it buys. One clear number in magenta.
12. **Closing** — vision one-liner + contact CTA ("Talk to us").

### mode: company (overview deck)
1. **Title** — ONDEWO + tagline + one-liner.
2. **Who we are** — boilerplate in one line; HQ/footprint. `‹confirm›`
3. **What we believe / mission** — the human-behind-automation angle.
4. **What we do** — the platform at a glance (one outcome-led sentence).
5. **How it works** — the modular stack (CAI, S2T, T2S, telephony) as a clean flow.
6. **Why ONDEWO is different** — on-premise data control, multilingual, real-time, modular. 3 pillars max.
7. **Proof** — customers / logos / a headline result. `‹confirm›`
8. **Deployment & security** — on-premise, data never leaves your infrastructure.
9. **Use cases** — 2–4 concrete scenarios (hotline, support, scheduling).
10. **The team / company** — size, expertise, partners. `‹confirm›`
11. **Contact / CTA** — "Book a demo" / "Talk to sales".

### mode: sales (customer meeting)
1. **Title** — co-branded if relevant; the meeting's purpose.
2. **Your challenge** — restate *their* pain in their words. Earns the room.
3. **The cost of doing nothing** — missed calls, hold times, handling cost. One number.
4. **Our solution** — ONDEWO mapped directly to their challenge.
5. **How it works** — simple flow; emphasise the demo, don't over-explain architecture.
6. **Outcomes / ROI** — answer 100% of calls, cut average handling time, languages added. The key uplift in magenta. `‹confirm›`
7. **Proof / case study** — a comparable customer and result. `‹confirm›`
8. **Deployment & integration** — on-premise, SIP/telephony, fits their stack, data control.
9. **Pricing / packages** — tiers or model; keep it clean. `‹confirm›`
10. **Implementation** — onboarding timeline and what's needed from them.
11. **Next steps** — one clear CTA and a date ("Book the pilot").

### mode: webinar
1. **Title** — topic + ONDEWO + presenter(s) + date.
2. **Presenters** — names, roles, one credibility line.
3. **Agenda** — 3–5 items; set expectations.
4. **Why this matters** — the hook / the stat that frames the session.
5–N. **Body** — one key takeaway per slide (aim for 3 core takeaways, each its own
   1-idea slide; use section-divider slides between them).
- **Live demo** — a "Demo" divider slide; keep the deck out of the way.
- **Recap** — the 3 takeaways on one slide.
- **Q&A** — prompt slide.
- **Resources** — links, docs, next webinar.
- **CTA / follow-up** — "Book a demo" / "Read the docs"; contact.

## 3. Slide design rules (the ONDEWO look)

- **One idea per slide.** If a slide needs two headlines, split it.
- **Big type.** Headline `4xl`–`5xl` Bold; body `lg`–`xl`. Never shrink below
  `base` to cram more in — cut content instead.
- **Magenta for the single key number.** Per slide, at most one element is magenta
  (a stat, a CTA, the eyebrow). Everything structural is blue/ink on white.
  Magenta ≤ ~10% of any slide and of the deck overall.
- **Whitespace is the design.** 96px outer margin on the 1920×1080 frame, 48px
  gutter, 4px-grid spacing. Lots of air.
- **Section dividers** may use the brand gradient or solid `#004C87` with the
  mono-white logo — these are the deck's "hero moments".
- **One brand motif** — the swirl/soundwave as a low-opacity watermark, used
  sparingly (already in `slide-title.svg` at opacity 0.05).
- **Eyebrow → headline → support** is the repeating grid for content slides.

## 4. Build — apply the brand

For SVG slides, this is the `create-brand-asset` build applied to a 16:9 frame —
the same logo/colour/type/contrast rules, just repeated per slide.

### Logo
Reuse the official artwork — copy the inner paths from `brand-kit/assets/logo/`:
- Lockup native `viewBox="26.2 26.5 543.4 130.1"` (full colour on white;
  `ondewo-logo-horizontal-mono-white.svg` on blue/gradient dividers).
- Mark = two paths (`fill="#BE216B"` front, `fill="#004C87"` back) in
  `viewBox="30 30 157 123"`. Scale via `<g transform>`; never trace by hand.

### Colours & type (tokens only)
- Surfaces: white / `neutral-50`. Primary structure: `#004C87`. Accent: `#BE216B`
  (one per slide). Muted captions: `#5A5560`. Dark dividers: `#00345C`/`#001A2E`.
- Font stack for self-contained SVG:
  `font-family="Jost, Futura, 'Century Gothic', sans-serif"`. Headlines sentence
  case; `ONDEWO` all-caps with `+0.12em`; all-caps eyebrows letter-spaced. In a
  self-contained SVG use an **absolute** `letter-spacing` (e.g. `letter-spacing="3.4"`
  at ~28px ≈ 0.12em) — some renderers ignore `em` on `letter-spacing`.

### Pick the output engine
| Output | How |
|--------|-----|
| **SVG slides** (default) | Copy `templates/slide-title.svg` → title + CTA slides. For each content slide, reuse its frame (top blue bar with the magenta inset, watermark, logo) and swap the eyebrow/headline/support. One `slide-NN.svg` per slide in the deck folder. |
| **PPTX** | Use **python-pptx** per `document-templates/PLAN.md`. Set a 16:9 frame: `prs.slide_width=Inches(13.333)`, `slide_height=Inches(7.5)`. Build colours from tokens: `RGBColor(0x00,0x4C,0x87)`, `RGBColor(0xBE,0x21,0x6B)`, `RGBColor(0x23,0x1F,0x20)`. Set fonts to "Jost" (or "Futura PT" only if the deck will open on a licensed machine). Embed the logo PNG/SVG; one idea per slide; magenta on a single run. |
| **Google Slides** | Use the Slides API generator in `document-templates/PLAN.md` (create presentation → batchUpdate text + shapes with the token hexes + Jost). |
| **PDF** | Render the SVG set (§5) to PNG/PDF and combine, or export the PPTX/HTML to PDF. Decks rendered to outlines may use Futura. |

If `document-templates/PLAN.md` is absent, default to the **SVG set** and offer to
generate a PPTX with python-pptx (`pip install python-pptx`).

## 5. Verify before delivering

- **Render every slide** — don't ship unseen:
  - SVG → PNG: `qlmanage -t -s 1920 -o <outdir> <slide>.svg` (macOS), or
    `rsvg-convert`/`resvg`/`inkscape`.
  - PPTX → check by opening, or `libreoffice --headless --convert-to pdf`.
  - View the PNGs; fix clipping, text overflow, off-brand detail, lonely slides.
- **Run `brand-check`** on the rendered slides (or manually run the checklist in
  `brand-kit/layout-and-spacing.md` §8 on each): tokens-only colours, magenta ≤ ~10%,
  Futura/Jost + type scale, 4px spacing, correct logo variant + clear space, one
  focal point + one CTA per slide.
- **Accessibility** — every text/bg pair must be on the approved list in
  `accessibility.md` §2 (ink-on-white, white-on-blue, blue-on-white, magenta-on-white
  at `500`/`#BE216B` or darker). Never blue-on-magenta or magenta-on-blue. Body text
  contrast ≥ 4.5:1.
- **Logo** — correct variant for the background, full clear space, ≥24px tall (mark
  only below that), not stretched/recoloured/shadowed.
- **Voice** — sentence-case headlines, active/present, `ONDEWO` all-caps, no banned
  words (voice-and-tone §5), one benefit per slide.

### Speaker notes
Give each content slide a 2–4 sentence note in ONDEWO voice: the point, the proof,
and the transition to the next slide. In SVG, deliver notes alongside as
`slide-NN.notes.md`; in PPTX/Google Slides, populate the notes pane. Keep on-slide
text sparse — the detail lives in the notes, not the slide.

## 6. Deliver

- Save the set to `brand-kit/generated/<deck-name>/` (create the folder; never
  overwrite `templates/` or `assets/`). Name slides `slide-01-title.svg`,
  `slide-02-problem.svg`, … and the master `ondewo-<mode>-deck.pptx` / `.pdf`.
- Include a `README.md` listing the slide order and which `‹confirm›` numbers the
  user must fill.
- Tell the user: what you built, where it is (absolute path), how to render/export at
  final resolution, which placeholders/metrics to confirm, and offer the alternate
  format (e.g. "want this as a PPTX too?").

## Guardrails
- No off-palette hex, no new typefaces, no redrawn or recoloured swirl.
- Magenta is an accent (≤ ~10%) — one key number/CTA per slide, never a base fill.
- Never blue-on-magenta or magenta-on-blue; use approved pairs only.
- On public web, use **Jost**, not commercial Futura files; Futura is fine for
  decks/PDFs on licensed machines or rendered to outlines.
- One idea per slide; cut content before shrinking type below `base`.
- Flag every inferred company fact / metric as `‹confirm›` — never present an
  invented number as real. Investor and sales decks live or die on accurate figures.