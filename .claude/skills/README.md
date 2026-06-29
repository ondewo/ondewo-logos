# ONDEWO Brand Skills

Reusable skills that let any AI coding agent produce on-brand ONDEWO material
without re-learning the brand each time. Each skill loads the `brand-kit/`
guidelines and tokens, then does its job. The marketing skills **compose** the base
skills (they reuse `create-brand-asset` for visuals and `brand-check` for QA) and
emit documents through the engines defined in
[`brand-kit/document-templates/PLAN.md`](../../brand-kit/document-templates/PLAN.md).

## Base skills (foundation)

| Skill | Trigger | Use it to… |
|-------|---------|-----------|
| **create-brand-asset** | "design / make / generate a … for ONDEWO" | Produce a finished visual asset (social post, banner, slide, web hero, card, signature, letterhead, favicon, badge). |
| **brand-check** | "is this on-brand?" / "review / audit this" | Audit a design, page, screenshot, or copy and report violations + fixes. |
| **brand-copy** | "write ONDEWO copy / headline / tagline" | Write or rewrite text in ONDEWO's voice. |

## Marketing-material skills

The 14 most important company marketing materials, covered by 11 focused skills:

| Skill | Materials covered | Priority |
|-------|-------------------|----------|
| **slide-deck** | Company Presentation / Pitch Deck · Sales Deck · Webinar deck (`mode: pitch\|company\|sales\|webinar`) | ⭐⭐⭐⭐⭐ / ⭐⭐⭐⭐ |
| **one-pager** | Product/Service One-Pager · Corporate Brochure (`mode: product\|service\|company-brochure`) | ⭐⭐⭐⭐⭐ / ⭐⭐⭐⭐ |
| **case-study** | Case Study / Success Story · Customer Testimonial (`mode: case-study\|testimonial`) | ⭐⭐⭐⭐⭐ |
| **explainer-video** | Explainer Video — script, VO, storyboard, shot list, style frames | ⭐⭐⭐⭐ |
| **blog-article** | Blog & Knowledge / SEO Articles | ⭐⭐⭐⭐ |
| **marketing-email** | Email Templates & nurture sequences (cold, nurture, newsletter, announcement, invite, follow-up) | ⭐⭐⭐⭐ |
| **social-media-kit** | Social Media Assets — multi-platform post sets, captions, calendar | ⭐⭐⭐⭐ |
| **whitepaper** | Whitepapers / eBooks (lead-gen long-form) | ⭐⭐⭐ |
| **infographic** | Infographics (data-driven SVG) | ⭐⭐⭐ |
| **press-kit** | Press Kit — release, fact sheet, bios, boilerplate, media index | ⭐⭐⭐ |
| **webinar-kit** | Webinar Materials — orchestrates social + email + landing + deck + recap | ⭐⭐⭐ |

## How an agent uses these
1. The user asks for branded work.
2. The matching skill activates (by description) and reads the relevant
   `brand-kit/*.md`, `brand-kit/tokens/`, and (for documents)
   `brand-kit/document-templates/PLAN.md`.
3. It produces the asset/copy/document using the official logo and tokens, then
   verifies (render + checklist) before delivering to `brand-kit/generated/`.

## Relationship to the rest of the kit
- **Skills** = the *how-to* for an agent (this folder).
- **brand-kit/** = the *source of truth* (guidelines, tokens, templates, assets).
- **brand-kit/document-templates/PLAN.md** = how to emit Office/Google/PDF documents.
- **Workflows** (`.claude/workflows/`) = orchestrate skills across many assets.
- **CLAUDE.md** (repo root) = the entry point that ties it all together.

These skills are also usable outside this repo: point an agent at the repo URL and
it can read `CLAUDE.md` → `brand-kit/` and follow the same process even without the
skills installed.
