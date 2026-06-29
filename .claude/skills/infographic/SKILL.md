---
name: infographic
description: Create data-driven ONDEWO infographics — single-stat hero, process/steps, comparison, timeline, and "by the numbers" layouts — as self-contained SVG (portrait 1080×1350 social + web). Use whenever the user asks to create, design, make, generate, or mock up an infographic, stat card, data viz, chart graphic, "by the numbers", process/steps diagram, timeline, or comparison graphic for ONDEWO. Renders on-brand using the official swirl logo, #004C87 blue, #BE216B magenta accent (≤10%), Futura/Jost type, and the design tokens.
---

# Create an ONDEWO infographic

You are producing a finished, on-brand ONDEWO **infographic**: a data-driven,
shareable graphic that turns a few numbers or a short process into a clean,
geometric, blue-led visual. Output is self-contained SVG you can render to PNG.
Follow this process exactly — it guarantees brand consistency without the user
re-explaining the brand.

This is the **infographic specialization of `create-brand-asset`**. It reuses that
skill's logo-embed, token, contrast, and render conventions and adds the data-viz
structure below (stat heroes, process, comparison, timeline, KPI grids). For a
generic social post, banner, slide, or web hero with **no data story**, use
`create-brand-asset` directly — don't rebuild it here.

## Load brand context (always do this first)

Read, in order:
1. `brand-kit/README.md` — kit map.
2. `brand-kit/color-system.md` — palette, the **blue/magenta scales** for charts, 60-30-10.
3. `brand-kit/typography.md` — Futura/Jost stack, type scale, all-caps tracking.
4. `brand-kit/layout-and-spacing.md` — 4px grid, whitespace, the arc/swirl graphic language, the pre-ship checklist (§8).
5. `brand-kit/accessibility.md` — approved text/bg contrast pairs (§2) and the "don't rely on colour alone" rule for charts (§4).
6. `brand-kit/logo-guidelines.md` — logo variants, clear space, §8 raw swirl geometry.
7. `brand-kit/voice-and-tone.md` — headline/label copy, sentence case, `ONDEWO` all-caps, banned words, `‹confirm›` facts.
8. `brand-kit/tokens/ondewo.tokens.json` — exact colour/type/space values (never paste raw hex from memory).
9. `brand-kit/document-templates/PLAN.md` — the document-template PLAN listing the **output engines/format** to use (if present). Otherwise use the render recipes in **Verify** below.
10. Nearest visual starting point: `brand-kit/templates/social-post-1080.svg` (logo embed, swirl watermark, eyebrow/headline/CTA/footer patterns to reuse).

Never invent colours, fonts, or redraw the logo — reuse tokens and the official SVG
paths from `brand-kit/assets/logo/`.

## Intake (infer first, ask only what blocks you)

From the brief, pin down — defaulting where you can:
- **The data** — the numbers/labels/sources. This is the one thing you cannot invent:
  if real figures are missing, use clearly-labelled `‹placeholder›` values and flag them.
- **The story / pattern** — which of the five layouts below fits (a single hero stat?
  a 3-step process? a head-to-head comparison? a dated timeline? a 3–4 stat grid?).
- **Format** — default **portrait 1080×1350** (Instagram/LinkedIn feed); offer
  **1080×1080** square or a responsive web variant if the channel differs.
- **Theme** — light (white bg, default) or brand (blue/gradient hero band).
- **Headline + source line** — draft per `voice-and-tone.md` if absent; offer it.

If the brief is clear, choose sensible defaults and proceed — don't over-ask.

## Structure (canonical infographic skeleton)

Every ONDEWO infographic shares this frame; the **body** swaps per pattern.

```
┌────────────────────────────── 1080 × 1350 ──────────────────────────────┐
│  [80px margin]  ⊙ ONDEWO logo (top-left, mono-white on brand theme)       │
│                                                                          │
│  ── magenta accent bar (64×8, rx4)                                       │
│  EYEBROW / CATEGORY            ← all-caps, magenta-500, +0.12em tracking  │
│  A sentence-case headline that states the takeaway.   ← blue-700/ink     │
│                                                                          │
│  ┌──────────────── BODY: one of the five patterns ────────────────┐      │
│  │                                                                 │      │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  Source: ‹…›  ·  one caveat            ondewo.com   ← neutral-500, small  │
│  [low-opacity swirl watermark bleeding off a corner, opacity ~0.06]      │
└──────────────────────────────────────────────────────────────────────────┘
```

Pick the body pattern:

1. **Single-stat hero** — one giant number is the whole point.
   Huge Bold figure (`text-5xl`+, blue-700; or magenta for the *one* hero stat),
   unit/`%` smaller beside it, a one-line caption under it, source at the foot.
   Optional thin arc or radial ring (swirl language) framing the number.

2. **Process / steps** — "how it works" in 3–5 stages.
   Numbered nodes (`01 02 03`) on a single sweeping connector line/arc; each node =
   small blue circle + Medium label + one-line detail. Magenta only on the final/key
   step. Vertical flow suits portrait.

3. **Comparison** — before/after or us-vs-them.
   Two columns or two stacked bars. Neutral/blue for the baseline, **magenta for the
   ONDEWO/winning side**. Label both sides in words and numbers — never colour alone.

4. **Timeline** — milestones over time.
   Vertical spine (blue), dated nodes top→bottom, year/Bold label + short note. One
   magenta node for the pivotal moment. Keep to 4–6 entries.

5. **By the numbers** — a grid of 3–4 KPIs.
   2×2 or stacked cards (white/`neutral-50`, 1px `neutral-100` border, `radius-lg`),
   each: Bold number + small caps label + tiny note. Lead in blue; tint **one** card
   magenta as the headline metric.

