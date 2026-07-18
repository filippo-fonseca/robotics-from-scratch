# 🤖 Robotics From Scratch

**45 days. One notebook a day. From "robotics-adjacent" to proper roboticist, in public.**

I'm Filippo, a MechE + EECS student at Yale ('28) and president of [Yale Undergraduate Robotics](https://yaleundergraduaterobotics.org). I have the pieces most people are missing (software, CAD, EE, controls classes), but I've never built the connective tissue of robotics as a discipline: the transform tree in my head, the sense→plan→act loop in my hands, the muscle memory of ROS 2. This repo is me fixing that, one day at a time, with every notebook, every bug, and every demo committed publicly.

**Follow along:** I post daily-ish progress on [LinkedIn](https://www.linkedin.com/in/filippo-fonseca/). The full curriculum lives in [`robotics-45-day-plan.md`](robotics-45-day-plan.md).

---

## The rules

Every single day, no exceptions:

1. **Watch** something visual first (~30-45 min). Intuition before formalism, always.
2. **Grasp** the idea in my own words, plus one formula explained symbol by symbol.
3. **Build** something that runs (~60-75 min). No passive days. No "just install" days.
4. **Stretch**: one deliberate-practice challenge slightly beyond comfort.
5. **Log**: commit to GitHub and write 3 lines in [`journal.md`](journal.md): what broke, why, how I fixed it.

The stack: **Ubuntu 24.04 + ROS 2 Jazzy + Gazebo Harmonic**, simulation only. Notebooks hold the lesson, the from-scratch algorithm implementations (NumPy, matplotlib animations), and the commands I run in real terminals.

## The compass

Everything in robotics slots into one of five boxes. When a topic feels disconnected, ask "which box is this?"

```
SENSE → ESTIMATE → PLAN → ACT
   └────── GLUE (transforms: TF2, URDF, the ROS 2 graph) ──────┘
```

## The spine project

The whole plan converges on one flagship demo built entirely in simulation: an **autonomous mobile manipulator**. A wheeled base maps an unknown world (SLAM), navigates it autonomously (Nav2), then uses a 6-DOF arm (MoveIt 2) to perceive, pick, and deliver an object. Healthcare framing: a hospital fetch-and-deliver robot, a clean line toward my long-term interest in surgical and cardio robotics.

- **Day 25** 🏁 autonomous mobile base milestone
- **Day 36** 🦾 pick-and-place milestone
- **Day 42** 🚀 the full loop, end to end

## Day-by-day index

Notebooks get linked here as they ship. Unlinked days are still ahead of me.

### Phase 0 — Environment setup (the evening before, not a whole day)

| Day | Topic | Notebook |
|----:|-------|----------|
| 0 | ✅ Ubuntu 24.04 + ROS 2 Jazzy installed, verified with the talker/listener demo, `gh` set up, repo live | — (no notebook, per the plan) |

### Phase A — Foundations: math intuition, ROS 2 core, transforms (Days 1-8)

| Day | Topic | Notebook |
|----:|-------|----------|
| 1 | The robotics stack + your first ROS 2 graph | [✅ Day 01](Day_01_Robotics_Stack_and_ROS2_Graph.ipynb) |
| 2 | Linear algebra you can see: rotations & vectors | |
| 3 | Rigid-body transforms & quaternions | |
| 4 | ROS 2 nodes, topics, pub/sub (deep) | |
| 5 | Services, parameters, launch files, colcon | |
| 6 | TF2: the transform tree | |
| 7 | Review · retrieve · teach-back | |
| 8 | URDF: describing a robot | |

### Phase B — Simulation, the mobile base & control (Days 9-16)

| Day | Topic | Notebook |
|----:|-------|----------|
| 9 | Gazebo simulation basics | |
| 10 | Sensors in simulation (LiDAR, depth, IMU, odom) | |
| 11 | ros2_control: actually driving the wheels | |
| 12 | Diff-drive kinematics & odometry from scratch | |
| 13 | Feedback control: PID intuition | |
| 14 | Review + mini-project: drive a perfect square | |
| 15 | Motion planning I: A* / Dijkstra from scratch | |
| 16 | Motion planning II: RRT / RRT* | |

### Phase C — Autonomy: state estimation, SLAM, Nav2 (Days 17-25)

| Day | Topic | Notebook |
|----:|-------|----------|
| 17 | Bayes filter → Kalman intuition | |
| 18 | EKF localization from scratch | |
| 19 | SLAM intuition | |
| 20 | SLAM in ROS 2 with slam_toolbox | |
| 21 | Review · retrieve · teach-back | |
| 22 | Nav2 architecture | |
| 23 | Nav2 bring-up on my robot | |
| 24 | Nav2 tuning + programmatic goals | |
| 25 | 🏁 **Milestone: autonomous mobile robot** | |

### Phase D — Manipulation: arms, kinematics, IK, MoveIt 2 (Days 26-36)

| Day | Topic | Notebook |
|----:|-------|----------|
| 26 | Arm kinematics intuition: DOF, C-space | |
| 27 | Forward kinematics from scratch | |
| 28 | Review · retrieve · teach-back | |
| 29 | Inverse kinematics I: analytic | |
| 30 | Inverse kinematics II: Jacobian-based | |
| 31 | The Jacobian: velocity kinematics & singularities | |
| 32 | Model a 6-DOF arm in simulation | |
| 33 | MoveIt 2 I: setup & planning | |
| 34 | MoveIt 2 II: programmatic pick-and-place | |
| 35 | Review · retrieve · teach-back | |
| 36 | 🦾 **Milestone: grasping + the manipulation frontier** | |

### Phase E — Perception, integration, capstone & the frontier (Days 37-45)

| Day | Topic | Notebook |
|----:|-------|----------|
| 37 | Perception basics: cameras, depth, point clouds | |
| 38 | From perception to a graspable pose | |
| 39 | Mobile manipulator: architecture & orchestration | |
| 40 | 🚀 Capstone 1: navigate to the station | |
| 41 | 🚀 Capstone 2: perceive + pick | |
| 42 | 🚀 **Capstone 3: deliver + the full loop** | |
| 43 | The frontier: learning-based robotics (RL, Isaac) | |
| 44 | Ship it like a series: docs & teaching | |
| 45 | Reflection & the road ahead | |

## How the notebooks get made: the `/new-robotics-day` plugin

Each day's notebook is generated by a small open-source **Claude Code plugin** that lives in this repo ([`robotics-day-plugin/`](robotics-day-plugin/)). It reads the 45-day plan, figures out which day is next from the `Day_XX_*.ipynb` files already present, and authors a full lesson notebook in the exact style of Day 01: intuition-first, runnable `# ▶️ RUN ME` cells, a Stretch challenge, and a teach-back prompt. It also updates the index above and drafts a short build-in-public blurb for LinkedIn.

```text
# next day in sequence, no notes
/new-robotics-day

# with a recap of yesterday + requests for today
/new-robotics-day Day 2 recap: the rotation-composition stretch tripped me up,
I want a 10-min warm-up on it. Also go deeper on quaternions vs Euler angles.

# force a specific day
/new-robotics-day build day 7
```

Anything you pass in gets folded into the lesson: struggles become spaced-retrieval warm-ups, requests reshape the day's emphasis, and schedule slips just shift the plan without skipping the retrieval.

**Install it** (this repo doubles as a Claude Code plugin marketplace):

```bash
/plugin marketplace add https://github.com/filippo-fonseca/robotics-from-scratch.git
/plugin install robotics-day@robotics-from-scratch
```

It is deliberately curriculum-agnostic in shape: fork this repo, swap in your own `robotics-45-day-plan.md` (or any day-by-day plan), and the same command will build *your* series.

## Repo structure

```text
robotics-from-scratch/
├── README.md                      ← you are here (index updates daily)
├── robotics-45-day-plan.md        ← the full curriculum + resource library
├── journal.md                     ← daily debug log: what broke, why, the fix
├── DAILY_NOTEBOOK_PROMPT.md       ← the original prompt the plugin grew out of
├── Day_XX_<topic>.ipynb           ← one lesson notebook per day
└── robotics-day-plugin/           ← the /new-robotics-day Claude Code plugin
```

## Why in public

Two reasons. Accountability: a public checkbox table is very hard to abandon quietly. And the protégé effect: as club president I turn every review day into teach-back material, so this repo doubles as the Yale Undergraduate Robotics onboarding track I wish existed.

If you're on a similar path (strong software or hardware background, missing the robotics connective tissue), fork it, follow along, or just steal the plan. Issues and PRs welcome.

## License

[MIT](LICENSE). The plan, notebooks, and plugin are all free to reuse and adapt.
