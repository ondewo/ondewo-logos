---
name: webinar-kit
description: Produce a complete, on-brand ONDEWO webinar package end-to-end — promo social posts, an invite/reminder/follow-up email sequence, a registration/landing page, the webinar slide deck, a run-of-show, an asset checklist with owners/deadlines, and a post-event recap blog — by orchestrating the social-media-kit, marketing-email, one-pager/web-hero, slide-deck (webinar mode), and blog-article skills. Use when the user asks to create/plan/build/launch/promote a webinar, webinar kit, webinar campaign, webinar funnel, online event, or virtual event, or says "set up our webinar", "webinar emails and landing page", "webinar deck and follow-up", or "do the whole webinar for me".
---

# Build an ONDEWO webinar kit (end-to-end)

You are the **orchestrator** for a full ONDEWO webinar launch. You don't hand-build
every artefact yourself — you compose the existing per-asset skills, keep one shared
brief so every piece is consistent, and deliver the whole package plus the plan to
run it. One topic in, a launch-ready webinar funnel out.

## Load brand context (always first)

Read these once, up front, and reuse the facts across every artefact so the package
is coherent:

1. `CLAUDE.md` (repo root) — brand TL;DR + hard rules.
2. `brand-kit/README.md` — kit map.
3. `brand-kit/voice-and-tone.md` — every word you write (and the sub-skills write) must match this.
4. `brand-kit/brand-foundation.md` — positioning, audience segments, messaging pillars, proof points, the `‹confirm›` facts.
5. `brand-kit/color-system.md`, `typography.md`, `logo-guidelines.md`, `layout-and-spacing.md`, `accessibility.md` — the visual rules for the deck, landing page, emails, and social art.
6. `brand-kit/tokens/ondewo.tokens.json` — exact colour/type/spacing values. **Use tokens, never raw hex.**
7. `brand-kit/document-templates/PLAN.md` — the **output-engine map** for multi-part documents (which engine/format produces the deck, HTML emails, landing page, and blog). If it's absent, fall back to the starters in `brand-kit/templates/`.

Then load the per-asset skills you will delegate to (read their SKILL.md so you brief
them correctly): `create-brand-asset`, `brand-copy`, `brand-check`, plus the
specialist skills below when installed.

## Intake (keep it lean — infer the rest)

Ask only for what you genuinely can't infer; draft sensible defaults for the rest and
show them for confirmation rather than blocking.

**Must have:** webinar **topic/title**, **date & time (with timezone)**, **duration**
(default 45 min), **target audience** (business / technical / developer — see
brand-foundation §4), and the **primary CTA** after the event (default "Book a demo").

**Infer or default:** presenter name(s)/role(s) `‹confirm›`, registration URL/platform
`‹confirm›`, 3–4 key takeaways (draft from the messaging pillars), promo window
(default 3 weeks), channels (default LinkedIn + X + email list), and the launch
date for the recap blog (default T+2 days).

If a fact is unknown and material (presenter, real registration link, attendee
numbers, proof-point figures), insert a `‹confirm›` placeholder — never invent it.

## Structure (the canonical webinar package)

Produce **five content deliverables** plus **two planning artefacts** — a
run-of-show (B) and an asset checklist (C). Timings are relative to the event
(**T** = go-live); adjust to the actual promo window.

### A. The five content deliverables (each via its own skill)

| # | Deliverable | Delegate to | Brief / contents |
|---|-------------|-------------|------------------|
| 1 | **Registration / landing page** | `one-pager` / `web-hero` (→ `create-brand-asset`, base `templates/web-hero.html`) | Eyebrow + H1 title, 1-line value prop, date/time/duration, 3–4 takeaways, presenter card, agenda, registration form/CTA, logo + footer. Ships **first** (T-21). |
| 2 | **Promo social posts** | `social-media-kit` (→ `create-brand-asset`, base `templates/social-post-1080.svg`, `social-banner-linkedin.svg`) | Announcement, "meet the speaker", a stat/teaser, "1 week to go", "tomorrow", "we're live". Per channel (LinkedIn/X), each with image + caption + link. |
| 3 | **Email sequence** | `marketing-email` | **Invite** (T-14), **Reminder 1** (T-7), **Last-chance** (T-1), **"We're live"** (T-0, ~1h before), **Follow-up / thank-you + on-demand link** (T+1). One subject line + preheader + body + single CTA each. |
| 4 | **Webinar slide deck** | `slide-deck` **mode: webinar** | Title → presenters → agenda → why-it-matters → ONDEWO approach → live demo → proof/results → recap → Q&A → resources → CTA/follow-up. 16:9; **draft by T-5**, **final for the dry run by T-2**. |
| 5 | **Post-event recap / blog** | `blog-article` | Recap of the session: hook, 3–4 key takeaways, a quote/stat, embedded on-demand link, CTA. Publish **T+2**. Drafted from the deck outline so it's ready early. |

