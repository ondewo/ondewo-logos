---
name: blog-article
description: Write an on-brand ONDEWO blog post, SEO article, or knowledge-base/how-to guide — produces title options, meta description, slug, H2/H3 outline, a full draft in ONDEWO voice, internal/external link suggestions, a CTA, and static-site Markdown front-matter. Use whenever the user asks to write, draft, generate, or outline a blog article, thought-leadership post, SEO/SEO-optimised article, knowledge-base article, help-center or how-to guide, or FAQ page for ONDEWO.
---

# Write an ONDEWO blog / SEO / knowledge article

You are producing a publish-ready, on-brand ONDEWO long-form article — SEO-optimised
thought leadership or a knowledge-base/how-to guide — as Markdown with static-site
front-matter. Follow this process exactly; it guarantees brand voice and search
quality without the user re-explaining the brand.

**Scope & hand-offs.** This skill owns the *written Markdown article*. For a gated
PDF/eBook lead magnet use `whitepaper`; for a customer story use `case-study`; hand
any hero/OG/social image to `create-brand-asset`; reuse `brand-copy`/`brand-check`
for the final voice pass. Compose these, don't reinvent them.

## 0. Load the brand context (always do this first)

Read, in order:
1. `brand-kit/README.md` — kit map.
2. `brand-kit/voice-and-tone.md` — voice principles, tone-by-context, grammar, the
   **like / avoid word lists**, copy patterns, tagline & boilerplate. This is the
   primary spec for this skill.
3. `brand-kit/brand-foundation.md` — positioning, audience, messaging pillars, proof
   points (and which facts are tagged `‹confirm›`).
4. `brand-kit/tokens/ondewo.tokens.json` — exact colour/type values for any rendered
   visual (OG card, inline callout), referenced by token, never re-typed.
5. `brand-kit/document-templates/PLAN.md` — the document output-engine plan: which
   renderer/format to target for long-form Markdown (static-site engine conventions,
   front-matter shape, how the draft becomes a page). If it isn't present yet, default
   to portable CommonMark + YAML front-matter and note that to the user.
6. Only if the article ships with a hero/OG image or styled callouts, also read
   `brand-kit/color-system.md`, `typography.md`, `logo-guidelines.md`,
   `layout-and-spacing.md`, and `accessibility.md`.

Never invent colours, fonts, stats, customer names, or redraw the logo — reuse tokens
and the official SVG paths from `brand-kit/assets/logo/`.

## 1. Intake (ask only what you can't infer — keep it lean)

Capture or sensibly infer four things, then proceed:

| Field | What it drives |
|-------|----------------|
| **Topic / angle** | The thesis and title |
| **Primary keyword** | Title, slug, meta, H1, first 100 words, one H2 |
| **Audience** | business (exec/ops) · technical (IT/architect) · developer — sets tone (voice-and-tone §3) |
| **Search intent** | informational · commercial · transactional → thought-leadership **or** knowledge/how-to variant |

