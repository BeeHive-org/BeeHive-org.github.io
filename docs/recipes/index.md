---
title: Recipes
description: Complete BeeHive builds you can reproduce — from reward delivery to gas analysis.
---

# Recipes

A **recipe** is a complete, documented build: which
[ingredients](../ingredients/index.md) (boards) it uses, how to wire them, and
the code to run them. Most recipes below come from real neuroscience labs, but
BeeHive is discipline-agnostic — see
[Beyond neuroscience](beyond-neuroscience.md).

## How to read a recipe

Every recipe follows the same shape:

- **Ingredients** — the boards and other parts, with quantities and their role.
- **How it works** — the setup and signal flow.
- **Wiring** — how everything connects.
- **Code** — a MicroPython (or C++) starting point.
- **Results / notes** — what it achieves, caveats, and source links.

The **Ingredients** table links each board to its entry in the
[catalogue](../ingredients/index.md), so you can check specs and source
schematics as you go.

## The recipes

| Recipe | What it does | Key ingredients |
| ------ | ------------ | --------------- |
| [Head-fixed reward delivery](head-fixed-reward.md) | Reward + lick detection for a head-fixed 2-photon rig | mainboard, solenoid control board |
| [Mouse maze](mouse-maze.md) | Closed-loop modular maze with reward ports | mainboard, IR sensor array, PCA9685 |
| [Odour stimulator](odour-stimulator.md) | Dual-channel olfactory stimulation, ms precision | mainboard, Spike & Hold (2×) |
| [LI-850 multiplexer](li850-multiplexer.md) | Parallelise metabolic measurement across 6 chambers | mainboard, solenoid control board (6×) |
| [5-choice serial reaction time](5-csrtt.md) | Classic attention/impulsivity paradigm, open hardware | mainboard, IR sensor array |
| [Mouse-wheel speed controller](mouse-wheel.md) | Motorised running wheel with clutch | mainboard, stepper driver |
| [OpenFlexure stage controller](openflexure-controller.md) | Standalone delta-stage controller with LCD | mainboard, rotary encoders, LCD |
| [Beyond neuroscience](beyond-neuroscience.md) | Incubators, heaters, and other fields | various |

!!! tip "Built something with BeeHive?"
    Recipes are community-contributed. See
    [Write your own recipe](write-your-own.md) to add yours.
