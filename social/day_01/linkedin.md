# Day 1 LinkedIn post

Day 1 of 45: rebuilding my robotics foundations, in public.

I've built robots before. PCBs, CAD, controls classes, president of Yale's undergraduate robotics club. What building fast and iterating quietly teaches you is how to route around what you don't fully understand and still ship something that works. I've done that plenty, and it's time to close those gaps properly instead of shipping around them.

So for the next 45 days I'm rebuilding the foundation on purpose, one day at a time: the transform tree, the sense-estimate-plan-act loop, the muscle memory of ROS 2. One lesson a day, one thing that runs, every bug logged publicly. It all converges on a single flagship demo: an autonomous mobile manipulator. A robot that maps a building it has never seen, drives itself around it, then picks up an object and delivers it. Think hospital fetch-and-deliver, entirely in simulation.

The rules, every day with no exceptions:

• watch something visual first (intuition before formalism)
• build something that actually runs
• log what broke, why, and the fix

Today was the foundation: the mental model of what a robot is as a system, plus my first two ROS 2 programs talking to each other (ROS 2 is the open-source nervous system most modern robots run on, and it clicked fast: it's a message bus wearing a lab coat).

Everything is open source and free to steal, notebooks, curriculum, and all: https://github.com/filippo-fonseca/robotics-from-scratch

Day 2 tomorrow.

---

## Alternative hooks

1. "Moving fast lets you skip understanding things fully. Time to stop skipping."
2. "45 days, one build a day, going back to first principles before I go any further."
