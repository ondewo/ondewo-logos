---
name: create-brand-asset
description: Create any ONDEWO-branded design asset (social post, banner, slide, web page/hero, business card, email signature, letterhead, favicon, README header, ad). Use whenever the user asks to design, generate, make, or mock up branded marketing/design material for ONDEWO. Produces on-brand SVG/HTML/PNG using the official logo, colours (#004C87 blue, #BE216B magenta), Futura/Jost type, and design tokens.
---

# Create an ONDEWO brand asset

You are producing a finished, on-brand ONDEWO design asset. Follow this process
exactly — it guarantees brand consistency without the user re-explaining the brand.

## 0. Load the brand context (always do this first)

Read, in order:
1. `brand-kit/README.md` — kit map.
2. The relevant spec for the asset:
   - colour → `brand-kit/color-system.md`
   - type → `brand-kit/typography.md`
   - logo → `brand-kit/logo-guidelines.md`
   - layout → `brand-kit/layout-and-spacing.md`
   - words → `brand-kit/voice-and-tone.md`
   - contrast → `brand-kit/accessibility.md`
3. `brand-kit/tokens/ondewo.tokens.json` — exact values.
4. The nearest starting point in `brand-kit/templates/`.

Never invent colours, fonts, or redraw the logo — reuse tokens and the official
SVG paths from `brand-kit/assets/logo/`.

## 1. Clarify (only what you can't infer)

Determine: asset type, dimensions/format, the headline/copy, the CTA, light vs.
brand/dark theme, output format (SVG, HTML, PNG, PDF). If the user gave a clear
brief, infer sensible defaults and proceed — don't over-ask. If copy is missing,
draft it per `voice-and-tone.md` and offer it.

## 2. Pick the base

| User wants | Start from |
|------------|-----------|
| Instagram/square post | `templates/social-post-1080.svg` |
| LinkedIn/X cover | `templates/social-banner-linkedin.svg` |
| Slide / title card | `templates/slide-title.svg` |
| Landing page / hero | `templates/web-hero.html` |
| UI mock (buttons/cards) | `templates/components.html` |
| Business card | `templates/business-card.svg` |
| Email signature | `templates/email-signature.html` |
| Letter / one-pager / PDF | `templates/letterhead.html` |
| README / badges | `templates/markdown-snippets.md` |
| Something new | closest of the above; keep tokens + logo |

## 3. Build

- **Embed the logo** by copying the inner paths from the right file in
  `brand-kit/assets/logo/` (mark = two paths in `viewBox="30 30 157 123"`; lockup
  native `viewBox="26.2 26.5 543.4 130.1"`). Scale with a `<g transform>`; never
  trace it by hand.
- **Colours:** only token values. Magenta ≤ ~10% of the surface (one CTA/accent).
- **Type:** the Futura/Jost stack. Headlines sentence-case, Bold or Light. All-caps
  labels get `letter-spacing:0.12em`. For self-contained SVGs use
  `font-family="Jost, Futura, 'Century Gothic', sans-serif"`.
- **Layout:** 4px-grid spacing, generous whitespace, one focal point, one primary CTA.
- **Contrast:** choose a text/bg pair from `accessibility.md` §2. Never blue-on-magenta.
- Theme: light (white bg) by default; brand gradient or `#004C87` for hero moments;
  use mono-white logo on dark/coloured backgrounds.

## 4. Verify before delivering

- Run the checklist in `brand-kit/layout-and-spacing.md` §8.
- **Render it** to confirm it looks right (don't ship unseen):
  - SVG → PNG: `qlmanage -t -s 1600 -o <outdir> <file.svg>` (macOS), or
    `rsvg-convert`/`resvg`/`inkscape` if available.
  - HTML → PNG: headless Chrome
    `--headless --screenshot=out.png --window-size=1280,900 file://<abs path>`.
  - View the PNG and fix any clipping, overflow, or off-brand detail.
- Confirm the logo has clear space and is the correct variant for the background.

## 5. Deliver

- Save source to `brand-kit/generated/<asset-name>.<ext>` (create the folder; never
  overwrite `templates/` or `assets/`). Name per the convention in
  `brand-kit/assets/ASSET-INDEX.md` §D.
- Tell the user what you made, where it is, how to export it at final resolution,
  and which placeholders to tweak.

## Guardrails
- Don't introduce new brand colours, fonts, or a redrawn logo.
- Don't put the full-colour logo on a busy/low-contrast background — use mono white.
- Don't use commercial Futura font files on public web — use Jost (see typography.md).
- Flag, don't fabricate, company facts tagged `‹confirm›` in `brand-foundation.md`.
