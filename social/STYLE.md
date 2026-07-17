# Build-in-public style guide

One post per day on LinkedIn and X, plus one banner image. Same skeleton every day; consistency is the engine of the format. Files live in `social/day_XX/` as `linkedin.md`, `x.md`, `banner.html`, `banner.png`.

## Post rules (both platforms)

1. First line is the hook AND the counter: "Day N of 45: ..." (X: "day N/45 of ..."). No throat-clearing before it.
2. One concrete artifact per post, named specifically (the thing that ran, the algorithm implemented, the demo gif). Never vague "learned a lot."
3. Day 1 explained the whole concept; every later day gets ONE line of series context max ("45 days, one build a day, all open source"), then goes straight to today.
4. Keep the day's specifics light: what it was and why it matters, not a tutorial. The repo link carries the detail.
5. One honest human moment per post: the bug, the confusion, the thing that took three tries. Pull it from `journal.md`.
6. Every post links the repo (or the day's notebook directly): https://github.com/filippo-fonseca/robotics-from-scratch
7. Zero hashtags. Zero or one emoji. No em dashes, ever; use commas, colons, periods, parentheses.
8. Close with continuity: "Day N+1 tomorrow." X adds "follow to keep up."
9. Length: LinkedIn 6-10 short paragraphs max, X under ~600 characters. Milestone days (25, 36, 42) can run longer and lead with the demo video.
10. LinkedIn is sentence case and full sentences; X is lowercase and looser. Same substance, different register.

## Banner system ("academic paper x Notion")

One 1600x900 image per day, generated from `banner.html` (copy the previous day's file, edit the fields), screenshotted headlessly. The identity:

- Warm paper background `#faf7f1`, faint dot lattice, ink `#1c1b18`, graphite `#6b675e`, ONE accent: annotation crimson `#a33327`. Never add colors.
- Serif everything (Charter/Georgia), like a journal cover. Mono (SF Mono/Menlo) only for code-ish strings: topic names, the GitHub URL, counters.
- Masthead: "Robotics from Scratch" left, "A 45-DAY FIELD LOG · BUILT IN PUBLIC" right, double rule under it.
- Giant serif day number ("01") with italic "of 45", then the day title (one italic word for emphasis), then a 2-line abstract with a crimson left border.
- Notion-style tag chips: crimson chip = phase ("Phase A · Foundations"), gray chips = topic tags.
- Right side: "Fig. 1", the day's concept as an ink diagram in a thin-bordered box, with a real academic caption ("Fig. 1. ...") and an italic margin note inside the figure. This diagram changes daily and is the creative slot.
- Footer: compass line "Sense → Estimate → Plan → Act" with "today: <box>" underlined in crimson (which of the five boxes today's topic belongs to), GitHub URL, and the 45-tick progress row with completed days filled crimson.

### Regenerating

```bash
# serve the folder, then screenshot at exactly 1600x900
.venv/bin/python -m http.server 8899 --bind 127.0.0.1 --directory social
# headless browser: viewport 1600x900 -> save social/day_XX/banner.png
```

Per-day edits in banner.html: day number, title, abstract, chips, the Fig. 1 SVG + caption, the "today:" compass box, and add one `done` class to the next tick.
