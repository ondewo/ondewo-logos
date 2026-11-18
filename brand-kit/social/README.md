# ONDEWO — Social & platform brand kits

One folder per platform with specs, images, profile copy and content guidelines.
Regenerate everything from the design tokens and official logos with:

```bash
make social                       # all platforms
make social PLATFORMS="linkedin"  # selected platforms
```

| Platform | Type | First assets (px) | Handle / URL |
|---|---|---|---|
| [LinkedIn](linkedin/README.md) | Social network (B2B) | 400×400, 400×400, 1128×191 | linkedin.com/company/ondewo ‹confirm› |
| [Facebook](facebook/README.md) | Social network | 720×720, 720×720, 820×312 | facebook.com/ondewo ‹confirm› |
| [Instagram](instagram/README.md) | Social network (visual) | 720×720, 720×720, 1080×1350 | @ondewo ‹confirm› |
| [TikTok](tiktok/README.md) | Short-form video | 720×720, 720×720, 1080×1920 | @ondewo ‹confirm› |
| [Bitbucket](bitbucket/README.md) | Source hosting (developer) | 256×256, 256×256, 1280×320 | bitbucket.org/ondewo ‹confirm› |
| [Jira](jira/README.md) | Work management (internal / partner) | 256×256, 256×256, 1280×320 | <site>.atlassian.net ‹confirm› |
| [Confluence](confluence/README.md) | Documentation (internal / partner) | 256×256, 256×256, 1920×400 | <site>.atlassian.net/wiki ‹confirm› |
| [Roblox](roblox/README.md) | Gaming platform (experimental) | 512×512, 512×512, 1920×1080 | ONDEWO (group) ‹confirm› |

Each folder contains `README.md`, `profile-copy.md`, `content-guidelines.md` and `images/`.

## Rules shared by all platforms

1. Colour balance 60% neutral · 30% blue · 10% magenta; magenta is only an accent (CTA, thin rule).
2. The swirl avatar is the profile image everywhere. White background by default, `avatar-blue` for dark surfaces.
   Keep the mark inside the centre 58% so circular crops never clip it.
3. One tagline: *We automate your phone calls.*
4. Hashtag starter set ‹confirm›: `#ONDEWO #VoiceAI #ConversationalAI #CallAutomation #ContactCenter #SpeechAI`.
5. Alt text on every image; captions on every video.
6. Every handle, URL and category marked ‹confirm› must be validated by ONDEWO marketing before launch.
7. Platform specs change: verify before upload. Templates are in `brand-kit/social/<platform>/images/`
   and are regenerated, not hand-edited, when the brand changes.

Company details for imprints and About sections: ONDEWO GmbH · Plankengasse 1/5-6 · 1010 Vienna · Austria · VAT: ATU72347427 · Company Reg.: FN473436f.

See also: [brand foundation](../brand-foundation.md) · [voice & tone](../voice-and-tone.md) ·
[colour system](../color-system.md) · [logo guidelines](../logo-guidelines.md).
