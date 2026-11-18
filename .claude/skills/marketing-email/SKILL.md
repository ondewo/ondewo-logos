---
name: marketing-email
description: Create ONDEWO marketing emails — cold outreach, 3–5 touch nurture/drip sequences, newsletters, product announcements, event invites, and follow-ups. Use whenever the user asks to write, draft, design, or build an email, email campaign, cold email, outreach, drip/nurture sequence, newsletter, launch/release announcement, webinar or event invite, or a follow-up for ONDEWO. Produces responsive table-based HTML using brand tokens (single magenta CTA, official logo, Futura/Jost), with subject-line options + preview text and a matching plain-text version.
---

# Create an ONDEWO marketing email

Produce a finished, on-brand, deliverable ONDEWO email — responsive table-based
HTML **plus** a plain-text alternative, with subject + preview lines drafted in the
ONDEWO voice. Follow this process so the user never has to re-explain the brand.

This skill is the **email specialisation of `create-brand-asset`** — it composes the
same brand-loading, token, and verify discipline, applied to the constraints of
email (tables, inlined hex, plain-text mirror, deliverability). It does **not**
replace it: for any standalone visual the email embeds (a hero/feature image, a
social card, an OG/share image), hand off to `create-brand-asset` rather than
reinventing it here.

## 0. Load brand context (always do this first)

Read, in order:
1. `brand-kit/README.md` — kit map.
2. `brand-kit/voice-and-tone.md` — subjects, body copy, CTAs, banned words. **Load this every time** (an email is mostly words).
3. The relevant design specs:
   - colour → `brand-kit/color-system.md`
   - type → `brand-kit/typography.md`
   - logo → `brand-kit/logo-guidelines.md`
   - layout/spacing → `brand-kit/layout-and-spacing.md`
   - contrast → `brand-kit/accessibility.md`
4. `brand-kit/tokens/ondewo.tokens.json` — exact hex/size values to inline.
5. `brand-kit/templates/email-signature.html` — the table pattern, logo raw-URL, and footer to reuse.
6. `brand-kit/document-templates/PLAN.md` — the document-template plan; it defines the **output engine/format** for generated documents. **Read it if present** and follow the engine it specifies for email. If it's absent, default to the hand-coded table-based HTML + plain-text approach in this skill.
7. `brand-kit/brand-foundation.md` — positioning, audience, proof points, and any `‹confirm›` facts.

Never invent colours, fonts, or redraw the logo. Reuse token hex values and the
official logo from `brand-kit/assets/logo/`.

## 1. Intake (ask/infer — keep it lean)

Infer from the brief; only ask when you truly can't. Pin down:

- **Type** — cold outreach · nurture sequence (how many touches) · newsletter · product announcement · event invite · follow-up.
- **Audience** — business (ops/CX leader), technical (architect), or developer. Sets the tone (voice-and-tone §3).
- **One key message + one CTA** — the single action this email drives ("Book a demo", "Read the docs", "Register").
- **Sender** — name + title for the signature; reply-to.
- **Links/assets** — destination URL, any stat or proof point (keep unknowns as `‹confirm›`).

If copy is missing, **draft it** per `voice-and-tone.md` and offer it. If the brief
is clear, infer sensible defaults and proceed — don't over-ask. For a nurture
sequence, also infer the cadence (e.g. day 0 / 3 / 7 / 14) and the goal of each touch.

## 2. Canonical structure (per type)

Every email shares the same **shell** (see §3): preheader → logo header → body →
**one** magenta CTA → divider → signature/footer (unsub + view-in-browser). Only the
body and the subject/preview change per type. Subjects are **sentence case**, ≤ ~50
characters; preview text is 40–90 characters and never repeats the subject.

### Cold outreach (50–125 words, one ask)
- **Subjects:** `Quick question about ‹company›’s call volume` · `Answering every call at ‹company›` · `‹Mutual context› — 15 minutes?`
- **Preview:** `A two-line idea for your hotline — no deck required.`
- **Body:** 1) one-line relevance hook (their pain/context) → 2) one sentence on what ONDEWO does for them (outcome, not features) → 3) one proof point `‹confirm›` → 4) single soft CTA ("Worth a 15-min look?"). No images beyond the logo. P.S. line optional.

