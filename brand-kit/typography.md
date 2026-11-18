# ONDEWO — Typography

The brand typeface is **Futura** — a geometric sans-serif designed by Paul Renner
(1927), built on circles and clean geometry. It mirrors the geometry of the swirl
mark. This page makes Futura usable everywhere, including where the licensed font
isn't available.

---

## 1. The typefaces

| Tier | Font | Notes |
|------|------|-------|
| **Brand (licensed)** | **Futura PT** / **Futura LT Pro** | Use when the license is installed (print, official decks, Adobe/Figma). |
| **Web fallback (free)** | **[Jost\*](https://fonts.google.com/specimen/Jost)** | Google Font; a faithful geometric Futura alternative. **Default for the web** when Futura PT isn't licensed for the medium. |
| **Ubiquitous fallback** | Century Gothic, Trebuchet MS, system-ui | Always available on the OS. |
| **Monospace** (code, data) | JetBrains Mono → Consolas → monospace | Docs, code blocks, technical figures. |

**Canonical font stack** (already in the tokens):
```css
font-family: "Futura PT", "Futura LT Pro", Futura, "Jost", "Century Gothic", "Trebuchet MS", system-ui, sans-serif;
```

> **Licensing:** Futura PT/LT Pro are commercial fonts (Adobe Fonts / Linotype).
> Do **not** embed them in public web pages or ship the files unless ONDEWO holds a
> web license. For public sites, email, and open-source repos, use **Jost** (open
> SIL license) via Google Fonts. Decks/PDFs rendered to outlines are fine.

**Load Jost on the web:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;700&display=swap" rel="stylesheet">
```

## 2. Type scale (1.25 — major third)

| Token | Size | rem | Typical use |
|-------|------|-----|-------------|
| `5xl` | 61 px | 3.8125 | Hero headline |
| `4xl` | 49 px | 3.0625 | Page H1 |
| `3xl` | 39 px | 2.4375 | Section H2 |
| `2xl` | 31 px | 1.9375 | H3 / large stat |
| `xl`  | 25 px | 1.5625 | H4 / lead paragraph |
| `lg`  | 20 px | 1.25  | Sub-head, large body |
| `base`| 16 px | 1.0   | Body (minimum for paragraphs) |
| `sm`  | 14 px | 0.875 | Captions, labels |
| `xs`  | 12 px | 0.75  | Legal, fine print |

## 3. Weights & styles

- **300 Light** — large display headlines (airy, elegant).
- **400 Regular** — body text.
- **500 Medium** — sub-heads, emphasis, buttons.
- **700 Bold** — the wordmark, strong headlines, key numbers.
- Avoid faux-italics; Futura's character is upright and geometric. Italics sparingly.

## 4. Line height & spacing

| Context | line-height | letter-spacing |
|---------|-------------|----------------|
| Display / hero | 1.1 (`tight`) | −0.01em |
| Headings | 1.25 (`snug`) | normal |
| Body | 1.5 (`normal`) | normal |
| Long-form reading | 1.7 (`relaxed`) | normal |
| **All-caps labels / wordmark-style** | 1.2 | **+0.12em (`wider`)** |

> Futura is geometric and wide; **all-caps text needs extra letter-spacing**
> (`0.12em`) to breathe — this echoes the spacing in the ONDEWO wordmark.

## 5. Rules

- **Headlines:** Futura/Jost, Light or Bold, sentence case (not Title Case).
- **Body:** Regular, ≥16px, max line length ~70 characters.
- **Brand name in headlines:** `ONDEWO` all-caps with `+0.12em` tracking.
- **Don't** mix in a second display typeface. One geometric sans does all the work.
- **Don't** set long body paragraphs in all-caps or in Light below 20px (hard to read).
- **Numbers/stats:** Bold, often in blue or magenta, paired with a small label.

## 6. CSS starter

```css
@import url("brand-kit/tokens/ondewo.css");

body  { font-family: var(--ondewo-font-body); font-size: var(--ondewo-text-base);
        line-height: var(--ondewo-leading-normal); color: var(--ondewo-text); }
h1    { font-family: var(--ondewo-font-display); font-weight: 700;
        font-size: var(--ondewo-text-4xl); line-height: var(--ondewo-leading-tight);
        letter-spacing: var(--ondewo-tracking-tight); }
h2    { font-family: var(--ondewo-font-display); font-weight: 700; font-size: var(--ondewo-text-3xl); }
.eyebrow, .label-caps {
        text-transform: uppercase; letter-spacing: var(--ondewo-tracking-wider);
        font-weight: 500; font-size: var(--ondewo-text-sm); color: var(--ondewo-magenta); }
```
