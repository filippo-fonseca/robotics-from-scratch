# Robotics From Scratch — A 45-Day Ground-Up Plan

*A day-by-day, project-first curriculum to close the gaps between "robotics-adjacent" and "proper roboticist."*

**Built for:** Filippo — MechE (ABET) + EECS '28 @ Yale, President of Yale Undergraduate Robotics, strong software / CAD / EE / PCB background, soft-robotics lab, north star = autonomous robots → surgical / cardio devices.
**Your constraints (baked into every day):** ~2–3 focused hrs/day · simulation-only · balanced across **manipulator arms + autonomous mobile robots + fundamentals** · **ROS 2 as the backbone** (deep, but not the entire point) · visual-first, intuition-before-formulae learner.

---

## 0. How to read this plan (read this first — 5 min)

You already have the hard-won pieces most people lack: real software chops, CAD, EE, controls exposure from classes. What you're missing is the *connective tissue* of robotics as a discipline — the transform tree in your head, the sense→plan→act loop in your hands, and the muscle memory of ROS 2. This plan is engineered to install exactly that, and nothing you already own.

### The one-sentence philosophy
> **Every single day you will watch something visual to get the intuition, then build something small that runs, then push it to GitHub.** No passive days. No "just install" days.

### The mental model of the whole field (your compass for 45 days)
A robot is a loop: **Sense → Estimate → Plan → Act**, glued together by a shared notion of *where everything is* (transforms). Almost everything you'll learn slots into one of those five boxes:

- **Sense** — cameras, LiDAR, IMU, encoders (Days 10, 37–38)
- **Estimate** — odometry, Kalman/EKF, SLAM (Days 12, 17–20)
- **Plan** — path/motion planning, A*, RRT, Nav2, MoveIt (Days 15–16, 22–24, 29–34)
- **Act** — controllers, PID, ros2_control, inverse kinematics (Days 11, 13, 29–31)
- **Glue** — TF2, URDF, the ROS 2 graph (Days 4–8)

Keep this diagram taped above your desk. When a topic feels disconnected, ask "which box is this?"

### The learning science this plan is built on (why it's shaped this way)
You asked me to use pedagogy, so here's what's actually driving the structure — not decoration, it's load-bearing:

1. **Intuition before formalism.** Cognitive-load research says symbols land only once you have a mental picture to hang them on. Every math day starts with a *visual* explainer (3Blue1Brown, StatQuest-style channels, MATLAB Tech Talks), *then* the equations, *then* code. You explicitly hate naked formulae — so we never lead with them.
2. **Project-based / learning-by-building.** Retention from "read about it" is a fraction of "built it and it broke and you fixed it." Every day ends in running code.
3. **Deliberate practice.** Each day has a **Stretch** — a task slightly beyond comfort with an *immediate feedback signal* (does the sim do the thing?). That tight feedback loop is the single biggest driver of skill growth.
4. **Interleaving + spaced retrieval.** We don't fully silo mobile vs. arms. Review days (roughly every 7th) pull *old* material back from memory — retrieval practice beats re-reading by a wide margin. The capstone re-interleaves everything.
5. **The protégé effect (your superpower here).** You're club president. Teaching *is* learning — explaining a concept forces the gaps into the open. On every review day you'll write a short explainer or prep a 5-min club talk. This doubles as content for Yale Robotics.
6. **Build in public.** Mirror Alex Xu's model exactly: a public GitHub repo, one notebook/folder per day, daily commits, README that reads like a series. This creates accountability, a portfolio, and a searchable memory.

### Your daily template (copy this into every day's notebook)
```
DAY N — <topic>
□ WATCH  (~30–45 min)  intuition first
□ GRASP  (~15 min)     write the idea in your own words + one formula, explained
□ BUILD  (~60–75 min)  make something run
□ STRETCH(~15 min)     the deliberate-practice challenge
□ LOG    (~5 min)      commit to GitHub + 3 lines in your debug journal:
                        what broke, why, how I fixed it
```

### The "spine" project (your flagship — everything feeds it)
You will build, in simulation, an **autonomous mobile manipulator**: a wheeled base that maps a world, navigates it autonomously, then uses an arm to pick an object and deliver it. This unifies all three of your goals (mobile + arms + autonomy) into one portfolio-grade demo. Optional healthcare framing: a **hospital delivery / fetch robot** ("go to the supply station, pick up the item, bring it to the bed"). By Day 25 you'll have the autonomous base; by Day 36 the arm; by Day 42 the whole thing working end to end.

