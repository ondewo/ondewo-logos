---
name: explainer-video
description: Produce a production-ready ONDEWO explainer-video pre-production package — logline, 2-sentence concept, timecoded script, voice-over (VO) copy, a shot-by-shot storyboard (visual | on-screen text | VO | duration), style-frame direction, music/tone, and a captions/SRT stub for a 60–90s explainer/product/overview video. Use when the user asks to create, write, script, storyboard, plan, or design an ONDEWO explainer video, product/demo video, 60–90 second video, animated overview, video script or brief, VO/voice-over script, storyboard, style frames, or video captions.
---

# Create an ONDEWO explainer video (pre-production package)

You produce a **finished, on-brand pre-production document** for a 60–90s ONDEWO
explainer video — the doc a video editor, motion designer, or AI-video tool needs
to make the film. **You do not render video.** The deliverable is the
production-ready package (Markdown), optionally with text-to-storyboard SVG
style-frames. Follow this process exactly — it guarantees brand consistency
without the user re-explaining the brand.

**Composes with, never replaces, the other skills.** This skill owns the *video
pre-production package*. For the actual on-brand SVG/HTML still frames, defer to
the **`create-brand-asset`** skill (it owns asset production); for any extended
copy beyond the VO, lean on **`brand-copy`**. Don't re-implement what they do.

## 0. Load brand context (always do this first)

Read, in order:
1. `brand-kit/README.md` — kit map.
2. `brand-kit/voice-and-tone.md` — the VO and on-screen copy must be in this voice.
3. `brand-kit/brand-foundation.md` — positioning, audience, messaging pillars,
   the swirl metaphor (two voices in conversation / a loop that never drops a call),
   and proof points (most are `‹confirm›`).
4. `brand-kit/layout-and-spacing.md` — **§7 Motion** (the swirl draw-in, easing,
   durations) and §6 shapes/graphic language drive the style-frame direction.
5. `brand-kit/color-system.md` (60-30-10, gradient) and `brand-kit/typography.md`
   (Futura → Jost) for any on-screen text and frames.
6. `brand-kit/logo-guidelines.md` + `brand-kit/accessibility.md` — logo variants,
   end-card lockup, contrast pairs for legible captions/on-screen text.
7. `brand-kit/tokens/ondewo.tokens.json` — exact colour/type/space/motion values.
8. **`brand-kit/document-templates/PLAN.md`** — the output-engine plan for document
   deliverables. **Read it if present** and use the engine/format it specifies for
   the `.md` package (and any export). If it is absent (planned file `‹confirm›`),
   default to a single self-contained **Markdown** deliverable.

Never invent colours, fonts, motion specs, or redraw the logo — reuse tokens and
the official SVG paths from `brand-kit/assets/logo/`.

## 1. Intake (only what you can't infer)

