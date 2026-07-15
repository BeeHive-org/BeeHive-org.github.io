---
title: LI-850 multiplexer
description: Parallelise metabolic-rate measurements by multiplexing a Licor LI-850 across up to six chambers.
---

# LI-850 multiplexer

A multiplexer that lets a single **Licor LI-850** CO₂/H₂O gas analyser serve up to **six** gas-tight chambers in turn, parallelising metabolic-rate measurements of small invertebrates. BeeHive routes air one chamber at a time, then logs the analyser's readings to CSV.

## Ingredients

| Board | Qty | Role |
| ----- | --- | ---- |
| [ESP32 BeeHive mainboard](../ingredients/index.md#esp32-mainboard) | 1× | Sequences the chambers, talks to the LI-850 over serial, and logs to CSV. |
| [Solenoid control board](../ingredients/index.md#solenoid-control-board) | 6× | One board per chamber, each switching that chamber's inflow and outflow valves. |

Plus (non-BeeHive parts): up to 6 gas-tight chambers, 12 inflow/outflow solenoid valves (one pair per chamber), a Licor LI-850 CO₂/H₂O gas analyser with serial output, and tubing/manifolds.

## How it works

Measuring metabolic rate one chamber at a time wastes most of the session waiting for readings to stabilise and swapping animals. Here, **six chambers stay loaded** and BeeHive cycles through them.

Each chamber has an **inflow** and an **outflow** solenoid valve, controlled independently by its own [solenoid control board](../ingredients/index.md#solenoid-control-board). To measure a chamber, the mainboard:

1. Closes every other chamber's valves and **opens the air path** through the selected chamber (its inflow and outflow valves).
2. Waits for the flow and gas concentration to **stabilise**.
3. **Pings the LI-850** over serial using its documented command grammar and reads back CO₂ and H₂O.
4. **Appends** the reading, with chamber ID and timestamp, to a CSV file.
5. Moves to the next chamber.

Because chambers are pre-loaded and cycled automatically, the per-experiment **stabilisation dead-time** and manual animal-swapping are cut sharply. Validation showed that **multiplexed stabilisation matches the single-chamber system** — routing through the manifold does not degrade the measurement.

## Wiring

- Each of the 6 [solenoid control boards](../ingredients/index.md#solenoid-control-board) → a mainboard data line, plus 12 V power and ground. Each board switches its chamber's inflow and outflow valves.
- LI-850 serial (UART) → the mainboard UART lines (respect the analyser's logic levels; add a [level shifter](../ingredients/index.md#level-shifter) if needed).
- Chambers plumb inflow → chamber → outflow → analyser through a shared manifold.

<!-- TODO: add manifold + valve schematic and plumbing diagram from the BeeHive repo -->

!!! note "Schematic"
    Board schematics, connector pinouts and the manifold layout live in the [BeeHive repository](https://github.com/BeeHive-org/BeeHive).

## Code

Controlled via MicroPython. This sketch drives the six chambers, pings the LI-850 and logs to CSV. Pin numbers and the exact serial grammar are placeholders — set them to your wiring and the LI-850 manual.

```python
# TODO: set pins to your wiring; confirm the LI-850 command/response grammar
#       against the analyser's manual.
from machine import Pin, UART
import time

# One solenoid control board per chamber; each exposes an inflow + outflow line.
CHAMBERS = [
    {"inflow": Pin(4,  Pin.OUT), "outflow": Pin(5,  Pin.OUT)},
    {"inflow": Pin(12, Pin.OUT), "outflow": Pin(13, Pin.OUT)},
    {"inflow": Pin(14, Pin.OUT), "outflow": Pin(15, Pin.OUT)},
    {"inflow": Pin(16, Pin.OUT), "outflow": Pin(17, Pin.OUT)},
    {"inflow": Pin(18, Pin.OUT), "outflow": Pin(19, Pin.OUT)},
    {"inflow": Pin(21, Pin.OUT), "outflow": Pin(22, Pin.OUT)},
]

STABILISE_S = 60            # dead-time to let flow + gas settle
uart = UART(2, baudrate=9600, tx=25, rx=26)   # link to the LI-850


def select_chamber(i):
    """Open the air path through chamber i, close all others."""
    for j, ch in enumerate(CHAMBERS):
        on = (j == i)
        ch["inflow"].value(on)
        ch["outflow"].value(on)


def read_li850():
    """Ping the LI-850 and parse CO2 / H2O from its reply."""
    uart.write(b"<li850><rs>?</rs></li850>\r\n")   # placeholder query
    time.sleep_ms(500)
    line = uart.readline()
    if not line:
        return None, None
    # placeholder parse: expect "CO2=<ppm>,H2O=<ppt>"
    fields = dict(kv.split("=") for kv in line.decode().strip().split(","))
    return float(fields.get("CO2", "nan")), float(fields.get("H2O", "nan"))


def run(cycles=10):
    with open("li850_log.csv", "a") as f:
        f.write("timestamp_ms,chamber,co2_ppm,h2o_ppt\n")
        for _ in range(cycles):
            for i in range(len(CHAMBERS)):
                select_chamber(i)
                time.sleep(STABILISE_S)          # wait for stabilisation
                co2, h2o = read_li850()
                f.write("{},{},{},{}\n".format(time.ticks_ms(), i, co2, h2o))
                f.flush()


run()
```

## Results / notes

The multiplexer turns one gas analyser into a six-chamber respirometry system, removing most of the per-chamber stabilisation dead-time and the manual animal-swapping that dominate single-chamber runs. Validation showed multiplexed stabilisation matching the single-chamber baseline, so throughput rises without loss of measurement quality.

!!! note "Source"
    See the [BeeHive repository](https://github.com/BeeHive-org/BeeHive) and the [Licor LI-850](https://www.licor.com/products/gas-analysis/LI-850) documentation for the serial command grammar.