### Nurture sequence (3–5 touches; each 75–150 words, one idea each)
A connected arc, one email per file. Suggested 4-touch cadence (day 0 / 3 / 7 / 14):
1. **Problem** — name the pain ("97% hang up after 2 min on hold"). Soft CTA: read/learn.
2. **Solution** — how ONDEWO automates the call; one concrete capability.
3. **Proof** — case study / metric / on-premise + data-control angle `‹confirm›`. CTA: see it.
4. **Invitation** — direct ask: "Book a demo". Optional touch 5 = breakup/last-call.
- **Subjects (per touch):** `The real cost of hold music` · `Answer every call — in any language` · `How ‹customer› cut handling time` · `See ONDEWO on your numbers`
- Each touch escalates CTA strength; keep one CTA per email. Output a `sequence.md` listing day, goal, subject, preview, CTA.

### Newsletter (scannable; 150–300 words across 2–4 blocks)
- **Subjects:** `ONDEWO this month: ‹headline item›` · `Voice AI notes — ‹month›` · `New in ONDEWO: ‹feature›`
- **Preview:** `‹Lead item›, plus two shorter reads.`
- **Body:** short intro line → 2–4 stacked story blocks (each: small eyebrow label, one-line H, 1–2 sentence summary, inline blue text link) → one primary CTA at the foot. Use a magenta eyebrow on **only one** lead block; the rest blue/ink.

### Product announcement (short; 75–150 words)
- **Subjects:** `New: ‹feature› in ONDEWO ‹product›` · `‹Capability› is here` · `Ship ‹outcome› with ONDEWO ‹product›`
- **Preview:** `What it does, who it helps, and how to try it.`
- **Body:** eyebrow "What's new" → headline (the feature, sentence case) → 2 sentences: what it does + the benefit → optional 3-bullet "what you get" → single CTA ("See what's new" / "Read the changelog"). One hero/feature image optional (keep text-to-image healthy, alt text required).

### Event invite (concise; details block is non-negotiable)
- **Subjects:** `You're invited: ‹event›` · `‹Topic› — live with ONDEWO, ‹date›` · `Join us at ‹event›`
- **Preview:** `‹Date› · ‹time/timezone› · ‹online or city›. Save your seat.`
- **Body:** eyebrow "Invitation" → event name → one-line value ("why attend") → **details block** (date, time + timezone, location/online, duration, speakers `‹confirm›`) as a bordered table row → single CTA ("Register" / "Save my seat"). Optional add-to-calendar link.

### Follow-up (very short; 40–90 words)
- **Subjects:** `Following up — ‹topic›` · `Next step on ‹topic›?` · `Re: ‹original subject›`
- **Preview:** `A quick recap and one next step.`
- **Body:** one line of context ("After our call…") → one-sentence recap of value → one explicit next step (a single CTA or a proposed time). Warm, brief, zero filler. No images beyond the logo.

## 3. Build

Apply the brand with email-safe techniques. **Email clients don't support CSS
variables, `<style>` is unreliable, and flexbox/grid don't work** — so inline the
**token hex values** and lay out with tables.

**Output engine/format:** follow `document-templates/PLAN.md` if it specifies one
(e.g. MJML). Otherwise hand-code the table shell below. Width **600px**, fluid to
100% on mobile, all critical styles inline.

