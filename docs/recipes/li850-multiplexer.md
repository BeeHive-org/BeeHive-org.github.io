---
title: LI-850 multiplexer
description: Parallelise metabolic-rate measurements by multiplexing a Licor LI-850 across up to six chambers.
---

# LI-850 multiplexer

A multiplexer that lets a single **Licor LI-850** CO₂/H₂O gas analyser serve up to **six** gas-tight chambers in turn, parallelising metabolic-rate measurements of small invertebrates. BeeHive routes air one chamber at a time, then logs the analyser's readings to CSV.

## Ingredients

BeeHive boards:

| Board | Qty | Role |
| ----- | --- | ---- |
| [ESP32 BeeHive mainboard](../ingredients/mainboards.md#esp32-mainboard) | 1× | Sequences the chambers, talks to the LI-850 over serial, and logs to CSV. |
| [Solenoid control board](../ingredients/actuators.md#solenoid-control-board) | 6× | One board per chamber, each switching that chamber's inflow and outflow valves. |

Other components:

| Component | Qty | Notes |
| --------- | --- | ----- |
| Gas-tight chambers | up to 6× | Hold the animals during measurement. |
| Inflow/outflow solenoid valves | 12× | One inflow + one outflow valve per chamber. |
| Licor LI-850 CO₂/H₂O gas analyser | 1× | Measures CO₂ and H₂O; serial output. |
| Tubing & manifolds | 1× | Plumb the shared air path. |

## How it works

Measuring metabolic rate one chamber at a time wastes most of the session waiting for readings to stabilise and swapping animals. Here, **six chambers stay loaded** and BeeHive cycles through them.

Each chamber has an **inflow** and an **outflow** solenoid valve, controlled independently by its own [solenoid control board](../ingredients/actuators.md#solenoid-control-board). To measure a chamber, the mainboard:

1. Closes every other chamber's valves and **opens the air path** through the selected chamber (its inflow and outflow valves).
2. Waits for the flow and gas concentration to **stabilise**.
3. **Pings the LI-850** over serial using its documented command grammar and reads back CO₂ and H₂O.
4. **Appends** the reading, with chamber ID and timestamp, to a CSV file.
5. Moves to the next chamber.

Because chambers are pre-loaded and cycled automatically, the per-experiment **stabilisation dead-time** and manual animal-swapping are cut sharply. Validation showed that **multiplexed stabilisation matches the single-chamber system** — routing through the manifold does not degrade the measurement.

## Wiring

- Each of the 6 [solenoid control boards](../ingredients/actuators.md#solenoid-control-board) to a mainboard data line, plus 12 V power and ground. Each board switches its chamber's inflow and outflow valves.
- LI-850 serial (UART) to the mainboard UART lines (respect the analyser's logic levels; add a [level shifter](../ingredients/utilities.md#level-shifter) if needed).
- Air is plumbed from each chamber's inflow, through the chamber and its outflow, to the analyser via a shared manifold.

<!-- TODO: add manifold + valve schematic and plumbing diagram from the BeeHive repo -->

!!! note "Schematic"
    Board schematics, connector pinouts and the manifold layout live in the [BeeHive repository](https://github.com/BeeHive-org/BeeHive).

## Code

Two parts: switching each chamber's valves (standard BeeHive code) and polling
the LI-850 over serial (specific to this setup).

**Valve control** uses the solenoid daughter-board pattern from the BeeHive
[solenoid driver example](https://github.com/BeeHive-org/BeeHive/blob/master/software/code_examples/solenoid_driver/example1.py)
— one output per valve, driven high to open:

```python
from machine import Pin
import time

# BeeHive solenoid-driver outputs; one Pin per inflow / outflow valve.
sole1 = Pin(2,  Pin.OUT, drive=Pin.DRIVE_3)
sole2 = Pin(15, Pin.OUT, drive=Pin.DRIVE_3)
sole3 = Pin(16, Pin.OUT, drive=Pin.DRIVE_3)
sole4 = Pin(17, Pin.OUT, drive=Pin.DRIVE_3)

sole1.on()              # open a chamber's valve
time.sleep_ms(1000)
sole1.off()
```

**Polling the LI-850** and logging to CSV is specific to this rig and isn't
published upstream. The sketch below shows the shape — confirm the serial
grammar against the
[LI-850 manual](https://www.licor.com/products/gas-analysis/LI-830-LI-850):

```python
# ILLUSTRATIVE — not upstream code; the serial grammar is a placeholder.
from machine import UART
import time

uart = UART(2, baudrate=9600, tx=25, rx=26)   # link to the LI-850

def read_li850():
    uart.write(b"<li850><rs>?</rs></li850>\r\n")   # placeholder query
    time.sleep_ms(500)
    line = uart.readline()
    return line.decode().strip() if line else None

# For each chamber in turn: open its valves, wait to stabilise, read + log.
```

## Results / notes

The multiplexer turns one gas analyser into a six-chamber respirometry system, removing most of the per-chamber stabilisation dead-time and the manual animal-swapping that dominate single-chamber runs. Validation showed multiplexed stabilisation matching the single-chamber baseline, so throughput rises without loss of measurement quality.

!!! note "Source"
    See the [BeeHive repository](https://github.com/BeeHive-org/BeeHive) and the [Licor LI-850](https://www.licor.com/products/gas-analysis/LI-830-LI-850) documentation for the serial command grammar.
