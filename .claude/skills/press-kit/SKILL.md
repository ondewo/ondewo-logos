---
name: press-kit
description: Assemble an ONDEWO press kit / media kit for media relations — an AP-style press release, company fact sheet, executive bios, product summaries, a logo/brand-asset index, the "About ONDEWO" boilerplate, and a media-contact block. Use when the user asks to create/write/build/draft a press release, news or launch announcement, embargo/media alert, newsroom kit, media kit, press kit, PR, "About ONDEWO" boilerplate, fact sheet, exec/leadership bio, or anything aimed at journalists / media relations. Produces a Markdown press-kit index plus the release exported to PDF/DOCX, using the official logo, design tokens (#004C87 blue, #BE216B magenta), and Futura/Jost type.
---

# Assemble an ONDEWO press kit

You are producing a finished, on-brand ONDEWO **press kit**: a Markdown index that
points to a set of media-ready documents, plus an AP-style press release exported to
PDF/DOCX. Follow this process exactly — it guarantees brand and editorial
consistency without the user re-explaining ONDEWO.

**Compose, don't duplicate.** This skill owns *editorial* deliverables (the release
and the kit documents). It does **not** re-implement design logic. For any *designed
visual* that ships with the kit — a launch social card, a newsroom hero banner, a
quote graphic, an embargoed-announcement image — invoke the **`create-brand-asset`**
skill and link its output into the index. For standalone copy in ONDEWO's voice use
**`brand-copy`**; to audit a finished asset use **`brand-check`**. All of these load
the same `brand-kit/` source of truth described below, so the brand stays identical
across the kit.

## 0. Load the brand context (always do this first)

Read, in order:
1. `brand-kit/README.md` — kit map.
2. `brand-kit/voice-and-tone.md` — **the boilerplate, one-liner, tagline, banned
   words, grammar, and tone-by-context table live here (§5 banned words, §6
   tagline/boilerplate).** All press copy is governed by this file.
3. `brand-kit/brand-foundation.md` — positioning (§2), audience (§4), the product
   portfolio (§1: CAI · S2T · T2S · VTSI · AIM), messaging pillars (§7), proof points
   (§8). Many items here are tagged `‹confirm›` — preserve those tags (see Guardrails).
4. `brand-kit/logo-guidelines.md` + `brand-kit/assets/ASSET-INDEX.md` — which logo
   files to list in the asset index and how journalists should use them.
5. `brand-kit/color-system.md`, `brand-kit/typography.md`,
   `brand-kit/layout-and-spacing.md`, `brand-kit/accessibility.md` — for the
   PDF/DOCX styling of the release.
6. `brand-kit/tokens/ondewo.tokens.json` — exact colour/type/spacing values. Reference
   tokens by name (or via `brand-kit/tokens/ondewo.css`); never paste raw hex.
7. **`brand-kit/document-templates/PLAN.md`** — the document-template plan that names
   the **output engine** for paginated docs (PDF/DOCX) and the page specs. Read it and
   use the engine it specifies. If that file or its named engine isn't present yet,
   fall back to the engines listed in **§3 Build**.
8. `brand-kit/templates/letterhead.html` — the A4 letter/one-pager base the release is
   built on (it already imports `../tokens/ondewo.css`, loads Jost, and draws the
   blue/magenta top bar, logo header, and footer).

Never invent colours, fonts, facts, or redraw the logo — reuse the tokens, the
official SVG paths in `brand-kit/assets/logo/`, and the exact boilerplate/tagline from
`voice-and-tone.md`.

## 1. Intake (ask/infer — keep it lean)

Infer what you can from the brief; only ask for what's genuinely missing. You need:

- **The news** — the one thing being announced (launch, funding, partnership, hire,
  milestone, event), in one sentence.
- **Release timing** — `FOR IMMEDIATE RELEASE` (default) or an **embargo** date/time.
- **Dateline** — city + country + date (default `VIENNA, Austria — <today>`; ONDEWO's
  HQ is `‹confirm›`).
- **Quote source** — which executive is quoted (name + title) `‹confirm›`.
- **Media contact** — name, title, email, phone, ondewo.com `‹confirm›`.
- **Scope** — full kit (index + all docs) or just the release. Default: full kit.
- **Output format** — PDF (default) and/or DOCX for the release; the index and the
  supporting docs are always Markdown.

If real facts (numbers, names, dates, quotes) weren't supplied, draft the document
with `‹confirm›` placeholders rather than inventing them. Draft any missing copy per
`voice-and-tone.md` and offer it.

## 2. Canonical structure (the press kit)

A press kit is a **folder** with an index that links to each document.