- **Colours — tokens only (inline the hex):** body text `#231F20` (ink) on `#FFFFFF`; muted `#5A5560`; structure/headings/links `#004C87` (blue); page backdrop `#F7F8FA`; borders `#E5E4E6`. **Magenta `#BE216B` is the accent (≤ ~10%): reserve it for small accents only — the single CTA button, the signature left-rule, the `ondewo.com` link, and at most one all-caps eyebrow label. Never a filled magenta background, body-text block, or second button.** Button hover `#A01C5A` (magenta-600). Never blue-on-magenta or magenta-on-blue.
- **One CTA.** A single "bulletproof" magenta button (table cell `bgcolor` + padded `<a>`, `border-radius:8px`). Secondary actions are inline blue text links, never second buttons.
- **Type — Futura → Jost stack, web-safe fallbacks:** `font-family:'Jost','Century Gothic','Trebuchet MS',Arial,sans-serif;`. Don't ship commercial Futura font files; link Jost via Google Fonts for clients that honour it, and let the fallbacks cover Outlook. Headlines **sentence case**, weight 700, blue. Body ≥ 16px, line-height 1.5–1.6. All-caps eyebrow labels get `letter-spacing:0.12em` in magenta.
- **Logo:** reference the official horizontal SVG by raw URL (as in `email-signature.html`): `https://raw.githubusercontent.com/ondewo/ondewo-logos/ai_brand_kit/brand-kit/assets/logo/ondewo-logo-horizontal.svg`, `width="150"`, `alt="ONDEWO"`. On a blue/dark band use the `-mono-white` variant. Never redraw or recolour it. (If a client may strip SVG, also keep a PNG fallback path `‹confirm CDN›`.)
- **Imagery:** the logo aside, don't hand-build any hero/feature graphic here — hand off to **`create-brand-asset`** to produce it on-brand (tokens, official logo paths, magenta ≤ ~10%), then reference the exported PNG/JPG by hosted URL with required `alt` text and a sensible `width`. Keep the text-to-image ratio healthy; never an image-only email.
- **Spacing:** 4px-grid; 40px side padding (24px on mobile via media query), generous whitespace, one focal point.
- **Preheader:** hidden preview-text `<div>` right after `<body>` (40–90 chars), padded with `&zwnj;&nbsp;` so client text doesn't leak in.
- **Footer:** reuse the signature pattern (magenta left-rule, name in blue, title, `ondewo.com`, tagline) + legal line: company name, address `‹confirm›`, **Unsubscribe** + **Preferences** links, and **View in browser**.
- **Plain-text alternative (always):** a `.txt` mirror — same message, no markup, links written out in full, dividers as `---`, an unsubscribe URL, tagline at the foot. This is required for deliverability and accessibility; never ship HTML alone.

**Reusable HTML shell** (swap the body block per type; keep everything else):