Helpful but optional (infer defaults, don't over-ask): 1–3 secondary keywords, target
length, internal pages to link to, the CTA, British vs. US English (default per
audience region — see voice-and-tone §4). If the user gave a clear brief, infer the
rest and draft; surface assumptions in the delivery note rather than blocking.

## 2. Canonical structure (reusable)

Output is **one Markdown file**: YAML front-matter + body.

### Front-matter (static-site, fill every field)
```yaml
---
title: "<≤60 chars, sentence case, primary keyword near the front>"
description: "<meta description, 140–160 chars, one benefit + a CTA verb>"
slug: "<lowercase-hyphenated-keyword-led-no-stopwords>"
date: "<YYYY-MM-DD — publish date>"
author: "ONDEWO"
category: "Blog"            # Blog | Knowledge
tags: ["voice-ai", "call-automation"]   # 2–5, lowercase
keywords: ["<primary>", "<secondary>"]
canonical: "https://www.ondewo.com/blog/<slug>"   # ‹confirm path›
image: "./ondewo-og-<slug>-blue-1200x630.png"     # OG/Twitter card, on-brand
draft: true                 # flip to false after human review
---
```

### A) Thought-leadership / SEO article (default)
1. **Title (H1)** — most engines render H1 from `title`; start the body at H2. Sentence
   case, primary keyword early.
2. **Lead (2–3 sentences)** — hook with the reader's pain or a stat `‹confirm›`; say
   what they'll get; land the primary keyword naturally in the first 100 words.
3. **Key takeaways** — 3–5 bullets (good for featured snippets). Optional.
4. **3–6 `##` H2 sections**, each mapped to a search sub-intent / related keyword, with
   `###` H3s where useful. One idea per section; lead with the benefit, then detail.
5. **Proof** — concrete numbers `‹confirm›`, examples, and how ONDEWO does it — woven in,
   never a mid-article hard sell.
6. **What this means for you** — short synthesis / conclusion.
7. **CTA block** — exactly one, verb-first, sentence case ("Book a demo", "Talk to
   sales", "Read the docs", "See it in action").
8. **FAQ (`## FAQ`)** — 3–5 `###` questions as real searcher phrasings (long-tail +
   snippet/`FAQPage` schema bait).

### B) Knowledge-base / how-to variant (intent = task completion)
Set `category: "Knowledge"` and add `type: "how-to"`. Tone = docs: precise, neutral,
helpful (voice-and-tone §3) — fewer rhetorical hooks, more task focus.
1. **Lead** — one line: what this guide does and who it's for.
2. **Prerequisites** — bullet list of what's needed first.
3. **Steps** — `## Step 1 …`, `## Step 2 …` (or one `## Steps` with an ordered list);
   imperative, one action per step; show real commands/values in code blocks.
4. **Troubleshooting** — common errors → fixes (calm, solution-first).
5. **Related articles** — internal links to neighbouring docs.
6. **FAQ** — optional; consider `HowTo` + `FAQPage` JSON-LD.

### Links (both variants)
- **2–4 internal links** with descriptive anchor text (never "click here"); if you don't
  know the real URL, propose a slug as `‹confirm URL›`.
- **1–3 external links** to credible, non-competitor authorities (standards bodies,
  research, neutral reference). Never link a competitor as "authority".

## 3. Build (apply the brand)

- **Voice (the core of this skill).** Clear over clever; confident, not boastful; human;
  precise. Active voice, present tense, "we" (ONDEWO) → "you" (the reader). Sentence
  case for the title and every heading; `ONDEWO` always all-caps (`ONDEWO CAI`,
  `ONDEWO S2T` for products). Oxford comma. Numerals for stats. Pick British **or** US
  English and stay consistent. Tagline when you need it: *We automate your phone calls.*
- **Words.** Favour: automate, conversation, voice, real-time, on-premise, multilingual,
  secure, scale, integrate, resolve, answer, flow. **Avoid:** revolutionary, disruptive,
  magic, ninja, "simply just", world-class (without proof), cutting-edge, "AI-powered" as
  filler, robotic clichés ("press 1 for…") unless contrasting against them. Run every
  draft past voice-and-tone §5 before finalising (a `brand-copy`/`brand-check` pass).
- **SEO without stuffing.** Reader first, search second. Place the primary keyword where
  it counts (title, meta, slug, H1, first 100 words, ≥1 H2) and let it recur 3–5× only
  where natural. Descriptive subheads. Short sentences; cut filler ("in order to" → "to").
- **Output engine.** Markdown + YAML front-matter targeting the engine named in
  `document-templates/PLAN.md` (else portable CommonMark). Don't hand-build site chrome
  or CSS — the site theme already imports the ONDEWO tokens (Futura PT → **Jost** on
  public web) and brand colours, so the article inherits them.
- **Any visual you generate** (OG/Twitter card 1200×630, inline callout): tokens only,
  magenta **≤ ~10%** of the surface, logo copied from `brand-kit/assets/logo/`
  (mono-white on blue/dark, full-colour on light) — **never redraw the swirl**. For the
  image itself, hand off to the `create-brand-asset` skill rather than reinventing it.
- **Drafting flow.** Offer **3 title options** + recommend one; write the meta and slug;
  build the H2/H3 outline; then the full draft; then links, CTA, and FAQ. Keep proof-point
  numbers as `‹confirm›` placeholders unless the user supplied real figures.

## 4. Verify before delivering

- **Preview/render.** Render the Markdown (the site's dev build, or Markdown→HTML) to
  confirm the front-matter parses, there's exactly one H1, the H2/H3 hierarchy has no
  skipped levels, links resolve, and code blocks are intact.
- **SEO checklist:**
  - [ ] Primary keyword in title (within first ~60 chars), meta description, slug, H1,
        first 100 words, and ≥1 H2 — no stuffing.
  - [ ] Title ≤ 60 chars; meta description 140–160 chars with a CTA verb.
  - [ ] Slug short, lowercase, hyphenated, keyword-led, no stop words.
  - [ ] Exactly one H1; logical H2/H3 nesting.
  - [ ] 2–4 internal links (descriptive anchors) + 1–3 authoritative external links.
  - [ ] Length fits intent (thought-leadership ≈ 1,200–2,000 words; how-to as long as the
        task needs — no padding).
  - [ ] FAQ present for snippet/schema capture; consider `Article`/`HowTo`/`FAQPage` JSON-LD.
  - [ ] OG/Twitter image set (1200×630), on-brand, with alt text.
  - [ ] `canonical` set; `draft: true` until reviewed.
- **Voice check** (effectively a `brand-copy`/`brand-check` pass): no banned words,
  `ONDEWO` all-caps everywhere, sentence-case headings, active/present, consistent
  spelling variant.
- **Accessibility.** Descriptive link text (not "click here"); alt text on every image;
  no heading-level skips; if a visual carries meaning, don't rely on colour alone. For any
  OG card pick a text/bg pair from `accessibility.md` §2 (e.g. white-on-blue `#FFFFFF`/
  `#004C87`); never blue-on-magenta. Run the `layout-and-spacing.md` §8 checklist for
  visuals.

## 5. Deliver

- Save the article to `brand-kit/generated/blog/<slug>/index.md` (create folders; never
  overwrite `templates/`, `assets/`, or `tokens/`). Put any OG image beside it as
  `ondewo-og-<slug>-blue-1200x630.png` (naming per `assets/ASSET-INDEX.md` §D).
- Tell the user: the file path; the recommended title plus the two alternatives; where to
  drop it into their static site (e.g. `content/blog/`); every `‹confirm›` placeholder to
  fill (stats, customer names, internal URLs, canonical path); and to flip `draft: false`
  after review.

## Guardrails

- No off-palette colours, no new typefaces, never a redrawn logo. On public web use
  **Jost**, not commercial Futura font files.
- Magenta is an accent (**≤ ~10%**) in any rendered visual — never the dominant fill;
  never blue-on-magenta / magenta-on-blue text.
- **Never fabricate** metrics, ROI figures, customer names, or case studies for ranking —
  mark each as `‹confirm›`. Flag, don't present as fact, anything tagged `‹confirm›` in
  `brand-foundation.md`.
- Don't invent internal URLs (propose `‹confirm›` slugs) and don't cite competitors as
  external authorities.
- Voice rules are non-negotiable: sentence-case headings, `ONDEWO` all-caps, active/present
  voice, no banned words, readers before keywords (no stuffing, no clickbait).