```
brand-kit/generated/press-kit-<slug>/
├── README.md                                       ← the press-kit INDEX (Markdown, entry point)
├── ondewo-press-release-<slug>-<YYYY-MM-DD>.md     ← release source
├── ondewo-press-release-<slug>-<YYYY-MM-DD>.pdf    ← exported release
├── ondewo-press-release-<slug>-<YYYY-MM-DD>.docx   ← (if requested)
├── fact-sheet.md
├── executive-bios.md
├── product-summaries.md
├── media-contact.md
└── assets/                                         ← (optional) visuals from create-brand-asset
```

### 2a. Press-kit index (`README.md`)
The top-level entry point a journalist opens first.
1. ONDEWO logo (embed `assets/logo/ondewo-logo-horizontal.svg`) + tagline
   *We automate your phone calls.*
2. One-line "what's in this kit" + the headline news.
3. **Contents table** — link to each document below with a one-line description.
4. **Boilerplate** — the ≈50-word "About ONDEWO", verbatim from `voice-and-tone.md` §6.
5. **Brand-asset / logo index** — a table linking to the `brand-kit/assets/logo/`
   files (horizontal lockup, mark, mono white/black, favicon) plus any kit visuals
   produced via `create-brand-asset`, each with a one-line usage note and a pointer to
   `logo-guidelines.md` (clear space; don't recolour/stretch/redraw).
6. **Media contact** block.
7. Last-updated date.

### 2b. Press release (AP style) — exact skeleton
```
FOR IMMEDIATE RELEASE
[ or: EMBARGOED UNTIL <Mon DD, YYYY, HH:MM TZ> ]

<Headline — sentence case, benefit-led, ONDEWO all-caps>
<Optional subhead / deck — one supporting line>

VIENNA, Austria — <Mon DD, YYYY> — <Lede: the single most important sentence —
who (ONDEWO), what, why it matters — answering the 5 Ws up front (inverted pyramid).>

<Body ¶1 — context and the key detail/number.>

<Body ¶2 — how it works / what's new, in plain, precise language.>

"<Quote — a real human voice, not marketing fluff>," said <Name>, <Title> at ONDEWO.
"<Second sentence of the quote — the why / the vision.>"

<Body ¶3 — availability, integration, on-prem/data point, next step.>

About ONDEWO
<Boilerplate — verbatim ≈50 words from voice-and-tone §6.>

Media contact
<Name> · <Title>
<email> · <phone>
ondewo.com

###
```
Rules: inverted pyramid (most important first); short, active-voice, present-tense
sentences; one or two quotes max; numbers as numerals; the centered `###` marks the
end of the release. Keep it to ~1 page (≈400–500 words).

### 2c. Company fact sheet (`fact-sheet.md`)
Scannable key:value facts for fast journalist reference:
- Company name: ONDEWO · Tagline: *We automate your phone calls.*
- What it is: voice-first conversational AI that automates phone calls (the one-liner
  from `voice-and-tone.md` §6).
- Founded / HQ / employees / website — `‹confirm›` each unless supplied.
- Products: one line each (see 2e).
- Key differentiators: voice-first, multilingual, **on-premise** data sovereignty
  (messaging pillars, brand-foundation §7).
- Markets/audience: enterprises & contact centres (brand-foundation §4).
- Proof points: concurrent calls, languages supported, deployments — all `‹confirm›`.

### 2d. Executive bios (`executive-bios.md`)
Per executive, a repeatable block:
- Name — Title
- Headshot: `‹link/asset›`
- Bio (≈60–90 words, third person, present tense, factual, no hype) `‹confirm›`
- LinkedIn / contact `‹confirm›`

### 2e. Product summaries (`product-summaries.md`)
One tight paragraph per product, drawn from brand-foundation §1 (don't invent features
beyond it; tag any unverified specifics `‹confirm›`):
**ONDEWO CAI** (conversational-AI engine) · **ONDEWO S2T** (speech-to-text) ·
**ONDEWO T2S** (text-to-speech) · **ONDEWO VTSI** (voice/telephony SIP integration) ·
**ONDEWO AIM** (agent/interaction management). Frame each as a building block of an
automated voice stack — "turn a phone call into software."

### 2f. Media contact block (`media-contact.md`)
Name · title · email · phone · ondewo.com · press-asset link. Reusable across docs.

## 3. Build (apply the brand)

- **Words first.** All copy obeys `voice-and-tone.md`: clear over clever, confident
  not boastful, active voice, present tense, sentence-case headlines, `ONDEWO` always
  all-caps, Oxford comma, numerals for stats. Use the **exact** boilerplate, one-liner,
  and tagline — don't paraphrase them. Avoid the banned words (§5: revolutionary,
  disruptive, magic, world-class without proof, cutting-edge, "AI-powered" as filler…).
