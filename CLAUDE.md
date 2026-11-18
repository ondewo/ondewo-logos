# CLAUDE.md — ONDEWO Brand Kit

This repository is the **ONDEWO brand & design system**. Any human or AI coding
agent can produce **on-brand ONDEWO design, copy and documents** by pointing at it.

**If the user asks you to design, write, generate or review ONDEWO-branded material,
start here.** Then load only the guideline files you need (see the router below).

---

## 1. Brand facts (memorise these)

| | |
|---|---|
| **Brand** | `ONDEWO` — always all-caps in prose (lowercase only in code, URLs, package names) |
| **Tagline** | *We automate your phone calls.* (use verbatim) |
| **What it is** | Voice-first conversational AI that automates phone calls — multilingual, deployable on-premise |
| **Blue** (primary) | `#004C87` · RGB 0/76/135 · CMYK 100/75/15/0 |
| **Magenta** (accent) | `#BE216B` · RGB 190/33/107 · CMYK 25/100/35/0 |
| **Ink** (text) | `#231F20` |
| **Typeface** | Futura PT / Futura LT Pro (licensed) → web fallback **Jost** |
| **Logo** | Two-tone swirl forming the "O" of `ONDEWO`. Official SVGs only: `brand-kit/assets/logo/` |
| **Balance** | 60% neutral · 30% blue · ≤10% magenta |
| **Personality** | Precise, calm, expert engineer — clear, confident, human; never hype |

Digital work uses the **artwork** hex values above. The 2019 print guideline lists
`#014C89` / `#BF206B`; use those (and CMYK/Pantone) only for professional print.

## 2. Router — what to read and which skill to use

| The user wants… | Skill (`.claude/skills/`) | Read first |
|---|---|---|
| Any visual asset (social post, banner, slide, web hero, business card, signature, letterhead, favicon, ad) | `create-brand-asset` | `logo-guidelines`, `color-system`, `layout-and-spacing`, `templates/` |
| Audit / "is this on-brand?" | `brand-check` | `accessibility`, `layout-and-spacing` §8 checklist |
| Headlines, taglines, ads, emails, UI text | `brand-copy` | `voice-and-tone` |
| Slide deck (pitch, sales, company, webinar) | `slide-deck` | `templates/slide-title.svg`, `typography` |
| One-pager, datasheet, brochure | `one-pager` | `document-templates/PLAN.md` |
| Case study, testimonial | `case-study` | `voice-and-tone` |
| Blog post, SEO/how-to article | `blog-article` | `voice-and-tone` |
| Email / drip / newsletter | `marketing-email` | `voice-and-tone`, `accessibility` |
| Social campaign across platforms | `social-media-kit` | `templates/social-*.svg` |
| Whitepaper, eBook | `whitepaper` | `document-templates/PLAN.md` |
| Infographic | `infographic` | `color-system`, `typography` |
| Explainer video script / storyboard | `explainer-video` | `voice-and-tone` |
| Press release / media kit | `press-kit` | `brand-foundation` |
| Full webinar package | `webinar-kit` | composes the skills above |
| Whole campaign from one message, or sweep many assets | workflows `campaign-kit`, `brand-audit` (`.claude/workflows/`) | run **only on explicit opt-in** |

All guideline files live in `brand-kit/`: `brand-foundation.md`, `voice-and-tone.md`,
`logo-guidelines.md`, `color-system.md`, `typography.md`, `layout-and-spacing.md`,
`accessibility.md`. Start at `brand-kit/README.md` if unsure.

If skills are not installed (different agent/tool), the same process works —
`brand-kit/` is plain Markdown plus open formats, readable directly.

## 3. Agent playbook

1. **Route** the request with the table above; read only the relevant guidelines.
2. **Use tokens, not raw values.** `brand-kit/tokens/` holds the palette, type and
   spacing as JSON (`ondewo.tokens.json` is canonical), CSS, SCSS and a Tailwind preset.
3. **Start from a template** in `brand-kit/templates/` rather than a blank canvas.
4. **Embed the real logo** by copying the official SVG — never redraw the swirl.
5. **Verify, then deliver:** run the checklist in
   `brand-kit/layout-and-spacing.md` §8, render the result and look at it, then save it
   to `brand-kit/generated/` (naming: `ondewo-<type>-<variant>-<theme>[-<WxH>].<ext>`).
6. **Summarise** what you made, which tokens/templates you used, and any `‹confirm›`
   items or assumptions the user should check.

## 4. Logo selector

| Situation | File in `brand-kit/assets/logo/` |
|---|---|
| Default (white / light background) | `ondewo-logo-horizontal.svg` |
| Blue, dark or photo background | `ondewo-logo-horizontal-mono-white.svg` |
| One-colour print | `ondewo-logo-horizontal-mono-black.svg` |
| Square slot, app icon, avatar, favicon | `ondewo-mark.svg`, `ondewo-app-icon.svg`, `ondewo-avatar.svg`, `ondewo-favicon.svg` |
| Narrow format (roll-up) — secondary only | `ONDEWO_Logo_vertical_4c_2019/…svg` |

Clear space **X = half the height of the "O"** on every side. Minimum height:
horizontal 5 mm / 24 px · vertical 10 mm / 40 px · mark 16 px.

