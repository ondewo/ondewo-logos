# ONDEWO — Logo Guidelines

The logo is the most protected brand asset. These rules are derived from the
official [2019 Logo & Identity Guideline](../ondewo_logo_identity_guideline_2019.pdf)
and extended for digital/agent use.

---

## 1. The logo system

The ONDEWO logo is a **wordmark + swirl mark**, where the two-tone swirl forms the
**"O"** of `ONDEWO`.

| Variant | File (clean, web-ready) | When to use |
|---------|-------------------------|-------------|
| **Primary — horizontal lockup** | [`assets/logo/ondewo-logo-horizontal.svg`](assets/logo/ondewo-logo-horizontal.svg) | **Default.** Almost everywhere: headers, decks, docs, footers. |
| **Mark only (symbol)** | [`assets/logo/ondewo-mark.svg`](assets/logo/ondewo-mark.svg) | App icons, avatars, favicons, watermarks, tight squares — only where "ONDEWO" appears elsewhere. |
| **Vertical / stacked** | `../ONDEWO_Logo_vertical_4c_2019/…svg` | Secondary. Narrow formats only (roll-ups, vertical banners) where the horizontal can't be prominent. |
| **Mono black** | [`assets/logo/ondewo-logo-horizontal-mono-black.svg`](assets/logo/ondewo-logo-horizontal-mono-black.svg) | 1-colour print, faxes, engraving, where colour is unavailable. |
| **Mono white** | [`assets/logo/ondewo-logo-horizontal-mono-white.svg`](assets/logo/ondewo-logo-horizontal-mono-white.svg) | On dark or photographic backgrounds. |
| **Favicon / app icon / avatar** | `assets/logo/ondewo-favicon.svg`, `ondewo-app-icon.svg`, `ondewo-avatar.svg` | Browser tabs, OS icons, social profile pictures. |

> The full original source files (`.ai`, `.eps`, `.pdf`, `.psd`, CMYK) live in the
> repo root and the `ONDEWO_Logo_*` folders — use those for professional print.
> The SVGs in `assets/logo/` are the cleaned, optimised versions for screens and
> code. See [`assets/ASSET-INDEX.md`](assets/ASSET-INDEX.md).

## 2. Colourways

- **Full colour** (magenta + blue) on **white or very light** backgrounds → default.
- **Mono white** on brand-blue, dark, or photographic backgrounds.
- **Mono black/ink** when only one colour is possible.
- Never recolour the swirl to arbitrary colours. Only the four approved forms above.

## 3. Clear space

Keep a margin of empty space around the logo equal to **X = half the height of the
"O"** (the swirl) in the logo. Nothing — text, images, edges — enters this zone.

```
   ┌──────────────────────────────┐
   │            ↕ X               │
   │   ┌──────────────────────┐   │
 X │   │   ⊙ N D E W O        │ X │   X = ½ the height of the "O"
   │   └──────────────────────┘   │
   │            ↕ X               │
   └──────────────────────────────┘
```

When in doubt, **more space is always safer**. For digital, a quick rule: pad by
at least the cap-height of the wordmark on every side.

## 4. Minimum size

| Variant | Print min | Digital min |
|---------|-----------|-------------|
| Horizontal lockup | **5 mm** tall | **24 px** tall (≈120 px wide) |
| Vertical / stacked | **10 mm** tall | **40 px** tall |
| Mark only | — | **16 px** (favicon) |

Below these sizes the swirl detail collapses — use the mark-only version instead.

## 5. Placement

- Preferred anchor: **top-left** (Western reading order) or centred for hero/splash.
- Maintain clear space from the canvas edge (≥ X, ideally ≥ 2X).
- Sit the logo on a calm area of any background — never on busy texture or where the
  swirl's magenta/blue clash with the background hue.

## 6. Misuse — never do these

| ❌ Don't | Why |
|---------|-----|
| Stretch, squash, or rotate | Distorts the geometry |
| Recolour the swirl or wordmark | Off-brand; breaks recognition |
| Add shadows, glows, bevels, outlines | The mark is flat by design |
| Place full-colour logo on a busy/low-contrast photo | Illegible — use mono white |
| Re-typeset "ONDEWO" in another font | The wordmark is fixed artwork |
| Put magenta logo on blue (or vice-versa) | Contrast 1.5 — fails legibility |
| Crop the swirl or rebuild it from scratch | Use the official SVG paths |
| Box the logo in a coloured pill it wasn't designed for | Reduces clear space |
| Use the old/low-res raster when an SVG exists | Pixelation |

## 7. Logo in code — copy-paste snippets

**HTML (inline SVG, scales crisply):**
```html
<img src="brand-kit/assets/logo/ondewo-logo-horizontal.svg" alt="ONDEWO" height="32">
```

**On a dark/blue background:**
```html
<div style="background:#004C87; padding:24px">
  <img src="brand-kit/assets/logo/ondewo-logo-horizontal-mono-white.svg" alt="ONDEWO" height="32">
</div>
```

**Favicon:**
```html
<link rel="icon" type="image/svg+xml" href="brand-kit/assets/logo/ondewo-favicon.svg">
```

**Markdown / README badge:**
```markdown
![ONDEWO](brand-kit/assets/logo/ondewo-logo-horizontal.svg)
```

## 8. The mark, as raw geometry (for generative use)

If an agent must embed the swirl directly (e.g. compose a new graphic), reuse the
**exact path data** from `assets/logo/ondewo-mark.svg` — two paths:
`fill="#BE216B"` (magenta, front sweep) and `fill="#004C87"` (blue, back sweep),
in `viewBox="30 30 157 123"`. **Do not redraw the swirl by hand** — it will never
match.
