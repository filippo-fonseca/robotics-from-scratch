# 🤖📅 robotics-day — a Claude Code plugin

One command, **`/new-robotics-day`**, that authors the next daily lesson notebook of a day-by-day robotics curriculum. Built for (and by) the [Robotics From Scratch](https://github.com/filippo-fonseca/robotics-from-scratch) 45-day build-in-public series, but curriculum-agnostic in shape: point it at any repo with a day-by-day `*plan*.md` and per-day `Day_XX_*.ipynb` notebooks.

## What it does

Each invocation:

1. Figures out the next unbuilt day from the `Day_XX_*.ipynb` files in the repo (or builds the day you name).
2. Reads the plan file as the spec for what to teach, and the latest existing notebook as the style template.
3. Folds in whatever you pass as arguments: recaps become continuity, struggles become spaced-retrieval warm-ups, requests reshape the day's depth and emphasis.
4. Authors and validates the notebook (`nbformat`), executing every runnable cell headlessly before shipping.
5. Updates the README's day index, makes a focused git commit, and drafts a short build-in-public LinkedIn blurb.

## Usage

```text
/new-robotics-day
/new-robotics-day Day 2 recap: rotation composition tripped me up, warm me up on it. Go deeper on quaternions today.
/new-robotics-day build day 7
/new-robotics-day only have 90 min today, keep the build lean
```

Depending on your Claude Code setup the command may be namespaced: `/robotics-day:new-robotics-day`.

## Install

From the marketplace bundled in the parent repo:

```text
/plugin marketplace add https://github.com/filippo-fonseca/robotics-from-scratch.git
/plugin install robotics-day@robotics-from-scratch
```

Or for local development:

```bash
claude --plugin-dir ./robotics-day-plugin
```

## Adapting it to your own series

Fork the parent repo (or copy this directory), replace `robotics-45-day-plan.md` with your own day-by-day plan, and hand-craft your Day 01 notebook as the style anchor. Everything else (pedagogy defaults, cell structure, validation) transfers as-is; edit `commands/new-robotics-day.md` to taste.

MIT licensed, like the parent repo.
