# ONDEWO Document Templates

Branded **document** generation — letters, offers/quotes, slide decks, reports,
one-pagers, and spreadsheets — across **Office** (PowerPoint, Word, Excel),
**Google Workspace** (Slides, Docs, Sheets), and **print/PDF**.

> **Status: plan / blueprint.** [`PLAN.md`](PLAN.md) is the implementation-ready
> design. The generator scripts and theme files it describes (`office/`, `google/`,
> `letters-offers/`, `shared/`, `build/`) are scaffolded as the plan is executed.

## Read this first
**[`PLAN.md`](PLAN.md)** — the full system: single-source → multi-format pipeline,
the document-type → engine matrix, the brand-token → engine mapping (exact hex
slots, OOXML theme, fonts), per-format approach with code, tooling/setup, folder
structure, an agent decision tree, and a P0/P1/P2 roadmap.

## The idea in one line
Author each document once as **Markdown + a data file**; a build step renders it to
every format, with the brand injected from
[`../tokens/ondewo.tokens.json`](../tokens/ondewo.tokens.json) — so a PDF offer and
its XLSX pricing model can never drift, and nothing ships off-palette.

## How it connects
The marketing-material skills (`slide-deck`, `one-pager`, `whitepaper`, …) use these
engines to emit PPTX / Google Slides / DOCX / PDF / XLSX. See
[`.claude/skills/`](../../.claude/skills/).
