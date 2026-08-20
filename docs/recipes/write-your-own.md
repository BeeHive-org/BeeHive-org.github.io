---
title: Write your own recipe
description: How to document a BeeHive build as a recipe others can reproduce.
---

# Write your own recipe

Built something with BeeHive? Writing it up as a **recipe** lets other people
reproduce it — and grows the library for everyone. A good recipe answers one
question: *"If I have these boards, how do I build this?"*

You don't need to be a writer. Follow the template below, be concrete, and link
the [ingredients](../ingredients/index.md) you used.

## The recipe template

Copy this into a new file at `docs/recipes/<your-recipe>.md` and fill it in:

```markdown
---
title: <Recipe name>
description: <one line — what it does and for whom>
---

# <Recipe name>

<1–2 sentences: what it does and who it's for.>

## Ingredients

BeeHive boards:

| Board | Qty | Role |
| ----- | --- | ---- |
| [<board>](../ingredients/<category>.md#<slug>) | 1× | <what it does here> |

Other components:

| Component | Qty | Notes |
| --------- | --- | ----- |
| <servo / valve / sensor / 3D-printed part> | 1× | <what it's for> |

## How it works

<The setup and the signal flow. What triggers what, and any timing.>

## Wiring

<How things connect — which board takes which data line, power rails, etc.>

## Code

<A short MicroPython (or C++) starting point. Placeholder pins are fine —
mark them with a TODO.>

## Results / notes

<What it achieves, caveats, and links to design files / papers.>
```

## What makes a recipe good

- **List every ingredient.** Give quantities and each board's role. Link each
  BeeHive board to its entry in the [catalogue](../ingredients/index.md) so
  readers can check specs and find schematics — see the
  [cross-linking](#cross-linking-ingredients) note below.
- **Name the non-BeeHive parts too.** Exact models matter: the servo, the
  solenoid valve part number, the motor, the 3D-printed frame.
- **Explain the flow, not just the parts.** What triggers a reward? What's the
  timing? A reader should understand the logic before touching a wire.
- **Give runnable code, even if minimal.** A short sketch beats none. Use
  placeholder pin numbers and mark them with a `# TODO` — it's a starting point,
  not production firmware.
- **Link your design files.** 3D models, PCB files, and the source repo let
  people build the physical parts.
- **Share your figures.** A wiring schematic or a photo of the finished build is
  worth a lot. Drop images in `docs/assets/` and reference them.

## Cross-linking ingredients

Each board lives on its category page under an anchor matching its slug, so link
to `../ingredients/<category>.md#<slug>`. For example:

- `[Solenoid control board](../ingredients/actuators.md#solenoid-control-board)`
- `[Level shifter](../ingredients/utilities.md#level-shifter)`
- `[ESP32 BeeHive mainboard](../ingredients/mainboards.md#esp32-mainboard)`

The [Ingredients overview](../ingredients/index.md) lists every board with its
category and slug.

## Missing an ingredient?

If your build uses a board that isn't in the catalogue yet, add it — see
[Build your own board](../techniques/build-your-own-board.md) and
[Contributing](../contributing.md). If it's an off-the-shelf third-party board
(e.g. an Adafruit driver), just link it externally in your ingredients list.

## Sharing it

Add your recipe to the `Recipes` section of `zensical.toml`'s navigation, then
open a pull request against the
[docs repository](https://github.com/BeeHive-org/BeeHive). See
[Contributing](../contributing.md) for the local preview workflow.

!!! tip "Not sure where to start?"
    Read an existing recipe first — the
    [LI-850 multiplexer](li850-multiplexer.md) is a complete worked example, from
    ingredients through to a runnable MicroPython sketch.
