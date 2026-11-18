---
name: social-media-kit
description: Generate a multi-platform ONDEWO social media kit — a coordinated post set across LinkedIn, X/Twitter, and Instagram from one topic, with hook options, body captions, hashtags, CTAs, threads/carousels, a content calendar, and matching on-brand post/banner graphics (with alt text). Use whenever the user asks to create/write/design social posts, a social media kit/campaign, LinkedIn/X/Twitter/Instagram content, captions, a thread or carousel, an announcement post, a content calendar, or social graphics for ONDEWO.
---

# ONDEWO social media kit

Turn one topic into a ready-to-publish, on-brand **post set** — copy (hook, body,
hashtags, CTA) plus matching imagery, sized per platform — without the user
re-explaining the brand.

This skill **orchestrates**; it does not replace the single-asset skills. It composes
`brand-copy` for the words and `create-brand-asset` for each visual, then packages
the result as a per-platform kit (and optionally a calendar). Hand individual images
to `create-brand-asset` rather than re-deriving the logo/token/render rules here.

## 0. Load brand context (always do this first)

Read, in order:
1. `brand-kit/README.md` — kit map.
2. `brand-kit/voice-and-tone.md` — **the core spec for captions**: voice principles,
   the tone-by-context table (incl. the "Social (LinkedIn)" row), grammar, like/avoid
   word lists, copy patterns, tagline & boilerplate.
3. For the visuals: `brand-kit/color-system.md`, `typography.md`, `logo-guidelines.md`,
   `layout-and-spacing.md`, `accessibility.md`.
4. `brand-kit/tokens/ondewo.tokens.json` — exact colour/type/space values. Reference
   tokens; never paste raw hex.
5. `brand-kit/document-templates/PLAN.md` — the **output-engine plan**: which engine
   renders which format (SVG→PNG, HTML→PNG/PDF), reference files, render commands.
   Use it to pick the renderer in §3/§4. If it isn't present yet, fall back to the
   render commands in §4 and note that to the user.
6. The two starting templates: `brand-kit/templates/social-post-1080.svg` and
   `brand-kit/templates/social-banner-linkedin.svg`.

Never invent colours, fonts, or redraw the logo — reuse tokens and the official SVG
paths from `brand-kit/assets/logo/`.

## 1. Intake (infer first, ask only what blocks you)

Capture, then proceed on sensible defaults:
- **Topic / angle** — the one idea (a launch, a stat, a use case, a how-it-works,
  an event). Required; if missing, ask for it in one line.
- **Platforms** — default to all three: **LinkedIn + X + Instagram**.
- **Goal & CTA** — awareness vs. demo vs. hire vs. docs. Default CTA "Book a demo".
- **Audience** — business / technical / developer (sets tone; see voice-and-tone §3).
- **Link, real numbers, event date** — if the user gives proof points, use them;
  otherwise keep them as `‹confirm›` placeholders (never fabricate stats).
- **Quantity / cadence** — default: 1 post per platform (a 3-post set). If they want
  a thread, a carousel, or a week/month, produce §2e / the §2d calendar accordingly.

Don't over-ask. A clear topic is enough to draft the full set and offer it.

## 2. Structure — the post set

### 2a. Per-post anatomy (reusable outline)

Every post, on every platform, is built from these slots:

1. **Hook (line 1)** — the scroll-stopper; the only line guaranteed to be read.
   Use a copy pattern from voice-and-tone §7: a sharp stat, a retired-pain line, or
   a pointed question. ≤ ~120 chars so it survives the "see more" truncation.
2. **Body** — context → insight → proof → takeaway. One idea per post. Short
   sentences, active voice, line breaks for breathing room.
