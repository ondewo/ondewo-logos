# ONDEWO Brand Skills

Reusable skills that let any AI coding agent produce on-brand ONDEWO material
without re-learning the brand each time. Each skill loads the `brand-kit/`
guidelines and tokens, then does its job.

| Skill | Trigger | Use it to… |
|-------|---------|-----------|
| **create-brand-asset** | "design / make / generate a … for ONDEWO" | Produce a finished asset (social post, banner, slide, web hero, card, signature, letterhead, favicon, badge). |
| **brand-check** | "is this on-brand?" / "review / audit this" | Audit a design, page, screenshot, or copy and report violations + fixes. |
| **brand-copy** | "write ONDEWO copy / headline / tagline" | Write or rewrite text in ONDEWO's voice. |

## How an agent uses these
1. The user asks for branded work.
2. The matching skill activates (by description) and reads the relevant
   `brand-kit/*.md` + `brand-kit/tokens/`.
3. It produces the asset/copy/report using the official logo and tokens, then
   verifies (render + checklist) before delivering.

## Relationship to the rest of the kit
- **Skills** = the *how-to* for an agent (this folder).
- **brand-kit/** = the *source of truth* (guidelines, tokens, templates, assets).
- **Workflows** (`.claude/workflows/`) = orchestrate skills across many assets.
- **CLAUDE.md** (repo root) = the entry point that ties it all together.

These skills are also usable outside this repo: point an agent at the repo URL and
it can read `CLAUDE.md` → `brand-kit/` and follow the same process even without the
skills installed.
