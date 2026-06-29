# ONDEWO Document Template System — Plan

> Single, implementation-ready plan for `brand-kit/document-templates/`. It defines how ONDEWO produces on-brand letters, offers, decks, reports, and spreadsheets — in Office, Google Workspace, and print/PDF — from one source of truth.
>
> **Ground truth (read these, never invent values):** `/Users/arath/ondewo/ondewo-logos/CLAUDE.md`, `brand-kit/README.md`, `brand-kit/color-system.md`, `brand-kit/typography.md`, `brand-kit/logo-guidelines.md`, `brand-kit/layout-and-spacing.md`, `brand-kit/voice-and-tone.md`, `brand-kit/accessibility.md`, `brand-kit/tokens/ondewo.tokens.json`, `brand-kit/templates/`, `brand-kit/assets/logo/`.
>
> **Brand constants (verified):** name **ONDEWO** (all-caps), tagline *"We automate your phone calls."*, Blue `#004C87`, Magenta `#BE216B` (accent ≤10%), Ink `#231F20`, neutral-50 `#F7F8FA`, type **Futura PT → Jost** (free web/embeddable fallback). The swirl logo lives in `brand-kit/assets/logo/` (horizontal lockup `viewBox="26.2 26.5 543.4 130.1"` ≈ 4.18:1; mark `viewBox="30 30 157 123"`). Generated output always lands in `brand-kit/generated/`; never overwrite `templates/`, `assets/`, or source logos. **Never redraw the swirl, recolour it, or place blue-on-magenta / magenta-on-blue text (contrast 1.52 — fails).**

---

## 1. Overview & goals

**Core principle — author once, render to many.** Every document is written as **Markdown + a YAML/JSON data file**, never directly in PowerPoint/Word/Excel/Slides. A build step pushes that single source through an **engine matrix** to produce PDF, PPTX, DOCX, XLSX, and Google formats. The brand never lives in the document — it lives in `brand-kit/tokens/ondewo.tokens.json` and is injected by per-engine *binding* files generated from those tokens.

```
                         ┌─────────────────────────────────────────────┐
  ondewo.tokens.json ──► │  build/generate-bindings.py (token → engine) │
   (single source of     └─────────────────────────────────────────────┘
    brand truth)              │        │         │        │        │
                              ▼        ▼         ▼        ▼        ▼
                          print.css  brand_   ondewo   ref.docx  brand.gs
   content.md  ─────┐       (PDF)   colors.py .marp.css +ref.pptx (Apps
   data.yaml/json ──┼─► [ ENGINE MATRIX ]      (Marp)             Script)
   assets/logo/ ────┘        │        │         │        │        │
                              ▼        ▼         ▼        ▼        ▼
                            PDF      PPTX      Slides    DOCX     Google
                                              + PDF      XLSX     Slides/Docs/Sheets
```

**Goals**

1. **Single-source → multi-format.** One `content.md` (+ structured data) renders to every required format; numbers/copy never diverge between a PDF offer and its XLSX pricing model because both read the same `items[]`.
2. **On-brand by default.** Colours, fonts, spacing, logo, and table/chart styling come only from tokens via generated bindings — an author cannot accidentally ship off-palette output. Magenta stays ≤10% structurally.
3. **Editable by humans and agents.** Everything is plain text / open format inside `brand-kit/`, so a non-Claude agent pointed at the repo can run `make` without the skills installed.
4. **Faithful, not invented.** The swirl is always embedded from the official SVGs; the digital-canonical hex (`#004C87` / `#BE216B`) is used in code, never the print-only guideline hex (`#014C89` / `#BF206B`).

Two hard rules carry through every engine: **(1)** colours, fonts, and spacing come only from tokens; **(2)** the swirl is embedded from `brand-kit/assets/logo/` and never redrawn.

---

## 2. Scope

In scope — the deliverables this system produces, with their primary engine:

| Deliverable | Format(s) | Primary engine |
|---|---|---|
| **Business letter / cover letter** (EN/DE, DIN 5008) | PDF + editable DOCX | WeasyPrint (PDF) · Pandoc `--reference-doc` (DOCX) |
| **Offer / quote / proposal** (line items, VAT, acceptance) | PDF + DOCX + XLSX | WeasyPrint · docxtpl · openpyxl (live formulas) |
| **Slide deck** (pitch, all-hands, board) | PPTX + PDF + Google Slides | Marp (fast) · python-pptx (pixel-exact) · Apps Script |
| **One-pager / datasheet** | PDF | Pandoc → WeasyPrint |
| **Editable report / whitepaper** | DOCX + PDF | Pandoc `--reference-doc` · Pandoc → XeLaTeX |
| **Spreadsheet / pricing model / data** | XLSX + Google Sheets | openpyxl · Apps Script / gspread |
| **Google Slides / Docs / Sheets** (live, shareable) | native Google files | Apps Script (clasp) + Drive import |
| **PowerPoint / Word / Excel** templates | `.potx` / `.dotx` / `.xltx` + `.pptx`/`.docx`/`.xlsx` | python-pptx / python-docx / openpyxl + hand-authored OOXML shells |

Out of scope (owned by the existing `create-brand-asset` skill): static social/banner/slide-card graphics (SVG → PNG) and web hero/email HTML. See §10.

---

## 3. Architecture

### 3.1 The single-source pipeline

The brand never lives in a document; it lives in tokens and is injected per engine. `build/generate-bindings.py` reads `ondewo.tokens.json` and emits one binding file per engine into `document-templates/shared/`. Change a hex once, regenerate, every format updates — this is what makes the system single-source.

```python
# build/generate-bindings.py  (sketch — the single-source step)
import json
T = json.load(open("brand-kit/tokens/ondewo.tokens.json"))
BR = T["color"]["brand"]
blue, magenta, ink = BR["blue"]["$value"], BR["magenta"]["$value"], BR["ink"]["$value"]

def hexrgb(h): return f"RGBColor(0x{h[1:3]}, 0x{h[3:5]}, 0x{h[5:7]})"
open("brand-kit/document-templates/shared/brand_colors.py", "w").write(
f'''# GENERATED from ondewo.tokens.json — do not edit
from pptx.dml.color import RGBColor
BLUE    = {hexrgb(blue)}      # {blue}
MAGENTA = {hexrgb(magenta)}   # {magenta}  accent <=10%
INK     = {hexrgb(ink)}       # {ink}
WHITE   = RGBColor(0xFF,0xFF,0xFF)
FONT_DISPLAY = "Jost"   # Futura PT only where licensed/installed (internal print)
FONT_BODY    = "Jost"
''')
# also emits: shared/themes/ondewo.marp.css + ondewo-print.css (re-export tokens as CSS vars),
#             shared/theme/ondewo-theme.xml (OOXML), google/brand.gs constants
```

Engines then *import* the binding, never literal hex. `make bindings` is the single-source gate — CI runs `make bindings && git diff --exit-code shared/` to fail if bindings drifted from tokens.

### 3.2 Document type → engine matrix

| Document type | Source format | Primary engine | Fallback / alt | Brand binding used |
|---|---|---|---|---|
| **Slide deck (pitch, all-hands)** | Markdown (Marp flavour) | **Marp CLI** → PPTX + PDF | `slide-title.svg` → PNG → python-pptx | `shared/themes/ondewo.marp.css` |
| **Pixel-perfect deck (sales/board)** | Markdown + YAML | **python-pptx** (from `reference.pptx`) | Marp for speed | `shared/brand_colors.py` + `reference.pptx` |
| **One-pager / datasheet** | Markdown + YAML | **Pandoc → HTML → WeasyPrint PDF** | Marp 1-slide PDF | `shared/themes/ondewo-print.css` |
| **Letter / cover letter** | Markdown + YAML | **Pandoc → WeasyPrint PDF** | `letterhead.html` → headless Chrome | `ondewo-print.css` (letterhead frame) |
| **Offer / quote / proposal** | Markdown + line-items YAML | **WeasyPrint PDF** (+ totals table) | docxtpl if client needs editable | `ondewo-print.css` + `brand_docx.py` |
| **Editable report (Word)** | Markdown | **Pandoc → DOCX** (`--reference-doc`) | python-docx for programmatic | `shared/reference.docx` |
| **Long report / whitepaper (PDF)** | Markdown | **Pandoc → XeLaTeX PDF** | WeasyPrint for HTML-styled | `shared/ondewo.latex` + `ondewo.sty` |
| **Spreadsheet / pricing model** | CSV/JSON/YAML | **openpyxl** | Google Sheets via Apps Script | `shared/brand_xlsx.py` |
| **Invoice / structured form** | JSON data | **WeasyPrint** (template) or openpyxl | python-docx | `ondewo-print.css` |
| **Google Slides / Docs / Sheets** | Markdown/JSON | **Apps Script + clasp** | Drive import of PPTX/DOCX/XLSX | `google/Brand.gs` |
| **PowerPoint / Word / Excel template** | data + shell | **python-{pptx,docx} / openpyxl** | hand-authored `.potx/.dotx/.xltx` | `shared/theme/ondewo-theme.xml` |

