# ONDEWO — Voice & Tone

How ONDEWO writes. Use this for every headline, button, email, slide, social
post, and UI string. A coding agent generating copy should follow these rules
exactly.

---

## 1. Voice (constant) vs. tone (situational)

**Voice** is who we are — it never changes. **Tone** flexes with context: a
product error message is calm and helpful; a launch announcement is confident and
energetic.

## 2. Voice principles

### Clear over clever
Say the thing. Lead with the benefit, then the detail.
- ✅ "Answer every call, day or night."
- ❌ "Synergistically leverage next-gen omnichannel voice paradigms."

### Confident, never boastful
State capabilities plainly; let proof points do the bragging.
- ✅ "Deploy on-premise. Your data never leaves your infrastructure."
- ❌ "The world's most revolutionary, unbeatable AI ever created."

### Human, because we automate humans' work
We build voice AI — our writing should sound like a smart person talking, not a
machine.
- ✅ "Hold music, retired."
- ❌ "Utilize the solution to facilitate caller throughput optimization."

### Precise & technically credible
When we talk to engineers, we are exact. Real terms, real numbers.
- ✅ "Stream audio over gRPC; get partial transcripts in <300 ms."
- ❌ "Super fast transcription, basically instant."

### Respectful of the reader's time
Short sentences. Active voice. Cut filler ("in order to" → "to"; "is able to" → "can").

## 3. Tone by context

| Context | Tone | Example |
|---------|------|---------|
| Website hero | Confident, benefit-led | "We automate your phone calls." |
| Product / feature | Clear, concrete | "Route, transcribe, and respond — in one call." |
| Developer docs | Precise, neutral, helpful | "Returns a `StreamingRecognizeResponse`. Errors surface as gRPC status codes." |
| Error / empty state | Calm, solution-first | "That number isn't connected yet. Add a SIP trunk in Settings to start." |
| Social (LinkedIn) | Insightful, professional, lightly bold | "97% of callers hang up after 2 minutes on hold. Your AI doesn't have to." |
| Sales / pitch | Outcome-led, credible | "Cut average handling time and answer 100% of calls — without hiring." |

## 4. Grammar & mechanics

- **Brand name:** `ONDEWO` — all caps, always. Products: `ONDEWO CAI`, `ONDEWO S2T` (caps).
  In running prose where all-caps feels shouty, "Ondewo" is acceptable only if a
  client style guide requires it; **default to ONDEWO**. Never "OnDewo" or "ondewo" (except in code, URLs, package names).
- **Voice:** active. **Tense:** present.
- **Person:** "we" (ONDEWO) talking to "you" (the customer).
- **Oxford comma:** yes.
- **Numbers:** numerals for stats ("3 languages", "24/7"). Spell out one–nine in soft prose.
- **Capitalisation:** sentence case for headlines and buttons ("Talk to sales"), not Title Case.
- **Punctuation in UI:** no trailing periods on buttons/labels; periods in full sentences.
- **Spelling:** British or US English — **pick one per asset and stay consistent**
  (the official guideline is EU-based; default to British English for EU-facing,
  US English for US-facing). `‹confirm›`

## 5. Words we like / avoid

**Like:** automate, conversation, voice, real-time, on-premise, multilingual,
secure, scale, integrate, resolve, answer, flow, seamless (sparingly).

**Avoid:** revolutionary, disruptive, magic, ninja, simply just, world-class
(unless backed by proof), cutting-edge, "AI-powered" as filler, robotic clichés
("press 1 for…") unless we're contrasting against them.

## 6. Tagline & boilerplate

- **Primary tagline:** *We automate your phone calls.*
- **One-liner `‹confirm›`:** *ONDEWO builds voice-first conversational AI that
  automates phone conversations — multilingual, scalable, and deployable on your
  own infrastructure.*
- **Boilerplate (≈50 words) `‹confirm›`:** *ONDEWO is a conversational-AI company
  that automates phone calls. Its modular platform — speech-to-text, text-to-speech,
  dialogue, and telephony integration — lets enterprises answer every call, in any
  language, 24/7, while keeping full control of their data through on-premise
  deployment.*

## 7. Copy patterns (ready to reuse)

**Headline formulas**
- `[Outcome], [time/scale qualifier].` → "Answer every call, around the clock."
- `[Old pain], [retired].` → "Hold music, retired."
- `[Verb] [object] — [differentiator].` → "Automate your hotline — in 30 languages."

**CTAs:** "Talk to sales" · "Book a demo" · "Read the docs" · "Start building" ·
"See it in action". (Sentence case, no period, verb-first.)

> When generating copy, draft 3 options and prefer the shortest one that keeps the
> benefit. Run it past §5 before finalising.
