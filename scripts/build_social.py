#!/usr/bin/env python3
"""Generate the ONDEWO social / platform brand kits.

For every platform in scripts/social_data.py this writes, into
brand-kit/social/<platform>/ :

    README.md              specs, asset table, usage
    profile-copy.md        ready-to-paste names, bios, descriptions (with limits)
    content-guidelines.md  tone, hooks, do / don't, safe zones
    images/*.svg|png       on-brand avatars, covers, post/story templates

plus brand-kit/social/README.md (index). Images are built from the official
logo SVGs and the design tokens; PNGs are rendered with headless Chrome.

Usage:
    python3 scripts/build_social.py                   # all platforms
    python3 scripts/build_social.py linkedin tiktok   # selected platforms
    python3 scripts/build_social.py --no-png          # SVG + markdown only

Requires: Python 3.8+ (stdlib only); Chrome/Chromium on PATH for PNG export.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_guideline import KIT, LOGO, TOKENS, find_chrome, font_face_css, svg_inner, val  # noqa: E402
from social_data import BOILERPLATE, CONFIRM, ONE_LINER, PLATFORMS, TAGLINE  # noqa: E402

OUT = KIT / "social"
FONT = "Jost, Futura, 'Century Gothic', sans-serif"
MARK = LOGO / "ondewo-mark.svg"
MARK_WHITE = LOGO / "ondewo-mark-mono-white.svg"
LOGO_WHITE = LOGO / "ondewo-logo-horizontal-mono-white.svg"


def num(x: float) -> str:
    return f"{x:.1f}".rstrip("0").rstrip(".")


def place(path: Path, x: float, y: float, width: float, opacity: float = 1) -> tuple[str, float]:
    """Nest a logo SVG at (x, y) with the given width; returns (markup, height)."""
    vb, inner = svg_inner(path)
    _, _, vw, vh = (float(p) for p in vb.split())
    h = width * vh / vw
    op = f' opacity="{opacity}"' if opacity != 1 else ""
    return (f'<svg x="{num(x)}" y="{num(y)}" width="{num(width)}" height="{num(h)}" viewBox="{vb}"{op}>{inner}</svg>', h)


def frame(w: int, h: int, body: str, title: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'font-family="{FONT}" role="img" aria-label="{title}">\n<title>{title}</title>\n{body}\n</svg>\n'
    )


# --------------------------------------------------------------- templates ---


def t_avatar(w: int, h: int, c: dict, dark: bool) -> str:
    bg, mark = (c["blue"], MARK_WHITE) if dark else ("#FFFFFF", MARK)
    mw = w * 0.58  # centre 58% survives circular crops
    vb = svg_inner(mark)[0].split()
    mh = mw * float(vb[3]) / float(vb[2])
    logo, _ = place(mark, (w - mw) / 2, (h - mh) / 2, mw)
    return f'<rect width="{w}" height="{h}" fill="{bg}"/>\n{logo}'


def t_highlight(w: int, h: int, c: dict) -> str:
    r = w * 0.3
    logo, _ = place(MARK_WHITE, w / 2 - r * 0.62, h / 2 - r * 0.49, r * 1.24)
    return (
        f'<rect width="{w}" height="{h}" fill="{c["blue"]}"/>\n'
        f'<circle cx="{w / 2}" cy="{h / 2}" r="{r}" fill="none" stroke="#FFFFFF" stroke-opacity=".25" stroke-width="{w * 0.004}"/>\n{logo}'
    )


def t_cover(w: int, h: int, c: dict) -> str:
    margin = max(w * 0.08, h * 0.2)
    logo_h = h * 0.26
    logo_w = logo_h * 4.18
    gap = h * 0.1
    tag = h * 0.1
    top = (h - (logo_h + gap + tag)) / 2
    wm_w = h * 1.7
    wm, _ = place(MARK_WHITE, w - wm_w * 0.85, (h - wm_w * 123 / 157) / 2, wm_w, 0.07)
    logo, _ = place(LOGO_WHITE, margin, top, logo_w)
    bar = max(4, h * 0.02)
    return (
        f'<rect width="{w}" height="{h}" fill="{c["blue"]}"/>\n{wm}\n{logo}\n'
        f'<text x="{num(margin)}" y="{num(top + logo_h + gap + tag * 0.8)}" font-size="{num(tag)}" font-weight="500" '
        f'fill="#FFFFFF">{TAGLINE}</text>\n'
        f'<rect x="0" y="{num(h - bar)}" width="{w}" height="{num(bar)}" fill="{c["magenta"]}"/>'
    )


def t_post(w: int, h: int, c: dict, safe: tuple[int, int] | None = None) -> str:
    u = min((w * h) ** 0.5 / 1080, w / 1080)
    m = 80 * u
    top, bottom = safe if safe else (m, m)
    logo, lh = place(LOGO_WHITE, m, top, 300 * u)
    size = 100 * u
    area_t, area_b = top + lh, h - bottom - 84 * u
    mid = (area_t + area_b) / 2
    wm_w = min(w, h) * 0.9
    wm, _ = place(MARK_WHITE, w - wm_w * 0.7, h - wm_w * 123 / 157 * 0.8, wm_w, 0.06)
    y1 = mid - size * 0.1
    pill_y = h - bottom - 84 * u
    return (
        f'<rect width="{w}" height="{h}" fill="{c["blue"]}"/>\n{wm}\n{logo}\n'
        f'<text x="{num(m)}" y="{num(y1 - size * 1.25)}" font-size="{num(28 * u)}" font-weight="500" letter-spacing="{num(3 * u)}" '
        f'fill="#FFFFFF" fill-opacity=".8">EYEBROW \u00b7 CATEGORY</text>\n'
        f'<text font-size="{num(size)}" font-weight="700" fill="#FFFFFF">'
        f'<tspan x="{num(m)}" y="{num(y1)}">Your headline</tspan>'
        f'<tspan x="{num(m)}" y="{num(y1 + size * 1.15)}">goes here</tspan></text>\n'
        f'<rect x="{num(m)}" y="{num(y1 + size * 1.5)}" width="{num(120 * u)}" height="{num(8 * u)}" fill="{c["magenta"]}"/>\n'
        f'<rect x="{num(m)}" y="{num(pill_y)}" width="{num(300 * u)}" height="{num(84 * u)}" rx="{num(42 * u)}" fill="{c["magenta"]}"/>\n'
        f'<text x="{num(m + 150 * u)}" y="{num(pill_y + 54 * u)}" font-size="{num(32 * u)}" font-weight="500" '
        f'text-anchor="middle" fill="#FFFFFF">Book a demo</text>'
    )


def build_svg(template: str, w: int, h: int, c: dict, alt: str, safe: tuple[int, int] | None) -> str:
    if template == "avatar":
        body = t_avatar(w, h, c, False)
    elif template == "avatar-blue":
        body = t_avatar(w, h, c, True)
    elif template == "highlight":
        body = t_highlight(w, h, c)
    elif template == "cover":
        body = t_cover(w, h, c)
    else:  # post | story
        body = t_post(w, h, c, safe)
    return frame(w, h, body, alt)


# ---------------------------------------------------------------- PNG export ---


def render_png(svg: str, w: int, h: int, out: Path, fonts: str, chrome: str) -> None:
    html = f"<!doctype html><meta charset=utf-8><style>{fonts}html,body{{margin:0;padding:0;background:#fff}}svg{{display:block}}</style>{svg}"
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "i.html"
        page.write_text(html, encoding="utf-8")
        cmd = [
            chrome, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1", f"--user-data-dir={tmp}/p", f"--window-size={w},{h}",
            f"--screenshot={out}", page.as_uri(),
        ]
        subprocess.run(cmd, capture_output=True, timeout=120)
    if not out.exists():
        sys.exit(f"error: Chrome did not produce {out}")


# ------------------------------------------------------------------ markdown ---


def table(rows: list[tuple[str, ...]], head: tuple[str, ...]) -> str:
    out = ["| " + " | ".join(head) + " |", "|" + "|".join("---" for _ in head) + "|"]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(out)


def md_readme(key: str, p: dict, png: bool) -> str:
    ext = "png" if png else "svg"
    rows = [(f"`{a[0]}.{ext}`", f"{a[1]} \u00d7 {a[2]}", a[4]) for a in p["assets"]]
    gallery = "\n".join(
        f"**{a[4]}** \u2014 `{a[1]}\u00d7{a[2]}`\n\n![{a[5]}](images/{a[0]}.{ext})\n" for a in p["assets"]
    )
    alts = "\n".join(f"- `{a[0]}`: \u201c{a[5]}\u201d" for a in p["assets"])
    snippet = f"\n## README snippet\n\n{p['snippet']}\n" if p.get("snippet") else ""
    note = f"\n> {p['note']}\n" if p.get("note") else ""
    safe = [a for a in p["assets"] if len(a) > 6]
    safe_md = ""
    if safe:
        t, b = safe[0][6]
        safe_md = (
            f"\n## Safe zone\n\nKeep logo, headline and CTA at least **{t} px from the top** and **{b} px from the "
            f"bottom** of 1080 \u00d7 1920 assets: the platform UI (name, caption, buttons) covers those areas. "
            f"The story template already respects this.\n"
        )
    return f"""# ONDEWO on {p['name']}