**Engine selection in one line:** *needs slides → Marp (fast) or python-pptx (exact); fixed-layout PDF → Pandoc+WeasyPrint (HTML/CSS) or Pandoc+XeLaTeX (long-form); client-editable Office file → Pandoc with a reference doc, or python-{docx,pptx,openpyxl} when generated from data; live collaborative doc → Apps Script.*

---

## 4. Brand-token → engine mapping (reference tables)

All hex values are the **digital-canonical artwork values**; never substitute the print-only guideline hex (`#014C89` / `#BF206B`) in code.

### 4.0 Canonical token values (ground truth every engine maps from)

| Token | Hex | RGB | Role |
|---|---|---|---|
| `color.brand.blue` | `#004C87` | 0,76,135 | Primary / structure / OOXML `accent1` |
| `color.brand.magenta` | `#BE216B` | 190,33,107 | Accent only ≤10% / `accent2` / focus ring |
| `color.brand.ink` | `#231F20` | 35,31,32 | Body text, mono-black logo |
| `color.brand.white` | `#FFFFFF` | 255,255,255 | Primary background |

- **Blue scale** (50→900): `#EBF1F5 #D6E2EC #A8C2D6 #739DBD #3873A1 #004C87 #004071 #00345C #002644 #001A2E`
- **Magenta scale**: `#FAEDF3 #F5DBE7 #E9B4CD #DB85AE #CC528C #BE216B #A01C5A #811649 #5F1036 #410B24`
- **Neutral scale** (0→900): `#FFFFFF #F7F8FA #E5E4E6 #C7C5C9 #A4A2A8 #7E7A83 #5A5560 #4C4751 #3D3A41 #2D2A30 #231F20`
- **Semantic**: success `#1E7A4B` · warning `#B5710A` · error `#C02626` · info `#004C87`
- **Gradient (brand)**: `linear-gradient(135deg, #BE216B 0%, #004C87 100%)`; subtle: `linear-gradient(135deg, #FAEDF3 0%, #EBF1F5 100%)`
- **Balance rule**: 60% neutral · 30% blue · **10% magenta accent (hard cap)**.

### 4.1 Colours → each engine

**The canonical OOXML 12-slot theme color scheme** (used identically by PowerPoint, Word, and Excel — they all carry `theme1.xml`). OOXML stores hex **uppercase, no `#`**:

| Theme slot | Token | Hex | Notes |
|---|---|---|---|
| `dk1` (Text 1) | ink | `231F20` | default text |
| `lt1` (Bg 1) | white | `FFFFFF` | default background |
| `dk2` (Text 2) | blue 500 | `004C87` | heading / dark accent |
| `lt2` (Bg 2) | neutral 50 | `F7F8FA` | subtle surface |
| **`accent1`** | blue 500 | `004C87` | primary |
| **`accent2`** | magenta 500 | `BE216B` | accent — use sparingly |
| **`accent3`** | blue 400 | `3873A1` | chart series 2 |
| **`accent4`** | blue 300 | `739DBD` | chart series 3 |
| **`accent5`** | magenta 300 | `DB85AE` | light accent / dark-bg accent |
| **`accent6`** | neutral 500 | `5A5560` | neutral series |
| `hlink` | blue 500 | `004C87` | hyperlinks stay blue |
| `folHlink` | blue 700 | `00345C` | visited links |

```xml
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="ONDEWO">
 <a:themeElements>
  <a:clrScheme name="ONDEWO">
   <a:dk1><a:srgbClr val="231F20"/></a:dk1>   <!-- Text 1  = Ink      -->
   <a:lt1><a:srgbClr val="FFFFFF"/></a:lt1>   <!-- Bg 1    = White     -->
   <a:dk2><a:srgbClr val="004C87"/></a:dk2>   <!-- Text 2  = Blue      -->
   <a:lt2><a:srgbClr val="F7F8FA"/></a:lt2>   <!-- Bg 2    = neutral-50 -->
   <a:accent1><a:srgbClr val="004C87"/></a:accent1>  <!-- Blue (primary) -->
   <a:accent2><a:srgbClr val="BE216B"/></a:accent2>  <!-- Magenta (≤10%) -->
   <a:accent3><a:srgbClr val="3873A1"/></a:accent3>  <!-- blue-400 -->
   <a:accent4><a:srgbClr val="739DBD"/></a:accent4>  <!-- blue-300 -->
   <a:accent5><a:srgbClr val="DB85AE"/></a:accent5>  <!-- magenta-300 -->
   <a:accent6><a:srgbClr val="5A5560"/></a:accent6>  <!-- neutral-500 -->
   <a:hlink><a:srgbClr val="004C87"/></a:hlink>
   <a:folHlink><a:srgbClr val="00345C"/></a:folHlink>
  </a:clrScheme>
  <a:fontScheme name="ONDEWO">
   <a:majorFont><a:latin typeface="Jost"/><a:ea typeface=""/><a:cs typeface=""/></a:majorFont>
   <a:minorFont><a:latin typeface="Jost"/><a:ea typeface=""/><a:cs typeface=""/></a:minorFont>
  </a:fontScheme>
  <a:fmtScheme name="ONDEWO"><!-- keep Office default fill/line/effect/bg styles --></a:fmtScheme>
 </a:themeElements>
</a:theme>
```

> **Caution:** `accent2`=magenta means Office auto-colours the *second* chart series magenta. Charts are blue-led — override the series order so magenta only marks the key series (see §4.5). Keep the default `clrMap` on the master (`bg1=lt1, tx1=dk1, bg2=lt2, tx2=dk2`). **Never** style runs as accent1-on-accent2 (blue-on-magenta fails contrast 1.52).

This canonical theme is stored once at `shared/theme/ondewo-theme.xml`; PPT/Word/Excel shells all reference it. Per-engine specifics:

**Word — styles** (`.docx` carries the same `theme1.xml`; styles reference hard hex):

| Word style | Token | Hex | Word XML |
|---|---|---|---|
| Normal (body) | ink | `231F20` | `<w:color w:val="231F20"/>` |
| Title / Heading 1 / 2 | blue 500 | `004C87` | `<w:color w:val="004C87"/>` |
| Heading 3 / 4 | ink | `231F20` | — |
| Subtitle / Caption | neutral 500 | `5A5560` | — |
| Intense Emphasis / eyebrow | magenta 500 | `BE216B` | character style |
| Hyperlink | blue 500 | `004C87` | — |
| Table header shading | blue 500 | `004C87` (white text) | `<w:shd w:val="clear" w:color="auto" w:fill="004C87"/>` |
| Table banding | neutral 50 | `F7F8FA` | — |
| Table border | neutral 100 | `E5E4E6` | — |

**Excel — ARGB** = `FF` + RGB (opaque). openpyxl: `PatternFill("solid", fgColor="004C87")`, `Font(color="FFFFFF", bold=True)`:

| Use | Token | ARGB |
|---|---|---|
| Table header fill | blue 500 | `FF004C87` (font `FFFFFFFF` bold) |
| Zebra odd / even | neutral 50 / white | `FFF7F8FA` / `FFFFFFFF` |
| Total / subtotal | blue 50 | `FFEBF1F5` (font ink bold) |
| KPI highlight | magenta 50 | `FFFAEDF3` (font `FFBE216B`) |
| Cell / table border | neutral 100 | `FFE5E4E6` |
| Body / muted text | ink / neutral 500 | `FF231F20` / `FF5A5560` |
| Cond-fmt good / warn / bad | success / warning / error | `FF1E7A4B` / `FFB5710A` / `FFC02626` |

**Google Apps Script — CSS-hex constants** (define once, reuse in `Brand.gs`; full scales in §5.2):
`range.setBackground('#004C87').setFontColor('#FFFFFF')`; Slides `shape.getFill().setSolidFill('#004C87')`.

**Pandoc / Marp — CSS custom properties:** reuse the shipped `brand-kit/tokens/ondewo.css` verbatim (`@import url('../tokens/ondewo.css')`) → every `--ondewo-*` var. Pandoc HTML: `pandoc -c brand-kit/tokens/ondewo.css …`.