```html
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light">
  <title>‹email title›</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&display=swap');
    body{margin:0;padding:0;width:100%!important;background:#F7F8FA;}
    a{color:#004C87;}
    .btn:hover{background:#A01C5A!important;}
    @media only screen and (max-width:600px){
      .container{width:100%!important;}
      .px{padding-left:24px!important;padding-right:24px!important;}
      .h1{font-size:26px!important;}
    }
  </style>
</head>
<body style="margin:0;padding:0;background:#F7F8FA;">
  <!-- Preheader / preview text (hidden) -->
  <div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:#F7F8FA;opacity:0;">
    ‹preview text 40–90 chars›&zwnj;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </div>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#F7F8FA;">
    <tr><td align="center" style="padding:24px 12px;">
      <table role="presentation" class="container" width="600" cellpadding="0" cellspacing="0" border="0"
        style="width:600px;max-width:600px;background:#FFFFFF;border:1px solid #E5E4E6;border-radius:8px;
        font-family:'Jost','Century Gothic','Trebuchet MS',Arial,sans-serif;color:#231F20;">

        <!-- Header / logo -->
        <tr><td class="px" style="padding:28px 40px 4px 40px;">
          <img src="https://raw.githubusercontent.com/ondewo/ondewo-logos/ai_brand_kit/brand-kit/assets/logo/ondewo-logo-horizontal.svg"
               width="150" alt="ONDEWO" style="display:block;border:0;">
        </td></tr>

        <!-- ===== BODY (swap per email type) ===== -->
        <tr><td class="px" style="padding:20px 40px 8px 40px;">
          <div style="text-transform:uppercase;letter-spacing:0.12em;font-weight:500;font-size:12px;color:#BE216B;margin-bottom:10px;">‹Eyebrow›</div>
          <h1 class="h1" style="margin:0 0 12px 0;font-weight:700;font-size:30px;line-height:1.25;color:#004C87;">‹Sentence-case headline›</h1>
          <p style="margin:0 0 16px 0;font-size:16px;line-height:1.6;color:#231F20;">‹Lead with the benefit. One idea per paragraph.›</p>
          <p style="margin:0 0 24px 0;font-size:16px;line-height:1.6;color:#231F20;">‹Supporting detail or one proof point ‹confirm›.›</p>
        </td></tr>

        <!-- CTA: single magenta bulletproof button -->
        <tr><td class="px" align="left" style="padding:0 40px 28px 40px;">
          <table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
            <td class="btn" bgcolor="#BE216B" style="border-radius:8px;">
              <a href="‹https://www.ondewo.com/...?utm_source=email&utm_medium=‹type›&utm_campaign=‹slug››"
                 style="display:inline-block;padding:14px 28px;font-family:'Jost','Century Gothic',Arial,sans-serif;
                 font-size:16px;font-weight:500;color:#FFFFFF;text-decoration:none;border-radius:8px;">‹Book a demo›</a>
            </td>
          </tr></table>
        </td></tr>

        <!-- Divider -->
        <tr><td class="px" style="padding:0 40px;"><div style="border-top:1px solid #E5E4E6;font-size:1px;line-height:1px;">&nbsp;</div></td></tr>

        <!-- Signature + footer -->
        <tr><td class="px" style="padding:20px 40px 28px 40px;font-size:12px;line-height:1.6;color:#7E7A83;">
          <div style="border-left:3px solid #BE216B;padding-left:14px;margin-bottom:14px;">
            <div style="font-weight:700;font-size:14px;color:#004C87;">‹Full Name›</div>
            <div style="color:#5A5560;font-size:13px;">‹Job Title›, ONDEWO</div>
            <div><a href="https://www.ondewo.com" style="color:#BE216B;text-decoration:none;font-weight:500;">ondewo.com</a> &middot; We automate your phone calls.</div>
          </div>
          ONDEWO GmbH &middot; ‹address ‹confirm›› &middot;
          <a href="‹{{unsubscribe_url}}›" style="color:#7E7A83;">Unsubscribe</a> &middot;
          <a href="‹{{preferences_url}}›" style="color:#7E7A83;">Preferences</a>
        </td></tr>
      </table>

      <table role="presentation" class="container" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;"><tr>
        <td align="center" style="padding:12px;font-family:'Jost',Arial,sans-serif;font-size:11px;color:#A4A2A8;">
          Trouble viewing? <a href="‹{{view_in_browser}}›" style="color:#7E7A83;">View in browser</a>
        </td>
      </tr></table>
    </td></tr>
  </table>
</body>
</html>
```

**Plain-text mirror** (`.txt`, ship alongside every HTML):

```text
ONDEWO — We automate your phone calls.

‹Sentence-case headline›

‹Lead with the benefit. One idea per line.›

‹Supporting detail or one proof point ‹confirm›.›

→ ‹Book a demo›: https://www.ondewo.com/...?utm_source=email&utm_medium=‹type›&utm_campaign=‹slug›

---
‹Full Name› — ‹Job Title›, ONDEWO
ondewo.com · We automate your phone calls.
ONDEWO GmbH · ‹address ‹confirm››
Unsubscribe: ‹{{unsubscribe_url}}›   Preferences: ‹{{preferences_url}}›
```