> {p['category']} \u00b7 {p['role']}
>
> Handle / URL: {p['handle']}

Everything here follows the [brand kit](../../README.md): blue `#004C87` base, magenta `#BE216B`
accent only (\u2264 10%), Jost/Futura type, the official swirl logo (never redrawn). Copy follows
[voice-and-tone](../../voice-and-tone.md): sentence-case headlines, `ONDEWO` always all-caps.

> Platform specs change often. Treat the sizes below as recommendations and verify them in the
> platform before uploading. Items marked {CONFIRM} are not yet confirmed by ONDEWO marketing.
{note}
## Specs

{table([(a, b) for a, b in p['specs']], ('Item', 'Recommendation'))}

## Assets

{table(rows, ('File', 'Size (px)', 'Use'))}

Files live in [`images/`](images/) as editable SVG (open it, replace the placeholder text) and
exported PNG. Regenerate everything with `make social` from the repository root.

{gallery}
## Alt text

Always add alt text when uploading:

{alts}

For post templates, extend it with the real headline, e.g. \u201cONDEWO: Answer every call, around the clock.\u201d
{safe_md}{snippet}
## More

- [Profile copy](profile-copy.md) \u2014 names, bios and descriptions to paste, with character limits
- [Content guidelines](content-guidelines.md) \u2014 tone, hooks, do and don't
- [Social kit index](../README.md)
"""


def md_profile(key: str, p: dict) -> str:
    lines = [f"# {p['name']} \u2014 profile copy", "", f"Paste-ready text. Counts are characters. Items marked {CONFIRM} need marketing sign-off.", ""]
    for label, text, limit in p["profile"]:
        count = len(text)
        if limit is not None and count > limit:
            sys.exit(f"error: {key} '{label}' is {count} chars (limit {limit})")
        meta = f" \u2014 {count}/{limit}" if limit else ""
        body = "\n".join(f"> {ln}" if ln else ">" for ln in text.split("\n"))
        lines += [f"## {label}{meta}", "", body, ""]
    lines += [
        "## Shared building blocks",
        "",
        f"- **Tagline:** {TAGLINE}",
        f"- **One-liner** {CONFIRM}: {ONE_LINER}",
        f"- **Boilerplate** {CONFIRM}: {BOILERPLATE}",
        "",
        "Source: [voice-and-tone \u00a76](../../voice-and-tone.md).",
        "",
    ]
    return "\n".join(lines)


def md_guidelines(key: str, p: dict) -> str:
    hooks = "\n".join(f"- {h}" for h in p["hooks"]) or "- Not applicable: this is a documentation / tooling surface."
    dos = "\n".join(f"- \u2705 {x}" for x in p["do"])
    donts = "\n".join(f"- \u274c {x}" for x in p["dont"])
    return f"""# {p['name']} \u2014 content guidelines

