#!/usr/bin/env python3
"""Generate the ONDEWO Logo & Identity Guideline PDF.

Single source of truth: the design tokens (brand-kit/tokens/ondewo.tokens.json)
and the logo SVGs (brand-kit/assets/logo/). Contrast ratios are computed, not
hard-coded. HTML is rendered to an A4 PDF with headless Chrome/Chromium.

Usage:
    python3 scripts/build_guideline.py                 # -> brand-kit/generated/
    python3 scripts/build_guideline.py --html-only     # write the HTML, skip PDF
    python3 scripts/build_guideline.py -o some/file.pdf

The official Adobe InDesign PDF in the repo root is the 2019 source of truth and
is never overwritten unless you pass it explicitly via --output.

Requires: Python 3.8+ (stdlib only) and google-chrome / chromium on PATH.
Fonts: Jost (open licence, Futura-style) is downloaded once into
scripts/.cache/fonts and embedded; without network the PDF falls back to
Century Gothic / system sans.
"""
from __future__ import annotations

import argparse
import base64
import datetime
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / "brand-kit"
LOGO = KIT / "assets" / "logo"
VERTICAL_SVG = ROOT / "ONDEWO_Logo_vertical_4c_2019" / "ONDEWO_Logo_4c_vertical_rgb_2019.svg"
TOKENS = KIT / "tokens" / "ondewo.tokens.json"
CACHE = ROOT / "scripts" / ".cache" / "fonts"
DEFAULT_OUT = KIT / "generated" / "ondewo_logo_identity_guideline.pdf"
FONT_URL = "https://cdn.jsdelivr.net/npm/@fontsource/jost@5/files/jost-latin-{w}-normal.woff2"
FONT_WEIGHTS = (300, 400, 500, 700)

# Official print values from the 2019 guideline (its Pantone entries were blank).
PRINT = {
    "blue": {"cmyk": "100 / 75 / 15 / 0", "guideline_hex": "#014C89"},
    "magenta": {"cmyk": "25 / 100 / 35 / 0", "guideline_hex": "#BF206B"},
    "ink": {"cmyk": "0 / 0 / 0 / 100", "guideline_hex": "#000000"},
}


# ---------------------------------------------------------------- helpers ---
def esc(s: str) -> str:
    return html.escape(s, quote=True)


def val(token) -> str:
    return str(token["$value"] if isinstance(token, dict) else token)


def to_px(size: str) -> float:
    num = float(re.sub(r"[^0-9.]", "", size))
    return num * 16 if size.strip().endswith("rem") else num