Ask/infer, then proceed — don't over-ask:
- **Topic & goal** — what the video sells/explains (e.g. ONDEWO CAI, "answer every
  call 24/7", a launch). Default: the brand-level "We automate your phone calls."
- **Audience** — business / technical / developer (sets tone; see voice §3 and
  brand-foundation §4). Default: business decision-makers.
- **Length** — 60, 75, or 90s. Default: **85s**.
- **Style** — motion-graphics (default, no actors needed), screencast, or live-action.
- **Any real numbers** — concurrent calls, languages, AHT reduction. If none, keep
  them as `‹confirm›` placeholders; never fabricate.

If the brief is clear, infer sensible defaults and draft the whole package.

## 2. Canonical structure (reusable beat sheet, ~85s)

A 60–90s explainer = one idea, one CTA. Use this six-beat arc; scale durations to
hit the target length (keep Hook ≤ 8s and the end-card ≥ 4s).

| # | Beat | Time | Purpose | On-screen | VO direction |
|---|------|------|---------|-----------|--------------|
| 1 | **Hook** | 0:00–0:08 | Name the pain / stat | One line, big | Confident question or stat (pain-led) |
| 2 | **Problem** | 0:08–0:22 | Raise the stakes | Supporting line | "Missed calls cost you customers." |
| 3 | **Solution** | 0:22–0:38 | Introduce ONDEWO | `ONDEWO` lockup + tagline | "ONDEWO automates your phone calls." |
| 4 | **How it works** | 0:38–0:58 | 2–3 capability beats | Short verb-led labels | Route · transcribe · respond; on-prem |
| 5 | **Proof / outcome** | 0:58–1:12 | Make it credible | One key stat (the magenta moment) | Outcome-led, `‹confirm›` numbers |
| 6 | **CTA + end card** | 1:12–1:25 | One action + logo | CTA + `ONDEWO` lockup | "Book a demo." / tagline read |

The package you write contains, in this order:

1. **Logline** — one sentence (≤ 20 words) capturing the whole film.
2. **Concept** — exactly 2 sentences: the idea + how it looks/feels.
3. **Script with timecodes** — the beat sheet above, filled, with `[0:00]` cues.
4. **Voice-over copy** — clean VO read, in ONDEWO voice, no stage directions
   (so it can be recorded or TTS'd directly). Keep ~2.2 words/sec → ≤ ~190 words
   for 85s.
5. **Storyboard (shot-by-shot table)** — the required four columns:

   | Shot | Time | Visual | On-screen text | VO | Dur |
   |------|------|--------|----------------|----|-----|
   | 1 | 0:00 | White frame; swirl mark draws in (single 360° sweep) | "97% hang up after 2 min on hold." `‹confirm›` | "Most callers won't wait." | 8s |

6. **Style-frame direction** — see §3.
7. **Music & tone** — see §3.
8. **Captions / SRT stub** — see §3.

## 3. Build (apply the brand)

**Style-frame direction (per `layout-and-spacing.md` §6–§7):**
- **Palette:** 60-30-10. Light theme default (`#FFFFFF` / `#F7F8FA` bg, `#231F20`
  text); one **brand-blue (`#004C87`) or brand-gradient** hero band for the
  Solution/end-card. **Magenta `#BE216B` ≤ ~10%** — reserve it for a single moment
  (the proof stat or the CTA button), never a base fill.
- **Signature move (the swirl draw-in):** the two-tone swirl **rotates/draws in on
  the opening frame — a single 360° sweep** ("the loop that never drops a call").
  Use it **once** (open) and echo it lightly on the end card. Don't repeat per beat.
- **Motion character:** smooth, confident, never bouncy. Easing
  `cubic-bezier(0.22, 1, 0.36, 1)`; transitions **400–800ms** for storytelling
  beats, 150–250ms for small UI/label moves. Note: spec is `‹confirm›` (motion §7).
- **Graphic language:** arcs, soundwave lines, flowing loops echoing the swirl; one
  motif per frame, generous whitespace. Any stock footage → blue+magenta **duotone**
  (shadows `#001A2E`, highlights `#FAEDF3`). No literal robots / "AI brain" clip-art.
- **Type:** Futura PT → **Jost** web fallback. On-screen lines sentence-case, Bold or
  Light, short. `ONDEWO` all-caps with `+0.12em` tracking. For self-contained SVG
  frames use `font-family="Jost, Futura, 'Century Gothic', sans-serif"`.
- **Logo:** end card uses the official lockup; **mono-white** lockup on blue/gradient
  backgrounds (`ondewo-logo-horizontal-mono-white.svg`), full-colour on white.
  Respect clear space (≥ X). Never recolour or redraw the swirl.

**Music & tone:** clean, confident, modern, **not bouncy** — building synth/strings
with light percussion; duck under VO; resolve on a short logo sting at the end card.
Match the brand dials (formality 7 · warmth 6 · boldness 5 · playfulness 3). Flag the
actual track choice/licensing as `‹confirm›`.

**Captions / SRT stub:** derive from the VO; provide a ready `.srt` block (caption
styling: white text on a subtle scrim or `#231F20` on light — an approved AA pair).
Example:
```srt
1
00:00:00,000 --> 00:00:04,500
Most callers won't wait on hold.

2
00:00:04,500 --> 00:00:08,000
97% hang up after two minutes. ‹confirm›
```

**Output engine/format:** the package is **Markdown** (per
`document-templates/PLAN.md` if present; if absent, a single self-contained `.md`).
**Optionally offer text-to-storyboard SVG style-frames** — one 1920×1080 (16:9)
frame per key beat. **Produce frames via the `create-brand-asset` skill** (it owns
SVG/HTML production); hand it a per-beat brief. Frame recipe it follows: start from
`brand-kit/templates/slide-title.svg`, embed the official logo/mark by copying the
inner paths (mark = two paths in `viewBox="30 30 157 123"`, `fill="#BE216B"` +
`fill="#004C87"`; lockup native `viewBox="26.2 26.5 543.4 130.1"`), tokens only,
magenta ≤ ~10%. **No video rendering** — frames are stills that illustrate the
storyboard.

## 4. Verify before delivering

- **Timing math:** shot durations sum to the target length (60–90s); Hook ≤ 8s,
  end-card ≥ 4s. VO word count ≈ length × 2.2 words/sec.
- **Voice pass:** run all VO + on-screen copy past `voice-and-tone.md` §5 — clear over
  clever, confident not boastful, active/present, `ONDEWO` all-caps, sentence-case
  lines, no banned words. Tagline is exactly **"We automate your phone calls."**
- **Brand checklist:** run `brand-kit/layout-and-spacing.md` §8 against the
  style-frame direction (and every SVG frame): brand tokens only, magenta ≤ ~10%,
  Futura/Jost, 4px-grid spacing, one focal point + one CTA, correct logo variant.
- **Accessibility:** every on-screen text / caption colour pair must be on the
  approved list in `accessibility.md` §2 (never blue-on-magenta). Note
  `prefers-reduced-motion`: the draw-in must have a static fallback.
- **If you produced SVG frames, render them** to confirm they look right (don't ship
  unseen): `qlmanage -t -s 1600 -o <outdir> <frame.svg>` (macOS) or
  `rsvg-convert`/`resvg`/`inkscape`. View the PNG; fix clipping/overflow/off-brand detail.

## 5. Deliver

- Save the package to `brand-kit/generated/explainer-<topic>/` (create the folder;
  never overwrite `templates/`, `assets/`, or `tokens/`):
  - `ondewo-explainer-<topic>.md` — the full package.
  - `ondewo-explainer-<topic>.srt` — the captions stub.
  - `frames/ondewo-explainer-<topic>-<beat>-light-1920x1080.svg` — optional style-frames.
  - Naming per `brand-kit/assets/ASSET-INDEX.md` §D (lower-case, hyphenated, `WxH`).
- Tell the user: what you made, where it is, the total runtime, which `‹confirm›`
  placeholders to fill (proof-point numbers, music licensing, motion spec), and how
  to hand it off — to a motion designer/editor, or paste the storyboard + VO into an
  AI-video/TTS tool. Offer to generate the SVG style-frames if not already made.

## Guardrails

- **No rendering.** Deliver the production-ready doc (+ optional still frames), not a
  video file.
- No off-brand colours, fonts, or a redrawn/recoloured swirl; magenta stays an accent
  (≤ ~10%) across all frames. Use mono-white logo on dark/blue/gradient.
- Don't use commercial Futura files for any web-shipped asset — use Jost.
- **Flag, don't fabricate** `‹confirm›` facts: proof-point numbers, mission/positioning
  (brand-foundation §2–§3, §8), the motion spec (layout §7), and music/track licensing.
- Honour `prefers-reduced-motion` in the direction (provide a static fallback for the
  draw-in). Keep one swirl draw-in (open), not one per beat.