## 5. Contrast cheat-sheet (WCAG AA, computed)

| ✅ Safe | Ratio | | ❌ Never | Ratio |
|---|---|---|---|---|
| Ink on white | 16.3 | | Blue on magenta (or reverse) | 1.52 |
| White on blue | 8.81 | | Blue-300 `#739DBD` text on white | 2.88 |
| White on magenta | 5.80 | | Magenta-400 `#CC528C` body text on white | 4.08 |
| White on blue-700 | 12.8 | | | |

Full list: `brand-kit/accessibility.md`. For a new pair, compute it — don't guess.

## 6. Copy cheat-sheet

- Active voice, present tense, "we" → "you". Short sentences; lead with the benefit.
- **Sentence case** for headlines and buttons ("Talk to sales"); no period on buttons.
- Oxford comma. Numerals for stats. One spelling (British *or* US) per asset.
- Avoid: revolutionary, disruptive, magic, ninja, world-class (without proof), cutting-edge, filler "AI-powered".
- Draft **3 options**, ship the shortest that keeps the benefit.
- Don't invent customers, quotes, statistics or product claims — use clearly marked placeholders (`‹N›`).

## 7. Hard rules (do not break)

1. Brand colours and tokens only — no off-palette hex, no new typefaces.
2. Never stretch, recolour, shadow, outline, crop or redraw the logo; respect clear space and minimum size.
3. Magenta is an **accent (≤ ~10%)**, never the dominant fill; use it for one key CTA per view.
4. Never blue-on-magenta or magenta-on-blue text; use approved pairs from `accessibility.md`.
5. Public web, email and open-source: use **Jost** (open licence), never ship Futura font files.
6. `ONDEWO` is all-caps in prose; headlines and CTAs are sentence case.
7. Items tagged **`‹confirm›`** (mostly `brand-foundation.md`, `voice-and-tone.md`) are inferred — flag them, never present as confirmed fact. Pantone values are still unconfirmed.
8. Write output to `brand-kit/generated/`. **Never overwrite or edit** `templates/`, `assets/`, `tokens/` outputs, the `ONDEWO_Logo_*` source folders, or `ondewo_logo_identity_guideline_2019.pdf` unless the user explicitly asks.
9. Alt text: logo → `alt="ONDEWO"`; decorative swirl → empty alt / `aria-hidden`.

## 8. Commands

```bash
# Regenerate the logo & identity guideline PDF (needs Chrome/Chromium; fetches Jost once)
python3 scripts/build_guideline.py                 # → brand-kit/generated/ondewo_logo_identity_guideline.pdf
python3 scripts/build_guideline.py --html-only     # inspect the HTML
python3 scripts/build_guideline.py -o path.pdf     # custom output
make social                                       # brand-kit/social/<platform>/ (linkedin, facebook, instagram, tiktok, bitbucket, jira, confluence, roblox)
make guideline-2026                               # social kits + ondewo_logo_identity_guideline_2026.pdf
```

The guideline PDF is built from `brand-kit/tokens/ondewo.tokens.json` and the logo
SVGs, and contrast ratios are computed. **When you change tokens, logos or guideline
content, rerun the script** and check the pages visually (e.g. `pdftoppm -r 70 -png`).
`scripts/.cache/` (downloaded fonts) is git-ignored.

## 9. Repository map

```
ondewo-logos/
├── CLAUDE.md                     ← agent entry point (this file)
├── README.md · CONTRIBUTING.md · RELEASE.md
├── scripts/
│   ├── build_guideline.py        ← generates the identity-guideline PDF from tokens + SVGs
│   ├── build_social.py           ← generates brand-kit/social/<platform>/ (md + svg + png)
│   └── social_data.py            ← platform specs, profile copy, guidelines (edit here)
├── brand-kit/
│   ├── README.md                 ← kit index + quick start
│   ├── brand-foundation.md · voice-and-tone.md · logo-guidelines.md
│   ├── color-system.md · typography.md · layout-and-spacing.md · accessibility.md
│   ├── tokens/                   ← JSON (canonical) · CSS · SCSS · Tailwind preset
│   ├── templates/                ← editable SVG/HTML starters (social, slide, hero, card, signature, letterhead)
│   ├── document-templates/       ← PLAN.md: branded Office/Google/PDF document system
│   ├── assets/                   ← web-ready logo SVGs + ASSET-INDEX.md
│   └── generated/                ← OUTPUT folder (incl. the guideline PDF)
├── .claude/
│   ├── skills/                   ← create-brand-asset · brand-check · brand-copy + 11 marketing skills
│   └── workflows/                ← campaign-kit.js · brand-audit.js
├── ONDEWO_Logo_*/                ← official print/source logos (.ai .eps .pdf .svg .psd): horizontal 1c/4c, vertical 1c/4c, Sonderformen
├── github/ · ondewo_*.png        ← social/profile images
└── ondewo_logo_identity_guideline_2019.pdf   ← original InDesign guideline (source of truth)
```

## 10. Provenance

All values trace to the official
[`ondewo_logo_identity_guideline_2019.pdf`](ondewo_logo_identity_guideline_2019.pdf)
and the colours embedded in the official vector logo files. Where they differ
(`#014C89` vs `#004C87`), the **artwork values are canonical for digital**;
CMYK/Pantone from the guideline are for print.