- **The release PDF/DOCX styling** comes from the tokens — no raw hex/fonts:
  - Build the PDF from `brand-kit/templates/letterhead.html` (it already imports
    `../tokens/ondewo.css`, loads Jost, and draws the blue/magenta top bar, logo header,
    and footer). Pour the release skeleton into the `.page` body; keep the logo in the
    header.
  - Type: the Futura PT → **Jost** stack (`var(--ondewo-font-display)` for the
    headline, `var(--ondewo-font-body)` for body). Headline in blue
    (`var(--ondewo-primary)`), body in ink (`var(--ondewo-text)`, `#231F20`). The
    eyebrow ("FOR IMMEDIATE RELEASE") is all-caps with `letter-spacing:0.12em` in
    magenta (`var(--ondewo-accent)`).
  - **Magenta ≤ ~10%** — the top-bar accent, the eyebrow, maybe one rule. Blue-led,
    white background, generous whitespace. Never a magenta page fill.
  - **Logo:** embed `assets/logo/ondewo-logo-horizontal.svg` (full colour on white).
    Use `ondewo-logo-horizontal-mono-white.svg` only on a blue/dark header band. Never
    recolour, stretch, shadow, or redraw — respect clear space (logo-guidelines §3).
- **Visuals → compose `create-brand-asset`.** If the kit needs a designed graphic
  (launch social card, newsroom banner, quote image), call the `create-brand-asset`
  skill to produce it on the same tokens and official logo, save it under the kit's
  `assets/` folder, and link it from the index. Don't hand-build branded graphics here.
- **Output engine** (use the one named in `document-templates/PLAN.md`; else default
  to these):
  - **PDF:** render the letterhead HTML headless — `chrome --headless
    --print-to-pdf=<out>.pdf --no-pdf-header-footer file://<abs path>` (or the
    browser's "Print → Save as PDF").
  - **DOCX:** `pandoc <release>.md -o <release>.docx` (apply an ONDEWO
    `--reference-doc` if `document-templates/` provides one; otherwise plain).
  - **Index + the supporting `.md` docs** are plain Markdown — no engine needed.

## 4. Verify (before delivering)

- **Render/preview the release** and look at it — don't ship unseen. Open the PDF (or
  screenshot the HTML: `chrome --headless --screenshot=preview.png
  --window-size=1240,1754 file://<abs path>`) and fix any clipping, overflow, or
  off-brand detail.
- **Brand checklist** (`layout-and-spacing.md` §8): only brand tokens; magenta ≤ ~10%;
  Futura/Jost stack + type scale; 4px-grid spacing & generous whitespace; correct logo
  variant with full clear space; one clear focal point.
- **Accessibility** (`accessibility.md` §2): every text/bg pair passes WCAG AA — ink
  `#231F20` on white (16.3), blue `#004C87` on white (8.81), white on blue (8.81),
  magenta `#BE216B` on white (5.80). **Never** blue-on-magenta or magenta-on-blue
  (1.52 — fails).
- **Editorial check:** dateline present and correctly formatted; lede answers the 5 Ws;
  `###` end mark present; `ONDEWO` all-caps everywhere; the boilerplate matches
  `voice-and-tone.md` verbatim; every quote attributed; no banned words.
- **Facts check:** every unverified fact still carries a `‹confirm›` tag.

## 5. Deliver

- Save the whole kit under `brand-kit/generated/press-kit-<slug>/` (create the folder;
  never overwrite `templates/`, `assets/`, or `tokens/`). Name the release
  `ondewo-press-release-<slug>-<YYYY-MM-DD>.<ext>` per the naming convention in
  `assets/ASSET-INDEX.md` §D (lower-case, hyphen-separated).
- Tell the user: what you created and where (absolute paths), how to export/print the
  release at final quality, **which `‹confirm›` placeholders they must fill** (dates,
  names, numbers, quotes, contact, HQ), and that the logo files are referenced
  read-only from `brand-kit/assets/`.

## Guardrails

- Don't introduce off-palette colours, new fonts, or a redrawn/recoloured/stretched/
  shadowed logo. Reuse the tokens and official SVG paths only. Magenta is an accent
  (≤ ~10%), never a page fill.
- Don't use commercial Futura font files in any web/HTML deliverable — use **Jost**
  (typography.md). Outlined/print PDFs are fine.
- **Never fabricate company facts** — founding year, headcount, funding, customer
  names, metrics, executive details, HQ. If not supplied, keep the `‹confirm›` tag and
  list it for the user. Items already tagged `‹confirm›` in `brand-foundation.md`
  (positioning, mission, pillars, proof points) and `voice-and-tone.md` (boilerplate,
  one-liner) stay tagged.
- Voice rules are non-negotiable: clear over clever, confident not boastful, active
  voice, present tense, `ONDEWO` all-caps, sentence-case headlines, no banned words.
- Use the **exact** tagline/boilerplate from `voice-and-tone.md` — don't paraphrase the
  brand's own words.
- Compose, don't duplicate: produce designed visuals via `create-brand-asset` and
  voice-only copy via `brand-copy`; this skill stays focused on the press kit.
