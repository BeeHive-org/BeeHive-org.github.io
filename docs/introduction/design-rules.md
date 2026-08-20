---
title: Design rules
description: The minimal rules that keep every BeeHive board interoperable.
---

# Design rules

BeeHive has deliberately **few** rules. Enough to keep every board
interoperable and buildable anywhere — but not so many that they get in the way
of new ideas. A handful are strict; the rest are strong recommendations.

## Strict rules

These define what makes a board "BeeHive". Follow them and your board works with
everything else.

1. **Two types of board.** *Mainboards* carry a microcontroller. *Daughter
   boards* each perform **one** function (e.g. control a solenoid valve).
2. **One connector.** Main-to-daughter connections use a **4-pin connector**:
   two general-purpose I/O (data) lines, one power line (VCC), and one ground
   line (GND).

![Connector pinout: DATA 1, DATA 2, VCC, GND](https://github.com/BeeHive-org/BeeHive/raw/master/hardware/PCBs/central_hub/central_hub_3D.png?raw=true){ width=320 }

## Recommended rules

Follow these so anyone, anywhere, can build and understand your board:

- **1–2 PCB layers.** Keep routing to top and bottom layers so boards can be
  replicated locally with perfboard, chemical etching, or CNC — or ordered
  cheaply from [JLCPCB](https://jlcpcb.com/), [PCBway](https://www.pcbway.com/),
  [OSH Park](https://oshpark.com/), or [Aisler](https://aisler.net).
- **Through-hole components** so boards can be hand-soldered with minimal kit,
  by people with no prior experience.
- **Populate one side** of the board only.
- **Label everything** by the existing convention: connector pin identifiers,
  the daughter-board name, and a version number.
- **Prefer a standard size:**
    - **Big** — 71 × 45.5 mm
    - **Small** — 48.5 × 45.5 mm
- **Size up** if the board is getting cramped.
- **Mounting holes:** typically 4, for M3 screws, each centre 3.5 mm from the
  board edge.
- **If in doubt — reach out!**

!!! tip "Ready to design one?"
    See **[Build your own board](../techniques/build-your-own-board.md)** for a
    step-by-step walkthrough from picking a function to submitting your design.
