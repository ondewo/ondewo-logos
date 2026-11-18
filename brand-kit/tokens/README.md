# ONDEWO Design Tokens

Machine-readable design tokens for ONDEWO. Use these instead of hard-coding hex
values, font names, or pixel sizes — they keep every asset on-brand and let the
whole system change from one place.

## Files

| File | Format | Use it when… |
|------|--------|--------------|
| `ondewo.tokens.json` | [W3C Design Tokens](https://design-tokens.github.io/community-group/format/) | You are the **canonical source**. Transform it with Style Dictionary / your own script. |
| `ondewo.css`         | CSS custom properties (`--ondewo-*`) | Building any website, web app, email, or HTML template. |
| `ondewo.scss`        | SCSS variables + maps | Working in a Sass codebase. |
| `tailwind.preset.js` | Tailwind preset | The project uses Tailwind CSS. |

All four are generated from `ondewo.tokens.json`. **If you change a value, change
it there first**, then regenerate or mirror it into the others.

## Quick reference

| Token | Value | Notes |
|-------|-------|-------|
| `--ondewo-blue` / `$blue` | `#004C87` | Primary brand colour |
| `--ondewo-magenta` / `$magenta` | `#BE216B` | Accent / secondary |
| `--ondewo-ink` | `#231F20` | Body text, 1-colour logo |
| `--ondewo-gradient-brand` | magenta → blue 135° | Signature gradient |
| `--ondewo-font-display` | Futura PT → Jost fallback | Headlines, wordmark |

## Consuming the tokens

**Plain HTML/CSS**
```html
<link rel="stylesheet" href="brand-kit/tokens/ondewo.css">
<h1 style="font-family: var(--ondewo-font-display); color: var(--ondewo-blue)">Hello</h1>
```

**Tailwind**
```js
// tailwind.config.js
module.exports = { presets: [require("./brand-kit/tokens/tailwind.preset.js")] };
```
```html
<button class="bg-ondewo-blue hover:bg-blue-700 text-white font-display rounded-pill">Talk to us</button>
```

**Style Dictionary (any platform: iOS, Android, JSON, etc.)**
```bash
npx style-dictionary build --source brand-kit/tokens/ondewo.tokens.json
```

## Rules

- Never introduce a colour that is not in this file. Need a new shade? Pick the
  nearest scale step (`blue-400`, `magenta-600`, …).
- Body text uses `--ondewo-text` on `--ondewo-bg`; never magenta-on-blue (contrast 1.5 — fails WCAG).
- See [`../accessibility.md`](../accessibility.md) for the approved contrast pairs.
