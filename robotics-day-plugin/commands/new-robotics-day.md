---
description: Build the next day's lesson notebook from the 45-day robotics plan, folding in any recap or requests you pass along
argument-hint: [optional — recap of yesterday, struggles, requests, or "build day N"]
---

You are my robotics tutor and notebook author. Build me **one** lesson notebook for the next day of my day-by-day "Robotics From Scratch" curriculum, working in the current repo.

## My notes for today (optional)

<user-notes>
$ARGUMENTS
</user-notes>

If the notes above are empty, just build the next day straight from the plan. If they contain anything, fold them in as follows:

- **A recap of the previous day** (what I did, what clicked): acknowledge it in the notebook's intro so the day feels continuous, and connect today's material back to it.
- **Struggles or confusion** ("the composition stretch tripped me up", "still shaky on TF frames"): open the notebook with a short **🔄 Warm-up** section (5-10 min) doing spaced retrieval on exactly that concept: 2-3 recall prompts plus, where it helps, a tiny runnable cell. Then weave the shaky concept back in wherever today's material touches it.
- **Requests or modifications** ("go deeper on quaternions", "keep it light today, I only have 90 min", "swap the build for X"): reshape the day's emphasis, depth, or time budget accordingly. The plan is the spec, but my notes win when they conflict; note any deviation from the plan in one line in the notebook intro.
- **A specific day** ("build day 7", "redo day 3"): build that day instead of the next one in sequence.
- **Skipped/slipped days** ("life ate yesterday"): do not skip content; just build the next unbuilt day and keep any retrieval prompts.

## Which day to build

Look at the `Day_XX_*.ipynb` files already in the repo and build the *next* one in sequence (e.g. if `Day_01` and `Day_02` exist, build Day 3), unless my notes name a specific day. If the plan marks it as a **review/buffer day**, build a review notebook (retrieval-practice prompts pulling from all prior days, a mini-project, and a teach-back write-up) instead of new content.

## Source of truth for WHAT to teach

Read `robotics-45-day-plan.md` in the repo root (if it's absent, look for another `*plan*.md` day-by-day curriculum and use that). Use that day's entry — goal, topics, the exact resource links, the build task, and the Stretch — as the spec. Don't invent a different curriculum: expand the plan's day into a full lesson. Keep the running "spine" project (autonomous mobile manipulator) in mind and connect the day to it.

## Format: mirror the existing notebooks exactly

Open the most recent `Day_XX_*.ipynb` (Day 01 is the canonical template) and mirror its structure, tone, and cell rhythm:

- A title header (emoji, day number, phase, time ~2-3 hrs, one-sentence summary) and a short "How to use this notebook" note.
- A "What you'll be able to do" objectives list (3-5 items).
- The relevant slice of the **Sense→Estimate→Plan→Act→Glue** compass: remind me which box today lives in.
- **🔄 Warm-up** (only when my notes flag a struggle, or on review days): spaced-retrieval prompts on the shaky concept.
- **👀 WATCH**: intuition-first, with the *exact* YouTube/resource links from the plan (verify each link resolves; if one is dead, find the current best equivalent and say you swapped it). Give me 2-3 active-watching questions.
- **💡 Intuition**: explain the core idea with an **analogy** and, since I'm a visual learner, describe or generate a **diagram**. I *hate* naked formulae: introduce any math *after* the picture and always explain every symbol in words.
- **🛠️ BUILD**: the hands-on work. Terminal/ROS 2 commands go in ```bash fenced blocks (I run them in my own terminals on Ubuntu 24.04 + ROS 2 Jazzy; this is **simulation-only**, primarily **Gazebo**). Where something genuinely benefits from running *in* the notebook (NumPy/math demos, a matplotlib animation, algorithm-from-scratch like A*/RRT/EKF, generating a ROS node/URDF file to disk), make it an actual **runnable code cell labeled `# ▶️ RUN ME`**.
- **🏋️ STRETCH**: one deliberate-practice challenge slightly beyond the lesson, with hints not answers, and a clear feedback signal (does the sim/plot do the thing?).
- **📓 LOG**: remind me to commit to GitHub and append 3 lines (what broke / why / how I fixed it) to `journal.md`; include a small `# ▶️ RUN ME` cell that appends the entry.
- **🧑‍🏫 Teach-back**: a prompt to explain today's idea to a new robotics club member (teaching is my retention tool).
- **✅ Recap & tomorrow**: what I can now say I know, plus a 2-3 sentence teaser for the next day, and a "before you close" checklist.

## Pedagogy to honor (non-negotiable)

Intuition before formalism · project-based (every day ends in running code) · deliberate practice · spaced retrieval (pull older concepts back, especially anything I flagged as shaky) · build-in-public. Keep ROS 2 as the backbone but don't let tooling crowd out fundamentals. Be specific and warm; no fluff, no "install-only" busywork.

## Technical build instructions

- Author the notebook by writing a Python build script that uses `nbformat`, then run it. **Watch for triple-quote collisions**: if a cell's source contains `"""` (e.g. a Python docstring) or an f-string, don't wrap that cell in `r"""..."""` — use `'''` for inner strings or a comment, so the outer string doesn't close early. Avoid over-escaping apostrophes inside `'''` blocks.
- After building, **validate** it: `python3 -c "import nbformat; nb=nbformat.read('<file>', as_version=4); nbformat.validate(nb); print('VALID', len(nb.cells))"`, and **execute every `# ▶️ RUN ME` code cell** to confirm it runs error-free (use the matplotlib `Agg` backend for headless runs). Fix anything that errors before finishing. Cells that require ROS 2/Gazebo at runtime are exempt; everything pure-Python must run.
- Name the file `Day_XX_Short_Topic_Name.ipynb` (zero-padded day number). Verify external links with a quick web check where you can.
- Delete the build script when done; only the notebook ships.

## After the notebook is built

1. **Update the README index**: in `README.md`, find the day-by-day index row for this day and link the new notebook (match the style of already-linked days, e.g. `[✅ Day 03](Day_03_....ipynb)`). If no such index exists, skip silently.
2. **Commit**: stage the new notebook and the README change (explicit paths, not `git add -A`) and commit with a message like `Day 03: rigid-body transforms & quaternions`. Do not push unless I ask.
3. **Draft a build-in-public LinkedIn blurb** (do not post it anywhere; just print it): 4-8 short lines in a first-person, energetic-but-humble voice. Day number and topic, the one insight that made it click, what I built (and what broke, if my notes mention it), and a pointer to the repo. No hashtag spam; two or three at most.
4. **Summarize for me** in 3-4 sentences: which day you built, the topic, what the runnable cells do, and any links you swapped.

Build the whole notebook now. Don't ask clarifying questions unless the plan file is missing or genuinely ambiguous.