---

## 1. Environment setup (do this on Day 0 / the evening before — NOT a whole day)

Reality check, because you're on a MacBook: **ROS 2, Gazebo, and Nav2 are Linux-native.** Trying to run the full stack directly on macOS will cost you days of pain. Pick one of these and move on — this should take an evening, not a study day:

- **Best for you (recommended): Ubuntu 24.04 LTS + ROS 2 Jazzy Jalisco**, on either (a) a dual-boot / spare x86 machine, or (b) your Yale robotics lab machine. Jazzy is the current LTS and pairs with Gazebo Harmonic. Install guide: https://docs.ros.org/en/jazzy/Installation.html
- **Zero-setup fallback (great on a Mac): The Construct** — full ROS 2 + Gazebo in your browser, nothing to install: https://www.theconstruct.ai/ . Use this if your machine fights you; you can do ~80% of this plan here.
- **Portable option: Docker** — official ROS 2 images (`ros:jazzy`) run on Apple Silicon, though GUI (RViz/Gazebo) needs an X server and 3D sim is sluggish. Fine for the pure-ROS days (4–8), less so for heavy sim.

**Two honest notes:**
- **Humble vs. Jazzy:** Many of the best tutorials (Articulated Robotics) use **ROS 2 Humble**. Jazzy is 95% identical for your purposes and is the longer-lived LTS. Go Jazzy; when a tutorial is on Humble, the concepts transfer directly — treat version-specific command differences as a *feature* (learning to read docs is a robotics skill).
- **NVIDIA Isaac Sim / Isaac Lab** (Days 43, and any RL) **require an NVIDIA RTX GPU** — they will *not* run on a Mac. Treat those as optional/stretch, run them on a Yale lab machine or cloud, or watch-and-conceptualize. **Gazebo is your primary simulator** because it runs almost anywhere.

Setup checklist for Day 0: install ROS 2 Jazzy (or open The Construct) → run the official talker/listener demo → install Gazebo Harmonic → create your GitHub repo `robotics-from-scratch` with a `README.md` and a `journal.md`. Done. That's it.

---

# PHASE A — Foundations: math intuition, ROS 2 core, transforms (Days 1–8)

*Goal: think in frames and nodes. By Day 8 you can describe a robot and move data through a ROS 2 graph in your sleep.*

### Day 1 — The robotics stack + your first ROS 2 graph
- **Intuition:** what *is* robotics as a system (Sense→Estimate→Plan→Act→Glue). Watch the intro of the **ROS 2 Jazzy Crash Course (2025)** — https://www.youtube.com/watch?v=Se5pvRlTX8s — and skim **Articulated Robotics** as your home base for the next 3 weeks: https://articulatedrobotics.xyz/
- **Build:** get the `talker`/`listener` demo running; then use `ros2 topic echo`, `ros2 node list`, `rqt_graph` to *see* the graph. Draw the graph by hand.
- **Stretch:** without copying, write a Python node that publishes your name to a topic once a second; confirm with `ros2 topic echo`.
- **Log:** initialize the repo; commit `day01/`. Write your Sense→Plan→Act diagram into `README.md`.

### Day 2 — Linear algebra you can *see* (rotations & vectors)
- **Intuition (visual):** 3Blue1Brown, **Essence of Linear Algebra** — watch *Vectors*, *Linear combinations*, *Linear transformations & matrices*, *Matrix multiplication as composition*: https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
- **Grasp:** a matrix is a *function that moves space*. A rotation matrix moves space rigidly. Write that in your own words.
- **Build:** in a NumPy notebook, define a 2D rotation matrix R(θ); rotate a set of points; plot before/after with matplotlib. Animate θ from 0→2π.
- **Stretch:** show numerically that R(θ₁)·R(θ₂) = R(θ₁+θ₂). You just discovered composition.

