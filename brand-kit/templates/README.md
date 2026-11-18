# ONDEWO — Templates

Ready-to-use, on-brand starting points. Each is editable by a human or an AI agent:
open it, replace the placeholder text (`‹...›`, "Your headline", etc.), and ship.

| Template | File | Output | Edit these |
|----------|------|--------|------------|
| Square social post | `social-post-1080.svg` | 1080×1080 (Instagram/LinkedIn) | eyebrow, headline, supporting line, CTA |
| Social/LinkedIn banner | `social-banner-linkedin.svg` | 1584×396 cover | tagline, sub-line |
| Presentation title slide | `slide-title.svg` | 1920×1080 (16:9) | title, subtitle, presenter |
| Business card | `business-card.svg` | 85×55mm @300dpi | name, title, contact |
| Web hero / landing | `web-hero.html` | Responsive web page | eyebrow, H1, lead, CTAs, stats |
| UI components | `components.html` | Buttons, badges, cards, forms, alerts | reference / copy into your app |
| Email signature | `email-signature.html` | HTML mail signature | name, title, contact |
| Letterhead / one-pager | `letterhead.html` | A4 → print to PDF | document body |
| Markdown / badges | `markdown-snippets.md` | README & docs snippets | project name |

## How to render / export

**SVG → PNG** (no extra tooling on macOS):
```bash
qlmanage -t -s 2000 -o ./out brand-kit/templates/social-post-1080.svg
```
Or with librsvg / Inkscape / resvg if installed:
```bash
rsvg-convert -w 2160 brand-kit/templates/social-post-1080.svg -o post.png   # 2x for retina
# or
resvg brand-kit/templates/slide-title.svg slide.png
```

**HTML → PDF/PNG**: open in a browser and Print → Save as PDF, or use a headless
renderer (Playwright/Puppeteer) for automation:
```bash
# Playwright one-liner sketch
npx playwright screenshot --full-page brand-kit/templates/web-hero.html hero.png
```

## Rules every template already follows

- Logo embedded from the official vector paths (never redrawn).
- Brand colours only; magenta used as a ≤10% accent.
- Futura/Jost type stack; sentence-case headlines.
- Clear space around the logo; generous whitespace.
- AA-contrast text/background pairs.

## Creating a new asset

1. Copy the nearest template.
2. Keep colours/fonts as tokens (don't hard-code new values).
3. Save generated output to `brand-kit/generated/` or a campaign folder — **don't
   overwrite** the templates or `assets/`.
4. Run the [brand checklist](../layout-and-spacing.md#8-layout-checklist-before-shipping-any-asset).

> For agent-driven generation, see the skills in `.claude/skills/` (e.g.
> `create-brand-asset`) and the campaign workflow in `.claude/workflows/`.
