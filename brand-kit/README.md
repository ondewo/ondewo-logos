# ONDEWO Brand Kit

A complete, AI-ready brand & design system for **ONDEWO** — *we automate your phone
calls.* Everything you (or a coding agent) need to produce on-brand material:
guidelines, design tokens, ready-to-edit templates, clean logo assets, and the
skills/workflows that automate it.

> **Agents:** read [`../CLAUDE.md`](../CLAUDE.md) first — it's the entry point.

---

## 30-second start

**I want to…**

| Goal | Go to |
|------|-------|
| Make a social post / banner / slide / web page | [`templates/`](templates/) → copy → edit text → render |
| Get the colours in code | [`tokens/`](tokens/) (CSS / SCSS / Tailwind / JSON) |
| Grab a logo | [`assets/logo/`](assets/logo/) · index → [`assets/ASSET-INDEX.md`](assets/ASSET-INDEX.md) |
| Write on-brand copy | [`voice-and-tone.md`](voice-and-tone.md) |
| Check something is on-brand | [`accessibility.md`](accessibility.md) + the checklist in [`layout-and-spacing.md`](layout-and-spacing.md) |
| Have an agent do it for me | `.claude/skills/create-brand-asset` (and `brand-copy`, `brand-check`) |

## The brand in one screen

| Element | Value |
|---------|-------|
| **Logo** | Two-tone swirl forming the "O" of `ONDEWO`. [Guidelines](logo-guidelines.md) |
| **Blue** | `#004C87` — primary, structure, trust |
| **Magenta** | `#BE216B` — accent only (≤10%), energy/voice |
| **Ink** | `#231F20` — body text |
| **Type** | Futura PT → **Jost** (free web fallback). Sentence-case headlines. |
| **Feel** | Clean, geometric, confident, human, engineering-led. Lots of whitespace. |
| **Voice** | Clear over clever. Confident, not boastful. *We automate your phone calls.* |

## Documentation

| Doc | What's inside |
|-----|---------------|
| [`brand-foundation.md`](brand-foundation.md) | Mission, positioning, audience, personality, messaging pillars |
| [`voice-and-tone.md`](voice-and-tone.md) | Voice principles, tone by context, grammar, word lists, copy patterns |
| [`logo-guidelines.md`](logo-guidelines.md) | Variants, clear space, min size, misuse, code snippets |
| [`color-system.md`](color-system.md) | Palette, 50–900 scales, gradient, 60-30-10, usage |
| [`typography.md`](typography.md) | Futura/Jost, type scale, weights, CSS starter |
| [`layout-and-spacing.md`](layout-and-spacing.md) | Grid, 4px spacing, imagery, icons, motion, pre-ship checklist |
| [`accessibility.md`](accessibility.md) | Pre-computed WCAG AA contrast pairs (approved & forbidden) |
| [`tokens/README.md`](tokens/README.md) | How to consume the design tokens |
| [`templates/README.md`](templates/README.md) | Every template + how to render/export |
| [`assets/ASSET-INDEX.md`](assets/ASSET-INDEX.md) | Every logo file and when to use it |

## What's in the box

```
brand-kit/
├── README.md                 ← this file
├── brand-foundation.md       ├─ docs (markdown)
├── voice-and-tone.md         │
├── logo-guidelines.md        │
├── color-system.md           │
├── typography.md             │
├── layout-and-spacing.md     │
├── accessibility.md          ┘
├── tokens/                   ← ondewo.tokens.json · ondewo.css · ondewo.scss · tailwind.preset.js
├── templates/                ← social, banner, slide, web hero, components, card, signature, letterhead, md snippets
└── assets/logo/              ← clean web-ready logo & mark SVGs (+ favicon, app icon, avatar)
```

## Principles

1. **Source of truth lives here.** Don't hard-code brand values elsewhere — import tokens.
2. **The logo is fixed artwork.** Reuse the official SVGs; never redraw the swirl.
3. **Restraint is on-brand.** Blue-led, magenta as a spark, generous whitespace.
4. **Accessible = on-brand.** Hit WCAG AA; use the approved contrast pairs.
5. **Editable by humans and agents.** Plain Markdown + open formats throughout.

---
<sub>Derived from the official <a href="../ondewo_logo_identity_guideline_2019.pdf">ONDEWO Logo & Identity Guideline (2019)</a>. ONDEWO · We automate your phone calls.</sub>
