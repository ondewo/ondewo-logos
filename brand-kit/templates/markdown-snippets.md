# ONDEWO — Markdown & README Snippets

Copy-paste blocks for GitHub READMEs, docs sites, and shields.io badges. All use
brand colours and the public logo URLs.

> Raw URLs below assume the `ai_brand_kit` branch. After merge to `master`, swap
> `ai_brand_kit` → `master` in the URLs.

## README header

```markdown
<p align="center">
  <img src="https://raw.githubusercontent.com/ondewo/ondewo-logos/ai_brand_kit/brand-kit/assets/logo/ondewo-logo-horizontal.svg" alt="ONDEWO" height="64">
</p>

<h1 align="center">Project Name</h1>
<p align="center"><em>We automate your phone calls.</em></p>
```

## Centered logo (dark-mode aware)

```markdown
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ondewo/ondewo-logos/ai_brand_kit/brand-kit/assets/logo/ondewo-logo-horizontal-mono-white.svg">
  <img src="https://raw.githubusercontent.com/ondewo/ondewo-logos/ai_brand_kit/brand-kit/assets/logo/ondewo-logo-horizontal.svg" alt="ONDEWO" height="48">
</picture>
```

## Shields.io badges (brand colours)

```markdown
![ONDEWO](https://img.shields.io/badge/ONDEWO-004C87?style=flat-square&logoColor=white)
![Status](https://img.shields.io/badge/status-live-BE216B?style=flat-square)
![Docs](https://img.shields.io/badge/docs-ondewo.com-004C87?style=flat-square)
```

- Brand blue badge colour: `004C87`
- Brand magenta accent colour: `BE216B`
- Use `style=flat-square` for a clean, geometric look that suits Futura.

## Callout / note block

```markdown
> **ONDEWO** · We automate your phone calls.
> Voice-first conversational AI — multilingual, on-premise.
```

## Footer

```markdown
---
<sub>Built by <a href="https://www.ondewo.com">ONDEWO</a> · We automate your phone calls.</sub>
```
