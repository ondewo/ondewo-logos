"""Platform specs, profile copy and content guidelines for the ONDEWO social kits.

Data only - rendering lives in build_social.py. Specs are recommendations taken
from each platform's public guidance at the time of writing; platforms change
them often, so every README tells the reader to verify before uploading.
Anything not confirmed by ONDEWO marketing is marked with the confirm tag.
"""
from __future__ import annotations

CONFIRM = "\u2039confirm\u203a"  # the kit's marker for unconfirmed facts

TAGLINE = "We automate your phone calls."
ONE_LINER = (
    "ONDEWO builds voice-first conversational AI that automates phone conversations "
    "\u2014 multilingual, scalable, and deployable on your own infrastructure."
)
BOILERPLATE = (
    "ONDEWO is a conversational-AI company that automates phone calls. Its modular platform "
    "\u2014 speech-to-text, text-to-speech, dialogue, and telephony integration \u2014 lets "
    "enterprises answer every call, in any language, 24/7, while keeping full control of their "
    "data through on-premise deployment."
)

# asset tuple: (file stem, width, height, template, what it is for, alt text)
# templates: avatar | avatar-blue | cover | post | story | highlight
# story assets carry safe-zone insets (top, bottom) in px as the 7th item.
PLATFORMS: dict[str, dict] = {
    "linkedin": {
        "name": "LinkedIn",
        "category": "Social network (B2B)",
        "role": "Primary B2B channel: thought leadership, product news, hiring, events.",
        "handle": "linkedin.com/company/ondewo " + CONFIRM,
        "assets": [
            ("avatar", 400, 400, "avatar", "Company logo (cropped to a rounded square / circle)", "ONDEWO swirl logomark on white"),
            ("avatar-blue", 400, 400, "avatar-blue", "Alternative logo for dark-mode / event pages", "ONDEWO swirl logomark in white on blue"),
            ("cover", 1128, 191, "cover", "Company page cover", "ONDEWO logo and tagline 'We automate your phone calls.' on blue"),
            ("cover-personal", 1584, 396, "cover", "Employee / founder profile cover", "ONDEWO logo and tagline on blue"),
            ("post-landscape", 1200, 627, "post", "Link and single-image post (1.91:1)", "ONDEWO post template with headline placeholder"),
            ("post-square", 1080, 1080, "post", "Single-image post (1:1)", "ONDEWO square post template"),
            ("carousel-slide", 1080, 1350, "post", "Document / carousel slide (4:5)", "ONDEWO carousel slide template"),
        ],
        "specs": [
            ("Company logo", "400 \u00d7 400 px, square PNG; keep the mark inside the centre 70%"),
            ("Company cover", "1128 \u00d7 191 px (personal profile cover: 1584 \u00d7 396 px)"),
            ("Image post", "1200 \u00d7 627 (1.91:1), 1080 \u00d7 1080 (1:1) or 1080 \u00d7 1350 (4:5)"),
            ("Carousel / document", "PDF, 1080 \u00d7 1350 portrait slides, \u2264 10 slides recommended"),
            ("Post length", "\u2248 600\u20131,300 characters; the hook must fit in the first \u2248 140 before \u2018see more\u2019"),
            ("Hashtags", "3\u20135, at the end of the post"),
        ],
        "profile": [
            ("Page name", "ONDEWO", 100),
            ("Tagline (\u2264 120)", "Voice-first conversational AI. " + TAGLINE, 120),
            ("About (\u2264 2,000)", ONE_LINER + "\n\n" + BOILERPLATE, 2000),
            ("Custom button", "Book a demo", None),
            ("Industry / size", "Software Development \u00b7 " + CONFIRM, None),
        ],
        "tone": "Insightful, professional, lightly bold. One idea per post, short sentences, white space between thoughts.",
        "hooks": ["Hold music, retired.", "Answer every call, around the clock.", "A stat or a pointed question about call volume."],
        "do": [
            "Lead with a stat, a retired-pain line or a pointed question",
            "Link in the post or first comment, one verb-first CTA",
            "Add alt text to every image (\u2018ONDEWO \u2026\u2019 describing what is shown)",
            "Tag partners and customers only with written permission",
        ],
        "dont": [
            "Use banned hype words (revolutionary, disruptive, magic, world-class) without proof",
            "Post a wall of hashtags or engagement-bait polls",
            "Cut the logo off or use the white-background avatar on a photo",
        ],
    },
    "facebook": {
        "name": "Facebook",
        "category": "Social network",
        "role": "Reach for events, webinars, employer brand and community updates.",
        "handle": "facebook.com/ondewo " + CONFIRM,
        "assets": [
            ("avatar", 720, 720, "avatar", "Page profile picture (shown as a circle)", "ONDEWO swirl logomark on white"),
            ("avatar-blue", 720, 720, "avatar-blue", "Alternative profile picture", "ONDEWO swirl logomark in white on blue"),
            ("cover", 820, 312, "cover", "Page cover (mobile crops to the centre \u2248 640 \u00d7 360)", "ONDEWO logo and tagline on blue"),
            ("post-landscape", 1200, 630, "post", "Link / image post (1.91:1)", "ONDEWO post template with headline placeholder"),
            ("post-square", 1080, 1080, "post", "Feed image (1:1)", "ONDEWO square post template"),
            ("story", 1080, 1920, "story", "Story / Reel (9:16)", "ONDEWO story template with headline placeholder", (250, 340)),
            ("event-cover", 1920, 1005, "post", "Event cover (webinars)", "ONDEWO event cover template"),
        ],
        "specs": [
            ("Profile picture", "Upload \u2265 320 \u00d7 320 px (shown at 170 px on desktop, circular crop)"),
            ("Cover photo", "820 \u00d7 312 px; keep logo and text in the centre 640 px for mobile"),
            ("Feed image", "1200 \u00d7 630 (link share) or 1080 \u00d7 1080 / 1080 \u00d7 1350"),
            ("Story / Reel", "1080 \u00d7 1920 (9:16); keep text \u2265 250 px from the top and \u2265 340 px from the bottom"),
            ("Event cover", "1920 \u00d7 1005 px"),
            ("Post length", "Short: 40\u201380 characters perform best; hard limit is far higher"),
        ],
        "profile": [
            ("Page name", "ONDEWO", 75),
            ("Intro (\u2264 101)", TAGLINE + " Voice AI, multilingual and on-premise.", 101),
            ("Description", ONE_LINER, 255),
            ("Category", "Software Company \u00b7 " + CONFIRM, None),
            ("Call to action", "Book a demo / Contact us", None),
        ],
        "tone": "Friendly-professional and concrete. Shorter than LinkedIn; lead with the benefit.",
        "hooks": ["Waiting on hold is obsolete.", "See ONDEWO live: join our next webinar.", "Every call answered, in any language."],
        "do": ["Use the event cover for every webinar", "Keep captions short, link in the post", "Reply to comments within one working day"],
        "dont": ["Paste LinkedIn copy unchanged", "Place text in the outer 90 px of the cover (mobile crop)", "Use more than 2 hashtags"],
        "note": "The repository root already contains the legacy `ondewo_facebook_profile.png`; the generated avatar replaces it.",
    },
    "instagram": {
        "name": "Instagram",
        "category": "Social network (visual)",
        "role": "Employer brand, behind-the-scenes, short explainers and event highlights.",
        "handle": "@ondewo " + CONFIRM,
        "assets": [
            ("avatar", 720, 720, "avatar", "Profile picture (circular crop)", "ONDEWO swirl logomark on white"),
            ("avatar-blue", 720, 720, "avatar-blue", "Alternative profile picture", "ONDEWO swirl logomark in white on blue"),
            ("post-portrait", 1080, 1350, "post", "Feed post and carousel slide (4:5)", "ONDEWO portrait post template"),
            ("post-square", 1080, 1080, "post", "Feed post (1:1)", "ONDEWO square post template"),
            ("story", 1080, 1920, "story", "Story / Reel cover (9:16)", "ONDEWO story template with headline placeholder", (250, 340)),
            ("highlight-cover", 1080, 1920, "highlight", "Story highlight cover (swirl centred)", "ONDEWO swirl logomark on blue"),
        ],
        "specs": [
            ("Profile picture", "Upload 720 \u00d7 720+ px square (displays at 110 px, circular)"),
            ("Feed post / carousel", "1080 \u00d7 1350 (4:5, preferred), 1080 \u00d7 1080 (1:1)"),
            ("Story / Reel", "1080 \u00d7 1920 (9:16); text \u2265 250 px from top and \u2265 340 px from bottom"),
            ("Highlight cover", "1080 \u00d7 1920 with the icon in the centre circle"),
            ("Bio", "\u2264 150 characters, one link"),
            ("Caption", "\u2248 125 characters before \u2018more\u2019; \u2264 2,200 total; 5\u201310 hashtags (may sit in the first comment)"),
        ],
        "profile": [
            ("Name", "ONDEWO \u2013 Voice AI", 64),
            ("Bio (\u2264 150)", TAGLINE + "\nVoice-first conversational AI\nMultilingual \u00b7 on-premise", 150),
            ("Link", "ondewo.com " + CONFIRM, None),
            ("Category", "Software Company \u00b7 " + CONFIRM, None),
            ("Contact button", "Email / Book a demo", None),
        ],
        "tone": "Visual-led and human. The image carries the idea; the caption supports it. Emoji sparingly.",
        "hooks": ["Hold music, retired.", "One call. Any language.", "Meet the team behind the voice."],
        "do": ["One idea per slide on carousels", "Burn captions into video", "Use highlight covers for Product, Events, Team, Careers"],
        "dont": ["Put the logo in the bottom 340 px of a story", "Use filters that shift brand colours", "Use stock photos of headset call-centre clich\u00e9s"],
    },
    "tiktok": {
        "name": "TikTok",
        "category": "Short-form video",
        "role": "Employer brand and short, human explainers. Educational, never salesy. " + CONFIRM,
        "handle": "@ondewo " + CONFIRM,
        "assets": [
            ("avatar", 720, 720, "avatar", "Profile photo (circular crop)", "ONDEWO swirl logomark on white"),
            ("avatar-blue", 720, 720, "avatar-blue", "Alternative profile photo", "ONDEWO swirl logomark in white on blue"),
            ("video-cover", 1080, 1920, "story", "Video cover / end card (9:16)", "ONDEWO video cover template with headline placeholder", (130, 480)),
            ("photo-mode", 1080, 1350, "post", "Photo-mode carousel slide (4:5)", "ONDEWO portrait slide template"),
        ],
        "specs": [
            ("Profile photo", "Upload \u2265 200 \u00d7 200 px square (we supply 720 \u00d7 720); circular crop"),
            ("Video", "1080 \u00d7 1920 (9:16), MP4/MOV; 15\u201360 s works best for B2B explainers"),
            ("Safe zone", "Keep text \u2265 130 px from the top and \u2265 480 px from the bottom (caption, buttons, sound label overlay)"),
            ("Bio", "\u2264 80 characters, one link"),
            ("Caption", "\u2264 4,000 characters; the first line is the hook; 3\u20135 hashtags"),
        ],
        "profile": [
            ("Display name", "ONDEWO", 30),
            ("Username", "@ondewo " + CONFIRM, 24),
            ("Bio (\u2264 80)", TAGLINE + " Voice AI, explained.", 80),
            ("Link", "ondewo.com " + CONFIRM, None),
        ],
        "tone": "Plain-spoken and quick; a calm expert who gets to the point in 2 seconds. Playfulness stays low (3/10).",
        "hooks": ["What happens in the 30 seconds after you call a hotline?", "Hold music, retired.", "Voice AI in 20 seconds."],
        "do": ["Hook in the first 2 seconds", "Burn in captions and keep logo end card \u2265 1.5 s", "Show real product screens (no fake demos)"],
        "dont": ["Use trending audio that implies endorsement", "Show real customer calls or personal data", "Speak in jargon without a one-line explanation"],
    },
    "bitbucket": {
        "name": "Bitbucket",
        "category": "Source hosting (developer)",
        "role": "Public/partner repositories and internal code: consistent workspace identity and READMEs.",
        "handle": "bitbucket.org/ondewo " + CONFIRM,
        "assets": [
            ("avatar", 256, 256, "avatar", "Workspace / project / repository avatar", "ONDEWO swirl logomark on white"),
            ("avatar-blue", 256, 256, "avatar-blue", "Alternative avatar for dark themes", "ONDEWO swirl logomark in white on blue"),
            ("readme-header", 1280, 320, "cover", "Header image at the top of a repository README", "ONDEWO logo and tagline on blue"),
        ],
        "specs": [
            ("Avatar", "Square PNG, \u2265 128 \u00d7 128 (we supply 256 \u00d7 256); shown in small circles/squares, so the mark must stay centred"),
            ("README header", "1280 \u00d7 320 px (4:1), referenced from the README as a relative image"),
            ("Badges", "Use brand blue `004C87` for the badge colour (see snippets in the README)"),
        ],
        "profile": [
            ("Workspace name", "ONDEWO", 255),
            ("Workspace description", "Voice-first conversational AI. " + TAGLINE, 255),
            ("Repository description", "ONDEWO <product>: <what it does in one line>", None),
        ],
        "tone": "Exact and engineering-led. Real terms, real numbers, copy-paste examples.",
        "hooks": [],
        "do": ["Start every README with the header image, then a one-line description", "Name products `ONDEWO CAI`, `ONDEWO S2T` (all-caps)", "Document install, quick start and API links first"],
        "dont": ["Recolour or stretch the header", "Use marketing superlatives in technical docs", "Commit large generated PNGs on every build"],
        "snippet": (
            "```markdown\n"
            "![ONDEWO](docs/images/readme-header.png)\n\n"
            "# ONDEWO <Product>\n\n"
            "> We automate your phone calls.\n\n"
            "![Status](https://img.shields.io/badge/status-stable-004C87)\n"
            "```"
        ),
    },
    "jira": {
        "name": "Jira",
        "category": "Work management (internal / partner)",
        "role": "Consistent project identity and clear, calm ticket writing.",
        "handle": "<site>.atlassian.net " + CONFIRM,
        "assets": [
            ("avatar", 256, 256, "avatar", "Site logo and project avatar", "ONDEWO swirl logomark on white"),
            ("avatar-blue", 256, 256, "avatar-blue", "Project avatar variant (e.g. to tell products apart)", "ONDEWO swirl logomark in white on blue"),
            ("dashboard-banner", 1280, 320, "cover", "Banner for dashboards and board descriptions", "ONDEWO logo and tagline on blue"),
        ],
        "specs": [
            ("Site / project avatar", "Square PNG, supply 256 \u00d7 256 (displayed from 24 px up)"),
            ("Dashboard banner", "1280 \u00d7 320 px, added via a text gadget with an image attachment"),
            ("Status lozenges", "Do not recolour: Jira fixes them. Use brand colours for labels, dashboards and attachments only"),
            ("Ticket title", "Verb-first, \u2264 80 characters, sentence case"),
        ],
        "profile": [
            ("Project name", "ONDEWO <Product> " + CONFIRM, None),
            ("Project key", "Short, all-caps (e.g. CAI, S2T, T2S) " + CONFIRM, None),
            ("Project description", "Work for ONDEWO <Product>. We automate your phone calls.", None),
        ],
        "tone": "Clear, precise, calm. State the problem, expected vs actual behaviour and how to reproduce.",
        "hooks": [],
        "do": ["Write titles as actions: \u2018Add gRPC health check\u2019", "Use the same product names as the website", "Link design assets from `brand-kit/` instead of attaching copies"],
        "dont": ["Use ALL-CAPS for emphasis (only the ONDEWO name)", "Attach screenshots with customer data", "Use red/green colour alone to convey status"],
    },
    "confluence": {
        "name": "Confluence",
        "category": "Documentation (internal / partner)",
        "role": "Spaces, runbooks and how-to guides in the ONDEWO voice.",
        "handle": "<site>.atlassian.net/wiki " + CONFIRM,
        "assets": [
            ("avatar", 256, 256, "avatar", "Space icon / site logo", "ONDEWO swirl logomark on white"),
            ("avatar-blue", 256, 256, "avatar-blue", "Space icon variant", "ONDEWO swirl logomark in white on blue"),
            ("page-banner", 1920, 400, "cover", "Page header / cover image", "ONDEWO logo and tagline on blue"),
        ],
        "specs": [
            ("Space icon", "Square PNG, supply 256 \u00d7 256"),
            ("Page header image", "1920 \u00d7 400 px (wide banner, keep content in the left 60%)"),
            ("Panels", "Info = blue-50 `#EBF1F5` with `#004C87`; note/important = magenta accent sparingly; success `#1E7A4B`, warning `#B5710A`, error `#C02626`"),
            ("Page title", "Sentence case, \u2264 60 characters"),
        ],
        "profile": [
            ("Space name", "ONDEWO <Team> " + CONFIRM, None),
            ("Space key", "Short all-caps " + CONFIRM, None),
            ("Space description", "Documentation for ONDEWO <Team>. We automate your phone calls.", None),
        ],
        "tone": "Instructional and precise. Lead with what the reader will achieve; numbered steps; one task per page.",
        "hooks": [],
        "do": ["Start pages with a one-sentence summary", "Use headings H2/H3 only, short paragraphs and tables for specs", "Add alt text to every image"],
        "dont": ["Paste raw logs without a summary", "Use more than one panel colour per page", "Leave `\u2039confirm\u203a` items unresolved in published pages"],
    },
    "roblox": {
        "name": "Roblox",
        "category": "Gaming platform (experimental)",
        "role": (
            "Optional, experimental channel for virtual events and recruiting. ONDEWO is a B2B voice-AI company, "
            "so presence is limited to a verified group and carefully scoped experiences. " + CONFIRM
        ),
        "handle": "ONDEWO (group) " + CONFIRM,
        "assets": [
            ("avatar", 512, 512, "avatar", "Group icon / experience icon", "ONDEWO swirl logomark on white"),
            ("avatar-blue", 512, 512, "avatar-blue", "Alternative icon", "ONDEWO swirl logomark in white on blue"),
            ("thumbnail", 1920, 1080, "post", "Experience thumbnail (16:9)", "ONDEWO experience thumbnail template"),
        ],
        "specs": [
            ("Group / experience icon", "512 \u00d7 512 px square PNG (displayed small; keep the mark centred and large)"),
            ("Experience thumbnail", "1920 \u00d7 1080 px (16:9), min 1280 \u00d7 720"),
            ("Audience", "Includes minors: all content must be age-appropriate and follow Roblox Community Standards"),
        ],
        "profile": [
            ("Group name", "ONDEWO", None),
            ("Group description", ONE_LINER + " Official ONDEWO group. " + CONFIRM, 1000),
            ("Experience title", "ONDEWO <event or demo name> " + CONFIRM, 50),
        ],
        "tone": "Friendly, simple and safe. Short sentences; no jargon; no data collection.",
        "hooks": [],
        "do": [
            "Get written approval from ONDEWO marketing and legal before publishing anything",
            "Keep the logo flat and unaltered on any in-world signage",
            "Use only synthetic demo voices and scripts",
        ],
        "dont": [
            "Record or process voice from players, especially minors",
            "Apply the logo to avatar items, clothing or UGC without approval",
            "Imply endorsement by Roblox",
        ],
    },
}