**LaTeX — `xcolor`:**
```latex
\usepackage[table]{xcolor}
\definecolor{ondewoBlue}{HTML}{004C87}
\definecolor{ondewoMagenta}{HTML}{BE216B}
\definecolor{ondewoInk}{HTML}{231F20}
\definecolor{blue400}{HTML}{3873A1}\definecolor{blue300}{HTML}{739DBD}\definecolor{blue700}{HTML}{00345C}
\definecolor{neutral50}{HTML}{F7F8FA}\definecolor{neutral100}{HTML}{E5E4E6}\definecolor{neutral500}{HTML}{5A5560}
% beamer:
\setbeamercolor{frametitle}{fg=ondewoBlue}\setbeamercolor{structure}{fg=ondewoBlue}
\setbeamercolor{alerted text}{fg=ondewoMagenta}  % the ≤10% accent
\hypersetup{colorlinks=true, linkcolor=ondewoBlue, urlcolor=ondewoBlue}
```

> Use the explicit 50–900 scales for fills/borders — do **not** rely on OOXML `lumMod/lumOff` auto-tints, which drift off-palette.

### 4.2 Typography → each engine

Canonical stacks: display `"Futura PT", "Futura LT Pro", Futura, "Jost", "Century Gothic", "Trebuchet MS", system-ui, sans-serif`; body `"Futura PT", "Jost", "Century Gothic", system-ui, …`; mono `"JetBrains Mono", …`.

| Engine | On-brand 1st | Portable substitute | Ultimate fallback | How set |
|---|---|---|---|---|
| PowerPoint / Word / Excel | **Jost** (default for shared files)¹ | Century Gothic (ships with Office) | Calibri | theme `majorFont/minorFont` latin = single name |
| Google Slides/Docs/Sheets | **Jost** (in Google Fonts) | Century Gothic | Arial | `setFontFamily('Jost')` |
| Marp / Pandoc-HTML | Futura PT if licensed, else **Jost** | Century Gothic | system-ui | CSS `--ondewo-font-display/body` |
| LaTeX (XeLaTeX + `fontspec`) | Futura PT if installed, else **Jost** | TeX Gyre Adventor (free geometric) | Latin Modern Sans | `\setmainfont{Jost}` |

> ¹ **Licensing (brand rule 5):** Futura PT/LT Pro are commercial (Adobe/Linotype). Never embed Futura or ship its files in generated `.pptx/.docx/.xlsx`, web, OSS, or email. The theme default for shared/generated files is **Jost** (geometric, OFL, embeddable). Set `Futura PT` only for internal print on machines that hold the license and have it installed. OOXML themes have **no multi-font fallback list** — set both the theme and the run/style font and rely on Office substitution. **Excel has no font embedding in the file format at all** — rely on Jost-installed-or-Century-Gothic.

**Type scale → engine units** (1px = 0.75pt; slides read larger):

| Token | px | Doc pt (Word/LaTeX/PDF) | Slide pt (PPT/Google) | Weight | Role |
|---|---|---|---|---|---|
| `5xl` | 61 | 46 | 40 | 300 / 700 | Hero |
| `4xl` | 49 | 37 | 36 | 700 | Title / H1 |
| `3xl` | 39 | 29 | 28 | 700 | Section H2 |
| `2xl` | 31 | 23 | 24 | 500/700 | H3 / large stat |
| `xl` | 25 | 19 | 20 | 500 | H4 / lead |
| `lg` | 20 | 15 | 18 | 500 | sub-head |
| `base` | 16 | 12 | 18 (slide min) | 400 | Body |
| `sm` | 14 | 10.5 | 14 | 400/500 | Caption |
| `xs` | 12 | 9 | 12 | 400 | Legal / fine print |

Line-heights: display `1.1` · headings `1.25` · body `1.5` · long-form `1.7`. Weights 300/400/500/700. **Headlines sentence case** (not Title Case); `ONDEWO` always all-caps in prose.

**All-caps tracking (`letterSpacing.wider = 0.12em`) per engine:**

