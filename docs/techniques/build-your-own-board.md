---
title: Build your own board
description: How to design a new BeeHive daughter board that follows the platform's design rules.
---

# Build your own board

Every BeeHive board is either a **mainboard** (carries a microcontroller) or a **daughter board** (does one job). If the function you need isn't in the [ingredients catalogue](../ingredients/index.md), you design a new daughter board. This guide summarises the design rules and how to submit it.

The workflow is simple: pick a function, design to the rules, then submit via the repo.

## What to design it in

Use **[KiCad](https://www.kicad.org/)** — a free, open-source, cross-platform
EDA suite for schematic capture and PCB layout. It's the standard FOSS tool for
this, and it's what BeeHive's own boards are drawn in, so you can open any
existing board's `.kicad_pcb` from the [ingredients catalogue](../ingredients/index.md)
(each board links its KiCad files) as a starting point or reference. KiCad also
exports the gerbers and bill of materials the fab houses and
[Kitspace](https://kitspace.org/) need.

!!! tip "Mechanical parts"
    If your board needs a 3D-printed frame, mount or enclosure, design those in
    **[FreeCAD](https://www.freecad.org/)** (open-source parametric CAD). KiCad
    can hand off the board outline and 3D model to it.

## 1. Pick a function

A daughter board does **one thing** — drive an actuator or read a sensor. If you find yourself putting two unrelated functions on one board, that's two boards. Keeping boards single-function is what lets them mix and match across recipes.

## 2. Design to the rules

### Strict rules

These are non-negotiable — they are what make a board a BeeHive board.

- **Two board types only.** Mainboards carry the MCU; daughter boards do not. A daughter board never hosts a microcontroller.
- **The 4-pin connector.** Every board connects through the standard 4-pin connector: **two GPIO data lines, power, and ground**. Design your board's interface around exactly those four pins.

### Recommended rules

Follow these so the board stays cheap, hand-buildable and easy to share.

- **1–2 PCB layers.** Keep it to one or two copper layers so the board can be home-etched, CNC-milled or perfboarded — or ordered cheaply from [JLCPCB](https://jlcpcb.com/), [PCBWay](https://www.pcbway.com/), [OSH Park](https://oshpark.com/) or [Aisler](https://aisler.net/).
- **Through-hole components** so the board can be hand-soldered. See [Soldering](soldering.md).
- **Populate one side only**, to keep assembly and mounting simple.
- **Label the board** with the connector pin identifiers, the daughter-board name and its version.
- **Use a preferred size:** **Big — 71 × 45.5 mm** or **Small — 48.5 × 45.5 mm**. If the layout is cramped, size up rather than shrinking traces.
- **Four M3 mounting holes**, with centres **3.5 mm from the edges**.

!!! tip "If in doubt, reach out"
    The rules are guidelines, not a straitjacket. If your board needs to bend one, ask — open an issue or discussion on the [BeeHive repository](https://github.com/BeeHive-org/BeeHive) before committing to a layout.

## 3. Submit via the repo

Once your board works, contribute it back so it can join the ingredients catalogue: open a pull request or issue on the [BeeHive repository](https://github.com/BeeHive-org/BeeHive) with your schematic, board files and a short description of the function.

!!! note "Source"
    Design rules and board templates: [BeeHive repository](https://github.com/BeeHive-org/BeeHive).