### Deliverability & length guidance
- **Subject:** ≤ ~50 chars (mobile truncates ~30–40); sentence case; no ALL-CAPS, no spammy "!!!", "FREE", "$$$". Front-load the value.
- **Preview text:** 40–90 chars, complements (never repeats) the subject. Always set it.
- **Length:** cold 50–125 words · nurture 75–150 · follow-up 40–90 · newsletter 150–300 · announcement/invite short and scannable. Shorter wins.
- **One CTA** above the fold; secondary actions as text links.
- **Weight:** keep HTML < ~100 KB (Gmail clips at 102 KB). Healthy text-to-image ratio; never an image-only email.
- **Always send multipart:** HTML **+** plain-text. Every image needs `alt`.
- **Compliance:** working **Unsubscribe** + a `List-Unsubscribe` header, physical sender address, and SPF/DKIM/DMARC alignment — coordinate with ops `‹confirm›`.
- **Voice:** clear over clever; confident, not boastful; active voice; "we" → "you"; avoid the §5 banned words (revolutionary, magic, world-class without proof, "AI-powered" filler).

## 4. Verify (before delivering)

- **Render & preview both widths** — don't ship unseen. Open the HTML in headless Chrome and screenshot at desktop and mobile:
  - `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --screenshot=preview-desktop.png --window-size=640,1200 file://<abs path>.html`
  - `… --screenshot=preview-mobile.png --window-size=375,1200 …`
  - View the PNGs; fix any clipping, overflow, broken logo, or magenta creeping past ~10%.
- **Brand checklist** — run `brand-kit/layout-and-spacing.md` §8 (logo clear space + right variant, tokens only, magenta ≤ ~10%, Futura/Jost stack + scale, 4px spacing, one focal point + one CTA).
- **Accessibility pairs** (`accessibility.md` §2) — confirm every text/bg pair is approved: ink `#231F20` on white (16.3), blue `#004C87` on white (8.81), **white on magenta `#BE216B` (5.80 — the CTA label)**, muted `#5A5560` on white (7.0). Never magenta-on-blue or blue-on-magenta. Logo `alt="ONDEWO"`; decorative rules `alt=""`. Touch targets ≥ 44px.
- **Copy pass** — sentence-case subject, `ONDEWO` all-caps, no banned words, links resolve, no leftover `‹...›` except intentional merge tags/`‹confirm›`.
- **Plain-text** — exists, mirrors the message, links spelled out, unsubscribe present.

## 5. Deliver

- Save to **`brand-kit/generated/email/`** (create it; never overwrite `templates/` or `assets/`):
  - Single email: `email/<type>-<slug>-<YYYYMMDD>.html` + matching `.txt` (e.g. `cold-outreach-banks-20260629.html`).
  - Nurture sequence: a folder `email/nurture-<topic>-<YYYYMMDD>/` with `touch-1.html` … `touch-N.html`, each `.txt`, plus `sequence.md` (day, goal, subject, preview, CTA per touch).
  - Keep the rendered preview PNGs next to the source.
- Tell the user: what you made and where; the **subject options + chosen preview text**; that both HTML and plain-text are included; which `‹...›` placeholders / merge tags / `‹confirm›` facts to fill (sender, address, links, unsubscribe/view-in-browser tokens, UTM); and how to paste it into their ESP (HubSpot/Mailchimp/etc.). Offer to draft alternative subject lines or the next sequence touch.

## Guardrails
- No off-palette hex and no new typefaces — inline only token values; Futura/Jost stack with web-safe fallbacks.
- Magenta is the accent (≤ ~10%): one CTA button + the signature rule. Never a magenta background block of body text, never blue-on-magenta / magenta-on-blue.
- Never redraw, recolour, stretch, or shadow the logo; reference the official SVG (mono-white on dark backgrounds), respect clear space and 24px min height.
- Always ship HTML **and** plain-text, with a working unsubscribe and a real sender address.
- Sentence-case subjects, ≤ ~50 chars; `ONDEWO` always all-caps; obey the voice rules and banned-word list.
- Flag, don't fabricate — keep stats, customer names, addresses, links, and boilerplate marked **`‹confirm›`** (the brand kit's unverified-fact marker; same intent as a `<confirm>` flag) until the user supplies real values. Anything tagged `‹confirm›` in `brand-foundation.md` (one-liner, boilerplate, proof points) is inferred — surface it, never assert it as fact.