**Charts inside any pattern** (bars, donut, dot/bar comparisons):
- **Lead with the blue scale** (`blue-500 #004C87 → 400 #3873A1 → 300 #739DBD → 200 #A8C2D6`)
  for ordered/secondary series; use **magenta `#BE216B` for the single most important
  series/value** only.
- **Minimal data-ink:** no chartjunk, 3D, heavy gridlines, or drop shadows. A thin
  `neutral-100` baseline, **direct value labels** on bars/segments instead of an axis.
- **Accessible, not colour-only:** every series carries a text label/value; differentiate
  with labels, order, or a subtle pattern so it survives greyscale/colour-blindness.
- Axis/caption text in `neutral-500`; numbers Bold in blue or the magenta accent.

## Build

- **Canvas:** `<svg width="1080" height="1350" viewBox="0 0 1080 1350" font-family="Jost, Futura, 'Century Gothic', sans-serif">`; background `#FFFFFF` (or `#004C87` / brand gradient for a hero theme). 80px outer margin; align everything to the 4px grid.
- **Embed the real logo** by copying paths from `brand-kit/assets/logo/` — never trace it:
  - Lockup (`ondewo-logo-horizontal.svg`, native `viewBox="26.2 26.5 543.4 130.1"`) top-left; on a brand/dark theme use `ondewo-logo-horizontal-mono-white.svg`.
  - The decorative swirl watermark = the two `ondewo-mark.svg` paths (`viewBox="30 30 157 123"`, `fill="#BE216B"` front + `fill="#004C87"` back) at `opacity≈0.06`, bleeding off a corner — `aria-hidden`. Scale with a `<g transform>`; never redraw.
- **Colours: tokens only.** Blue leads (structure, bars, spine, headings). **Magenta ≤ ~10% of the surface** — one hero stat, one winning bar, one final step, or one CTA. Never a magenta background field behind data.
- **Type:** the Futura/Jost stack. Headlines sentence case, Bold or Light; numbers Bold; eyebrow/labels all-caps with `letter-spacing≈0.12em` (use `letter-spacing="3.4"` at ~28px). Body ≥ `text-base` (16px); captions `text-sm`.
- **Contrast:** pick a text/bg pair from `accessibility.md` §2 (ink-on-white, white-on-blue, magenta-on-white for accents). **Never blue-on-magenta or magenta-on-blue.**
- **Brand texture, restrained:** one swirl/arc motif per layout — the watermark *or* a connector arc, not both loud. Generous whitespace over decoration.
- **Copy:** sentence-case headline stating the takeaway; `ONDEWO` all-caps; numerals for stats; cite a source line. Tagline *We automate your phone calls.* only where it fits.

Output format: a single **self-contained SVG** (fonts referenced by stack, logo paths
inlined) so it renders identically everywhere and exports cleanly to PNG.

## Verify (render — never ship unseen)

1. **Render to PNG and look at it:**
   ```bash
   qlmanage -t -s 2000 -o ./out brand-kit/generated/<file>.svg   # macOS, no deps
   # or, if installed:
   rsvg-convert -w 2160 brand-kit/generated/<file>.svg -o out.png   # 2× retina
   resvg brand-kit/generated/<file>.svg out.png
   ```
   View the PNG; fix any clipping, overflow, off-grid spacing, or off-brand detail.
2. **Brand checklist** — run `brand-kit/layout-and-spacing.md` §8: brand colours/tokens only; magenta ≤ ~10%; Futura/Jost + type scale; 4px grid + whitespace; AA contrast; one focal point.
3. **Logo:** correct variant for the background, full clear space, not stretched/recoloured/shadowed, ≥ 24px tall (else mark-only).
4. **Accessibility pairs:** confirm every text/bg combo is on `accessibility.md` §2; confirm each chart series is distinguishable **without colour** (labels/values present, survives greyscale).
5. **Numbers:** re-read every figure against the source; ensure `‹placeholder›`/`‹confirm›` items are still flagged, not presented as fact.

## Deliver

- Save the SVG to `brand-kit/generated/` (create the folder if needed; **never** overwrite `templates/`, `assets/`, or `tokens/`).
- Name per `assets/ASSET-INDEX.md` §D: `ondewo-infographic-<topic>-<theme>-1080x1350.svg`
  (e.g. `ondewo-infographic-hold-times-light-1080x1350.svg`). Save the rendered PNG alongside as `…-1080x1350.png`.
- Tell the user: what you made and which pattern, where it is, how to export at final resolution (the `qlmanage`/`rsvg-convert` line), which placeholders/numbers to replace, and any `‹confirm›` facts they must verify before publishing.

## Guardrails

- **No off-brand colours or fonts** — token values only; extend along the blue/magenta/neutral scales, never a new hue. No commercial Futura files on public web — use **Jost** (`typography.md`).
- **Magenta is the spark, not the base** — ≤ ~10%, for the single key stat/series/CTA. Never magenta-on-blue or blue-on-magenta (contrast 1.52, fails).
- **Never redraw, stretch, recolour, or shadow the swirl/logo** — reuse the official SVG paths; respect clear space and min size.
- **Don't invent data.** Real figures only; otherwise clearly-labelled `‹placeholder›`/`‹confirm›`, flagged to the user — never present inferred numbers as confirmed fact (`CLAUDE.md` hard rule 7).
- **Charts must not rely on colour alone** — always label series/values for accessibility.
- **Voice:** clear over clever, confident not boastful, active voice, sentence-case headlines/labels, `ONDEWO` all-caps, no banned words (`voice-and-tone.md` §5).
