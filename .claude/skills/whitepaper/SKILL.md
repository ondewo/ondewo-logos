---
name: whitepaper
description: Write and design an ONDEWO whitepaper or eBook — long-form, gated lead-gen content with a branded cover, TOC, executive summary, framework, data/evidence, solution, CTA, references and about page. Use when the user asks to create/write/design/produce a whitepaper, white paper, eBook, e-book, lead magnet, gated PDF, long-form report, thought-leadership piece, industry guide, or downloadable asset for ONDEWO. Outputs a branded PDF (HTML/Pandoc) plus a designed cover SVG, using the official logo, tokens (#004C87 blue, #BE216B magenta), and Futura/Jost type.
---

# Create an ONDEWO whitepaper / eBook

Produce a finished, authoritative, on-brand long-form lead-gen document: a designed
cover, a structured argument backed by evidence, an ONDEWO solution section, a clear
CTA, and the gated landing-page copy that captures the download. Voice is
**authoritative and low-hype** — proof points, not adjectives.

## 0. Load brand context (always do this first)

Read, in order:
1. `brand-kit/README.md` — kit map.
2. `brand-kit/voice-and-tone.md` — **non-negotiable for a whitepaper**: clear over
   clever, confident not boastful, precise, banned-word list, boilerplate.
3. `brand-kit/document-templates/PLAN.md` — the document-template plan: which
   **output engine** to use (HTML + print CSS vs. Pandoc) and the page/cover specs.
   If it's missing, default to the HTML→PDF engine described in §4.
4. The relevant specs:
   - colour → `brand-kit/color-system.md`
   - type → `brand-kit/typography.md`
   - logo → `brand-kit/logo-guidelines.md`
   - layout → `brand-kit/layout-and-spacing.md`
   - contrast → `brand-kit/accessibility.md`
5. `brand-kit/tokens/ondewo.tokens.json` — exact values (colour, type scale,
   spacing, radii, shadows). Reference tokens by name; never paste raw hex.
6. The nearest print/long-form starter in `brand-kit/templates/` (start from
   `letterhead.html` for the body shell; `slide-title.svg` shows the cover pattern).

Never invent colours, fonts, or redraw the swirl — reuse tokens and the official SVG
paths from `brand-kit/assets/logo/`.

**Compose, don't duplicate.** The designed cover and any standalone figures/charts
are built with the same logo-embedding, token, and render loop as the
**`create-brand-asset`** skill — reuse it for those pieces. This skill adds the
long-form document structure, the gated landing copy, and the multi-page PDF on top;
it does **not** replace `create-brand-asset`.

## 1. Intake (ask/infer — keep it lean)

Infer sensible defaults from the brief and proceed; ask only what blocks you:
- **Topic & thesis** — the one argument the paper makes.
- **Format** — whitepaper (~2,500–4,000 words, analytical) or eBook (~4,000–8,000
  words, more chapters/visuals).
- **Audience** — business buyer, technical evaluator, or developer (sets tone/depth).
- **Proof points** — real stats/quotes/case data. If absent, draft the structure and
  mark every figure as `‹confirm›` — never fabricate numbers, customers, or quotes.
- **Page size & language** — default A4, British English for EU / US English for US
  (pick one and stay consistent).
- **CTA** — "Book a demo" / "Talk to sales" / "Read the docs" (default: Book a demo).

If the brief is clear, draft copy per `voice-and-tone.md` and offer it.

## 2. Canonical structure (the outline — reuse this)

Cover + front matter, then the argument, then back matter. Word counts are targets
for a whitepaper (scale up ~2× for an eBook). Every section gets a heading on the
4px/baseline grid and starts a new page where noted.

| # | Section | Words | Notes / figure callouts |
|---|---------|-------|-------------------------|
| — | **Cover** (own page, designed SVG) | — | Eyebrow `WHITEPAPER`/`EBOOK`, title (sentence case), one-line subtitle, ONDEWO logo, swirl motif, date + version. See §3. |
| — | **Title / legal page** | ~40 | Full title, version, date, `© 2026 ONDEWO`, contact URL. |
| — | **Table of contents** | — | Auto-generated from H2s; page numbers; max 2 levels deep. |
| 1 | **Executive summary** | 150–250 | Stand-alone: thesis, why it matters now, the answer, one headline stat. A busy reader should grasp the whole paper here. |
| 2 | **The problem / context** | 400–700 | Define the pain with evidence. `[FIGURE 1: stat callout or trend chart]`. |
| 3 | **Approach / framework** | 500–900 | The model or method that solves it — vendor-neutral. `[FIGURE 2: framework diagram / flow]`. |
| 4 | **Evidence / data** | 500–900 | Benchmarks, results, third-party data — cited. `[FIGURE 3: chart]` `[TABLE 1: comparison]`. Charts lead with the blue scale; magenta marks the single most important series. |
| 5 | **The ONDEWO solution** | 400–700 | How ONDEWO applies the framework; concrete capabilities (S2T/T2S, dialogue, on-premise, multilingual, 24/7). `[FIGURE 4: architecture or before/after]`. |
| 6 | **Conclusion + CTA** | 150–300 | Restate the thesis, the takeaway, one primary CTA. |
| — | **References** | — | Numbered, cited inline as `[1]`; real sources only. |
| — | **About ONDEWO** | 50–100 | Boilerplate from `voice-and-tone.md` §6 (mark `‹confirm›` bits), logo, contact, CTA. |

**Figure/infographic callouts:** place inline as `[FIGURE n: description]` /
`[TABLE n: description]`. For each, note: caption (sentence case), data source
(cited or `‹confirm›`), and palette (blue scale leading, one magenta highlight, line
icons at 2px stroke). Generate simple charts/diagrams as inline SVG using tokens —
via the `create-brand-asset` loop, not a bespoke style; mark complex infographics as
design placeholders for a human.

### Gated landing-page copy block (always include, separate from the PDF)

Deliver this alongside the document so marketing can publish the gate:

```
Eyebrow:    WHITEPAPER            (all-caps, +0.12em, magenta)
H1:         <benefit-led title, sentence case>
Subhead:    <1–2 sentences: who it's for and the payoff>
What you'll learn:
  • <takeaway 1>
  • <takeaway 2>
  • <takeaway 3>
Form CTA:   Download the whitepaper     (verb-first, no period)
Privacy:    We'll email you the PDF. No spam — unsubscribe anytime.   ‹confirm›
```

Headlines/CTAs sentence case; draft 3 title options and keep the shortest that holds
the benefit (per `voice-and-tone.md`).

## 3. Cover layout (designed SVG)

A4 portrait (default 1240×1754 px @150dpi, or 595×842 pt). Build it the
`create-brand-asset` way (start from `templates/slide-title.svg`); this section just
fixes the cover's content and proportions. Calm, blue-led, generous whitespace —
restraint is on-brand:
- **Background:** white / `neutral-50`, or a `#004C87` / brand-gradient band on the
  lower or upper third. The swirl mark may bleed off-canvas at low opacity as a
  watermark (one motif only).
- **Eyebrow:** `WHITEPAPER` or `EBOOK`, all-caps, `letter-spacing:0.12em`, magenta
  (`#BE216B`) or white on blue.
- **Title:** Futura/Jost, Bold or Light, sentence case, large (`4xl`–`5xl`),
  left-aligned top-left or centred.
- **Subtitle:** one line, `xl`, `neutral-500` (or white on blue).
- **Logo:** horizontal lockup top-left with full clear space; switch to
  `ondewo-logo-horizontal-mono-white.svg` on blue/gradient/photographic backgrounds.
- **Footer strip:** date · version · `ondewo.com`.
Embed the logo/swirl by copying the official paths — mark = two paths
(`fill="#BE216B"`, `fill="#004C87"`) in `viewBox="30 30 157 123"`; lockup native
`viewBox="26.2 26.5 543.4 130.1"`. Scale with a `<g transform>`; never trace by hand.

## 4. Build (apply the brand)

- **Output engine** (per `document-templates/PLAN.md`):
  - **Default — HTML + print CSS → PDF.** Author body as one HTML file importing
    `brand-kit/tokens/ondewo.css`; use `@page { size: A4; margin: 18mm; }`, running
    header/footer with page numbers, `page-break-before` on each H2, and the cover
    SVG as the first page. Render with headless Chrome:
    `chrome --headless --print-to-pdf=out.pdf --no-pdf-header-footer "file://<abs path>"`.
  - **Alternative — Pandoc.** Author body as Markdown; render with a branded HTML
    template + `--pdf-engine` (weasyprint/wkhtmltopdf) or a LaTeX template carrying
    the tokens. Use whichever the PLAN specifies.
- **Colours:** token values only. **Magenta ≤ ~10%** of any page — eyebrows, one key
  stat, the CTA button, a single chart series, rule lines. Blue leads structure;
  neutral/white dominates. Use the signature gradient only on the cover/dividers,
  never under body text.
- **Type:** the Futura/Jost stack (`--ondewo-font-display` / `--ondewo-font-body`).
  Body Regular ≥16px, line-height 1.7 (`relaxed`) for long-form reading, max ~70
  chars/line. Headings sentence case, Bold/Light. All-caps labels get `+0.12em`.
  `ONDEWO` always all-caps with tracking. On public/embedded output use **Jost**
  (open license), not commercial Futura files.
- **Layout:** 18mm A4 margins, baseline grid, 4px spacing scale, one focal point per
  spread. Section dividers = a thin gradient band or single sweeping curve (one motif).
  Charts: blue scale + one magenta series; tables get a `neutral-100` 1px border and
  blue header row, never heavy shadows.
- **Contrast:** every text/bg pair must be on the approved list in
  `accessibility.md` §2 (ink-on-white body; white-on-blue surfaces; magenta `500`+
  for accent text). Never blue-on-magenta or magenta-on-blue.

## 5. Verify (before delivering)

- **Render and read it.** Produce the PDF and the cover PNG and actually view them:
  - HTML→PDF: headless Chrome `--print-to-pdf` (above); open the PDF.
  - Cover SVG→PNG: `qlmanage -t -s 2000 -o ./out <cover.svg>` (macOS), or
    `rsvg-convert`/`resvg`/Inkscape. Fix clipping, overflow, widows/orphans, bad
    page breaks, or off-brand detail.
- **Brand checklist** (`layout-and-spacing.md` §8): correct logo variant + clear
  space; only brand tokens; magenta ≤10%; Futura/Jost + type scale; 4px-grid
  spacing & whitespace; AA contrast; one focal point + one primary CTA per spread.
- **Accessibility:** confirm each text/bg pair is on the approved list; alt text
  `alt="ONDEWO"` on the logo, decorative swirls `aria-hidden`; tagged headings/TOC
  for a navigable PDF; figures have captions, not colour-only meaning.
- **Voice pass:** clear over clever, confident not boastful, active/present, no
  banned words (revolutionary, disruptive, magic, world-class without proof,
  AI-powered as filler). Every stat/quote/customer is real or marked `‹confirm›`.

## 6. Deliver

- Save outputs to `brand-kit/generated/ondewo-whitepaper-<topic-slug>/` (create the
  folder; never overwrite `templates/`, `assets/`, or source files):
  - `ondewo-whitepaper-<topic-slug>-light.pdf` — the final document
  - `ondewo-whitepaper-<topic-slug>-light.html` (or `.md`) — the editable source
  - `ondewo-whitepaper-<topic-slug>-cover-light.svg` — the designed cover
  - `ondewo-whitepaper-<topic-slug>-landing-copy.md` — the gated landing-page copy
- Naming: lowercase, hyphenated, `ondewo-<type>-<variant>-<theme>` per
  `assets/ASSET-INDEX.md` §D.
- Tell the user: what you produced and where; the word count vs. targets; which
  `‹confirm›` placeholders (stats, quotes, boilerplate) still need real data; how to
  re-render the PDF; and the landing-page copy to publish the gate.

## Guardrails

- No off-palette hex, no new typefaces, no redrawn/recoloured/stretched/shadowed
  logo — tokens and official SVG paths only.
- Magenta is an accent (≤ ~10%), never a base fill or full page.
- Never blue-on-magenta or magenta-on-blue; use approved contrast pairs.
- On public/embedded output use Jost, not commercial Futura font files.
- `ONDEWO` always all-caps; headlines/CTAs sentence case, no trailing period on CTAs.
- **Flag, don't fabricate:** mark every statistic, benchmark, quote, customer name,
  and the boilerplate/one-liner tagged `‹confirm›` in `brand-foundation.md` /
  `voice-and-tone.md` with **`‹confirm›`** — the brand kit's unverified-fact marker
  (same intent as a `<confirm>` flag) — and have the user confirm it before
  publishing; never invent it. Authoritative, low-hype voice throughout — let proof
  points do the bragging.