## Tone

{p['tone']}

Personality dials (0\u201310): formality 7 \u00b7 warmth 6 \u00b7 boldness 5 \u00b7 technicality 7 \u00b7 playfulness 3.

## Hook / headline starters

{hooks}

## Do

{dos}

## Don't

{donts}

## Always

- `ONDEWO` in all-caps in prose; headlines and CTAs in sentence case
- Blue base, magenta as a single accent; never blue text on magenta or magenta on blue
  ([accessibility](../../accessibility.md))
- Use the official logo files from [`assets/logo/`](../../assets/logo/); never stretch, recolour or add effects
- Run the banned-word check from [voice-and-tone](../../voice-and-tone.md) before publishing
- No personal data, customer calls or unreleased claims; numbers need a source
"""


def md_index(keys: list[str]) -> str:
    rows = []
    for k in keys:
        p = PLATFORMS[k]
        rows.append((f"[{p['name']}]({k}/README.md)", p["category"], ", ".join(f"{a[1]}\u00d7{a[2]}" for a in p["assets"][:3]), p["handle"]))
    return f"""# ONDEWO \u2014 Social & platform brand kits

One folder per platform with specs, images, profile copy and content guidelines.
Regenerate everything from the design tokens and official logos with:

```bash
make social                       # all platforms
make social PLATFORMS="linkedin"  # selected platforms
```

