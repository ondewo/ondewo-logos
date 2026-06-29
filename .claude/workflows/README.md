# ONDEWO Brand Workflows

Multi-agent workflow scripts that orchestrate branded production at scale. They run
on the Claude Code `Workflow` tool (deterministic fan-out over the brand skills).

> Workflows spawn multiple agents and consume tokens — they run only when the user
> explicitly opts in (e.g. "run the campaign-kit workflow" or via the `ultracode`
> keyword). A single asset doesn't need a workflow — just use the
> `create-brand-asset` skill.

| Workflow | What it does | Example args |
|----------|--------------|--------------|
| `campaign-kit.js` | From one message, generates copy + a full asset set (social post, banner, slide, landing hero) in parallel, then brand-checks each. | `{ "message": "Launching ONDEWO S2T v2", "theme": "brand", "assets": ["social-post","linkedin-banner","slide"] }` |
| `brand-audit.js` | Audits many files/a repo against the brand guidelines in parallel and returns a prioritised compliance report. | `{ "glob": "marketing site HTML/SVG" }` or `{ "files": ["site/index.html","deck.svg"] }` |

## Run

```text
# In Claude Code, with explicit opt-in:
Run the campaign-kit workflow with message "We answer every call, 24/7" theme brand
```

The agent invokes:
```js
Workflow({ name: "campaign-kit", args: { message: "We answer every call, 24/7", theme: "brand" } })
```

## How they stay on-brand
Every agent step invokes the brand **skills** (`create-brand-asset`, `brand-check`,
`brand-copy`), which load the `brand-kit/` guidelines and tokens. The workflows just
decide *what* to make and *in what order*; the skills enforce *how*.

## Extending
Copy a script, adjust `meta` + the asset list, and keep each agent step pointed at a
brand skill so quality is enforced. Use `pipeline()` (default) so each asset is
brand-checked the moment it's produced; use `parallel()` only when you need all
results before the next step.
