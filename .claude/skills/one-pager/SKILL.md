---
name: one-pager
description: Create an ONDEWO product/service one-pager or corporate brochure — a single-page product sheet, service overview, sell/fact/spec sheet, datasheet, sales leave-behind, capabilities one-pager, OR a multi-page/multi-section company brochure. Use whenever the user asks to create, write, design, make, draft, or lay out a one-pager, "one pager", product sheet, sell sheet, fact sheet, datasheet/spec sheet, service overview, leave-behind, or brochure for ONDEWO. Outputs print PDF, DOCX, Google Docs, or an on-screen HTML page using the official swirl logo, design tokens (#004C87 blue, #BE216B magenta accent ≤10%), and Futura/Jost type.
---

# Create an ONDEWO one-pager or brochure

Produce a finished, on-brand ONDEWO marketing document — a **single-page one-pager**
or a **multi-section brochure** — with copy in the ONDEWO voice and a layout built
only from brand tokens, the official logo, and the existing document patterns.

**Composes `create-brand-asset`, doesn't replace it.** This skill is the *document
orchestrator*: it sets the page structure, writes the copy, and assembles multiple
on-brand blocks into a one-pager or brochure. The lower-level mechanics — embedding
the official logo SVG paths, applying token colours/type, and rendering/verifying a
single visual — follow the same rules as `create-brand-asset`; reuse that skill's
machinery for any individual element (cover band, hero, stat card). If the user
actually wants **one standalone asset** (a single social post, banner, card, or
signature — not a paginated document), use `create-brand-asset` instead.

## 0. Load the brand context (always do this first)

Read, in order:
1. `brand-kit/README.md` — kit map.
2. `brand-kit/voice-and-tone.md` — voice, tone-by-context, grammar, tagline, boilerplate, copy patterns (you are writing real copy here).
3. The layout/look specs:
   - colour → `brand-kit/color-system.md` (60-30-10, scales, gradient)
   - type → `brand-kit/typography.md` (Futura/Jost stack, scale, all-caps tracking)
   - logo → `brand-kit/logo-guidelines.md` (variants, clear space, min size)
   - layout → `brand-kit/layout-and-spacing.md` (4px grid, whitespace, checklist)
   - contrast → `brand-kit/accessibility.md` (approved text/bg pairs, §2)
4. `brand-kit/tokens/ondewo.tokens.json` (+ `tokens/ondewo.css`) — exact values; use the tokens, never raw hex.
5. **`brand-kit/document-templates/PLAN.md`** — the document-template plan: which **output engine** to use for each format (print PDF / DOCX / Google Docs / on-screen HTML), the reference/base files, and the render commands. **If it exists, it is authoritative for *how* to emit the chosen format — follow it.** If it's absent, fall back to the inline engine recipes in §3 and the render commands in §4.
6. The nearest existing patterns to reuse:
   - `brand-kit/templates/letterhead.html` — A4 print frame (blue/magenta top bar, header logo, footer) → base for **print PDF**.
   - `brand-kit/templates/web-hero.html` — hero, eyebrow/H1/lead, button styles, stat strip → base for **on-screen HTML** and section heroes.
   - `brand-kit/templates/components.html` — buttons, badges, cards → product grid.

Never invent colours, fonts, or redraw the logo. Reuse tokens and the official SVG
paths from `brand-kit/assets/logo/`.

## 1. Intake (infer first, ask only what blocks you)

Pick a **mode** and the few facts you genuinely need:

| Need | Default if unstated |
|------|---------------------|
| **mode**: `product` · `service` · `company-brochure` | infer from the request (a named product/feature → `product`; an offering/engagement → `service`; "brochure"/"about the company" → `company-brochure`) |
| Subject (which product/service/company) | the one named; else ONDEWO CAI / the platform |
| Audience (business · technical · developer) | business buyer; shift tone per voice-and-tone §3 |
| One key message + 3 benefits | draft from brand-foundation/voice; offer them |
| Proof points / stats | use `‹confirm›` placeholders unless real numbers given |
| Primary CTA | "Book a demo" (one only) |
| Output format | **print PDF (A4)** unless the user says HTML / DOCX / Google Docs |
| Theme | light (white) default; one brand-gradient or blue band for the hero/cover |

If copy is missing, **draft it** per `voice-and-tone.md` (3 options, prefer the
shortest that keeps the benefit) and proceed — don't interrogate the user.

## 2. Canonical structure (reusable outline)

**One-pager (`product` / `service`) — single page, one focal point, one CTA:**

1. **Header** — logo (horizontal lockup) top-left; optional thin blue top bar with a magenta inset (from `letterhead.html`).
2. **Eyebrow** — category / product line. All-caps, magenta, `letter-spacing:0.12em`, `text-sm`. (e.g. "Conversational voice AI")
3. **Headline** — outcome-led, sentence case, Futura/Jost Bold or Light, blue. (formula: `[Outcome], [time/scale qualifier].`)
4. **Value prop / lead** — 1–2 sentences, `text-xl`, muted ink, ≤38ch wide. The single key message.
5. **3 benefits** — line-icon + bold label + one supporting line each, in a 3-col row. (`service` mode: frame as outcomes/deliverables.)
6. **How it works** — 3–4 numbered steps (`product`: capture → understand → respond → integrate; `service`: discover → build → deploy → support).
7. **Proof / stats** — 2–3 numbers (bold, blue or magenta) each with a small label. Mark unverified figures `‹confirm›`.
8. **CTA** — one primary button (magenta or blue fill, white text) + optional ghost secondary ("Read the docs").
9. **Footer** — tagline "We automate your phone calls.", contact, ondewo.com.

**Brochure (`company-brochure`) — multi-page/multi-section; reuse the blocks above per product, and add:**

- **Cover** — full-bleed brand-gradient or blue band, mono-white logo, tagline as headline, one-line positioning, hero swirl/visual.
- **About** — company boilerplate (the ≈50-word boilerplate from voice-and-tone §6, kept `‹confirm›`), mission/positioning, 1–2 proof stats.
- **Product / solution grid** — a card per product (ONDEWO CAI, S2T, T2S, telephony…): name, one-line, 2–3 bullets; reuse `components.html` card styles.
- **Per-section spreads** — one one-pager block (eyebrow → headline → benefits → how-it-works → proof) per key product/solution.
- **Proof / customers** — stats band, use-cases, logos/testimonials (`‹confirm›`).
- **Contact / back cover** — CTA, office address(es) `‹confirm›`, email, ondewo.com; repeat the tagline.

Keep **one** brand motif per layout (a single swirl watermark or one gradient band),
generous whitespace, and exactly **one** primary CTA per page/spread.

## 3. Build (apply the brand)

- **Choose the engine** for the requested format — from `document-templates/PLAN.md`
  if present, otherwise the inline recipes below:
  - **On-screen HTML** → build on `web-hero.html` patterns + `tokens/ondewo.css`; responsive, Jost via the Google Fonts link in `typography.md`.
  - **Print PDF (A4/Letter)** → build on the `letterhead.html` frame (`@page { size:A4; margin:0 }`); render HTML → PDF (browser Print → Save as PDF, or headless Chrome `--headless --print-to-pdf`). Use pt sizes; body ~11pt, H1 ~22pt.
  - **DOCX / Google Docs** → use the engine PLAN.md specifies; else Markdown → `pandoc` (apply an ONDEWO `--reference-doc` if one exists), or an HTML/Docs import. Map the same block structure to native heading styles; keep the token colours and Futura→Jost/Century Gothic fallback.
- **Embed the logo** by copying the inner paths from `brand-kit/assets/logo/` —
  horizontal lockup `viewBox="26.2 26.5 543.4 130.1"`, mark `viewBox="30 30 157 123"`
  (magenta `#BE216B` front sweep + blue `#004C87` back sweep). Scale via `<g transform>`;
  never trace or redraw it. Use `ondewo-logo-horizontal.svg` on light backgrounds,
  `…-mono-white.svg` on the blue/gradient cover.
- **Colour:** token values only; 60% neutral / 30% blue / **magenta ≤ ~10%** (one CTA or one accent stat per view). Gradient only for a cover/hero band, never under body text.
- **Type:** the Futura/Jost stack (`var(--ondewo-font-display)` / `--body`). Headlines sentence case; all-caps eyebrows/labels get `0.12em` tracking; body ≥16px (≥11pt print), max ~70ch. `ONDEWO` always all-caps.
- **Layout:** 4px-grid spacing tokens, soft blue-tinted shadows or 1px `neutral-100` borders, `md`/`pill` radii — pick one. Lots of whitespace.
- **Contrast:** pick text/bg pairs from `accessibility.md` §2 (ink on white, white on blue, white on magenta). **Never** blue-on-magenta or magenta-on-blue.

## 4. Verify (before delivering)

- **Render/preview the document** — don't ship it unseen:
  - HTML/PDF → headless Chrome screenshot or `--print-to-pdf`, or `qlmanage`/Playwright; open the output and check every page for clipping, overflow, widows, off-brand detail.
  - DOCX/Google Docs → open and confirm headings, colours, and logo survived the conversion.
- Run the **layout checklist** in `brand-kit/layout-and-spacing.md` §8 (logo clear space + correct variant, tokens only, magenta ≤10%, Futura/Jost scale, 4px grid, one focal point + one CTA).
- **Accessibility:** verify each text/bg pair against `accessibility.md` §2; flag anything <4.5:1 (or <3:1 for large text). Logo has `alt="ONDEWO"`; colour is not the only signal.
- Confirm copy passes voice-and-tone §5 (no banned words; clear, confident, active, present; sentence-case headlines; `ONDEWO` all-caps; no trailing period on buttons).

## 5. Deliver

- Save source to `brand-kit/generated/` (create it; never overwrite `templates/`,
  `assets/`, or source files). Name per `brand-kit/assets/ASSET-INDEX.md` §D, e.g.
  `brand-kit/generated/one-pager-<subject>-<mode>.<html|pdf|docx>` or
  `brand-kit/generated/brochure-<topic>.<ext>` (kebab-case).
- Tell the user: what you made and the mode, where it is, how to export/print at
  final quality (the render command), and which `‹confirm›` placeholders to fill in
  before publishing.

## Guardrails

- No off-palette hex, no new typefaces, no redrawn/recoloured/stretched/shadowed logo — reuse the official SVG paths.
- Magenta is an accent (**≤ ~10%**), never a dominant fill; never blue-on-magenta or magenta-on-blue text.
- On public web/HTML use **Jost** (open license), not commercial Futura font files.
- Headlines/CTAs sentence case; `ONDEWO` all-caps; no trailing period on buttons.
- **Flag, don't fabricate:** keep company facts, stats, addresses, and boilerplate
  tagged `‹confirm›` (from `brand-foundation.md` / `voice-and-tone.md`) as placeholders
  until the user confirms real figures.