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

## Banner system (vintage engineering drawing sheet)

One 1600x900 image per day, generated from `banner.html` (copy the previous day's file, edit the fields), screenshotted headlessly. The identity is an ASME-style engineering drawing sheet; it was chosen after researching AI-design tells (no gradients, no pills/chips, no cards, no centered-symmetric layout, no decorative emoji; asymmetry, print conventions, and content specificity are what read as human).

- Paper `#f5f2e8`, ink `#22201b`, faded ink `#55524a`, faint drafting grid, ONE accent: stamp red `#ab372b`. Never add colors.
- Type: American Typewriter (fallback Courier New) for everything except tiny letterspaced Helvetica caps for cell labels (TITLE, DWG NO., REV...).
- Double border frame (2.5px outer, 1px inner) with zone ticks and letters/numbers along all four edges (4-3-2-1 top/bottom, C-B-A sides).
- Header: series name big slab caps + one-line sub ("A 45-DAY BUILD LOG · SIMULATION ONLY · ALL WORK PUBLIC"). Revision table upper-right (REV / DESCRIPTION / DATE), one row per notable series event.
- Left column: huge "DAY NN/45", the day title in caps, a GENERAL NOTES numbered list (the concept in 3-4 lines, always ending with the GitHub URL as a note), and a parts list table (ITEM / DESCRIPTION / QTY) whose rows are the day's actual components.
- Right column: the day's concept as ink line-art with drafting conventions: dash-dot centerline, numbered leader-line bubbles matching the parts list, italic annotations, an italic "Fig. 1." caption line. This drawing changes daily and is the creative slot.
- Title block bottom-right (the signature element): TITLE, DWG NO. RFS-0NN, SHEET NN OF 45, REV, DATE, SCALE NTS, PHASE, DRAWN BY F. FONSECA YALE '28, SOURCE = repo URL.
- Rotated red boxed stamp upper-right: "BUILT IN PUBLIC / DAY NN".
- No em dashes anywhere on the sheet; separators are "·", commas, or slashes.

### Regenerating

```bash
# serve the folder, then screenshot at exactly 1600x900
.venv/bin/python -m http.server 8899 --bind 127.0.0.1 --directory social
# headless browser: viewport 1600x900 -> save social/day_XX/banner.png
```

Per-day edits in banner.html: day number, title, abstract, chips, the Fig. 1 SVG + caption, the "today:" compass box, and add one `done` class to the next tick.
