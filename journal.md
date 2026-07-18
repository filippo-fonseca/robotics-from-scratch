# 🛠️ Debug journal

Three lines a day: what broke, why, how I fixed it. This becomes my personal robotics reference.

---

## Day 0 — 2026-07-17

- **What broke:** `sudo` kept failing with "a terminal is required to read the password" when installing `gh` and Gazebo/pip through Claude Code's command runner, even with a heredoc script.
- **Why:** Claude Code's shell execution doesn't attach a real TTY, so anything needing an interactive password prompt (`sudo`) silently has nowhere to read it from.
- **How I fixed it:** ran the install scripts myself in an actual terminal window instead of through the assistant; everything installed cleanly once `sudo` had a real prompt to talk to. ROS 2 Jazzy was already on the machine — verified it with the `talker`/`listener` demo (listener logged `I heard: [Hello World: N]`), confirming the ROS 2 graph works end to end before Day 1.

---