3. **CTA** — one verb-first action ("Book a demo", "Read the docs", "See it in
   action"). Sentence case, no trailing period.
4. **Hashtags** — platform-appropriate count (table §2c), on topic. Starter set
   (`‹confirm›` the official tag list with the user):
   `#ONDEWO #VoiceAI #ConversationalAI #CallAutomation #ContactCenter #SpeechAI`.
5. **Image spec** — which template + size (table §2b), the on-image headline/eyebrow,
   theme (light default / brand for hero), and **alt text** (`alt="ONDEWO …"`).

Draft **3 hook options** per platform (outcome-led / pain-led / proof-led) and
recommend the shortest that keeps the benefit — same discipline as `brand-copy`.

### 2b. Platform sizes & which template to start from

| Platform | Format | Pixels | Safe ratio | Start from | Engine |
|----------|--------|--------|-----------|-----------|--------|
| Instagram | Feed square | **1080×1080** | 1:1 | `templates/social-post-1080.svg` | SVG→PNG |
| Instagram | Feed portrait (more reach) | **1080×1350** | 4:5 | post template, extend canvas to 1350 | SVG→PNG |
| Instagram | Story / Reel cover | **1080×1920** | 9:16 | post template, 9:16 canvas, text in central 80% | SVG→PNG |
| LinkedIn | Feed single image | **1200×1200** (1080 ok) | 1:1 | `templates/social-post-1080.svg` | SVG→PNG |
| LinkedIn | Feed portrait | **1080×1350** | 4:5 | post template, extend canvas | SVG→PNG |
| LinkedIn | Link/landscape card | **1200×627** | ~1.91:1 | post template, landscape canvas | SVG→PNG |
| LinkedIn | Profile / page banner | **1584×396** | 4:1 | `templates/social-banner-linkedin.svg` | SVG→PNG |
| X / Twitter | In-stream single image | **1600×900** (1200×675 ok) | 16:9 | post template, 16:9 canvas | SVG→PNG |
| X / Twitter | Square | **1080×1080** | 1:1 | `templates/social-post-1080.svg` | SVG→PNG |
| X / Twitter | Header banner | **1500×500** | 3:1 | `templates/social-banner-linkedin.svg`, retrim to 1500×500 | SVG→PNG |

Keep all text + logo inside the central **80% safe area**; never let the logo touch
an edge (respect clear space). For a new ratio, copy the post template and change the
canvas — keep tokens, logo, and the eyebrow/headline/CTA structure. For a square
**profile picture/avatar**, use `assets/logo/ondewo-avatar.svg` (don't crop the
lockup).

### 2c. Caption voice rules by platform

All platforms inherit the brand voice (clear over clever, confident not boastful,
human, precise; `ONDEWO` all-caps; sentence-case headlines; Oxford comma; numerals
for stats). Per-platform deltas:

| Platform | Tone | Caption length | First-line hook | Hashtags | Notes |
|----------|------|----------------|-----------------|----------|-------|
| **LinkedIn** | Insightful, professional, lightly bold | ~600–1,300 chars (hook in first ~140 before truncation) | Stat or pointed question | **3–5**, at the end | Whitespace between thoughts; one idea; link in post or first comment |
| **X / Twitter** | Punchy, one sharp idea | **≤ 280 chars** | Lead with the payoff | **0–2**, inline/end | Use a thread for depth (§2e); link last |
| **Instagram** | Visual-led, human | ~125 chars before "more"; ≤ 2,200 total | Curiosity/benefit in first line | **5–10** (can sit in first comment) | Caption supports the image; emoji sparingly and on-brand (restraint) |

Banned-word check every caption against voice-and-tone §5 (no *revolutionary,
disruptive, magic, world-class* without proof, *AI-powered* as filler). Pick British
**or** US English per kit and stay consistent (`‹confirm›` the locale).

### 2d. Content-calendar template (use when the ask is a week/month, not one post)

```
| Date | Platform | Format (px) | Topic / angle | Hook | CTA | Hashtags | Asset file | Status |
|------|----------|-------------|---------------|------|-----|----------|-----------|--------|
| 2026-07-01 | LinkedIn | 1200×1200 | <pillar> | <hook> | Book a demo | #ONDEWO … | post-…​.png | Draft |
| 2026-07-02 | X        | 1600×900   | <pillar> | <hook> | Read the docs | #VoiceAI | post-…​.png | Draft |
| 2026-07-03 | Instagram| 1080×1350  | <pillar> | <hook> | See it in action | #ONDEWO … | post-…​.png | Draft |
```

Spread topics across the messaging pillars; keep one idea per post; rotate CTAs.

### 2e. Threads & carousels (when one idea needs more room)

- **X/LinkedIn thread:** a hook post (the §2a hook, standalone and complete) →
  2–5 proof/detail posts (one point each, ≤280 chars on X) → a final CTA post with
  the link. Number them only if it aids reading.
- **Carousel (LinkedIn doc / Instagram):** a sequence of **1080×1080** or
  **1080×1350** slides — slide 1 = hook cover, middle slides = one idea each, final
  slide = CTA. Build each slide from the post template; keep a consistent eyebrow/logo
  position so the set reads as one family. Caption still follows §2a/§2c.

## 3. Build

**Copy** — invoke the `brand-copy` discipline: draft 3 hook options per platform,
self-check against the word lists/grammar, keep proof numbers as `‹confirm›` unless
the user gave real figures. Assemble each post per the §2a anatomy.

**Visuals** — hand each image spec to **`create-brand-asset`** (so the logo, tokens,
contrast, and render step are handled identically). Each spec gives it:
- **Base:** the right template from §2b (`social-post-1080.svg` for square posts,
  `social-banner-linkedin.svg` for covers); copy into `generated/`, change the canvas
  for other ratios.
- **Logo:** embed from `brand-kit/assets/logo/` (full-colour lockup on light;
  **mono-white** lockup/mark on the brand-blue/gradient hero); never redraw the swirl.
- **Colour:** token values only; **magenta ≤ ~10%** of the surface (one accent — the
  CTA pill, the eyebrow, or a single stat). Light theme by default; `#004C87` or the
  brand gradient for a hero moment.
- **Type:** the Futura/Jost stack (`font-family="Jost, Futura, 'Century Gothic',
  sans-serif"` in self-contained SVGs). Sentence-case headline; all-caps eyebrow gets
  `letter-spacing:0.12em`.
- **Layout:** 4px-grid spacing, generous whitespace, one focal point, one CTA; copy
  inside the 80% safe area.
- Map the on-image headline to the post hook (don't restate the whole caption on the
  image — one line that earns the read).

## 4. Verify (before delivering)

- **Render every image** (don't ship unseen). Use the engine from
  `document-templates/PLAN.md`, or fall back to:
  - SVG → PNG: `qlmanage -t -s 2000 -o <outdir> <file.svg>` (macOS), or
    `rsvg-convert -w 2160 <file.svg> -o out.png` / `resvg <file.svg> out.png`.
  - HTML → PNG: headless Chrome `--headless --screenshot=out.png
    --window-size=1280,1280 file://<abs path>`, or `npx playwright screenshot`.
  - View each PNG; fix clipping, overflow, safe-area breaches, off-brand detail.
- **Brand checklist** — run `brand-kit/layout-and-spacing.md` §8 on each asset
  (logo clear space + correct variant; tokens only; magenta ≤10%; Futura/Jost; 4px
  grid; one focal point + one CTA).
- **Accessibility** — every on-image text/bg pair must be on the approved list in
  `accessibility.md` §2 (ink-on-white, white-on-blue, white-on-magenta, magenta-on-
  white). **Never blue-on-magenta or magenta-on-blue.** Below 24px tall, use the
  mark-only logo. Provide alt text per post.
- **Copy** — banned-word pass, `ONDEWO` all-caps, sentence-case headline/CTA, hashtag
  count matches the platform, hook survives truncation, locale consistent.

## 5. Deliver

- Save sources + rendered PNGs to **`brand-kit/generated/social/<topic-or-campaign>/`**
  (create the folder; never overwrite `templates/` or `assets/`).
- Name: `<platform>-<format>-<topic>.<ext>` — e.g.
  `linkedin-1200x1200-on-prem-launch.svg` (+ `.png`),
  `x-1600x900-on-prem-launch.png`, `ig-1080x1350-on-prem-launch.png`.
- Present the kit as: per platform → the recommended **hook** (+ 2 alternatives),
  **body caption**, **hashtags**, **CTA**, and the **image** (path + alt text). If a
  thread/carousel or calendar was requested, include the §2e / §2d structure.
- Tell the user where the files are, how to export at final resolution (2× for
  retina), which `‹confirm›` placeholders (stats, link, locale, hashtag list) to fill,
  and that they can ask to adjust any hook, swap a platform, or extend to a calendar.

## Guardrails

- No off-palette hex and no new typefaces — tokens + Futura/Jost only.
- Magenta is an accent (**≤ ~10%**), never the dominant fill; one accent per image.
- Never recolour, stretch, shadow, or redraw the logo; mono-white on dark/coloured
  backgrounds; respect clear space; mark-only below 24px.
- Never use a forbidden contrast pair (blue-on-magenta / magenta-on-blue).
- Don't fabricate metrics, customer names, or claims — flag inferred facts as
  `‹confirm›` (and treat the boilerplate/one-liner from voice-and-tone §6 as `‹confirm›`).
- Voice: clear over clever, confident not boastful, active/present, `ONDEWO` all-caps,
  sentence-case headlines/CTAs, no banned words; one locale per kit.
- Compose, don't duplicate: route words through `brand-copy` and each image through
  `create-brand-asset`; this skill only coordinates and packages the set.