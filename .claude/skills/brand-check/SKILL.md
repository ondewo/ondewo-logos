---
name: brand-check
description: Audit an existing design, web page, screenshot, slide, or copy against the ONDEWO brand guidelines and report violations with fixes. Use when the user asks to review/check/audit something for brand compliance, "is this on-brand?", or wants a brand QA pass before publishing.
---

# ONDEWO brand check

Review the target artefact against the ONDEWO brand system and return a structured,
actionable report. Be specific and cite the rule.

## Inputs you may get
A file path (SVG/HTML/CSS/PNG/PDF/MD), a URL, a screenshot/image, or pasted copy.

## Load the rules
Read `brand-kit/color-system.md`, `typography.md`, `logo-guidelines.md`,
`accessibility.md`, `voice-and-tone.md`, and `tokens/ondewo.tokens.json`.

## Check each dimension

1. **Colour**
   - Are all colours from the token palette? Flag any off-palette hex.
   - Is magenta an accent (≤ ~10%), not a dominant fill?
   - Any forbidden pairs (blue-on-magenta / magenta-on-blue)?
2. **Logo**
   - Correct variant for the background (mono white on dark)?
   - Clear space respected? Not stretched, recoloured, shadowed, or below min size?
   - Using the official SVG (not a traced/low-res copy)?
3. **Typography**
   - Futura/Jost stack (not Arial/Times/random)? Sentence-case headlines?
   - All-caps labels letter-spaced? Body ≥ 16px?
4. **Layout & spacing**
   - 4px-grid spacing, generous whitespace, single focal point + one primary CTA?
5. **Accessibility**
   - Compute contrast for every text/bg pair; flag anything < 4.5:1 (or < 3:1 large).
   - Colour not the only signal; visible focus states; alt text on logos.
6. **Voice & tone** (if copy present)
   - Clear over clever, confident not boastful, active voice, sentence case,
     `ONDEWO` all-caps, approved vocabulary, no banned words (§5 of voice-and-tone).

## How to inspect
- For SVG/HTML/CSS: read the source; grep for hex colours
  (`grep -oiE '#[0-9a-f]{6}'`) and font-families and compare to tokens.
- For images/screenshots: view the image and assess visually; sample colours if needed.
- Compute contrast ratios with the WCAG formula (see accessibility.md / tokens).

## Output format
A markdown report:

```
## Brand check: <target>
**Verdict:** ✅ On-brand / ⚠️ Minor issues / ❌ Off-brand

### Issues
| Severity | Dimension | Problem | Rule | Fix |
|----------|-----------|---------|------|-----|
| High | Colour | #FF0000 used for error | not in palette | use #C02626 (semantic.error) |
...

### What's good
- ...

### Suggested patch
<concrete edits, or a diff if you can edit the file>
```

Offer to apply the fixes if the artefact is an editable file in the repo.
