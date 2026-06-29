# ONDEWO — Layout, Spacing, Imagery & Icons

The connective tissue that makes assets feel like one family: grids, spacing,
imagery direction, iconography, motion.

---

## 1. Spacing scale (4 px base)

All spacing is a multiple of **4 px**. Use the `--ondewo-space-*` tokens.

| Token | px | Use |
|-------|----|-----|
| 1 | 4 | Icon ↔ label gap |
| 2 | 8 | Tight inner padding |
| 3 | 12 | Compact controls |
| 4 | 16 | Default element gap, card padding |
| 5 | 24 | Between related groups |
| 6 | 32 | Between components |
| 7 | 48 | Section padding (mobile) |
| 8 | 64 | Section padding (desktop) |
| 9 | 96 | Major section breaks |
| 10 | 128 | Hero whitespace |

**Whitespace is part of the brand.** ONDEWO leans clean and uncluttered — when in
doubt, add space, not decoration.

## 2. Grid

- **Web:** 12-column fluid grid, max content width **1200–1280 px**, 24px gutters,
  centred. Breakpoints: 640 / 768 / 1024 / 1280.
- **Slides (16:9):** 12-col grid on a 1920×1080 frame, 96px outer margin, 48px gutter.
- **Print A4:** 12–18mm margins; align everything to a baseline grid.
- **Social:** safe area = keep text/logo within the central 80%; never let the
  logo touch an edge (respect clear space, §logo-guidelines).

## 3. Corner radius & elevation

- Radii: `sm 4px` (inputs), `md 8px` (cards/buttons), `lg 16px` (modals/large cards),
  `pill` (chips, tag buttons, primary CTAs can be pill or md — pick one per product).
- Shadows are **soft and blue-tinted** (`rgba(0,38,68,…)`), never harsh black.
  Prefer 1px borders (`neutral-100`) over heavy shadows for a clean, engineered feel.

## 4. Imagery & photography direction

| Do | Avoid |
|----|-------|
| Real people in real work settings (contact centres, offices) | Cheesy stock "headset smiling at camera" |
| Clean tech/abstract: soundwaves, network flows, geometric loops echoing the swirl | Literal robots, generic "AI brain" clip-art |
| Bright, airy, blue-leaning grade; pops of magenta | Dark, noisy, cluttered scenes |
| Diverse, European, professional | Dated, overly corporate stock |
| Duotone treatment in brand blue + magenta for unifying mixed photos | Random Instagram filters |

**Duotone recipe (for unifying stock photos):** map shadows → `#001A2E`,
highlights → `#FAEDF3`, or a blue→magenta duotone for hero imagery.

## 5. Iconography

- **Style:** line icons, **2px stroke**, rounded joints, geometric — consistent with
  Futura's circles. Recommended sets: **Lucide**, **Phosphor** (regular), or
  **Feather**. Pick one set per product and stick to it.
- **Colour:** ink or blue by default; magenta only to highlight one key icon.
- **Size:** 16/20/24/32 on the 4px grid. Keep optical weight even across a set.
- Don't mix filled and outline styles in the same view.

## 6. Shapes & graphic language

The swirl gives ONDEWO a vocabulary of **arcs, loops, and flowing curves**.

- Use **circular/arc motifs**, soundwave lines, and the swirl as a watermark
  (low-opacity, off-canvas bleed) to add brand texture.
- Section dividers can use a single sweeping curve or the brand gradient as a thin band.
- Keep it restrained — one brand motif per layout, not many.

## 7. Motion (for web / video / UI) `‹confirm›`

- **Character:** smooth, confident, never bouncy. Easing `cubic-bezier(0.22, 1, 0.36, 1)`.
- **Duration:** 150–250ms for UI; 400–800ms for hero/storytelling.
- **Signature move:** the swirl can rotate/draw-in on load (a single 360° sweep),
  echoing "the loop that never drops a call". Use once, not everywhere.
- Respect `prefers-reduced-motion` — disable non-essential animation.

## 8. Layout checklist (before shipping any asset)

- [ ] Logo has full clear space and is the right variant for the background.
- [ ] Only brand colours/tokens used; magenta ≤ ~10% of the surface.
- [ ] Type uses the Futura/Jost stack and the type scale.
- [ ] Spacing is on the 4px grid; generous whitespace.
- [ ] Text contrast passes AA ([`accessibility.md`](accessibility.md)).
- [ ] One clear focal point and one primary CTA.