### B. Run-of-show (live event timeline — default 45 min)

| Time | Segment | Owner |
|------|---------|-------|
| T-10 → T-0 min | Pre-roll holding slide (title + "starting soon"), AV/mic check | Host |
| 0:00–0:03 | Welcome, housekeeping (recording, Q&A, captions) | Host |
| 0:03–0:06 | Speaker intro + agenda | Host |
| 0:06–0:15 | The problem / why this matters (the stakes) | Speaker |
| 0:15–0:30 | ONDEWO approach + **live demo** | Speaker |
| 0:30–0:37 | Proof / results / customer story `‹confirm›` | Speaker |
| 0:37–0:43 | Q&A (seed 2–3 questions in advance) | Host + Speaker |
| 0:43–0:45 | Recap + **primary CTA** + thank-you slide | Host |
| Post | Stop recording, export, send follow-up | Host |

### C. Asset checklist (owners + deadlines)

Deliver this as a table the team can drive the launch from. Default owners are
placeholders — fill with real names.

| Asset | Skill | Owner | Deadline | Status |
|-------|-------|-------|----------|--------|
| Landing / registration page | one-pager/web-hero | `‹confirm›` Marketing | **T-21** | ☐ |
| Announcement social posts | social-media-kit | `‹confirm›` Social | **T-21** | ☐ |
| Invite email | marketing-email | `‹confirm›` Lifecycle | **T-14** | ☐ |
| Speaker / teaser social posts | social-media-kit | `‹confirm›` Social | **T-10** | ☐ |
| Reminder email #1 | marketing-email | `‹confirm›` Lifecycle | **T-7** | ☐ |
| Webinar deck (draft) | slide-deck (webinar) | `‹confirm›` Presenter | **T-5** | ☐ |
| Deck final + dry run | slide-deck (webinar) | `‹confirm›` Presenter | **T-2** | ☐ |
| Run-of-show confirmed | this skill | `‹confirm›` Host | **T-1** | ☐ |
| "Tomorrow" + "Live" social | social-media-kit | `‹confirm›` Social | **T-1 / T-0** | ☐ |
| Last-chance + "we're live" emails | marketing-email | `‹confirm›` Lifecycle | **T-1 / T-0** | ☐ |
| Follow-up email + on-demand link | marketing-email | `‹confirm›` Lifecycle | **T+1** | ☐ |
| Recap blog | blog-article | `‹confirm›` Content | **T+2** | ☐ |

## Build (apply the brand, route to the right engine)

Hold one **shared brief** (title, value prop, takeaways, CTA, audience, tone) and pass
it to every sub-skill so the funnel reads as one voice. For each artefact:

- **Delegate first.** If the specialist skill exists (`social-media-kit`,
  `marketing-email`, `one-pager`/`web-hero`, `slide-deck`, `blog-article`), invoke it
  with the shared brief. If it isn't installed, fall back to `create-brand-asset`
  (visual assets) or `brand-copy` (text) over the matching `brand-kit/templates/` file
  — the brand result must be identical either way.
- **Output engine / format** — pick per `brand-kit/document-templates/PLAN.md`:
  - Slide deck → the deck engine (16:9, 1920×1080 frame); else `templates/slide-title.svg` per slide.
  - Emails → responsive HTML email; keep inline-safe colours from tokens.
  - Landing page → `templates/web-hero.html` (Jost via Google Fonts).
  - Recap blog → Markdown/HTML article; `templates/markdown-snippets.md` for badges/logo.
  - Social → `templates/social-post-1080.svg` (square) / `social-banner-linkedin.svg`.