def hex_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def luminance(h: str) -> float:
    def ch(c: int) -> float:
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (ch(c) for c in hex_rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(fg: str, bg: str) -> float:
    a, b = luminance(fg), luminance(bg)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


def verdict(ratio: float) -> tuple[str, str]:
    if ratio >= 7:
        return "AAA", "ok"
    if ratio >= 4.5:
        return "AA", "ok"
    if ratio >= 3:
        return "Large text only", "warn"
    return "Fail", "bad"


def svg_inner(path: Path) -> tuple[str, str]:
    """Return (viewBox, inner markup) of a clean ONDEWO logo SVG."""
    text = path.read_text(encoding="utf-8")
    vb = re.search(r'viewBox="([^"]+)"', text).group(1)
    inner = re.sub(r"</?svg[^>]*>|<title>.*?</title>", "", text, flags=re.S).strip()
    return vb, inner


def svg_logo(path: Path, height: str | None = None, width: str | None = None) -> str:
    vb, inner = svg_inner(path)
    size = (f'height="{height}" ' if height else "") + (f'width="{width}" ' if width else "")
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" {size}role="img" aria-label="ONDEWO">{inner}</svg>'


def img_data_uri(path: Path, mime: str) -> str:
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def font_face_css() -> str:
    """Embed Jost as base64 @font-face; silently falls back to system fonts offline."""
    CACHE.mkdir(parents=True, exist_ok=True)
    css = []
    for w in FONT_WEIGHTS:
        f = CACHE / f"jost-{w}.woff2"
        if not f.exists():
            try:
                with urllib.request.urlopen(FONT_URL.format(w=w), timeout=20) as r:
                    f.write_bytes(r.read())
            except Exception as exc:
                print(f"warning: could not fetch Jost {w}: {exc}", file=sys.stderr)
                continue
        b64 = base64.b64encode(f.read_bytes()).decode()
        css.append(
            f'@font-face{{font-family:"Jost";font-weight:{w};font-style:normal;'
            f'src:url(data:font/woff2;base64,{b64}) format("woff2");}}'
        )
    return "\n".join(css)


def find_chrome() -> str:
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"):
        p = shutil.which(name)
        if p:
            return p
    sys.exit("error: no Chrome/Chromium found on PATH (needed to render the PDF)")


def scale(tokens: dict, name: str) -> list[tuple[str, str]]:
    return [(k, val(v)) for k, v in tokens["color"][name].items() if isinstance(v, dict) and "$value" in v]


# ------------------------------------------------------------------ pages ---
def build_pages(t: dict) -> list[str]:
    pages: list[str] = []
    c = t["color"]
    blue, magenta, ink = (val(c["brand"][k]) for k in ("blue", "magenta", "ink"))
    n100, n50 = val(c["neutral"]["100"]), val(c["neutral"]["50"])
    year = datetime.date.today().year
    main_logo = LOGO / "ondewo-logo-horizontal.svg"
    white_logo = LOGO / "ondewo-logo-horizontal-mono-white.svg"
    black_logo = LOGO / "ondewo-logo-horizontal-mono-black.svg"
    mark = LOGO / "ondewo-mark.svg"

    def page(title: str, body: str) -> None:
        pages.append(
            f'<section class="page"><header class="ph"><span>{title}</span>{svg_logo(mark, height="9mm")}</header>'
            f'<div class="pb">{body}</div>'
            f'<footer class="pf"><span>ONDEWO Logo &amp; Identity Guideline</span><span class="pn"></span></footer></section>'
        )

    # ---- cover
    pages.append(
        f'''<section class="page cover">
  <div class="cover-top">{svg_logo(main_logo, height="20mm")}</div>
  <div class="cover-swirl">{svg_logo(mark, width="150mm")}</div>
  <div class="cover-mid">
    <p class="eyebrow">Brand &amp; design system</p>
    <h1>Logo &amp; identity<br>guideline</h1>
    <p class="lead">How to use the ONDEWO logo, colour, typography and layout &mdash; so every
    asset looks and sounds like ONDEWO.</p>
  </div>
  <div class="cover-foot"><span>We automate your phone calls.</span>
  <span>Version {esc(t["meta"]["version"])} &middot; {year}</span></div>
</section>'''
    )

    # ---- 1 brand foundation
    page(
        "1 &middot; Brand foundation",
        f'''
<h2>Who we are</h2>
<p class="lead">ONDEWO builds conversational AI that automates voice and phone interactions &mdash;
so organisations can answer every call, in any language, around the clock.</p>
<div class="grid2">
 <div class="card"><h3>Tagline</h3><p class="big">We automate your phone calls.</p>
  <p class="muted">Official. Use verbatim, in sentence case.</p></div>
 <div class="card"><h3>Positioning</h3><p>Voice-first, multilingual conversational AI that can be deployed
  <b>on-premise</b> for full data sovereignty.</p></div>
</div>
<h3>Personality</h3>
<table class="t"><tr><th>We are</th><th>We are not</th></tr>
<tr><td>Clear &amp; precise</td><td>Jargon-heavy or vague</td></tr>
<tr><td>Confident &amp; credible</td><td>Boastful or over-promising</td></tr>
<tr><td>Human &amp; approachable</td><td>Robotic or cold</td></tr>
<tr><td>Engineering-led</td><td>Buzzword-led</td></tr>
<tr><td>European, data-respecting</td><td>Careless with privacy</td></tr></table>
<h3>The idea behind the mark</h3>
<div class="row">
 <div>{svg_logo(mark, width="42mm")}</div>
 <ul class="tight">
  <li><b>Two voices in conversation</b> &mdash; magenta and blue flow into each other (caller &harr; AI).</li>
  <li><b>A sound wave</b> &mdash; motion, voice, signal.</li>
  <li><b>Continuity</b> &mdash; an endless loop that never drops a call.</li>
 </ul>
</div>
<h3>Voice in one line</h3>
<p>Clear over clever &middot; confident, never boastful &middot; human, never robotic. The name is always
written <b>ONDEWO</b> (all caps). Headlines and buttons use sentence case.</p>
''',
    )

    # ---- 2 logo system
    vert_uri = img_data_uri(VERTICAL_SVG, "image/svg+xml")
    page(
        "2 &middot; Logo system",
        f'''
<h2>Primary logo</h2>
<p>The horizontal lockup is the default logo. The two-tone swirl forms the &ldquo;O&rdquo; of the
wordmark. Use it almost everywhere: headers, documents, decks, footers.</p>
<div class="stage">{svg_logo(main_logo, width="130mm")}</div>
<div class="spec"><span class="tag">Minimum height</span>{svg_logo(main_logo, height="5mm")}
 <i>5&nbsp;mm print &middot; 24&nbsp;px digital</i></div>

<h2>Vertical logo</h2>
<div class="row">
 <div class="stage small"><img src="{vert_uri}" alt="ONDEWO vertical logo" style="height:42mm"></div>
 <div>
  <p>The vertical logo is the <b>secondary</b> logo. Use it only when the primary logo cannot be placed
  prominently enough &mdash; for example on narrow formats such as roll-ups or quick-screens.</p>
  <div class="spec"><span class="tag">Minimum height</span><i>10&nbsp;mm print &middot; 40&nbsp;px digital</i></div>
 </div>
</div>

<h2>Logomark</h2>
<div class="row">
 <div class="stage small">{svg_logo(mark, height="28mm")}</div>
 <div><p>The swirl alone is for app icons, avatars, favicons and watermarks &mdash; and only where the name
 ONDEWO already appears nearby. Below 24&nbsp;px logo height, switch to the mark.</p>
 <div class="spec"><span class="tag">Minimum size</span><i>16&nbsp;px (favicon)</i></div></div>
</div>
''',
    )

    # ---- 3 clear space + colourways
    x = 61.5  # X = half the height of the "O" (the swirl is ~123 units tall in the artwork)
    vx, vy, vw, vh = (float(n) for n in svg_inner(main_logo)[0].split())
    inner = svg_inner(main_logo)[1]
    mid_x, mid_y = vx + vw / 2, vy + vh / 2
    clear = (
        f'<svg viewBox="{vx - x} {vy - x} {vw + 2 * x} {vh + 2 * x}" class="cs" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="{vx - x}" y="{vy - x}" width="{vw + 2 * x}" height="{vh + 2 * x}" fill="{val(c["blue"]["50"])}"'
        f' stroke="{blue}" stroke-dasharray="6 5" stroke-width="1.5"/>'
        f'<rect x="{vx}" y="{vy}" width="{vw}" height="{vh}" fill="#fff"/>{inner}'
        f'<g font-family="Jost,sans-serif" font-size="26" font-weight="500" fill="{magenta}" text-anchor="middle">'
        f'<text x="{mid_x}" y="{vy - x / 2 + 9}">X</text><text x="{mid_x}" y="{vy + vh + x / 2 + 9}">X</text>'
        f'<text x="{vx - x / 2}" y="{mid_y + 9}">X</text><text x="{vx + vw + x / 2}" y="{mid_y + 9}">X</text></g></svg>'
    )
    page(
        "3 &middot; Clear space &amp; colourways",
        f'''
<h2>Clear space</h2>
<p>The shaded area must stay free of other elements &mdash; text, images and edges. The minimum
clear space is <b>X</b>, which equals <b>half the height of the &ldquo;O&rdquo;</b> in the logo.
More space is always safer. On canvases keep the logo at least X (ideally 2X) from the edge.</p>
<div class="stage">{clear}</div>

<h2>Colourways</h2>
<div class="grid3">
 <div class="cw bordered">{svg_logo(main_logo, width="48mm")}<p>Full colour<br><span>White or very light backgrounds &mdash; the default</span></p></div>
 <div class="cw" style="background:{blue};color:#fff">{svg_logo(white_logo, width="48mm")}<p>Mono white<br><span>Brand blue, dark or photographic backgrounds</span></p></div>
 <div class="cw bordered">{svg_logo(black_logo, width="48mm")}<p>One colour (ink)<br><span>When only one print colour is available</span></p></div>
</div>
<p class="muted">Only these approved forms exist. Never recolour the swirl or wordmark.</p>
''',
    )

    # ---- 4 misuse
    def bad(label: str, style: str = "", bg: str = "#fff", overlay: str = "") -> str:
        return (
            f'<div class="mis"><div class="mis-box" style="background:{bg}">'
            f'<div style="{style}">{svg_logo(main_logo, width="40mm")}</div>{overlay}<b class="x">&times;</b></div>'
            f"<p>{label}</p></div>"
        )

    retype = (
        '<span class="retype">ONDEWO</span>'
    )
    stripes = f"repeating-linear-gradient(45deg,{magenta},{magenta} 8px,{blue} 8px,{blue} 16px)"
    page(
        "4 &middot; Logo misuse",
        f'''
<h2>Never do this</h2>
<p>The logo is fixed artwork. Always use the official files from <code>brand-kit/assets/logo/</code>
(or the source files in the repository root for professional print).</p>
<div class="grid3">
{bad("Stretch or squash", "transform:scaleX(1.2) scaleY(.7)")}
{bad("Rotate or skew", "transform:rotate(-12deg)")}
{bad("Recolour", "filter:hue-rotate(110deg) saturate(1.4)")}
{bad("Add shadows, glows or outlines", "filter:drop-shadow(2px 3px 3px rgba(0,0,0,.7))")}
{bad("Full-colour logo on brand blue", bg=blue)}
{bad("Busy or low-contrast background", bg=stripes)}
{bad("Reduce opacity", "opacity:.3")}
{bad("Crop the swirl", "width:30mm;overflow:hidden;justify-content:flex-end")}
{bad("Re-typeset the name", overlay=retype)}
</div>
<h3>Also avoid</h3>
<ul class="tight">
 <li>Boxing the logo in a coloured pill or badge it was not designed for &mdash; it reduces clear space.</li>
 <li>Redrawing the swirl or rebuilding the wordmark from scratch.</li>
 <li>Using a low-resolution raster when an SVG, EPS or PDF exists.</li>
 <li>Writing the brand as &ldquo;Ondewo&rdquo; in running text &mdash; always <b>ONDEWO</b>.</li>
</ul>
''',
    )

    # ---- 5 colour
    def swatch(name: str, hexv: str, role: str, key: str) -> str:
        r, g, b = hex_rgb(hexv)
        p = PRINT[key]
        return (
            f'<div class="sw"><div class="chip" style="background:{hexv}"><b>{name}</b><span>{role}</span></div>'
            f'<dl><dt>Hex (digital)</dt><dd>{hexv}</dd><dt>RGB</dt><dd>{r} / {g} / {b}</dd>'
            f'<dt>CMYK (print)</dt><dd>{p["cmyk"]}</dd><dt>Guideline hex</dt><dd>{p["guideline_hex"]}</dd>'
            f'<dt>Pantone</dt><dd class="muted">&#8249;confirm&#8250;</dd></dl></div>'
        )

    def scale_row(name: str) -> str:
        cells = "".join(
            f'<div style="background:{h};color:{"#fff" if luminance(h) < 0.22 else ink}"><b>{k}</b><span>{h}</span></div>'
            for k, h in scale(t, name)
        )
        return f'<div class="scale"><h4>{name.title()}</h4><div class="srow">{cells}</div></div>'

    page(
        "5 &middot; Colour",
        f'''
<h2>Core palette</h2>
<div class="grid3">
{swatch("ONDEWO Blue", blue, "Primary", "blue")}
{swatch("ONDEWO Magenta", magenta, "Accent", "magenta")}
{swatch("Ink", ink, "Text &amp; one-colour logo", "ink")}
</div>
<p class="muted">The 2019 print guideline lists #014C89 / #BF206B. The vector logo files use #004C87 / #BE216B.
Use the artwork values for all digital work and the CMYK values for professional print.</p>

<h3>The 60 &middot; 30 &middot; 10 balance</h3>
<div class="bal"><div style="flex:60;background:{n50};color:{ink}">60% neutral</div>
<div style="flex:30;background:{blue}">30% blue</div><div style="flex:10;background:{magenta}">10%</div></div>
<p>Blue leads; magenta is a deliberate spark &mdash; a key call to action, one highlight, the swirl.
Never a dominant fill.</p>

<h3>Extended scales</h3>
{scale_row("blue")}{scale_row("magenta")}{scale_row("neutral")}
<div class="scale"><h4>Signature gradient</h4><div class="grad" style="background:{val(t["gradient"]["brand"])}"></div>
<p class="muted">Hero bands and dividers only. Never under body text.</p></div>
''',
    )

    # ---- 6 accessibility (computed)
    white = val(c["neutral"]["0"])
    pairs = [
        ("Ink", ink, "White", white),
        ("White", white, "Blue", blue),
        ("Blue", blue, "White", white),
        ("White", white, "Magenta", magenta),
        ("Magenta", magenta, "White", white),
        ("White", white, "Blue 700", val(c["blue"]["700"])),
        ("Neutral 500", val(c["neutral"]["500"]), "White", white),
    ]
    forbidden = [
        ("Blue", blue, "Magenta", magenta),
        ("Magenta", magenta, "Blue", blue),
        ("Blue 300", val(c["blue"]["300"]), "White", white),
        ("Magenta 400", val(c["magenta"]["400"]), "White", white),
    ]

    def prow(a: str, ah: str, b: str, bh: str) -> str:
        r = contrast(ah, bh)
        label, kind = verdict(r)
        return (
            f'<tr><td><span class="demo" style="background:{bh};color:{ah}">Aa</span></td>'
            f'<td>{a} on {b}</td><td>{ah} / {bh}</td><td>{r:.2f}:1</td><td class="v {kind}">{label}</td></tr>'
        )

    head = "<tr><th></th><th>Pair</th><th>Foreground / background</th><th>Ratio</th><th>Result</th></tr>"
    page(
        "6 &middot; Accessibility",
        f'''
<h2>Contrast &amp; accessibility</h2>
<p>Target <b>WCAG 2.1 AA</b> for everything public: 4.5:1 for normal text, 3:1 for large text
(&ge;&nbsp;24&nbsp;px, or &ge;&nbsp;19&nbsp;px bold) and for UI components. Ratios are computed from the tokens.</p>
<h3>Approved pairs</h3>
<table class="t pairs">{head}{"".join(prow(*p) for p in pairs)}</table>
<h3>Do not use</h3>
<table class="t pairs">{head}{"".join(prow(*p) for p in forbidden)}</table>
<h3>Beyond contrast</h3>
<ul class="tight">
 <li>Never rely on colour alone &mdash; pair magenta &ldquo;important&rdquo; with an icon or label.</li>
 <li>Visible 2&nbsp;px magenta focus ring; never remove outlines.</li>
 <li>Touch targets &ge;&nbsp;44&times;44&nbsp;px. Honour <code>prefers-reduced-motion</code>.</li>
 <li>Alt text: logo &rarr; <code>alt="ONDEWO"</code>; decorative swirl &rarr; empty alt.</li>
</ul>
''',
    )

    # ---- 7 typography
    sizes = t["typography"]["fontSize"]
    rows = "".join(
        f'<tr><td>{k}</td><td>{to_px(val(sizes[k])):g}&nbsp;px</td>'
        f'<td style="font-size:{min(to_px(val(sizes[k])), 40) * 0.75:.1f}pt;line-height:1.15">We automate your phone calls.</td></tr>'
        for k in ("5xl", "4xl", "3xl", "2xl", "xl", "lg", "base", "sm", "xs")
        if k in sizes
    )
    page(
        "7 &middot; Typography",
        f'''
<h2>Futura</h2>
<div class="spec-type">
 <div class="aa">Aa</div>
 <div><p class="big" style="margin:0">Futura PT / Futura LT Pro</p>
 <p class="glyphs">ABCDEFGHIJKLMNOPQRSTUVWXYZ&Auml;&Ouml;&Uuml;<br>abcdefghijklmnopqrstuvwxyz&auml;&ouml;&uuml;&szlig;<br>1234567890 @&euro;</p></div>
</div>
<p>Futura is a geometric sans-serif designed by Paul Renner and released in 1927. It is built on geometric
shapes, especially the circle &mdash; similar in spirit to the Bauhaus &mdash; and mirrors the geometry of the swirl.
This document is set in Jost, the free Futura-style fallback.</p>
<h3>Font stack</h3>
<table class="t"><tr><td><b>Brand (licensed)</b></td><td>Futura PT / Futura LT Pro &mdash; print, official decks, Adobe/Figma</td></tr>
<tr><td><b>Web fallback (free)</b></td><td>Jost (open licence) &mdash; default on public web, email and open source</td></tr>
<tr><td><b>System fallback</b></td><td>Century Gothic, Trebuchet MS, system-ui</td></tr>
<tr><td><b>Monospace</b></td><td>JetBrains Mono, Consolas</td></tr></table>
<p class="muted">Futura PT/LT Pro are commercial fonts: do not embed or ship the files on public sites without a licence.</p>
<h3>Rules</h3>
<ul class="tight">
 <li>Headlines: Light or Bold, <b>sentence case</b>. Body: Regular, &ge;&nbsp;16&nbsp;px, about 70 characters per line.</li>
 <li>Weights: 300 display &middot; 400 body &middot; 500 sub-heads &amp; buttons &middot; 700 wordmark, key numbers.</li>
 <li>All-caps labels need <b>+0.12em</b> letter-spacing. One geometric sans does all the work.</li>
</ul>
<h3>Type scale (1.25 &mdash; major third)</h3>
<table class="t scale-t"><tr><th>Token</th><th>Size</th><th>Specimen (scaled)</th></tr>{rows}</table>
''',
    )

    # ---- 8 layout
    bars = "".join(
        f'<div class="sp"><span>{k}</span><i style="width:{to_px(val(v)):g}px"></i><em>{to_px(val(v)):g}&nbsp;px</em></div>'
        for k, v in t["space"].items()
        if re.fullmatch(r"\d+", k) and val(v) not in ("0", "0px")
    )
    page(
        "8 &middot; Layout, imagery &amp; iconography",
        f'''
<h2>Spacing &amp; grid</h2>
<div class="row top">
 <div class="half"><h3>4&nbsp;px spacing scale</h3>{bars}</div>
 <div class="half"><h3>Grids</h3><ul class="tight">
  <li><b>Web:</b> 12 columns, max width 1200&ndash;1280&nbsp;px, 24&nbsp;px gutters.</li>
  <li><b>Slides 16:9:</b> 1920&times;1080, 96&nbsp;px margin, 48&nbsp;px gutter.</li>
  <li><b>Print A4:</b> 12&ndash;18&nbsp;mm margins on a baseline grid.</li>
  <li><b>Social:</b> text and logo inside the central 80%.</li></ul>
  <p>Whitespace is part of the brand. When in doubt, add space, not decoration.</p>
  <h3>Radius &amp; elevation</h3><p>4 / 8 / 16&nbsp;px radii. Soft, blue-tinted shadows; prefer 1&nbsp;px borders.</p></div>
</div>
<h3>Imagery</h3>
<table class="t"><tr><th>Do</th><th>Avoid</th></tr>
<tr><td>Real people in real work settings</td><td>Cliche &ldquo;smiling headset&rdquo; stock</td></tr>
<tr><td>Clean tech / abstract: soundwaves, flows, loops echoing the swirl</td><td>Literal robots, &ldquo;AI brain&rdquo; clip-art</td></tr>
<tr><td>Bright, airy, blue-leaning grade with pops of magenta</td><td>Dark, noisy, cluttered scenes</td></tr>
<tr><td>Blue&ndash;magenta duotone to unify mixed photos</td><td>Random filters</td></tr></table>
<h3>Iconography &amp; motion</h3>
<ul class="tight">
 <li>Line icons, 2&nbsp;px stroke, rounded joints (Lucide, Phosphor Regular or Feather). One set per product; ink or blue, magenta for one key icon.</li>
 <li>Graphic language: arcs, loops and soundwave lines. The swirl may act as a low-opacity watermark. One motif per layout.</li>
 <li>Motion: smooth, never bouncy; 150&ndash;250&nbsp;ms UI, 400&ndash;800&nbsp;ms storytelling. Respect reduced motion.</li>
</ul>
<h3>Checklist before shipping</h3>
<ul class="check">
 <li>Right logo variant with full clear space</li><li>Only brand colours; magenta &le; ~10%</li>
 <li>Futura / Jost and the type scale</li><li>4&nbsp;px spacing, generous whitespace</li>
 <li>Contrast passes AA</li><li>One focal point and one primary call to action</li>
</ul>
''',
    )

    # ---- 9 social & platform kits
    from social_data import PLATFORMS  # local import: optional data module

    def inline_svg(path: Path) -> str:
        # inline (not <img>) so the embedded Jost font applies to the template text
        txt = re.sub(r'\s(width|height)="[^"]+"', "", path.read_text(encoding="utf-8"), count=2)
        return txt.replace("<svg ", '<svg style="width:100%;height:auto" ', 1)

    srows = "".join(
        f"<tr><td><b>{esc(pl['name'])}</b><br><span class='muted'>{esc(pl['category'])}</span></td>"
        f"<td>{esc(', '.join(f'{a[1]}&times;{a[2]} {a[0]}' for a in pl['assets'][:4]))}</td>"
        f"<td style='white-space:nowrap'><code>social/{k}/</code></td></tr>"
        for k, pl in PLATFORMS.items()
    ).replace("&amp;times;", "&times;")
    thumbs = ""
    for k, f, w in (("linkedin", "cover", "100%"), ("instagram", "post-square", "100%"), ("tiktok", "video-cover", "100%")):
        img = KIT / "social" / k / "images" / f"{f}.svg"
        if img.exists():
            thumbs += f'<div><div style="width:{w};border:.25mm solid #E5E4E6;line-height:0">{inline_svg(img)}</div><p class="muted">{esc(PLATFORMS[k]["name"])} &middot; {f}</p></div>'
    page(
        "9 &middot; Social &amp; platform kits",
        f'''
<p>Each platform has a folder with specs, ready-made images, profile copy and content guidelines.
Avatars use the swirl on white (or white on blue) inside the centre 58%; covers and posts use a blue base
with a single magenta accent.</p>
<table class="t"><tr><th>Platform</th><th>Key assets (px)</th><th>Folder</th></tr>{srows}</table>
<div class="grid3">{thumbs}</div>
<p class="muted">Rebuild with <code>make social</code>. Platform specs change often &mdash; verify before uploading.
Handles and URLs marked &lsaquo;confirm&rsaquo; still need ONDEWO marketing sign-off.</p>
''',
    )

    # ---- 10 resources
    page(
        "10 &middot; Resources",
        f'''
<h2>Files &amp; tokens</h2>
<table class="t"><tr><th>What</th><th>Where</th></tr>
<tr><td>Web-ready logo SVGs (colour, mono, mark, favicon, app icon, avatar)</td><td><code>brand-kit/assets/logo/</code></td></tr>
<tr><td>Print source logos (.ai .eps .pdf .psd, CMYK)</td><td><code>ONDEWO_Logo_*/</code> in the repository root</td></tr>
<tr><td>Design tokens (JSON, CSS, SCSS, Tailwind)</td><td><code>brand-kit/tokens/</code></td></tr>
<tr><td>Editable templates (social, slides, web hero, signature, letterhead)</td><td><code>brand-kit/templates/</code></td></tr>
<tr><td>Full written guidelines</td><td><code>brand-kit/*.md</code></td></tr></table>
<h3>Working with AI agents</h3>
<p>The repository is built to be read by AI coding agents: point the agent at <code>CLAUDE.md</code> and it
loads the right guideline, tokens and templates. Skills cover slide decks, one-pagers, case studies,
emails, social kits, whitepapers and more; the brand-check skill audits finished work against this document.</p>
<h3>Regenerating this document</h3>
<p><code>python3 scripts/build_guideline.py</code> &mdash; values are read from the design tokens and logo SVGs,
and contrast ratios are computed, so the PDF stays in sync with the kit.</p>
<h3>Company details</h3>
<p>ONDEWO GmbH &middot; Plankengasse 1/5-6 &middot; 1010 Vienna &middot; Austria<br>VAT: ATU72347427 &middot; Company Reg.: FN473436f</p>
<h3>Questions</h3>
<p>Contact the ONDEWO marketing team before using the logo in a way not covered here.</p>
<div class="end">{svg_logo(main_logo, width="70mm")}<p>ONDEWO &copy; 2019&ndash;{year}</p></div>
''',
    )
    return pages


CSS = """
@page{size:A4;margin:0}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;font-family:"Jost","Futura PT","Century Gothic","Trebuchet MS",system-ui,sans-serif;color:#231F20;font-size:10.4pt;line-height:1.5;counter-reset:pg}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page;background:#fff;counter-increment:pg}
.ph{display:flex;justify-content:space-between;align-items:center;padding:12mm 16mm 0;font-weight:500;letter-spacing:.12em;text-transform:uppercase;font-size:8pt;color:#004C87;height:24mm}
.pb{padding:4mm 16mm 0;height:255mm;overflow:hidden}
.pf{position:absolute;left:16mm;right:16mm;bottom:9mm;display:flex;justify-content:space-between;font-size:7.5pt;color:#5A5560;border-top:.25mm solid #E5E4E6;padding-top:3mm}
.pn::after{content:counter(pg)}
h1{font-weight:700;font-size:40pt;line-height:1.05;letter-spacing:-.01em;margin:0 0 6mm;color:#fff}
h2{font-weight:700;font-size:17pt;line-height:1.2;margin:0 0 3mm;color:#004C87}
h2:not(:first-child){margin-top:7mm}
h3{font-weight:700;font-size:11pt;margin:5mm 0 2mm}
h4{margin:0 0 1.5mm;font-size:8pt;letter-spacing:.12em;text-transform:uppercase;color:#5A5560;font-weight:500}
p{margin:0 0 2.5mm}
.lead{font-size:12pt;font-weight:300;line-height:1.4}
.big{font-size:14pt;font-weight:500;color:#BE216B}
.muted{color:#5A5560;font-size:8.2pt}
.eyebrow{letter-spacing:.12em;text-transform:uppercase;font-weight:500;color:#DB85AE;font-size:9pt;margin-bottom:4mm}
code{font-family:"JetBrains Mono",Consolas,monospace;font-size:8pt;background:#F7F8FA;padding:.2mm 1mm;border-radius:1mm}
ul{margin:0 0 2mm;padding-left:5mm}ul.tight li{margin-bottom:1.2mm}
.row{display:flex;gap:8mm;align-items:center}.row.top{align-items:flex-start}.half{flex:1}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin:4mm 0}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm;margin:3mm 0}
.card{background:#F7F8FA;border-radius:2mm;padding:4mm 5mm}.card h3{margin-top:0}
.t{width:100%;border-collapse:collapse;margin:0 0 3mm}
.t th{text-align:left;background:#004C87;color:#fff;font-weight:500;padding:1.8mm 3mm;font-size:8.5pt}
.t td{padding:1.6mm 3mm;border-bottom:.25mm solid #E5E4E6;vertical-align:top}
.stage{background:#fff;border:.3mm solid #E5E4E6;border-radius:2mm;display:flex;align-items:center;justify-content:center;padding:9mm;margin:3mm 0}
.stage.small{padding:6mm 9mm;flex:none}
.stage svg,.stage img{display:block}
.spec{display:flex;align-items:center;gap:5mm;margin:2mm 0}
.tag{background:#EBF1F5;color:#004C87;font-weight:500;padding:1mm 4mm;border-radius:1mm;font-size:8.5pt;white-space:nowrap}
.spec i{font-style:normal;color:#5A5560;font-size:8.5pt}
.cs{width:100%;height:auto}
.cw{border-radius:2mm;padding:8mm 4mm 5mm;text-align:center;display:flex;flex-direction:column;align-items:center;gap:6mm;min-height:52mm}
.cw.bordered{border:.3mm solid #E5E4E6}
.cw p{margin:0;font-weight:500;font-size:8.5pt}.cw span{font-weight:400;font-size:7.5pt;opacity:.8}
.mis-box{position:relative;height:34mm;border:.3mm solid #E5E4E6;border-radius:2mm;display:flex;align-items:center;justify-content:center;overflow:hidden}
.mis-box>div{display:flex;justify-content:center}.mis-box>div svg{flex:none}
.retype{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font:italic 700 9mm Georgia,serif;color:#004C87;background:#fff}
.mis p{margin:1.5mm 0 0;font-size:8.2pt;text-align:center}
.x{position:absolute;top:1.5mm;right:2.5mm;color:#C02626;font-size:15pt;line-height:1;z-index:2}
.sw .chip{height:30mm;border-radius:2mm 2mm 0 0;padding:4mm;display:flex;flex-direction:column;justify-content:flex-end;color:#fff}
.chip b{font-size:11pt}.chip span{font-size:8pt;opacity:.9}
.sw dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:.6mm 3mm;font-size:8pt;border:.3mm solid #E5E4E6;border-top:0;border-radius:0 0 2mm 2mm;padding:3mm}
.sw dt{color:#5A5560}.sw dd{margin:0;font-weight:500;text-align:right}
.bal{display:flex;height:11mm;border-radius:2mm;overflow:hidden;color:#fff;font-weight:500;font-size:8.5pt;margin-bottom:2mm}
.bal div{display:flex;align-items:center;padding-left:4mm}
.scale{margin-bottom:3mm}.srow{display:flex;border-radius:1.5mm;overflow:hidden}
.srow div{flex:1;padding:2mm 1mm;font-size:6.2pt;display:flex;flex-direction:column;align-items:center;line-height:1.3}
.srow b{font-size:7pt}.srow span{opacity:.85}
.grad{height:9mm;border-radius:1.5mm;margin-bottom:1.5mm}
.pairs td:first-child{width:14mm}.demo{display:inline-block;padding:1mm 3mm;border-radius:1mm;font-weight:700;border:.2mm solid #E5E4E6}
.v{font-weight:500}.v.ok{color:#1E7A4B}.v.warn{color:#B5710A}.v.bad{color:#C02626}
.spec-type{display:flex;gap:8mm;align-items:center;margin-bottom:3mm}
.aa{font-size:64pt;font-weight:700;line-height:1;color:#004C87}
.glyphs{font-weight:500;font-size:13pt;line-height:1.35;margin:2mm 0 0}
.scale-t td{padding:.8mm 3mm;vertical-align:middle}.scale-t td:nth-child(3){white-space:nowrap}
.sp{display:flex;align-items:center;gap:3mm;font-size:8pt;margin-bottom:1mm}
.sp span{width:5mm;color:#5A5560}.sp i{height:3mm;background:#004C87;border-radius:.6mm;display:block;max-width:60mm}.sp em{font-style:normal;color:#5A5560}
.check{list-style:none;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:1.4mm 6mm}
.check li::before{content:"\\2713";color:#BE216B;font-weight:700;margin-right:2mm}
.end{margin-top:14mm;text-align:center}.end svg{display:inline-block}.end p{margin-top:4mm;color:#5A5560}
.cover{background:linear-gradient(135deg,#004C87 0%,#002644 100%);color:#fff;display:flex;flex-direction:column;justify-content:space-between;padding:20mm 20mm 16mm;counter-increment:none}
.cover::before{content:"";position:absolute;left:0;right:0;top:0;height:3mm;background:linear-gradient(90deg,#BE216B,#004C87)}
.cover-top{background:#fff;align-self:flex-start;padding:7mm 9mm;border-radius:2mm;position:relative;z-index:1}
.cover-top svg{display:block}
.cover-mid{position:relative;z-index:1}.cover .lead{color:#D6E2EC;max-width:120mm}
.cover-swirl{position:absolute;right:-48mm;bottom:20mm;opacity:.09}
.cover-foot{display:flex;justify-content:space-between;font-size:9pt;letter-spacing:.12em;text-transform:uppercase;font-weight:500;position:relative;z-index:1;border-top:.3mm solid rgba(255,255,255,.35);padding-top:4mm}
"""


def build_html(tokens: dict) -> str:
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        "<title>ONDEWO Logo &amp; Identity Guideline</title>"
        '<meta name="author" content="ONDEWO">'
        f"<style>{font_face_css()}\n{CSS}</style></head><body>{''.join(build_pages(tokens))}</body></html>"
    )


def render_pdf(html_path: Path, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as profile:
        cmd = [
            find_chrome(), "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
            f"--user-data-dir={profile}", f"--print-to-pdf={out}", html_path.as_uri(),
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if not out.exists() or out.stat().st_size == 0:
        sys.exit(f"error: Chrome failed to produce the PDF\n{res.stderr[-800:]}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate the ONDEWO Logo & Identity Guideline PDF.")
    ap.add_argument("-o", "--output", type=Path, default=DEFAULT_OUT,
                    help=f"PDF path (default: {DEFAULT_OUT.relative_to(ROOT)})")
    ap.add_argument("--html-only", action="store_true", help="write the HTML next to the PDF path and skip rendering")
    args = ap.parse_args()

    html_doc = build_html(json.loads(TOKENS.read_text(encoding="utf-8")))
    out = args.output.resolve()
    if args.html_only:
        target = out.with_suffix(".html")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html_doc, encoding="utf-8")
        print(f"wrote {target}")
        return
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "guideline.html"
        src.write_text(html_doc, encoding="utf-8")
        render_pdf(src, out)
    print(f"wrote {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