{table(rows, ('Platform', 'Type', 'First assets (px)', 'Handle / URL'))}

Each folder contains `README.md`, `profile-copy.md`, `content-guidelines.md` and `images/`.

## Rules shared by all platforms

1. Colour balance 60% neutral \u00b7 30% blue \u00b7 10% magenta; magenta is only an accent (CTA, thin rule).
2. The swirl avatar is the profile image everywhere. White background by default, `avatar-blue` for dark surfaces.
   Keep the mark inside the centre 58% so circular crops never clip it.
3. One tagline: *{TAGLINE}*
4. Hashtag starter set {CONFIRM}: `#ONDEWO #VoiceAI #ConversationalAI #CallAutomation #ContactCenter #SpeechAI`.
5. Alt text on every image; captions on every video.
6. Every handle, URL and category marked {CONFIRM} must be validated by ONDEWO marketing before launch.
7. Platform specs change: verify before upload. Templates are in `brand-kit/social/<platform>/images/`
   and are regenerated, not hand-edited, when the brand changes.

Company details for imprints and About sections: ONDEWO GmbH · Plankengasse 1/5-6 · 1010 Vienna · Austria · VAT: ATU72347427 · Company Reg.: FN473436f.

See also: [brand foundation](../brand-foundation.md) \u00b7 [voice & tone](../voice-and-tone.md) \u00b7
[colour system](../color-system.md) \u00b7 [logo guidelines](../logo-guidelines.md).
"""


# ---------------------------------------------------------------------- main ---


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate ONDEWO social / platform brand kits.")
    ap.add_argument("platforms", nargs="*", help=f"subset of: {', '.join(PLATFORMS)} (default: all)")
    ap.add_argument("--no-png", action="store_true", help="write SVG + markdown only")
    args = ap.parse_args()

    keys = args.platforms or list(PLATFORMS)
    unknown = [k for k in keys if k not in PLATFORMS]
    if unknown:
        sys.exit(f"error: unknown platform(s): {', '.join(unknown)}")

    tokens = json.loads(TOKENS.read_text(encoding="utf-8"))
    c = {"blue": val(tokens["color"]["brand"]["blue"]), "magenta": val(tokens["color"]["brand"]["magenta"])}
    png = not args.no_png
    fonts, chrome = (font_face_css(), find_chrome()) if png else ("", "")

    for key in keys:
        p = PLATFORMS[key]
        folder = OUT / key
        (folder / "images").mkdir(parents=True, exist_ok=True)
        for asset in p["assets"]:
            stem, w, h, template, _use, alt = asset[:6]
            safe = asset[6] if len(asset) > 6 else None
            svg = build_svg(template, w, h, c, alt, safe)
            (folder / "images" / f"{stem}.svg").write_text(svg, encoding="utf-8")
            if png:
                render_png(svg, w, h, folder / "images" / f"{stem}.png", fonts, chrome)
        (folder / "README.md").write_text(md_readme(key, p, png), encoding="utf-8")
        (folder / "profile-copy.md").write_text(md_profile(key, p), encoding="utf-8")
        (folder / "content-guidelines.md").write_text(md_guidelines(key, p), encoding="utf-8")
        print(f"{p['name']:<11} {len(p['assets'])} images -> {folder.relative_to(KIT.parent)}")

    # the index always lists every platform, regardless of the subset built
    (OUT / "README.md").write_text(md_index(list(PLATFORMS)), encoding="utf-8")
    print(f"index       -> {(OUT / 'README.md').relative_to(KIT.parent)}")


if __name__ == "__main__":
    main()
