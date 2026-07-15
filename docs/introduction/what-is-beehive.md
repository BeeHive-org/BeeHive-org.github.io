---
title: What is BeeHive?
description: The concepts behind BeeHive — mainboards, daughter boards, and the ingredients-and-recipes model.
---

# What is BeeHive?

**BeeHive is an open system that makes it easier to build scientific equipment
and to learn basic electronics.** It grew out of a simple problem: researchers
often need custom instruments, but building one usually means either
commissioning a company or starting a bespoke design from scratch — and the
result rarely gets reused.

BeeHive fixes that with a small set of standard, reusable parts and a **minimal
set of design rules** that keep everything interoperable.

## The building blocks

BeeHive has just two kinds of board:

- **Mainboard** — carries the microcontroller (an ESP32) and breaks out every
  pin through standard connectors. Most builds need exactly one.
- **Daughter boards (DBs)** — each does *one* job: drive a solenoid, switch
  high-power LEDs, read a temperature sensor, and so on.

They connect through a single **4-pin connector** — two data lines, one power
line, one ground — so any daughter board plugs into any port. Because each DB is
self-contained and single-purpose, the same board works across wildly different
experiments: a solenoid controller might meter a water reward for a mouse in one
lab and drive greenhouse irrigation in another.

→ Browse the full catalogue in **[Ingredients](../ingredients/index.md)**.

## Ingredients and recipes

We describe BeeHive the way you'd describe cooking:

| Metaphor | In BeeHive |
| -------- | ---------- |
| **Ingredients** | Boards — the mainboard and daughter boards |
| **Recipes** | Complete builds that combine boards into a working instrument |
| **Techniques** | The skills a recipe assumes: soldering, flashing firmware, board design |

A [recipe](../recipes/index.md) lists the ingredients it uses (e.g. *mainboard
1×, solenoid control board 6×*), how to wire them, and the code to run them —
just like a cooking recipe lists ingredients and method.

## Software

- **MicroPython first.** BeeHive is driven mostly with
  [MicroPython](https://micropython.org/), a Python 3 implementation for
  microcontrollers. Since it's the same language most researchers already use
  for data analysis, you can go from experiment control to plotting without
  switching languages — and beginners learn one language for everything.
- **C++ when you need it.** The ESP32 can also run Arduino/C++, so you can reuse
  existing libraries (the [mouse maze](../recipes/mouse-maze.md) recipe does
  exactly this for the Adafruit servo driver).

## Why not use an existing system?

BeeHive is compatible with prototyping systems like
[Grove](https://wiki.seeedstudio.com/Grove_System/),
[Qwiic](https://www.sparkfun.com/qwiic) and
[STEMMA](https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma)
(same connector order; adapter boards available). But it exists because those
systems weren't built for the lab:

1. **Power.** Scientific gear often needs currents and voltages hobby systems
   don't handle — e.g. Peltier elements at 12 V / 5 A. BeeHive runs on 12 V DC
   and its boards are rated for it.
2. **Control.** Owning the ecosystem means we can design exactly the daughter
   boards research needs, behaving exactly as required — and fill gaps where no
   commercial board exists.

!!! tip "Where next?"
    Read the **[Design rules](design-rules.md)** to understand what keeps
    BeeHive interoperable, or jump to **[Getting started](getting-started.md)**
    to pick a path.