| Engine | Setting | Value |
|---|---|---|
| CSS / Marp / HTML | `letter-spacing` | `0.12em` (`var(--ondewo-tracking-wider)`) |
| PowerPoint (DrawingML) | run `spc` (1/100 pt) | `spc = round(0.12 × sizePt × 100)` → 18pt caps = `spc="216"` |
| Word (`styles.xml`) | `<w:spacing w:val>` (1/20 pt) | `val = round(0.12 × sizePt × 20)` → 12pt caps = `val="29"` |
| Google Apps Script | — | **No letter-spacing API** — keep caps short; rely on weight/colour (flag, don't fake) |
| Excel | — | No tracking control — uppercase + bold only |
| LaTeX | `microtype` `\textls` (1/1000 em) | `\textls[120]{ONDEWO}` |

### 4.3 Logo → each engine (never redraw — embed the official asset)

| Engine | Default (colour, light bg) | On dark / blue / photo | Format rule |
|---|---|---|---|
| Web / Marp / Pandoc-HTML | `ondewo-logo-horizontal.svg` | `ondewo-logo-horizontal-mono-white.svg` | **SVG** |
| PowerPoint / Word / Excel | **PNG @2x** of horizontal lockup | mono-white PNG@2x | **PNG @2x** (Office SVG support is inconsistent across versions/platforms) |
| Google Slides/Docs/Sheets | hosted **PNG @2x** via `insertImage(url)` | mono-white PNG@2x | **PNG @2x** (`insertImage` rejects SVG) |
| LaTeX | vector PDF/EPS via `\includegraphics` | mono variant on dark | **vector PDF/EPS** |

- **Rasterise once:** `rsvg-convert -w 1024 brand-kit/assets/logo/ondewo-logo-horizontal.svg -o ondewo-logo@2x.png` (or `qlmanage -t -s 1024 -o ./out …`, or CairoSVG — see §5.1). Render at ≥300 dpi for print docs. Mono-white PNG must come from `ondewo-logo-horizontal-mono-white.svg` (there is no white PNG in the repo).
- **Placement:** top-left in the clear-space margin (or centred for hero/title slides). **Clear space `X = ½ the height of the "O"`**; keep ≥X (ideally ≥2X) from canvas edges. Min size **24px tall digital / 5mm print**; below 24px use the mark-only SVG.
- **Colourway:** full-colour on white/very-light only; **mono-white on `#004C87`/dark/photo**; mono-black/ink for one-colour. Never recolour, stretch, rotate, shadow, or box. `alt="ONDEWO"`; decorative watermark `alt=""`/`aria-hidden`.

### 4.4 Spacing & tables

**Spacing** — base unit 4px; `space-1…10` = 4,8,12,16,24,32,48,64,96,128 px. Slides (16:9, 1920×1080): outer margin 96px, gutter 48px, 12-col. Word/LaTeX A4: margin 12–20mm. Web/Marp: section 64px desktop / 48px mobile, content max 1200–1280px. Whitespace is part of the brand — when in doubt, add space.

**Table styling (constant across engines):** header fill blue `#004C87` + white bold; zebra band neutral-50 `#F7F8FA` alternating with white; 1px borders neutral-100 `#E5E4E6`; body ink; optional total row blue-50 `#EBF1F5`; magenta only to flag a single key cell or as a total rule.
```css
th{background:var(--ondewo-blue);color:#fff;font-weight:700;padding:.5rem .75rem}
td{padding:.5rem .75rem;border:1px solid var(--ondewo-border);color:var(--ondewo-text)}
tbody tr:nth-child(odd){background:var(--ondewo-neutral-50)}
```

### 4.5 Chart palette order

**Lead with the blue scale; reserve magenta for the single most important series.** Categorical order: `#004C87` (blue 500) → `#3873A1` (blue 400) → `#739DBD` (blue 300) → `#A8C2D6` (blue 200) → `#BE216B` (**magenta 500 — the key series**, move it onto whichever series matters most) → `#5A5560` (neutral 500). Sequential: blue 100→900. Always pair colour with labels/patterns; magenta ≤10% of ink. In Office, override the auto `accent2`=magenta default so series-2 isn't magenta.

### 4.6 Compliance quick-check (all engines)

- [ ] Only token hex; magenta ≤10% of the surface; digital uses `#004C87`/`#BE216B` not `#014C89`/`#BF206B`.
- [ ] Type uses Jost (web/OSS/email/shared Office) → Century Gothic → Calibri; headlines sentence-case; `ONDEWO` all-caps +0.12em.
- [ ] Logo is an **embedded official asset** (SVG web/vector, PNG@2x Office/Google), correct variant, full clear space (≥X), ≥24px/5mm.
- [ ] Tables = blue header + neutral-50 zebra + neutral-100 borders; charts blue-led, magenta only on the key series.
- [ ] AA pairs only: ink-on-white **16.3**, white-on-blue **8.81**, white-on-magenta **5.80**; **never** blue-on-magenta / magenta-on-blue (**1.52** — fails).

---

## 5. Per-format approach

### 5.1 Office / OOXML branch (PowerPoint, Word, Excel)

**Recommended pattern — "branded shell + thin code generator" hybrid:**

1. **Author the brand shell once** as a real OOXML template (`.potx`/`.dotx`/`.xltx`) carrying the ONDEWO theme (`theme1.xml` from §4.1), slide masters/layouts (PPT), named styles (Word/Excel), header/footer logo, and optionally embedded Jost. This captures what the Python libs can't model well.
2. **Drive content with the libraries** — they *open the shell* and pour in data, inheriting the theme.

| Format | Primary engine | Does well | Push to the shell |
|---|---|---|---|
| **PowerPoint** | **python-pptx** | slides from layouts, text, pictures, tables, native charts; 16:9; theme colours via `MSO_THEME_COLOR` | masters/layouts, `fmtScheme`, font embedding (no theme API — patch XML) |
| **Word** | **python-docx** / **Pandoc `--reference-doc`** | runs/paragraphs, headings, tables, header/footer images, sections | document theme XML, font embedding, content controls |
| **Excel** | **openpyxl** | `NamedStyle` cells, fills, number/conditional formats, images, charts, freeze/auto-filter | full theme swap (limited), font embedding (not supported by format) |

**Prefer hand-authored `.potx/.dotx/.xltx`** when humans open *File ▸ New from template* and edit in Office (masters, layouts, theme colour picker, gallery styles, embedded fonts). **Prefer pure code** when generation is automated/server-side and the output won't be hand-edited. In practice: **commit the shells, generate content with code.** The canonical `shared/theme/ondewo-theme.xml` is the single source all three shells share.

**Local tooling reality (verified on this machine, 2026-06-29):**
```
Python 3.13.12 · python-pptx 1.0.2 ✅ · CairoSVG 2.9.0 ✅ (SVG→PNG, pure-Python) · Pillow 12.2.0 ✅ · lxml 6.1.1 ✅
python-docx ❌  -> pip install python-docx
openpyxl    ❌  -> pip install openpyxl
fonttools   ❌  -> pip install fonttools   (only if you embed/subset Jost)
pandoc      ❌  -> brew install pandoc      (only for the Word/Pandoc route)
Jost font   ❌  -> download OFL TTFs into shared/fonts/Jost/
```

**Logo: SVG → PNG via CairoSVG** (works today). `shared/logo.py`:
```python
import cairosvg
from pathlib import Path
ASSETS   = Path(__file__).resolve().parents[1] / "assets/logo"
LOGO_SVG = Path(__file__).resolve().parents[3] / "assets/logo"   # brand-kit/assets/logo

def render_logo(name="ondewo-logo-horizontal", target_in=1.6, dpi=300):
    out = ASSETS / f"{name}@2x.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(url=str(LOGO_SVG / f"{name}.svg"), write_to=str(out),
                     output_width=int(target_in * dpi))   # alpha preserved
    return out
```
Build PNGs once: full-colour for light headers, `…-mono-white` for blue/dark bands, `ondewo-mark` for watermark/Excel corner. Preserve aspect from `viewBox="26.2 26.5 543.4 130.1"` (≈4.18:1). Slide size 16:9 = `Inches(13.333) × Inches(7.5)` (1920×1080 at 144 dpi). Master carries: thin blue top rule with a ~⅓-width magenta segment, logo top-left, footer `ONDEWO · We automate your phone calls. · ondewo.com`.

**Office branch folder layout:**
```
brand-kit/document-templates/office/
├── README.md  · requirements.txt
├── shared/    -> reuses ../shared (tokens.py, theme_ooxml.py, logo.py, fonts.py)
├── powerpoint/ build_pptx_template.py · seed/ondewo-seed.pptx (16:9 shell) · out/
├── word/       build_docx_template.py · reference.docx (Pandoc) · out/
└── excel/      build_xlsx_template.py · out/
```

**PowerPoint — `powerpoint/build_pptx_template.py`** (theme-patch fallback when there's no seed shell):
```python
import json
from pathlib import Path
from lxml import etree
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from shared.logo import render_logo

BK  = Path(__file__).resolve().parents[3]
T   = json.loads((BK / "tokens/ondewo.tokens.json").read_text())
HEX = lambda p: T["color"]["brand"][p]["$value"].lstrip("#")
BLUE, MAGENTA, INK = HEX("blue"), HEX("magenta"), HEX("ink")   # 004C87 / BE216B / 231F20
A = "http://schemas.openxmlformats.org/drawingml/2006/main"; q = lambda t: f"{{{A}}}{t}"

def apply_ondewo_theme(prs):
    """Patch theme1.xml in place (python-pptx has no theme API)."""
    part = prs.slide_masters[0].part.part_related_by(RT.THEME)
    root = etree.fromstring(part.blob)
    clr  = root.find(f".//{q('clrScheme')}")
    slots = {"dk1": INK, "lt1": "FFFFFF", "dk2": BLUE, "lt2": "F7F8FA",
             "accent1": BLUE, "accent2": MAGENTA, "accent3": "3873A1",
             "accent4": "739DBD", "accent5": "DB85AE", "accent6": "5A5560",
             "hlink": BLUE, "folHlink": "00345C"}      # canonical scheme, §4.1
    for slot, val in slots.items():
        node = clr.find(q(slot)); node.clear()
        etree.SubElement(node, q("srgbClr")).set("val", val)
    for role in ("majorFont", "minorFont"):
        root.find(f".//{q(role)}/{q('latin')}").set("typeface", "Jost")
    part._blob = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)

prs = Presentation()                       # or Presentation("seed/ondewo-seed.pptx")
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)   # 16:9
apply_ondewo_theme(prs)
s = prs.slides.add_slide(prs.slide_layouts[6])                    # blank
bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Pt(9))
bar.fill.solid(); bar.fill.fore_color.rgb = RGBColor.from_string(BLUE); bar.line.fill.background()
seg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(4.44), Pt(9))
seg.fill.solid(); seg.fill.fore_color.rgb = RGBColor.from_string(MAGENTA); seg.line.fill.background()
s.shapes.add_picture(str(render_logo()), Inches(0.667), Inches(0.6), height=Inches(0.5))
tb = s.shapes.add_textbox(Inches(0.667), Inches(3.1), Inches(11), Inches(1.6))
r = tb.text_frame.paragraphs[0].add_run(); r.text = "Presentation title"
r.font.name = "Jost"; r.font.size = Pt(54); r.font.bold = True; r.font.color.rgb = RGBColor.from_string(BLUE)
Path("out").mkdir(exist_ok=True); prs.save("out/ondewo-deck.pptx")
```

**Word — `word/build_docx_template.py`:**
```python
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.oxml.ns import qn
from shared.logo import render_logo
BLUE = RGBColor(0x00,0x4C,0x87); MAGENTA = RGBColor(0xBE,0x21,0x6B); INK = RGBColor(0x23,0x1F,0x20)

def set_font(style, name="Jost"):            # make the font name stick (ascii+hAnsi)
    style.font.name = name
    rpr = style.element.get_or_add_rPr(); rpr.get_or_add_rFonts()
    rpr.rFonts.set(qn("w:ascii"), name); rpr.rFonts.set(qn("w:hAnsi"), name)

doc = Document()
n  = doc.styles["Normal"];    set_font(n);  n.font.size = Pt(11); n.font.color.rgb = INK
h1 = doc.styles["Heading 1"]; set_font(h1); h1.font.size = Pt(22); h1.font.bold = True; h1.font.color.rgb = BLUE
h2 = doc.styles["Heading 2"]; set_font(h2); h2.font.size = Pt(16); h2.font.bold = True; h2.font.color.rgb = MAGENTA
doc.sections[0].header.paragraphs[0].add_run().add_picture(str(render_logo(target_in=1.4)), height=Inches(0.28))
doc.add_heading("Document title", level=1); doc.add_paragraph("We automate your phone calls.")
Path("out").mkdir(exist_ok=True); doc.save("reference.docx"); doc.save("out/ondewo-doc.docx")
```
Pandoc route: `pandoc report.md -o out/report.docx --reference-doc=word/reference.docx`. For the Word colour-picker palette, swap `word/theme/theme1.xml` in the `.docx`/`.dotx` zip with `shared/theme/ondewo-theme.xml`; `styles.xml` colours alone already deliver visible branding.

**Excel — `excel/build_xlsx_template.py`:**
```python
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import NamedStyle, Font, PatternFill, Alignment, Side, Border
from openpyxl.drawing.image import Image as XLImage
from shared.logo import render_logo
BLUE, MAGENTA, INK, SUBTLE = "FF004C87", "FFBE216B", "FF231F20", "FFF7F8FA"

wb = Workbook(); ws = wb.active; ws.title = "ONDEWO"
hdr = NamedStyle("ondewo_header")
hdr.font = Font(name="Jost", bold=True, color="FFFFFFFF", size=11)
hdr.fill = PatternFill("solid", fgColor=BLUE)
hdr.alignment = Alignment(horizontal="left", vertical="center")
hdr.border = Border(bottom=Side(style="medium", color=MAGENTA))    # magenta accent rule
body = NamedStyle("ondewo_body"); body.font = Font(name="Jost", color=INK, size=11)
pct  = NamedStyle("ondewo_pct");  pct.font = Font(name="Jost", color=INK); pct.number_format = "0.0%"
eur  = NamedStyle("ondewo_eur");  eur.font = Font(name="Jost", color=INK); eur.number_format = '#,##0.00" €"'
for s in (hdr, body, pct, eur): wb.add_named_style(s)
ws.merge_cells("A1:F1"); ws.row_dimensions[1].height = 30
ws["A1"] = "Quarterly report"; ws["A1"].style = "ondewo_header"
img = XLImage(str(render_logo(target_in=1.2))); img.height, img.width = 22, 92; ws.add_image(img, "H1")
for col, head in zip("ABCDEF", ["Metric","Q1","Q2","Q3","Q4","Total"]):
    ws[f"{col}3"] = head; ws[f"{col}3"].style = "ondewo_header"
ws.freeze_panes = "A4"; ws.auto_filter.ref = "A3:F3"
Path("out").mkdir(exist_ok=True); wb.save("out/ondewo-workbook.xlsx")   # or .xltx
```
Excel theme colours can be added by replacing `xl/theme/theme1.xml` in the saved zip with the canonical theme; explicit `PatternFill`s + `NamedStyle`s already give correct branding regardless.

**Build & verify:**
```bash
cd brand-kit/document-templates/office
python -m pip install -r requirements.txt   # python-pptx present; adds docx/openpyxl/cairosvg/fonttools
python -m shared.logo                        # (optional) pre-render logo PNGs
python -m powerpoint.build_pptx_template
python -m word.build_docx_template
python -m excel.build_xlsx_template
```
Open each output in Office (or LibreOffice) and confirm the theme colour picker shows the ONDEWO accents and the logo is crisp.

### 5.2 Google Workspace branch (Slides, Docs, Sheets)

**Honest constraint:** Google files are server-side, not on-disk diff-able sources. This branch ships the three things that *can* live in git and reproduce a branded Google file:

| Track | What | Best for | Lives in git as |
|---|---|---|---|
| **A — Apps Script brand library** (primary) | `.gs` that generates/themes Slides/Docs/Sheets from `BRAND` constants | repeatable on-brand generation; "ONDEWO Brand" menu; bulk/automated | `google/*.gs` + `appsscript.json` |
| **B — Office import** | upload §5.1 `.pptx/.docx/.xlsx`; Drive auto-converts to native | pixel-faithful masters humans tweak | references `office/` |
| **C — Shared Drive + gallery** | master Google files surfaced via `/copy` links + org gallery | non-technical staff: click → Make a copy | `share-links.md` registry |

Two baked-in constraints: **logos must be PNG** (`insertImage` rejects SVG → host rasterised PNGs), and **the Workspace font is Jost** (Futura PT is not in Google's web-font catalogue; `setFontFamily('Jost')` renders for every viewer).

**Branch folder layout:**
```
brand-kit/document-templates/google/
├── README.md · appsscript.json · .clasp.json.example
├── Brand.gs   (BRAND constants from tokens, hosted logo URLs, helpers)
├── Slides.gs  (createBrandedTitleSlide, themePresentation)
├── Docs.gs    (buildBrandedLetterhead, themeDocument)
├── Sheets.gs  (themeSpreadsheet, newBrandedReport)
├── Menu.gs    (onOpen/onInstall "ONDEWO Brand" editor menu)
└── share-links.md  (master file IDs + /copy links + gallery status)
```

**`Brand.gs` — the reusable Brand object** (mirrors tokens; a CI check, below, keeps it in sync):
```javascript
const BRAND = {
  color: {
    blue:'#004C87', magenta:'#BE216B', ink:'#231F20', white:'#FFFFFF',
    bgSubtle:'#F7F8FA', border:'#E5E4E6', textMuted:'#5A5560',
    blue700:'#00345C', blue900:'#001A2E', magenta300:'#DB85AE'
  },
  font: { display:'Jost', body:'Jost', mono:'Roboto Mono' },   // Jost is in the Google Fonts picker
  size: { title:40, h1:22, h2:17, lead:17, body:11, eyebrow:9, caption:8.5 },
  logo: {  // PNG exports of the official SVGs (SVG is NOT accepted by insertImage)
    fullColor:'https://raw.githubusercontent.com/ondewo/ondewo-logos/main/brand-kit/assets/logo/png/ondewo-logo-horizontal.png',
    monoWhite:'https://raw.githubusercontent.com/ondewo/ondewo-logos/main/brand-kit/assets/logo/png/ondewo-logo-horizontal-mono-white.png',
    watermark:'https://raw.githubusercontent.com/ondewo/ondewo-logos/main/brand-kit/assets/logo/png/ondewo-mark-watermark.png',
    aspect: 4.18   // width/height of the horizontal lockup (viewBox 543.4/130.1)
  },
  tagline:'We automate your phone calls.', company:'ONDEWO GmbH', url:'ondewo.com'
};
function logoBlob_(url){ return UrlFetchApp.fetch(url).getBlob(); }
```

**`Slides.gs` — branded 16:9 title slide:**
```javascript
function createBrandedTitleSlide(title, subtitle, presenter) {
  title=title||'Presentation title'; subtitle=subtitle||'Subtitle'; presenter=presenter||'Presenter · Role · 2026';
  const deck = SlidesApp.create('ONDEWO — ' + title);
  const W=720, slide=deck.getSlides()[0];                 // 16:9 = 720×405 pt
  slide.getPageElements().forEach(el => el.remove());
  slide.insertImage(BRAND.logo.watermark, 470, 150, 240, 240).sendToBack();
  bar_(slide,0,0,W,6,BRAND.color.blue); bar_(slide,0,0,240,6,BRAND.color.magenta);   // blue bar + magenta accent
  slide.insertImage(BRAND.logo.fullColor, 52, 40, 150, 150/BRAND.logo.aspect);
  bar_(slide,52,150,36,5,BRAND.color.magenta);            // magenta eyebrow
  textBox_(slide,title,52,166,600,90,BRAND.size.title,true,BRAND.color.blue);
  textBox_(slide,subtitle,52,252,600,44,BRAND.size.lead,false,BRAND.color.ink);
  textBox_(slide,presenter,52,366,420,24,BRAND.size.body,false,BRAND.color.textMuted);
  const right=textBox_(slide,BRAND.url,420,366,248,24,BRAND.size.body,false,BRAND.color.textMuted);
  right.getText().getParagraphStyle().setParagraphAlignment(SlidesApp.ParagraphAlignment.END);
  return deck.getUrl();
}
function bar_(s,x,y,w,h,hex){ const r=s.insertShape(SlidesApp.ShapeType.RECTANGLE,x,y,w,h);
  r.getFill().setSolidFill(hex); r.getBorder().setTransparent(); return r; }
function textBox_(s,str,x,y,w,h,pt,bold,hex){ const b=s.insertTextBox(str,x,y,w,h);
  b.getText().getTextStyle().setFontFamily(BRAND.font.display).setForegroundColor(hex).setBold(!!bold).setFontSize(pt); return b; }
```

**`Docs.gs`** builds an A4 letterhead: borderless 2-col table (logo left + company meta right), a thin blue brand rule (a 2pt single-cell table — Docs has no full-bleed shapes), eyebrow (magenta) → H1 (blue) → body (Jost 11pt ink) → footer (tagline · company · url). **`Sheets.gs`** `themeSpreadsheet()` applies a blue header row + neutral banding + Jost + frozen header + blue tab via `applyRowBanding` / `setHeaderRowColor('#004C87')` / `setSecondRowColor('#F7F8FA')`. **`Menu.gs`** detects the host and adds an "ONDEWO Brand" menu (`onOpen`/`onInstall`).

**`appsscript.json`** declares scopes (`presentations`, `documents`, `spreadsheets`, `drive`, `script.external_request`) and the `addOns.common` block for an internal Editor Add-on.

**Logo hosting** — export PNGs from the official SVGs (run from repo root):
```bash
mkdir -p brand-kit/assets/logo/png
for f in ondewo-logo-horizontal ondewo-logo-horizontal-mono-white ondewo-mark; do
  rsvg-convert -w 1200 -a -f png "brand-kit/assets/logo/$f.svg" -o "brand-kit/assets/logo/png/$f.png"
done
# pre-faded ~5% swirl watermark:
rsvg-convert -w 1200 brand-kit/assets/logo/ondewo-mark.svg -o /tmp/mark.png
magick /tmp/mark.png -channel A -evaluate multiply 0.05 +channel brand-kit/assets/logo/png/ondewo-mark-watermark.png
```
No `rsvg-convert`? `qlmanage -t -s 1200 -o /tmp/out brand-kit/assets/logo/ondewo-logo-horizontal.svg`. Then set `BRAND.logo.aspect` to the real export `width/height`.

**Deploy (clasp):**
```bash
npm i -g @google/clasp && clasp login
cd brand-kit/document-templates/google
clasp create --type standalone --title "ONDEWO Brand Library"   # writes .clasp.json (gitignore; commit .example)
clasp push                                                       # uploads *.gs + appsscript.json
clasp open                                                       # authorise scopes, run createBrandedTitleSlide once
```
Domain-wide menu: publish as an **internal Editor Add-on** (Marketplace SDK, same `appsscript.json` `addOns` + `onInstall`), restricted to the ONDEWO org.

**Track B (import):** build masters in `office/`, upload to the shared Drive, *Open with → Google Slides/Docs/Sheets*; re-apply **Jost** (Office Futura substitutes on conversion) or run the Track-A theming functions; verify blue/magenta bars survived and magenta ≤10%.

**Publish & share:** Shared Drive `ONDEWO Templates` (Slides/Docs/Sheets subfolders, *Anyone in ONDEWO – Viewer*); **"Make a copy" URLs** (swap trailing `/edit` → `/copy` so recipients get a copy, never the master) recorded in `share-links.md`; **org custom template gallery** (Submit template → [ONDEWO] tab, governed in Admin console → Drive and Docs → Templates).

**Keep tokens in sync (CI guard):**
```bash
for hex in 004C87 BE216B 231F20 F7F8FA E5E4E6 5A5560 00345C; do
  grep -qi "$hex" brand-kit/document-templates/google/Brand.gs \
    || { echo "Brand.gs out of sync: #$hex"; exit 1; }
done
```

**Limitations to state plainly:** no editable native source in git (only generators + import masters + link registry); SVG not accepted (host PNGs; cache a Drive copy as fallback); **no letter-spacing API** (the +0.12em all-caps tracking can't be set programmatically — flag, don't fake); **no full-bleed shapes in Docs** (the blue bar is a thin background-coloured table); **gradients aren't native** (the magenta→blue band must be a pre-rendered PNG); magenta discipline is on the author + reviewer.

### 5.3 Letters & Offers branch

A single-source system for ONDEWO business letters and offers/quotes/proposals. One canonical `.md` (YAML front-matter + Markdown body) renders to print-ready PDF and editable DOCX; offer pricing is tied to a shared XLSX/Sheets engine driven from the same `items[]` JSON. It extends `brand-kit/templates/letterhead.html` and references only `brand-kit/tokens/ondewo.css`.

```
source.md (YAML front-matter + body) ──► HTML (Jinja2 + ondewo.css) ──► WeasyPrint ──► PDF (print)
                                     ├──► Pandoc --reference-doc ──────────────────► DOCX (letters)
                                     ├──► docxtpl (Jinja-in-Word) ─────────────────► DOCX (offers w/ tables)
                                     └──items[]──► openpyxl ───────────────────────► XLSX (live VAT/total formulas)
                                                 └─ gspread / CSV import ──────────► Google Sheets
```

**Branch folder layout:**
```
brand-kit/document-templates/letters-offers/
├── README.md · build.py · Makefile
├── shared/  ondewo-doc.css (@page A4, imports ../../tokens/ondewo.css) · partials/ · ondewo-reference.docx
│            · fonts/Jost/ · legal.yml (single source of <confirm> legal facts)
├── letter/  letter.html.j2 · letter.example.{en,de}.md · i18n/{en,de}.yml
├── offer/   offer.html.j2 · offer.docx.j2 · offer.schema.json · offer.example.en.md · i18n/{en,de}.yml
└── pricing/ build_xlsx.py · push_sheets.py · pricing.example.json
```
**Naming** (output → `brand-kit/generated/`): `ondewo-letter_<recipient>_<yyyy-mm-dd>_<lang>.{pdf,docx}`, `ondewo-offer_<account>_<quote-no>_<yyyy-mm-dd>_<lang>.{pdf,docx,xlsx}`; `quote-no` = `Q-<yyyy>-<nnnn>`.

**Single-source front-matter** (`letter.example.en.md` — same keys drive PDF/DOCX/XLSX):
```markdown
---
doc_type: letter            # letter | offer
lang: en                    # en | de  -> i18n labels + locale date/number
date: 2026-06-29            # ISO; EN "29 June 2026" / DE "29.06.2026"
reference: "OND-2026-0612"
sender:    { name: "Jane Doe", title: "Head of Sales", email: "jane.doe@ondewo.com" }
recipient: { company: "ACME GmbH", attn: "Mr John Smith", street: "Musterstraße 1",
             postcode_city: "1010 Wien", country: "Austria" }
subject: "Proposal for automated inbound call handling"
salutation: "Dear Mr Smith,"
sign_off: "Kind regards,"
enclosures: ["Offer Q-2026-0142", "ONDEWO CAI datasheet"]
---
Thank you for your time on Tuesday. As discussed, ONDEWO can automate your inbound
hotline in three languages while keeping all audio on-premise.
```

**Letter structure** (DE follows DIN 5008): topbar (blue + magenta left segment) → sender/logo header → address window (DE: 45mm from top, left margin 25mm, window-envelope safe) → reference line → **subject bold with no "Betreff:" label** (DIN 5008) → salutation → body (11pt, 1.5) → sign-off + 16–20mm signature space + typed name → enclosures → legal footer.

`shared/ondewo-doc.css` (token-driven print CSS, abbreviated):
```css
@import url("../../tokens/ondewo.css");
@font-face{ font-family:"Jost"; src:url("fonts/Jost-Regular.ttf"); font-weight:400; }
@page { size:A4; margin:25mm 20mm 28mm 25mm; @bottom-center{ content:element(footer);} }   /* DIN 5008 left 25mm */
body{ font-family:var(--ondewo-font-body); color:var(--ondewo-text); font-size:11pt; line-height:1.5; }
.topbar{ position:fixed; top:0; left:0; right:0; height:8mm; background:var(--ondewo-blue); }
.topbar::before{ content:""; position:absolute; left:0; top:0; width:60mm; height:8mm; background:var(--ondewo-magenta); }
h1.subject{ font-family:var(--ondewo-font-display); font-weight:700; font-size:14pt; color:var(--ondewo-primary); }
.eyebrow{ text-transform:uppercase; letter-spacing:var(--ondewo-tracking-wider); color:var(--ondewo-accent); font-size:8.5pt; }
footer{ position:running(footer); border-top:1px solid var(--ondewo-border); font-size:7.5pt; color:var(--ondewo-text-muted); }
```
`letter/letter.html.j2` renders via Jinja2 (`t`=i18n dict, `d`=front-matter); the logo is `<img src="../../../assets/logo/ondewo-logo-horizontal.svg">`. **EN/DE switch the label dict + date/number locale only — never the template** (`dateloc` filter: `%d %B %Y` EN / `%d.%m.%Y` DE; DE labels e.g. `our_ref: "Unser Zeichen"`, `default_sign_off: "Mit freundlichen Grüßen"`).

**Offer structure:** cover (blue band or `--ondewo-gradient-brand-subtle` once; mono-white logo if on blue; eyebrow `OFFER`/`ANGEBOT`; title; account; quote no.; **valid until**) → intro → scope → deliverables → **line-item pricing table** → totals/VAT (reverse-charge note for intra-EU B2B) → terms & validity → two-column acceptance/signature. Pricing-table CSS uses blue header + neutral-50 zebra + **magenta strictly as the grand-total top rule** and one accent heading:
```css
.pricing thead th{ background:var(--ondewo-blue); color:#fff; font-weight:500; padding:6px 8px; }
.pricing tbody tr:nth-child(even){ background:var(--ondewo-neutral-50); }
.pricing tfoot .grand th,.pricing tfoot .grand td{ border-top:2px solid var(--ondewo-magenta);  /* the 10% accent */
  font-weight:700; color:var(--ondewo-primary); }
.acceptance h2{ color:var(--ondewo-accent); }
```

**Line-item schema (single source for PDF + XLSX)** — `pricing/pricing.example.json`; the same array is embedded in the offer front-matter (`items:`):
```json
{ "currency":"EUR", "lang":"en", "vat_mode":"net", "reverse_charge":false,
  "quote_no":"Q-2026-0142", "valid_until":"2026-07-31", "document_discount_pct":0,
  "items":[
    {"line_no":1,"sku":"OND-CAI-SETUP","name":"ONDEWO CAI — pilot setup","qty":1,"unit":"package","unit_price":18000.00,"discount_pct":0,"tax_rate":20},
    {"line_no":2,"sku":"OND-CAI-LIC-M","name":"ONDEWO CAI license (monthly)","qty":12,"unit":"month","unit_price":2500.00,"discount_pct":10,"tax_rate":20},
    {"line_no":3,"sku":"OND-PROF-DAY","name":"Professional services","qty":8,"unit":"day","unit_price":1200.00,"discount_pct":0,"tax_rate":20}
  ] }
```
Computation contract (one implementation in `build.py`, reused by all engines): `line_net = round(qty*unit_price*(1-discount_pct/100),2)`; `line_tax = round(line_net*tax_rate/100,2)`; `subtotal = sum(line_net)`; `tax_by_rate = {rate: sum(line_tax)}`; `grand_total = subtotal - doc_discount + sum(tax_by_rate)`. `offer.schema.json` (draft-2020-12) validates types/ranges and is run in `build.py` before render. HTML/DOCX write resolved values; **XLSX writes live formulas** so finance can tweak qty/price and totals recompute:
```python
# pricing/build_xlsx.py — branded workbook with live formulas
ws[f"I{r}"] = f"=D{r}*F{r}*(1-G{r}/100)"   # line_net
ws[f"J{r}"] = f"=I{r}*H{r}/100"            # line_tax
ws[f"I{r}"].number_format = EUR_DE if p["lang"]=="de" else EUR_EN   # '#.##0,00 €' / '#,##0.00 "€"'
# header fill 004C87 + white bold; zebra F7F8FA; grand total in BLUE with a magenta top-border rule
```
`push_sheets.py` pushes the same values + formula strings via gspread and applies header fill `#004C87` / total border `#BE216B`; a no-API path exports CSV → Import into a brand-styled Sheets template. The offer PDF/DOCX and the XLSX/Sheet are **two renderings of one `items[]`** — edit the JSON, rebuild, all stay in sync.

**Build commands:**
```bash
python build.py pdf  letter/letter.example.en.md    # -> brand-kit/generated/ondewo-letter_..._en.pdf
python build.py docx letter/letter.example.de.md    # pandoc --reference-doc=shared/ondewo-reference.docx
python build.py docx offer/offer.example.en.md       # docxtpl offer.docx.j2 (native Word tables)
python build.py xlsx pricing/pricing.example.json
make offer SRC=offer/offer.example.en.md             # pdf + docx + xlsx
```
Core of `build.py pdf`: `HTML(string=rendered, base_url=tmpl_dir).write_pdf(out_pdf)` (WeasyPrint, `@page A4`, embeds Jost; `money`/`dateloc` filters registered).

**Legal placeholders — `shared/legal.yml`** (one edit propagates to every footer/cover). **All values are `<confirm>` placeholders and must be verified before any document ships:**
```yaml
entity:        "ONDEWO GmbH"            # <confirm> exact legal name
postcode_city: "<confirm> 1010 Wien"     # <confirm> seat (AT vs DE)
vat:           "VAT/ATU: <confirm>"      # AT 'ATU########' or DE 'DE#########'
reg_no:        "FN <confirm>"            # AT Firmenbuchnummer / DE HRB
default_vat_rate: 20                     # <confirm> AT 20% / DE 19%
payment_terms:   "<confirm> 14 days net"
governing_law:   "<confirm> Austrian law, venue Vienna"
tagline:       "We automate your phone calls."   # confirmed brand fact
```
Render rule: if any field still contains `<confirm>`, `build.py` warns and (with `--strict`) refuses to emit a final PDF, so unverified legal data can't be sent.

---

## 6. Tooling & setup (install commands)

Probed on macOS: present = `node/npm/npx`, `python3/pip3`, `qlmanage`, plus (for the Office branch) python-pptx 1.0.2, CairoSVG 2.9.0, Pillow 12.2.0, lxml 6.1.1. Install the gaps:

```bash
# ── Homebrew base ───────────────────────────────────────────────
brew install pandoc            # Markdown → DOCX/PDF/HTML/LaTeX hub
brew install librsvg           # rsvg-convert: SVG → PNG/PDF (logo rasterisation)
brew install --cask libreoffice  # soffice headless: any-format → PDF safety net, PPTX→PDF
brew install tectonic          # self-contained XeLaTeX (no full MacTeX); fallback: brew install --cask mactex-no-gui
brew install pango gdk-pixbuf libffi   # WeasyPrint native deps

# ── PDF from HTML/CSS (token-driven; preferred over LaTeX for branded layouts) ──
pip install weasyprint

# ── Python Office engines (repo venv) ───────────────────────────
python3 -m venv .venv && source .venv/bin/activate
pip install python-pptx python-docx openpyxl cairosvg pillow pyyaml jinja2 markdown
pip install docxtpl gspread        # optional: editable-Word offers, Google Sheets push
pip install fonttools              # only if embedding/subsetting Jost

# ── Slides + HTML rendering ─────────────────────────────────────
npm i -g @marp-team/marp-cli                      # Markdown → HTML/PDF/PPTX with a CSS theme
npm i -g playwright && npx playwright install chromium   # HTML → PDF/PNG (web fonts, gradients)

# ── Google formats ──────────────────────────────────────────────
npm i -g @google/clasp && clasp login

# ── SVG quick-look already present on macOS ─────────────────────
# qlmanage -t -s 2000 -o ./out brand-kit/assets/logo/ondewo-logo-horizontal.svg
```

**Fonts:** install **Jost** for every render path lacking licensed Futura PT (`brew install --cask font-jost`, or have the build download the OFL TTFs into `shared/fonts/`). WeasyPrint, Marp-Chromium, LibreOffice, and LaTeX all need the font file present locally. **Public/web/shared output uses Jost, never embedded commercial Futura PT.**

Per-branch `requirements.txt` (Office branch): `python-pptx>=1.0`, `python-docx>=1.1`, `openpyxl>=3.1`, `cairosvg>=2.7`, `Pillow>=10`, `fonttools>=4.0` (embedding only).

---

## 7. Folder structure

Proposed tree to **create** at `brand-kit/document-templates/` (it does not exist yet). Generated bindings carry a header comment `# GENERATED from ondewo.tokens.json — do not edit`. Rendered output always goes to `brand-kit/generated/`; `templates/` and `assets/` are never overwritten.

```
brand-kit/document-templates/
├── README.md                      ← index + "which engine for what" (mirrors §3.2)
│
├── shared/                        ← cross-engine brand bindings (generated + curated)
│   ├── brand_colors.py            ← GENERATED from tokens (RGBColor consts, font names)
│   ├── tokens.py                  ← loads ../../tokens/ondewo.tokens.json -> hex/RGB
│   ├── theme_ooxml.py             ← build/patch clrScheme + fontScheme XML (all OOXML engines)
│   ├── logo.py                    ← CairoSVG SVG->PNG rasteriser + on-disk cache
│   ├── fonts.py                   ← font-name resolution; optional fonttools embed/subset
│   ├── brand_pptx.py · brand_docx.py · brand_xlsx.py   ← per-engine helpers/NamedStyles
│   ├── theme/ondewo-theme.xml     ← canonical <a:theme> (single source for PPT/Word/Excel shells)
│   ├── reference.docx · reference.pptx                 ← Pandoc / python-pptx masters
│   ├── themes/                    ← ondewo.marp.css · ondewo-print.css · ondewo.latex · ondewo.sty
│   ├── partials/                  ← header-logo.html · footer.html (reused HTML)
│   ├── assets/logo/               ← built PNG artefacts (committed): *@2x.png, mono-white, mark
│   └── fonts/Jost/                ← Jost-*.ttf (OFL) for install/embedding
│
├── build/                         ← engine layer (NO brand values live here)
│   ├── Makefile                   ← top-level targets (§9 / below)
│   ├── generate-bindings.py       ← tokens → shared/* (the single-source step)
│   ├── render_pdf.py · render_pptx.py · render_docx.py · render_xlsx.py
│   ├── verify_brand.py            ← contrast / logo / magenta-share checks
│   └── lib/logo.py                ← load official SVG, rasterise to sized PNG
│
├── office/                        ← PPTX/DOCX/XLSX (§5.1): powerpoint/ word/ excel/ + out/
├── letters-offers/                ← business correspondence (§5.3): letter/ offer/ pricing/ shared/
└── google/                        ← Apps Script (§5.2): Brand/Slides/Docs/Sheets/Menu.gs + appsscript.json
```

**Naming conventions:** folders `kebab-case`, type-led (`deck-pitch/`, `offer-quote/`); source content `content.md` (prose), `data.yaml`/`items.yaml` (structured), `meta.yaml` (title/author/date/lang); output `ondewo-<doctype>-<slug>-<YYYYMMDD>.<ext>` (e.g. `ondewo-offer-acme-voicebot-20260629.pdf`).

**Build layer — `build/Makefile` concept** (thin orchestration; all brand values arrive via `shared/`):
```makefile
TOKENS := ../../tokens/ondewo.tokens.json
OUT    := ../../generated
SHARED := ../shared
bindings:        ## tokens -> per-engine bindings (run first / on token change)
	python3 generate-bindings.py $(TOKENS) $(SHARED)
deck-marp: bindings
	marp ../office/deck-pitch/content.md --theme $(SHARED)/themes/ondewo.marp.css --pptx -o $(OUT)/ondewo-deck-$(SLUG).pptx
one-pager: bindings
	pandoc ../office/one-pager/content.md -t html5 | weasyprint - $(OUT)/ondewo-onepager-$(SLUG).pdf -s $(SHARED)/themes/ondewo-print.css
letter offer: bindings ; python3 render_pdf.py --kind $@ --src ../letters-offers/$@ --out $(OUT)
report: bindings ; pandoc ../office/report-word/content.md --reference-doc $(SHARED)/reference.docx -o $(OUT)/ondewo-report-$(SLUG).docx
xlsx: bindings ; python3 render_xlsx.py --src ../office/pricing-sheet/data.yaml --out $(OUT)
google: bindings ; cd ../google && clasp push
verify: ; python3 verify_brand.py $(OUT)
```
`make bindings` is the single-source gate; CI runs `make bindings && git diff --exit-code shared/` to fail if bindings drifted.

---

## 8. Agent decision tree (which engine/template for a requested doc)

```
REQUEST: "make a <document> for ONDEWO"
│
├─ 0. ALWAYS load brand context first:
│     CLAUDE.md → brand-kit/README.md → the relevant spec(s)
│     (color-system / typography / logo-guidelines / layout / voice / accessibility)
│     → tokens/ondewo.tokens.json. (Reuse the create-brand-asset skill's "load" step.)
│
├─ 1. What is the OUTPUT artifact?
│   ├─ Slides ──────────► pixel-exact / client-supplied master?
│   │                       ├─ no  → MARP   (content.md + ondewo.marp.css)      → PPTX+PDF
│   │                       └─ yes → python-pptx from shared/reference.pptx (seed shell)
│   ├─ Fixed PDF (1–4 pp) ► one-pager / letter / offer
│   │                       → Pandoc → ondewo-print.css → WeasyPrint
│   ├─ Long PDF (report) ─► Pandoc → XeLaTeX (ondewo.latex + ondewo.sty)
│   ├─ Editable Word ─────► Pandoc --reference-doc=shared/reference.docx → DOCX
│   ├─ Spreadsheet ───────► openpyxl + shared/brand_xlsx.py (header band, blue totals, live formulas)
│   ├─ Live Google file ──► Apps Script (Brand.gs) via clasp  OR  Drive-import the rendered PPTX/DOCX/XLSX
│   └─ Static graphic ────► existing templates/*.svg → qlmanage/rsvg (owned by create-brand-asset, §10)
│
├─ 2. CONTENT: write/Q copy per voice-and-tone.md (sentence-case headlines,
│        ONDEWO all-caps, benefit-led). Put structured data (line items, stats,
│        contacts) in data.yaml — never inline in the engine.
│
├─ 3. BRAND TOKENS: import the generated binding for that engine
│        (brand_colors.py / ondewo-print.css / ondewo.marp.css / Brand.gs).
│        Logo = embed official SVG (lockup on light; mono-white on blue/photo; PNG@2x for Office/Google).
│        Magenta ≤10%: exactly one accent (a CTA, one stat, the top-bar block, a total rule).
│        60/30/10 neutral/blue/magenta. Never blue-on-magenta text.
│
├─ 4. BUILD:  make <target>   (or call the render/ script directly)
│
└─ 5. VERIFY → render to PNG/PDF, run layout-and-spacing.md §8 + accessibility pairs,
         confirm logo clear space + correct variant, then save to
         brand-kit/generated/ (never overwrite templates/ or assets/).
```

---

## 9. Implementation roadmap (P0/P1/P2)

### P0 — Must-have (single source proven end-to-end)
**Scope:** the tokens→bindings generator; `shared/` (brand_colors.py, ondewo-print.css, ondewo.marp.css, reference.docx, reference.pptx, logo.py, theme/ondewo-theme.xml); three engines live — **Marp deck**, **WeasyPrint one-pager/letter**, **Pandoc DOCX**; Makefile targets `bindings deck-marp one-pager letter report`.
**Acceptance criteria:**
- `make bindings` regenerates `shared/*` purely from `ondewo.tokens.json`; no hex/font literal exists outside tokens (grep proves it).
- A one-pager and a pitch deck render from a single `content.md` with **zero** off-palette colours and the **official** logo embedded (not redrawn).
- Output passes the `layout-and-spacing.md §8` checklist and `accessibility.md` contrast pairs; magenta ≤10% surface.
- Files land in `brand-kit/generated/` with the naming convention; `templates/` and `assets/` untouched.

### P1 — Should-have (Office fidelity + data docs)
**Scope:** **python-pptx** exact decks from `reference.pptx`; **openpyxl** pricing/data sheets; **offer/quote** with totals table + terms + the line-item schema; XeLaTeX long-report path; the OOXML `.potx/.dotx/.xltx` shells; `verify_brand.py` automated checks (logo present, magenta-share, contrast, font names).
**Acceptance criteria:**
- A board deck generated by python-pptx is visually equal to the reference master (title, footer logo, blue headings) and opens cleanly in PowerPoint + Google Slides.
- An offer PDF computes line-item totals from `items.yaml`/`pricing.json`, shows the blue/magenta top-bar frame, and the single accent is the total rule or CTA; PDF totals match the XLSX live-formula totals.
- `make verify` blocks any artifact that uses a non-token colour or a recoloured/missing logo.

### P2 — Nice-to-have (live Google + automation + skill wiring)
**Scope:** **Google Apps Script** (`Brand.gs` + clasp) building Slides/Docs/Sheets directly, plus Drive-import fallback and the shared-Drive `/copy`-link + gallery distribution; CI job (`make bindings && verify`); a new **`create-brand-document`** skill (sibling to `create-brand-asset`) that runs the decision tree; optional watch/rebuild.
**Acceptance criteria:**
- `clasp push` produces a branded Google Slides deck from the same `content.md`/`data.yaml` (or Drive-imports the rendered PPTX) with correct colours and embedded logo.
- The skill, given "make an offer for Acme," selects the engine via §8, generates in-voice copy, renders, verifies, and saves to `generated/` with no human brand input.
- CI fails the PR if `shared/` bindings are stale vs. tokens, or if `Brand.gs` drifts from token hex.

---

## 10. How this connects to the marketing-material skills

This system is the **rendering backend** the existing skills call — it does not replace them, it gives them deterministic, on-brand engines. Everything stays inside `brand-kit/`, plain-text and open-format, so a non-Claude agent pointed at the repo can still run `make` without the skills installed.

- **`create-brand-asset`** keeps owning *static graphics* — social/banner/slide-card SVG → `qlmanage`/`rsvg`, web hero HTML → Playwright — exactly as today. Its "load brand context" step (CLAUDE.md → brand-kit → tokens) is reused verbatim as **step 0** of the document decision tree (§8).
- A new **`create-brand-document`** skill (P2) handles *multi-page / multi-format* deliverables (decks, one-pagers, letters, offers, reports, sheets) by walking §8 and invoking `make <target>`. A "one-pager" becomes editable Markdown that also exports DOCX/PDF; a "deck" exports PPTX + PDF + Google Slides from one source.
- **`brand-copy`** feeds `content.md` / front-matter (voice-and-tone rules unchanged: clear over clever, sentence-case headlines, `ONDEWO` all-caps).
- **`brand-check`** becomes `make verify` / `verify_brand.py` — the same checklist (logo clear space, ≤10% magenta, AA contrast, token-only colours) now runs automatically on every rendered artifact and can audit `brand-kit/generated/` in bulk via the existing `brand-audit` workflow.

**Key absolute paths:** source of truth `/Users/arath/ondewo/ondewo-logos/brand-kit/tokens/ondewo.tokens.json` (+ `ondewo.css`); logos `/Users/arath/ondewo/ondewo-logos/brand-kit/assets/logo/`; render patterns to reuse `/Users/arath/ondewo/ondewo-logos/.claude/skills/create-brand-asset/SKILL.md` and `/Users/arath/ondewo/ondewo-logos/brand-kit/templates/letterhead.html`; **new system root to create** `/Users/arath/ondewo/ondewo-logos/brand-kit/document-templates/`.