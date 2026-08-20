---
title: Soldering
description: Tools, components, and technique for assembling BeeHive boards.
---

# Soldering

BeeHive boards use **through-hole components** so they can be hand-soldered with
a basic kit and no prior experience. This page covers what you need and how to
put a board together. If you've never soldered before, SparkFun's
[through-hole soldering tutorial](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering/all)
is an excellent primer.

## Tools

Links below are for reference — any equivalent brand works.

- [Soldering iron](https://pine64.org/devices/pinecil/) (a temperature-controlled
  iron or station is ideal)
- Solder
- Flush cutters
- Solder wick (for desoldering mistakes)
- An extractor fan / fume extraction
- Helping hands or a board holder

## Components

Most parts can be sourced through [Kitspace](https://kitspace.org), which reads
a board's bill of materials directly. Typical BeeHive components:

### Resistors

Use a [resistor colour-band calculator](https://www.digikey.co.uk/en/resources/conversion-calculators/conversion-calculator-resistor-color-code)
to identify values. Common values across BeeHive boards:

| Value | Bands |
| ----- | ----- |
| 47 Ω | yellow · violet · black · gold |
| 220 Ω | red · red · black · black · brown |
| 560 Ω | green · blue · brown |
| 1 kΩ | brown · black · red |
| 4.7 kΩ | yellow · violet · black · brown |
| 10 kΩ | brown · black · black · red |

### Connectors

- 2-, 3-, and 4-pin JST-PH connectors
- Barrel jack connector
- 20-pin female headers (mainboard footprint)

<!-- TODO: pull the authoritative per-board BOM from kitspace.yaml / the board YAML. -->

## Assembling a board

1. **Get to know the board.** Look over the component IDs printed on the sil
   screen and where each part goes before you start.
2. **Work shortest-first.** Solder the lowest-profile parts first (resistors,
   diodes), then taller ones (capacitors, connectors, headers). This keeps parts
   flat against the board while you flip it to solder.
3. **Mind orientation.** Polarised parts must go the right way round:
    - **Electrolytic capacitors** — the stripe marks the negative leg.
    - **Diodes, ICs, transistors** — match the marked pin/notch to the silk
      screen.
4. **Check JST footprints** — make sure each connector matches its outline
   before soldering; they only fit one way.
5. **Inspect.** Look for cold joints (dull, blobby) and bridges between pins;
   reflow or wick as needed.

!!! warning "Known issues"
    On the H-bridge driver and high-power switch array, some resistor footprints
    are currently a tight fit — too large for 1 kΩ, too small for 47 Ω parts.
    <!-- TODO: confirm against latest board revision and update or remove. -->

!!! tip "Next"
    Once your mainboard is assembled, **[flash MicroPython](micropython.md)**
    onto it.
