# ONDEWO — Colour System

Two brand colours, expanded into a working system. Always reference these by token
name (see [`tokens/`](tokens/)) rather than pasting hex values.

---

## 1. Core palette (official)

| Colour | Hex (web) | RGB | CMYK | Guideline hex | Role |
|--------|-----------|-----|------|---------------|------|
| **ONDEWO Blue** | `#004C87` | 0, 76, 135 | 100/75/15/0 | `#014C89` | Primary. Trust, depth, technology. |
| **ONDEWO Magenta** | `#BE216B` | 190, 33, 107 | 25/100/35/0 | `#BF206B` | Accent. Energy, voice, the human spark. |
| **Ink (black)** | `#231F20` | 35, 31, 32 | 0/0/0/100* | `#000000` | Body text, mono logo. |
| **White** | `#FFFFFF` | 255,255,255 | — | — | Primary background. |

> The official 2019 guideline lists `#014C89` / `#BF206B`. The vector logo files
> use `#004C87` / `#BE216B`. **For all digital/code work use `#004C87` and
> `#BE216B`** (the values baked into the artwork). Use the CMYK/Pantone values for
> professional print. The differences are imperceptible on screen.

## 2. The 60-30-10 balance

ONDEWO is **predominantly clean and blue-led**, with magenta as a deliberate spark.

- **60% neutral** — white / very light grey backgrounds, generous space.
- **30% blue** — primary structure: headers, key surfaces, primary buttons, charts.
- **10% magenta** — accents only: a key CTA, a highlight, the swirl, one stat.

Magenta is a **seasoning, not a base**. Large magenta fills are reserved for
moments that should feel energetic (a single hero band, a campaign).

## 3. Extended scales

Use tints/shades for hovers, surfaces, borders, charts, and states. Generated from
the brand colours (see [`tokens/ondewo.tokens.json`](tokens/ondewo.tokens.json)).

**Blue**
| 50 | 100 | 200 | 300 | 400 | **500** | 600 | 700 | 800 | 900 |
|----|-----|-----|-----|-----|---------|-----|-----|-----|-----|
| `#EBF1F5` | `#D6E2EC` | `#A8C2D6` | `#739DBD` | `#3873A1` | **`#004C87`** | `#004071` | `#00345C` | `#002644` | `#001A2E` |

**Magenta**
| 50 | 100 | 200 | 300 | 400 | **500** | 600 | 700 | 800 | 900 |
|----|-----|-----|-----|-----|---------|-----|-----|-----|-----|
| `#FAEDF3` | `#F5DBE7` | `#E9B4CD` | `#DB85AE` | `#CC528C` | **`#BE216B`** | `#A01C5A` | `#811649` | `#5F1036` | `#410B24` |

**Neutral**
| 0 | 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 |
|---|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| `#FFFFFF` | `#F7F8FA` | `#E5E4E6` | `#C7C5C9` | `#A4A2A8` | `#7E7A83` | `#5A5560` | `#4C4751` | `#3D3A41` | `#2D2A30` | `#231F20` |

## 4. Semantic colours

Chosen to coexist with the brand without clashing. (Info reuses brand blue.)

| State | Hex |
|-------|-----|
| Success | `#1E7A4B` |
| Warning | `#B5710A` |
| Error | `#C02626` |
| Info | `#004C87` |

## 5. Signature gradient

The swirl's energy as a gradient — use sparingly for hero bands, section dividers,
or the mark's halo. **Never** under body text.

```css
background: linear-gradient(135deg, #BE216B 0%, #004C87 100%); /* --ondewo-gradient-brand */
```

## 6. Usage rules

- **Text:** ink (`#231F20`) on white; white on blue/magenta. See [`accessibility.md`](accessibility.md).
- **Primary button:** blue fill, white text. **Hover:** `blue-700` (`#00345C`).
- **Accent / key CTA:** magenta fill, white text. Use **once** per view.
- **Links:** blue (`#004C87`), underline on hover.
- **Surfaces/cards:** white or `neutral-50` on a `neutral-100` background; 1px `neutral-100` border.
- **Charts:** lead with the blue scale; use magenta for the single most important series.
- **Never** put blue text on magenta or magenta text on blue (contrast 1.52 — fails).
- **Never** invent a new hue. Extend only along the scales above.

## 7. Backgrounds & themes

| Theme | Background | Text | Accent |
|-------|-----------|------|--------|
| **Light** (default) | `#FFFFFF` / `#F7F8FA` | `#231F20` | blue + magenta |
| **Brand** (hero) | `#004C87` or brand gradient | `#FFFFFF` | magenta `#DB85AE` for contrast |
| **Dark** | `#001A2E` / `#002644` | `#FFFFFF` | `blue-300`, `magenta-300` (lightened for contrast) |

The dark theme tokens are in [`tokens/ondewo.css`](tokens/ondewo.css) under `.ondewo-dark`.