### Day 3 — Rigid-body transforms & quaternions (the language of "where")
- **Intuition (visual):** 3B1B **Visualizing quaternions (interactive)** — https://eater.net/quaternions and the companion video https://www.youtube.com/watch?v=zjMuIxRvygQ . Then the transforms intuition from **Modern Robotics, Ch. 3** (Kevin Lynch, Northwestern) — full course playlist: https://www.youtube.com/playlist?list=PLggLP4f-rq02vX0OQQ5vrCxbJrzamYDfx (book + free software: https://modernrobotics.northwestern.edu/ )
- **Grasp:** homogeneous transform T = [R | p; 0 1] bundles rotation + translation into one 4×4 you can chain. This *is* the transform tree you'll live in.
- **Build:** implement `compose(T_a, T_b)` and `transform_point(T, p)` in NumPy. Place a "camera" frame and a "robot" frame; express a point in both.
- **Stretch:** compute the end-effector position of a 2-link planar arm (link lengths l₁, l₂; angles θ₁, θ₂) purely by chaining two transforms. (Foreshadows forward kinematics on Day 27.)

### Day 4 — ROS 2 nodes, topics, pub/sub (deep)
- **Watch:** **Robotics Back-End / Edouard Renard** free ROS 2 course — https://www.youtube.com/watch?v=Zj5M0qLu5uQ (and his site https://roboticsbackend.com/ ). Official tutorials: https://docs.ros.org/en/jazzy/Tutorials.html
- **Build:** create your own package (`ros2 pkg create`), write a publisher and a subscriber in Python, wire them with a custom message.
- **Stretch:** build a "sensor + filter" pair — one node publishes noisy fake sensor data, a second subscribes and publishes a running average.

### Day 5 — Services, parameters, launch files, colcon (proper practices)
- **Watch:** continue Robotics Back-End; **ROS 2 launch & parameters** from official docs.
- **Build:** add a service (`/reset`) to yesterday's system; expose a parameter (e.g., filter window size); write a **launch file** that starts both nodes with params set.
- **Stretch:** make the whole mini-system reconfigurable at runtime with `ros2 param set`. This is the "proper practices" muscle you said you lacked.

### Day 6 — TF2: the transform tree (the heart of ROS)
- **Watch:** Articulated Robotics on TF, plus official **tf2 tutorials**: https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html
- **Grasp:** every frame (`map`, `odom`, `base_link`, `laser`, `camera`) is a node in a tree; tf2 answers "where is A relative to B, right now?" This is the glue box of the whole field.
- **Build:** broadcast a static transform and a moving transform; look them up in a listener node; visualize the frames in **RViz2**.
- **Stretch:** create a 3-frame chain (`world → base → sensor`) and query the sensor's pose in `world` as `base` moves.

### Day 7 — REVIEW · RETRIEVE · TEACH-BACK (+ buffer)
- **Retrieve (no notes):** re-derive the homogeneous transform and re-explain pub/sub vs. services from memory into `journal.md`.
- **Teach-back (protégé effect):** write a 1-page "TF2 for Yale Robotics newcomers" explainer, or record a 5-min Loom. This is real club onboarding material.
- **Explore:** browse **PythonRobotics** (Atsushi Sakai) — every core algorithm implemented with animations, perfect for a visual software person: https://github.com/AtsushiSakai/PythonRobotics
- **Buffer:** finish anything that spilled over. Rest is legitimate — spacing consolidates memory.

