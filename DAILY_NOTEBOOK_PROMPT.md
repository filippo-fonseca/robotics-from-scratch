# 📋 Daily Notebook Generator — paste this into Claude Code

**How to use:** open Claude Code in your `robotics-from-scratch` repo folder (the one containing `robotics-45-day-plan.md` and your `Day_XX_*.ipynb` files) and paste everything below the line. By default it builds **the next day** automatically. To force a specific day, replace `THE NEXT DAY` with e.g. `Day 7`.

---

You are my robotics tutor and notebook author. Build me **one** lesson notebook for **`THE NEXT DAY`** of my 45-day "Robotics From Scratch" curriculum.

**Figure out which day to build:** look at the `Day_XX_*.ipynb` files already in this folder and make the *next* one in sequence (e.g. if `Day_01` and `Day_02` exist, build Day 3). If I named a specific day above, build that one instead. If it's a **review/buffer day** in the plan, make a review notebook (retrieval-practice prompts, a mini-project, and a teach-back write-up) instead of new content.

**Your source of truth for WHAT to teach:** read `robotics-45-day-plan.md` in this folder and use that day's entry (goal, topics, the exact resource links, the build task, and the Stretch) as the spec. Don't invent a different curriculum — expand the plan's day into a full lesson. Keep the running "spine" project (autonomous mobile manipulator) in mind and connect the day to it.

**Match the format of `Day_01_Robotics_Stack_and_ROS2_Graph.ipynb` exactly.** Open it and mirror its structure, tone, and cell rhythm:
- A title header (emoji, day number, phase, time ~2–3 hrs, one-sentence summary) and a short "How to use this notebook" note.
- A "What you'll be able to do" objectives list (3–5 items).
- The relevant slice of the **Sense→Estimate→Plan→Act→Glue** compass — remind me which box today lives in.
- **👀 WATCH** — intuition-first, with the *exact* YouTube/resource links from the plan (verify each link resolves; if one is dead, find the current best equivalent and say you swapped it). Give me 2–3 active-watching questions.
- **💡 Intuition** — explain the core idea with an **analogy** and, since I'm a visual learner, describe or generate a **diagram**. I *hate* naked formulae: introduce any math *after* the picture and always explain every symbol in words.
- **🛠️ BUILD** — the hands-on work. Terminal/ROS 2 commands go in ```bash fenced blocks (I run them in my own terminals on Ubuntu 24.04 + ROS 2 Jazzy — this is **simulation-only**, primarily **Gazebo**). Where something genuinely benefits from running *in* the notebook (NumPy/math demos, a matplotlib animation, algorithm-from-scratch like A*/RRT/EKF, generating a ROS node/URDF file to disk), make it an actual **runnable code cell labeled `# ▶️ RUN ME`**.
- **🏋️ STRETCH** — one deliberate-practice challenge slightly beyond the lesson, with hints not answers, and a clear feedback signal (does the sim/plot do the thing?).
- **📓 LOG** — remind me to commit to GitHub and append 3 lines (what broke / why / how I fixed it) to `journal.md`; include a small `# ▶️ RUN ME` cell that appends the entry.
- **🧑‍🏫 Teach-back** — a prompt to explain today's idea to a new Yale Robotics club member (I'm the president; teaching is my retention tool).
- **✅ Recap & tomorrow** — what I can now say I know, plus a 2–3 sentence teaser for the next day, and a "before you close" checklist.

**Pedagogy to honor (non-negotiable):** intuition before formalism · project-based (every day ends in running code) · deliberate practice · spaced retrieval (pull older concepts back on review days) · build-in-public. Keep ROS 2 as the backbone but don't let tooling crowd out fundamentals. Be specific and warm; no fluff, no "install-only" busywork.

**Technical build instructions:**
- Author the notebook by writing a Python build script that uses `nbformat` (like the one that made Day 1), then run it. **Watch for triple-quote collisions**: if a cell's source contains `"""` (e.g. a Python docstring) or an f-string, don't wrap that cell in `r"""..."""` — use `'''` for inner strings or a comment, so the outer string doesn't close early. Avoid over-escaping apostrophes inside `'''` blocks.
- After building, **validate** it: `python3 -c "import nbformat; nb=nbformat.read('<file>', as_version=4); nbformat.validate(nb); print('VALID', len(nb.cells))"`, and **execute every `# ▶️ RUN ME` code cell** to confirm it runs error-free (use the matplotlib `Agg` backend for headless runs). Fix anything that errors before finishing.
- Name the file `Day_XX_Short_Topic_Name.ipynb` (zero-padded day number). Verify any external links with a quick web check where you can.
- When done, give me a 3–4 sentence summary: which day you built, the topic, what the runnable cells do, and any links you had to swap.

Build the whole notebook now — don't ask me clarifying questions unless the plan file is missing or genuinely ambiguous.
