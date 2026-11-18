# ONDEWO — Asset Index

Every brand asset in this repository, what it is, and when to reach for it.

---

## A. Web-ready, optimised SVGs (use these in code) — `brand-kit/assets/logo/`

| File | Description | Best for |
|------|-------------|----------|
| `ondewo-logo-horizontal.svg` | **Primary** full-colour lockup (swirl + ONDEWO) | Default everywhere |
| `ondewo-logo-horizontal-mono-black.svg` | Ink one-colour lockup | 1-colour / light bg |
| `ondewo-logo-horizontal-mono-white.svg` | White one-colour lockup | Dark / blue / photo bg |
| `ondewo-mark.svg` | Swirl symbol only, full colour | Icons, avatars, watermarks |
| `ondewo-mark-mono-black.svg` | Swirl, ink | Mono contexts |
| `ondewo-mark-mono-white.svg` | Swirl, white | Dark contexts |
| `ondewo-favicon.svg` | Mark, tight square, transparent | Browser favicon |
| `ondewo-app-icon.svg` | White mark on blue rounded square | OS / app icon, PWA |
| `ondewo-avatar.svg` | Mark on white square, padded | Social profile picture |

> These were generated from the official vector source (`ONDEWO_Logo_Sonderformen_2019`)
> — exact paths, exact brand colours, cleaned for screens.

## B. Official source files (repo root & `ONDEWO_Logo_*/`)

Use these for **professional print**, design tools, or when you need CMYK/editable layers.

| Location | Formats | Notes |
|----------|---------|-------|
| `ONDEWO_Logo_4c_horizontal_*` (root) | `.ai .eps .pdf .svg .png .jpg .psd` | 4-colour horizontal, RGB + CMYK |
| `ONDEWO_Logo_horizontal_4c_2019/` | same set | Folder copy of the horizontal 4c |
| `ONDEWO_Logo_horizontal_1c_2019/` | same set | One-colour (ink) horizontal |
| `ONDEWO_Logo_vertical_4c_2019/` | `.ai .eps .pdf .svg .png .jpg .psd` | **Vertical/stacked** 4-colour |
| `ONDEWO_Logo_vertical_1c_2019/` | same set | Vertical one-colour |
| `ONDEWO_Logo_Sonderformen_2019/` | same set | "Special forms" — mark/lockup variants |
| `ondewo_logo_identity_guideline_2019.pdf` | PDF | **The official brand guideline** |
| `ondewo_facebook_profile.png` | PNG | Legacy social profile image |
| `ondewo_we_automate_your_phone_calls.png` | PNG | Tagline lockup graphic |
| `github/ondewo_logo_github_2.png` | PNG | README header image |

**Format cheat-sheet:**
- `.svg` → web, scalable, recolourable. **Default for code.**
- `.png` → raster with transparency; slides, quick embeds.
- `.jpg` → photos / where transparency isn't needed (smaller).
- `.pdf` / `.eps` / `.ai` → print & professional design tools (vector).
- `.psd` → layered Photoshop source (raster editing).
- CMYK files → **print only**; RGB/hex → **screens only**.

## C. Colour quick-grab

| | Hex | Token |
|-|-----|-------|
| Blue | `#004C87` | `--ondewo-blue` |
| Magenta | `#BE216B` | `--ondewo-magenta` |
| Ink | `#231F20` | `--ondewo-ink` |

Full system → [`../color-system.md`](../color-system.md) · tokens → [`../tokens/`](../tokens/)

## D. Naming convention (for new assets you create)

```
ondewo-<type>-<variant>-<theme>[-<size>].<ext>
e.g.  ondewo-banner-linkedin-light-1584x396.png
      ondewo-social-launch-dark-1080.svg
```
Lower-case, hyphen-separated, dimensions as `WxH` for raster. Keep new generated
assets under `brand-kit/generated/` (or a campaign folder) — never overwrite §A/§B.