### Day 8 — URDF: describing a robot
- **Watch:** Articulated Robotics URDF videos (part of the **Building a Mobile Robot** series: https://www.youtube.com/playlist?list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT )
- **Build:** write a URDF for a simple **differential-drive robot** (base + 2 wheels + a caster + a LiDAR link); view it in RViz2 with `joint_state_publisher_gui`.
- **Stretch:** add a camera link and confirm every frame shows up correctly in the TF tree. You now have a robot *described*; next phase makes it *move*.

---

# PHASE B — Simulation, the mobile base & control (Days 9–16)

*Goal: a robot that drives itself around a simulated world under closed-loop control, and the from-scratch planners that will guide it.*

### Day 9 — Gazebo simulation basics
- **Watch:** Articulated Robotics "Simulating with Gazebo" (https://articulatedrobotics.xyz/ ); reference the **MOGI-ROS Gazebo basics** repo (Jazzy + Harmonic): https://github.com/MOGI-ROS/Week-3-4-Gazebo-basics
- **Build:** spawn your Day-8 URDF into a Gazebo world; add a simple environment (walls/obstacles).
- **Stretch:** build a small custom world (a "room") — this becomes your spine-project map.

### Day 10 — Sensors in simulation
- **Build:** add Gazebo sensor plugins — a **2D LiDAR**, a **depth camera**, an **IMU**, and wheel **odometry**. Visualize the LiDAR scan and camera feed in RViz2.
- **Grasp:** in sim you get ground-truth *and* noisy sensor data — the perfect lab to learn estimation without hardware.
- **Stretch:** confirm the LiDAR "sees" your obstacles; walk the beams in your head from `laser` frame to `map` frame.

### Day 11 — ros2_control: actually driving the wheels
- **Watch:** Articulated Robotics **"Using ros2_control to drive our robot"** — https://www.youtube.com/watch?v=4VVrTCnxvSw
- **Build:** configure a `diff_drive_controller`; teleop the robot with `teleop_twist_keyboard` around your world.
- **Stretch:** publish `/cmd_vel` from your *own* node to drive a fixed path (e.g., forward 2 m, turn 90°). You're now in the **Act** box.

### Day 12 — Differential-drive kinematics & odometry (from scratch)
- **Intuition:** Modern Robotics mobile-robot chapter (Ch. 13) / Articulated Robotics odometry explainer.
- **Grasp then derive:** wheel velocities → body twist (v, ω) → pose integration. Write each equation *with* its picture (you hate naked formulae — draw the wheel geometry).
- **Build:** implement odometry yourself in a node from wheel encoder ticks; compare *your* estimated pose against Gazebo ground-truth. Watch the drift accumulate — that drift is *why SLAM exists* (foreshadowing Day 19).

### Day 13 — Feedback control: PID intuition
- **Watch (visual):** MATLAB Tech Talks **Understanding PID Control** series — https://www.youtube.com/playlist?list=PLn8PRpmsu08pQBgjxYFXSsODEF3Jqmm-y (Brian Douglas's animations are gold for a visual learner). Optionally start **Steve Brunton's Control Bootcamp** for depth: https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m
- **Build:** a proportional (then PI, then PID) heading controller that drives the robot to a target waypoint and stops.
- **Stretch:** tune the gains until it converges without oscillating; log the step response. Connect it to your classes — this is the loop closed.

### Day 14 — REVIEW · TEACH-BACK · mini-project (+ buffer)
- **Mini-project:** "Drive a perfect square" — closed-loop, using your controller + odometry, no teleop. Record a screen-capture GIF for your repo.
- **Retrieve:** re-derive diff-drive kinematics from memory.
- **Teach-back:** short write-up "why does odometry drift?" for the club.

### Day 15 — Motion planning I: graph search (A*, Dijkstra) from scratch
- **Watch:** MATLAB **Intro to Motion Planning Algorithms** — https://www.youtube.com/watch?v=-fePRPyeKnc ; browse **PythonRobotics** planning animations.
- **Build:** implement **A\*** on a 2D occupancy grid yourself, with a matplotlib animation of the frontier expanding. (Your software background makes this fun, not scary.)
- **Stretch:** swap heuristics (Manhattan vs. Euclidean) and watch the explored set change. This is the **Plan** box, from first principles.

### Day 16 — Motion planning II: sampling-based (RRT / RRT*)
- **Watch:** **RRT explained + implemented** — https://www.youtube.com/watch?v=OXikozpLFGo
- **Build:** implement **RRT** in a 2D world with obstacles, animated; then extend toward **RRT\***.
- **Stretch:** compare A* (grid) vs. RRT (continuous) on the same map — write 4 sentences on when you'd pick each. (You'll meet RRT again inside MoveIt on Day 33.)

---

# PHASE C — Autonomy: state estimation, SLAM, Nav2 (Days 17–25)

*Goal: the robot builds a map of an unknown world and navigates it fully autonomously. This is the "I built an autonomous robot" milestone.*

### Day 17 — State estimation intuition: Bayes filter → Kalman
- **Watch (visual):** MATLAB **Understanding Kalman Filters** series — https://www.youtube.com/playlist?list=PLn8PRpmsu08pzi6EMiYnR-076Mh-q3tWr . Intuition backbone from **Cyrill Stachniss** (Bonn), the best free robotics-estimation lecturer alive: https://www.ipb.uni-bonn.de/teaching/
- **Grasp:** estimation = "combine a noisy prediction with a noisy measurement, weighted by how much you trust each." Draw the two Gaussians merging.

### Day 18 — EKF localization (from scratch)
- **Build:** implement a 2D **Extended Kalman Filter** that fuses your drifting odometry with noisy "GPS-like" or landmark measurements; use **PythonRobotics'** EKF as your reference: https://github.com/AtsushiSakai/PythonRobotics
- **Stretch:** show the covariance ellipse shrinking when a measurement arrives, growing during dead-reckoning. Now you *feel* why fusion matters.

### Day 19 — SLAM intuition (the crown jewel of mobile robotics)
- **Watch:** **Cyrill Stachniss — Introduction to SLAM** https://www.youtube.com/watch?v=0I30M6yTklo and his **SLAM course playlist** https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_
- **Grasp:** the chicken-and-egg (need a map to localize, need to localize to map), front-end vs. back-end, and **loop closure**. No coding today — build the mental model well.

### Day 20 — SLAM in ROS 2 with slam_toolbox
- **Build:** run **slam_toolbox** (https://github.com/SteveMacenski/slam_toolbox ) on your Gazebo robot; teleop around your world and watch the map build live in RViz2; **save the map**.
- **Stretch:** deliberately drive a loop and observe loop-closure snapping the map straight. Save this as a demo GIF — it's genuinely magical.

### Day 21 — REVIEW · RETRIEVE · TEACH-BACK (+ buffer)
- **Retrieve:** explain the Kalman gain and "what loop closure fixes" from memory.
- **Teach-back:** "SLAM in 5 minutes" explainer for the club — you'll almost certainly reuse this as prez.
- **Buffer:** consolidate the mapping pipeline; make sure map-save/load is reliable (you need it tomorrow).

### Day 22 — Nav2 architecture (the professional autonomy stack)
- **Watch/Read:** **Nav2 docs & getting started** — https://docs.nav2.org/getting_started/index.html ; overview video https://www.youtube.com/watch?v=Xbij9Tst-WA
- **Grasp:** the pieces — costmaps (global/local), a **planner** (there's your A*/RRT again), a **controller** (DWB/RPP), **AMCL** localization, and a **behavior tree** orchestrating recovery. Map each piece to a box from Day 1.

### Day 23 — Nav2 bring-up on *your* robot
- **Build:** load your saved map; localize with **AMCL**; send a single "Nav2 Goal" from RViz2 and watch the robot plan + drive there autonomously, avoiding obstacles.
- **Stretch:** place an unexpected obstacle in its path and watch the local costmap + controller react.

### Day 24 — Nav2 tuning + programmatic goals
- **Build:** tune costmap inflation & controller params for smooth motion; then drive goals **from code** using the **Nav2 Simple Commander** Python API (waypoint following).
- **Stretch:** script a patrol — visit 3 waypoints in a loop. This is autonomy you *commanded*, not clicked.

### Day 25 — 🏁 MILESTONE: Autonomous Mobile Robot
- **Build:** stitch it together — bring up sim → localize → accept goals → navigate obstacle-filled world, all launched from **one launch file**. Record a clean demo video.
- **Reflect:** you have now *built an autonomous robot* in the traditional sense — the thing you said you'd never done. Write the milestone up in your README like an Alex-Xu "Day N" entry.
- **Teach-back:** this is a natural Yale Robotics workshop / recruiting demo.

---

# PHASE D — Manipulation: arms, kinematics, IK, MoveIt 2 (Days 26–36)

*Goal: understand and command robot arms from first principles, then with the industry-standard MoveIt 2. Closest phase to your surgical/cardio-device dream.*

### Day 26 — Arm kinematics intuition: DOF, joints, configuration space
- **Watch:** **Peter Corke's Robot Academy** (bite-sized, visual) — https://robotacademy.net.au/ ; Modern Robotics Ch. 4 (Forward Kinematics) from the playlist above.
- **Grasp:** configuration space vs. task space; why 6 DOF reaches any pose in 3D; what "redundancy" (7 DOF) buys you (hello, surgical arms working around obstacles).

### Day 27 — Forward kinematics (from scratch)
- **Build:** implement **FK for a 3-DOF arm** in NumPy by chaining the transforms you wrote on Day 3 (product-of-exponentials or DH — pick one, understand it). Verify the end-effector position against a hand calculation.
- **Stretch:** animate the arm sweeping its joints and trace the end-effector path. Reference **Peter Corke's `RVC3-python`** toolbox to check yourself: https://github.com/petercorke/RVC3-python

### Day 28 — REVIEW · RETRIEVE · TEACH-BACK (+ buffer)
- **Retrieve:** re-derive the 2-link FK from a blank page.
- **Teach-back:** "what is a robot's configuration space?" explainer.
- **Buffer / interleave:** revisit one mobile-robot concept you felt shaky on (retrieval across phases).

### Day 29 — Inverse kinematics I: analytic (the core skill)
- **Watch:** IK intuition — **"Easy inverse kinematics for robot arms"** https://www.youtube.com/watch?v=Q-UeYEpwXXU ; Modern Robotics Ch. 6.
- **Grasp:** IK = "given where I want the hand, find the joint angles" — often many/no solutions.
- **Build:** derive and code **analytic IK for a 2-link planar arm** yourself (the classic elbow-up/elbow-down two solutions). This is a rite of passage — do it by hand first, then in code.

### Day 30 — Inverse kinematics II: numerical (Jacobian-based)
- **Build:** implement a **Jacobian pseudo-inverse IK** solver; animate the end-effector converging to a moving target (visual, satisfying).
- **Stretch:** show it handle a target the analytic method can't (e.g., a 3-DOF arm). Note where it struggles near singularities → tomorrow.

### Day 31 — The Jacobian: velocity kinematics & singularities
- **Watch:** Modern Robotics Ch. 5 (velocity kinematics) from the playlist.
- **Grasp:** the Jacobian maps joint velocities → end-effector velocity; a **singularity** is where the arm loses a direction it can move (the pseudo-inverse blows up). Critical for surgical safety.
- **Build:** visualize the manipulability ellipsoid; find and plot a singular configuration.

### Day 32 — Model an arm in simulation
- **Build:** URDF a **6-DOF arm**; spawn in Gazebo with **ros2_control** (position/trajectory controllers). Reference the **MOGI-ROS simple-arm** repo (Jazzy + Harmonic + MoveIt 2): https://github.com/MOGI-ROS/Week-9-10-Simple-arm
- **Stretch:** command a single joint trajectory and watch it track.

### Day 33 — MoveIt 2 I: setup & planning
- **Watch/Read:** **MoveIt 2 tutorials** — https://moveit.picknik.ai/main/index.html ; **"Robotic Arms Workflow of MoveIt 2"** https://www.youtube.com/watch?v=GuOgQzuwNB0
- **Build:** run the **MoveIt Setup Assistant** on your arm; plan a collision-free motion to a pose in RViz2 and execute it in Gazebo. (Notice RRT running *inside* the planner — Day 16 pays off.)

### Day 34 — MoveIt 2 II: programmatic motion & pick-and-place
- **Build:** drive MoveIt from **Python/C++** — plan and execute to named targets; implement a basic **pick → lift → place** sequence with a gripper.
- **Stretch:** add a collision object to the planning scene and confirm the plan avoids it.

### Day 35 — REVIEW · RETRIEVE · TEACH-BACK (+ buffer)
- **Retrieve:** explain analytic vs. numerical IK, and what a singularity is, from memory.
- **Teach-back:** "How a robot arm decides how to move" — great club content.

### Day 36 — 🦾 MILESTONE: Grasping + the manipulation frontier
- **Build:** a reliable **pick-and-place of an object** in Gazebo via MoveIt. Record the demo.
- **Go deeper (optional, visual + rigorous):** **Russ Tedrake, MIT 6.4210 "Robotic Manipulation"** — free course, notes, and lectures: https://manipulation.csail.mit.edu/ (and **Underactuated Robotics**: https://underactuated.csail.mit.edu/ ). This is the intellectual home of modern (and medical) manipulation — skim to see where the field goes next.

---

# PHASE E — Perception, integration, capstone & the frontier (Days 37–45)

*Goal: close the Sense loop, then fuse everything into the flagship autonomous mobile manipulator.*

### Day 37 — Perception basics: cameras, depth, point clouds
- **Build:** in ROS 2, grab your sim camera feed; use **OpenCV** to detect an object by color/shape; get its pixel location. Look at the depth image / point cloud in RViz2.
- **Grasp:** pixels → rays → 3D points via camera intrinsics + the TF tree. This is the **Sense→Estimate** bridge.

### Day 38 — From perception to a graspable pose
- **Build:** convert your detected object into a **3D pose in the arm's frame** (using depth + TF), and hand that pose to MoveIt as a grasp target. Perception now *drives* manipulation.
- **Stretch:** make it robust to the object moving to a new spot.

### Day 39 — Mobile manipulator: architecture & orchestration
- **Build:** put the arm on the mobile base (combine URDFs); design the capstone as a **state machine / behavior tree**: `NAVIGATE → PERCEIVE → PICK → NAVIGATE → PLACE`. Sketch it before you code it.
- **Grasp:** this orchestration layer is what separates a demo from a *system* — exactly the "proper practices" gap you named.

### Day 40 — 🚀 Capstone build 1: navigate to the station
- **Build:** robot autonomously navigates (Nav2) from home to a "supply station" pose in the mapped world, reliably. First third of the spine project working end to end.

### Day 41 — 🚀 Capstone build 2: perceive + pick
- **Build:** at the station, perceive the target object and pick it with MoveIt. Handle the "object not found → recover" branch.

### Day 42 — 🚀 Capstone build 3: deliver + the full loop
- **Build:** navigate to the drop-off, place the object, return home — the **entire autonomous loop** running from one launch. Record the flagship demo video.
- **Reflect:** this is a genuinely strong portfolio piece and a Yale Robotics showcase. (Healthcare framing: a hospital fetch-and-deliver robot — a clean line to your surgical/cardio interests.)

### Day 43 — The frontier: learning-based robotics (optional / GPU-gated)
- **Watch:** **Reinforcement Learning for Robots — Isaac Lab** https://www.youtube.com/watch?v=TMHkFDhVt7g ; repo https://github.com/isaac-sim/IsaacLab ; NVIDIA's beginner Isaac Sim guide https://developer.nvidia.com/blog/a-beginners-guide-to-simulating-and-testing-robots-with-ros-2-and-nvidia-isaac-sim/
- **Do (if you have an NVIDIA RTX machine — Yale lab/cloud):** run a pre-built RL locomotion/manipulation example. **If not:** watch + write one page on how RL policies differ from the classical planners you built, and where each wins. (Sim-to-real, imitation learning, and diffusion policies are the current surgical-robotics research edge.)

### Day 44 — Ship it like a series (documentation & teaching)
- **Build:** polish the repo Alex-Xu-style — clean `README.md` with a day-by-day index, per-day notebooks/folders, demo **GIFs**, and a short "what I learned" per phase. Record a 3–5 min capstone walkthrough.
- **Teach-back:** turn it into a **Yale Robotics workshop / lightning talk** outline. You've now built the onboarding curriculum you wished existed.

### Day 45 — Reflection & the road ahead
- **Consolidate:** finalize `journal.md` — your debug log is now a personal reference. Do one last blank-page retrieval of the whole Sense→Estimate→Plan→Act→Glue map.
- **Plan forward:** pick your next mountain. Toward your dream: **surgical robotics kinematics** (remote-center-of-motion / RCM constraints, the dVRK open research platform), medical imaging + perception, or a real hardware build with the club. Write 5 concrete next steps.
- **Celebrate:** 45 days ago your robotics knowledge was scattered; now it's a stack you can reason about end to end. Tell Anna. 🎉

---

## 2. Master resource list (your permanent library)

**Backbone courses (return to these often)**
- **Modern Robotics** — Kevin Lynch, Northwestern (the definitive theory, visual, free): playlist https://www.youtube.com/playlist?list=PLggLP4f-rq02vX0OQQ5vrCxbJrzamYDfx · book/software https://modernrobotics.northwestern.edu/ · Coursera https://www.coursera.org/specializations/modernrobotics
- **Articulated Robotics** — the best hands-on ROS 2 mobile-robot series: https://articulatedrobotics.xyz/ · "Building a Mobile Robot" playlist https://www.youtube.com/playlist?list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT
- **Robotics Back-End (Edouard Renard)** — clean ROS 2 fundamentals: https://roboticsbackend.com/ · https://www.youtube.com/watch?v=Zj5M0qLu5uQ
- **ROS 2 Jazzy Crash Course (2025)**: https://www.youtube.com/watch?v=Se5pvRlTX8s
- **The Construct** — browser-based ROS 2 (Mac-friendly, zero setup): https://www.theconstruct.ai/

**Fundamentals & math (visual-first)**
- **3Blue1Brown, Essence of Linear Algebra**: https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
- **Quaternions, interactive** (Ben Eater + 3B1B): https://eater.net/quaternions
- **MATLAB Tech Talks** — PID: https://www.youtube.com/playlist?list=PLn8PRpmsu08pQBgjxYFXSsODEF3Jqmm-y · Kalman Filters: https://www.youtube.com/playlist?list=PLn8PRpmsu08pzi6EMiYnR-076Mh-q3tWr
- **Steve Brunton, Control Bootcamp**: https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m
- **Peter Corke** — Robot Academy https://robotacademy.net.au/ · *Robotics, Vision and Control (Python)* code https://github.com/petercorke/RVC3-python

**Algorithms you'll implement**
- **PythonRobotics (Atsushi Sakai)** — animated implementations of nearly everything: https://github.com/AtsushiSakai/PythonRobotics
- **RRT explained + coded**: https://www.youtube.com/watch?v=OXikozpLFGo · **Motion planning intro**: https://www.youtube.com/watch?v=-fePRPyeKnc

**Autonomy & SLAM**
- **Cyrill Stachniss** — teaching hub https://www.ipb.uni-bonn.de/teaching/ · Intro to SLAM https://www.youtube.com/watch?v=0I30M6yTklo · SLAM course https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_
- **Nav2**: https://docs.nav2.org/ · **slam_toolbox**: https://github.com/SteveMacenski/slam_toolbox

**Manipulation**
- **MoveIt 2**: https://moveit.picknik.ai/main/index.html · workflow video https://www.youtube.com/watch?v=GuOgQzuwNB0
- **MOGI-ROS simple arm** (Jazzy/Harmonic/MoveIt2): https://github.com/MOGI-ROS/Week-9-10-Simple-arm
- **Russ Tedrake, MIT — Robotic Manipulation**: https://manipulation.csail.mit.edu/ · **Underactuated Robotics**: https://underactuated.csail.mit.edu/

**Simulation**
- **Gazebo (Harmonic)** docs: https://gazebosim.org/docs · **MOGI-ROS Gazebo basics**: https://github.com/MOGI-ROS/Week-3-4-Gazebo-basics
- **NVIDIA Isaac Sim** (RTX GPU): https://developer.nvidia.com/blog/a-beginners-guide-to-simulating-and-testing-robots-with-ros-2-and-nvidia-isaac-sim/ · **Isaac Lab** (RL): https://github.com/isaac-sim/IsaacLab

---

## 3. Guardrails & tips (from the pedagogy, and from experience)

- **Don't rabbit-hole on install/version errors.** If a tool fights you for >45 min, switch to The Construct or Docker and keep moving. Momentum > purity. (This is also why we picked Gazebo over GPU-gated Isaac Sim as the default.)
- **The Stretch is the point.** The days you feel slightly lost are the days you grow most — that discomfort is deliberate practice working. If a day feels *too* easy, add a constraint.
- **Commit daily, even ugly.** A broken notebook with a good debug-journal note beats a perfect notebook you didn't finish. Your `journal.md` will become your most valuable asset.
- **Teach on every review day.** As club president you have a built-in audience and the strongest possible reason to actually understand things. Your explainers ARE the Yale Robotics onboarding track.
- **It's 45 days, not a sprint to the death.** You have "tons planned" this summer. The review/buffer days are real slack — if life eats a day, slide the plan; don't skip the retrieval. Spacing helps memory anyway.
- **When stuck, name the box.** Sense? Estimate? Plan? Act? Glue? Ninety percent of "I'm lost" is "I don't know which box this is." Return to the compass.

You've got the software, the CAD, the EE, the drive, and now a map. Go build the robot. 🤖
