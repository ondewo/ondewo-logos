# CLAUDE.md — ONDEWO Brand Kit

This repository is the **ONDEWO brand & design system**. It exists so that any
human — or any AI coding agent — can produce **on-brand ONDEWO design and marketing
material** quickly and correctly, just by pointing at this repo.

**If you are an AI agent and the user asks you to design, generate, or review any
ONDEWO-branded material, this file is your entry point.** Read it, then load the
specific guideline(s) you need from `brand-kit/`.

---

## TL;DR brand facts

| | |
|---|---|
| **Brand** | ONDEWO (always all-caps) |
| **Tagline** | *We automate your phone calls.* |
| **What it is** | Voice-first conversational AI that automates phone calls — multilingual, on-premise. |
| **Blue (primary)** | `#004C87` |
| **Magenta (accent)** | `#BE216B` |
| **Ink (text)** | `#231F20` |
| **Typeface** | Futura PT / Futura LT Pro → free web fallback **Jost** |
| **Logo** | Two-tone swirl forming the "O" in `ONDEWO`. Use the SVGs in `brand-kit/assets/logo/`. |
| **Colour balance** | 60% neutral · 30% blue · **10% magenta accent** |

## How to use this repo (agent playbook)

1. **Read the brand context.** Start at [`brand-kit/README.md`](brand-kit/README.md),
   then the relevant spec (colour, type, logo, layout, voice, accessibility).
2. **Use the tokens, never raw values.** [`brand-kit/tokens/`](brand-kit/tokens/)
   has the palette/type/spacing as JSON, CSS, SCSS and a Tailwind preset.
3. **Start from a template.** [`brand-kit/templates/`](brand-kit/templates/) has
   ready-to-edit social posts, banners, slides, a web hero, components, business
   card, email signature, and letterhead.
4. **Embed the real logo.** Copy the official SVG paths from
   [`brand-kit/assets/logo/`](brand-kit/assets/logo/) — **never redraw the swirl**.
5. **Verify, then deliver.** Run the checklist in
   [`brand-kit/layout-and-spacing.md`](brand-kit/layout-and-spacing.md#8-layout-checklist-before-shipping-any-asset),
   render the asset to confirm it looks right, save it to `brand-kit/generated/`.

## Skills & workflows (if running in Claude Code)

- **Skills** — [`.claude/skills/`](.claude/skills/): `create-brand-asset` (make an
  asset), `brand-check` (audit for compliance), `brand-copy` (write in-voice copy).
  They activate automatically from the user's request.
- **Workflows** — [`.claude/workflows/`](.claude/workflows/): `campaign-kit`
  (generate a full campaign from one message) and `brand-audit` (sweep many assets).
  Run only on explicit user opt-in.

If the skills aren't installed (you're a different agent/tool), the process above
still works — `brand-kit/` is plain Markdown + open formats designed to be read directly.

## Repository map

```
ondewo-logos/
├── CLAUDE.md                     ← you are here (agent entry point)
├── README.md                     ← human landing page
├── brand-kit/
│   ├── README.md                 ← brand kit index + quick start
│   ├── brand-foundation.md       ← mission, positioning, audience, personality
│   ├── voice-and-tone.md         ← how ONDEWO writes
│   ├── logo-guidelines.md        ← logo variants, clear space, misuse
│   ├── color-system.md           ← palette, scales, gradient, usage
│   ├── typography.md             ← Futura/Jost type system & scale
│   ├── layout-and-spacing.md     ← grid, spacing, imagery, icons, motion
│   ├── accessibility.md          ← WCAG contrast pairs (pre-computed)
│   ├── tokens/                   ← design tokens: JSON · CSS · SCSS · Tailwind
│   ├── templates/                ← editable SVG/HTML asset starters
│   └── assets/                   ← clean web-ready logo SVGs + ASSET-INDEX.md
├── .claude/
│   ├── skills/                   ← create-brand-asset · brand-check · brand-copy
│   └── workflows/                ← campaign-kit.js · brand-audit.js
├── ONDEWO_Logo_*/                ← official source logos (.ai .eps .pdf .svg .psd)
└── ondewo_logo_identity_guideline_2019.pdf  ← original guideline (source of truth)
```

## Hard rules (do not break)

1. Only brand colours/tokens — no off-palette hex, no new typefaces.
2. Never stretch, recolour, shadow, or redraw the logo; respect clear space and min size.
3. Magenta is an **accent (≤ ~10%)**, never the dominant fill.
4. Never place blue text on magenta or magenta on blue (contrast fails). Use the
   approved pairs in `accessibility.md`.
5. On public web, use **Jost** (open license), not commercial Futura font files.
6. `ONDEWO` is always all-caps in prose. Headlines and CTAs are sentence case.
7. Items marked **`‹confirm›`** in `brand-foundation.md` are inferred — flag them,
   don't present them as confirmed fact.
8. Save generated output to `brand-kit/generated/`; never overwrite `templates/`,
   `assets/`, or the official source files.

## Provenance
All values trace to the official
[`ondewo_logo_identity_guideline_2019.pdf`](ondewo_logo_identity_guideline_2019.pdf)
and the colours embedded in the official vector logo files. Where the guideline and
the artwork differ slightly (`#014C89` vs `#004C87`), the **artwork values are
canonical for digital**; CMYK/Pantone from the guideline are for print.