- **Colours:** tokens only. Blue-led (≈30%), neutral/whitespace (≈60%), **magenta ≤ ~10%** —
  one accent per view (the key CTA, one stat, the swirl). Never blue-on-magenta or magenta-on-blue.
- **Logo:** embed the official SVG from `brand-kit/assets/logo/` — horizontal lockup by
  default; **mono-white** on blue/dark/photographic backgrounds; mark-only below 24px.
  Respect clear space (½ the height of the "O"). **Never redraw the swirl.**
- **Type:** the Futura/Jost stack. Headlines sentence case (Light or Bold); `ONDEWO`
  all-caps with `+0.12em` tracking; all-caps labels letter-spaced; body ≥ 16px. On
  public web/email use **Jost**, not commercial Futura files.
- **Layout:** 4px-grid spacing, generous whitespace, one focal point + one primary CTA per surface.
- **Copy:** route every word through `voice-and-tone.md` — clear over clever, confident
  not boastful, active voice, present tense, "we"→"you". Draft 3 options for headlines/
  subjects and keep the shortest that holds the benefit. Avoid the banned words (§5).

## Verify (before delivering anything)

- **Render/preview each visual artefact** — don't ship unseen:
  - SVG → PNG: `qlmanage -t -s 1600 -o <outdir> <file.svg>` (macOS), or `rsvg-convert`/`resvg`/`inkscape`.
  - HTML (landing/email) → PNG: headless Chrome `--headless --screenshot=out.png --window-size=1280,900 file://<abs path>`.
  - View each PNG; fix clipping, overflow, or off-brand detail.
- **Run `brand-check`** on every artefact, or manually run the checklist in
  `brand-kit/layout-and-spacing.md` §8: tokens-only colours, magenta ≤ ~10%, Futura/Jost,
  4px spacing, correct logo variant + clear space, one focal point + one CTA.
- **Accessibility:** every text/bg pair must be on the approved list in
  `accessibility.md` §2 (ink-on-white, white-on-blue, magenta-on-white ≥ 5.8:1, …).
  Magenta tints `300`/`400` fail for body — use `#BE216B` (500) or darker. Honour
  `prefers-reduced-motion`; alt text `alt="ONDEWO"` on logos; touch targets ≥ 44px.
- **Cross-artefact consistency:** title, date/time/timezone, takeaways, CTA, and
  registration URL match across the landing page, every email, the deck, and the social posts.

## Deliver

- Save the whole package under a single dated folder:
  `brand-kit/generated/webinar-<topic-slug>-<YYYY-MM-DD>/` with subfiles, e.g.:
  - `landing.html`
  - `email-1-invite.html`, `email-2-reminder.html`, `email-3-lastchance.html`, `email-4-live.html`, `email-5-followup.html`
  - `deck.<ext>`
  - `social-announce.svg`, `social-speaker.svg`, `social-live.svg` (+ a `captions.md`)
  - `recap-blog.md`
  - `run-of-show.md`, `asset-checklist.md`
  Create the folder; **never overwrite `templates/`, `assets/`, or source files.**
- Tell the user, concisely: what each file is, where it lives (absolute path), how to
  export/publish it (render the SVGs to PNG, host the HTML, paste emails into the ESP),
  the promo timeline, the run-of-show, the owner/deadline checklist, and exactly which
  `‹confirm›` placeholders (presenter, registration link, proof-point numbers) they must
  fill before launch.

## Guardrails

- **No off-brand colours or fonts.** Tokens only; no new hex, no second display typeface.
  Magenta is an accent (≤ ~10%), never the dominant fill. Never blue-on-magenta / magenta-on-blue.
- **The logo is fixed artwork** — reuse the official SVGs, correct variant for the
  background, full clear space; never stretch, recolour, shadow, or redraw the swirl.
- **Jost on public web/email**, not commercial Futura files.
- **`ONDEWO` always all-caps;** headlines and CTAs sentence case; one primary CTA per surface.
- **Flag, don't fabricate.** Presenter, dates, registration URL, attendance, and any
  metric tagged `‹confirm›` in `brand-foundation.md` stay as placeholders until the user confirms.
- **Consistency is the job.** If a fact changes (time, title, CTA), propagate it to every
  artefact before delivering — a webinar kit that contradicts itself is off-brand.
