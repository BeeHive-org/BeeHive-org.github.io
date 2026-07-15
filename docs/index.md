---
title: Open electronics for research
description: A flexible open electronics platform for building research equipment and teaching electronics.
---

# BeeHive

**BeeHive is an open-source electronics ecosystem for building your own research
equipment** — and for learning the electronics and programming to do it. An
ESP32 **mainboard** plus single-function **daughter boards** click together like
building blocks, so you can assemble, repurpose, and share custom instruments
without starting from scratch each time.

![BeeHive mainboard](https://github.com/BeeHive-org/BeeHive/raw/master/hardware/PCBs/central_hub/central_hub_3D.png?raw=true){ width=420 }

!!! success "Free & open source"
    All BeeHive hardware designs, firmware, and docs are released under
    open-source licences — free to copy, learn from, modify, and build on. The
    designs live at
    [github.com/BeeHive-org/BeeHive](https://github.com/BeeHive-org/BeeHive).

## Ingredients & recipes

BeeHive is organised around a simple metaphor:

- 🧩 **[Ingredients](ingredients/index.md)** — the boards. A *mainboard* carries
  the microcontroller; *daughter boards* each do one job (drive a solenoid, read
  a sensor, switch an LED). They share one 4-pin connector, so they mix freely.
- 🍯 **[Recipes](recipes/index.md)** — the builds. Combine ingredients to make a
  working instrument: a [reward-delivery rig](recipes/head-fixed-reward.md), an
  [odour stimulator](recipes/odour-stimulator.md), a
  [gas-analyser multiplexer](recipes/li850-multiplexer.md), and more.
- 🔧 **[Techniques](techniques/soldering.md)** — the kitchen skills: soldering a
  board, flashing MicroPython, and designing your own daughter board.
- 🎓 **[Courses](courses/intro-to-electronics.md)** — a project-based
  introduction to electronics and MicroPython for total beginners.

## Why BeeHive

- ⚡ **Built for the lab.** Runs on 12 V DC (mains adapter *or* battery),
  handles the currents and voltages real equipment needs (e.g. Peltier elements
  at 12 V / 5 A) that hobby prototyping systems don't.
- 🔁 **Interoperable.** The connector order matches
  [Grove](https://wiki.seeedstudio.com/Grove_System/),
  [Qwiic](https://www.sparkfun.com/qwiic) and
  [STEMMA](https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma),
  and a MikroBUS mainboard opens up 500+ Click Boards.
- 🐍 **One language, end to end.** Program in MicroPython — the same Python you
  already use for data analysis — from experiment control to plotting. Or drop
  to C++ (Arduino) when you need an existing library.
- 🌍 **Buildable anywhere.** Through-hole parts, 1–2 layer boards, and cheap
  worldwide-available components mean boards can be hand-soldered or home-etched.

!!! tip "New here?"
    Start with [What is BeeHive?](introduction/what-is-beehive.md) for the
    concepts, then [Getting started](introduction/getting-started.md) to pick
    your path — build a recipe, learn the basics, or design a new board.
