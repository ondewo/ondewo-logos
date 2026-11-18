# ONDEWO — Accessibility & Contrast

On-brand must also mean accessible. Target **WCAG 2.1 AA** for everything public.
These pairs are pre-computed so an agent can pick a safe combination instantly.

---

## 1. The rule

- **Normal text (< 18px / < 14px bold):** contrast ratio **≥ 4.5:1**.
- **Large text (≥ 24px, or ≥ 19px bold):** **≥ 3:1**.
- **UI components & focus indicators:** **≥ 3:1** against adjacent colours.

## 2. Approved text/background pairs

| Text | Background | Ratio | Verdict |
|------|-----------|-------|---------|
| `#231F20` Ink | `#FFFFFF` White | **16.3** | ✅ AAA — default body |
| `#FFFFFF` White | `#004C87` Blue | **8.81** | ✅ AAA |
| `#004C87` Blue | `#FFFFFF` White | **8.81** | ✅ AAA — links, headings |
| `#FFFFFF` White | `#BE216B` Magenta | **5.80** | ✅ AA (AAA for large) |
| `#BE216B` Magenta | `#FFFFFF` White | **5.80** | ✅ AA — accent text/links |
| `#FFFFFF` White | `#00345C` Blue-700 | **12.8** | ✅ AAA — dark surfaces |
| `#5A5560` Neutral-500 | `#FFFFFF` White | **7.2** | ✅ AAA — muted text |
| `#A8C2D6` Blue-200 | `#001A2E` Blue-900 | **9.4** | ✅ AAA — dark-theme muted |

## 3. Forbidden pairs (do not use)

| Text | Background | Ratio | Why |
|------|-----------|-------|-----|
| `#004C87` Blue | `#BE216B` Magenta | **1.52** | ❌ Fails — never blue-on-magenta or magenta-on-blue |
| `#739DBD` Blue-300 | `#FFFFFF` White | 2.88 | ❌ Fails for text (decorative only) |
| `#CC528C` Magenta-400 | `#FFFFFF` White | 4.08 | ⚠️ Large text only — not body |
| White | `#3873A1` Blue-400 | ~5.1 | ✅ OK, but prefer Blue-500+ for safety |

> Need magenta text on white? Use **`#BE216B` (500)** or darker (`600`/`700`) — the
> `300`/`400` tints fail for normal-size text.

## 4. Beyond contrast

- **Don't rely on colour alone.** Pair magenta "error/important" with an icon or
  label. Charts need labels/patterns, not just hue, to be colour-blind safe.
- **Focus states:** visible 2px ring in magenta (`--ondewo-focus-ring`) with ≥3:1
  against the background; never remove outlines.
- **Logo legibility:** below 24px tall, switch to the mark-only SVG.
- **Alt text:** logos → `alt="ONDEWO"`; decorative swirls → `alt=""` / `aria-hidden`.
- **Motion:** honour `prefers-reduced-motion`.
- **Touch targets:** ≥ 44×44px.

## 5. Quick agent check

When generating any asset with text, verify the chosen text colour is on the
**approved list (§2)** for its background. If not, switch to ink-on-light or
white-on-blue. Recompute with the formula in
[`tokens/ondewo.tokens.json`](tokens/ondewo.tokens.json) if you introduce a new pair.
