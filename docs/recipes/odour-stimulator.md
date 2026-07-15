---
title: Odour stimulator
description: A dual-channel olfactory stimulator with millisecond-precision odour delivery.
---

# Odour stimulator

An open reimplementation of a dual-channel olfactory stimulator (Raiser et al. 2017) for insect olfaction experiments. It delivers two precisely controlled odour streams, balanced by two clean-air streams, for stable flow with millisecond precision.

## Ingredients

BeeHive boards:

| Board | Qty | Role |
| ----- | --- | ---- |
| [ESP32 BeeHive mainboard](../ingredients/mainboards.md#esp32-mainboard) | 1× | Sequences and times the valve switching. |
| [Spike & Hold board](../ingredients/actuators.md#spike-and-hold-board) | 2× | Fast, precise switching of the Teflon solenoid valves. |

Other components:

| Component | Qty | Notes |
| --------- | --- | ----- |
| Three-way Teflon solenoid valves (LHDA1233415H, Lee Company) | 4× | Two odour + two clean-air streams. |
| Custom 3D-printed mixing block (polypropylene) | 1× | Mixes odour and clean-air streams; expandable channels. |
| Air supply & flow regulation | 1× | Balanced streams for stable flow. |
| Photoionization detector (PID) | 1× | For validating stimulus timing (optional). |

## How it works

The stimulator runs **two odour channels balanced by two clean-air channels**. When an odour stream is switched *in*, a matched clean-air stream is switched *out*, so the total flow reaching the animal stays constant — this is what keeps the stimulus free of pressure and flow artefacts. Each stream is gated by a **three-way Teflon solenoid valve** (LHDA1233415H) feeding a custom **3D-printed polypropylene mixing block**, chosen for its chemical inertness to odourants.

The valves are switched by two [Spike & Hold boards](../ingredients/actuators.md#spike-and-hold-board), which briefly overdrive each solenoid so it opens in hundreds of microseconds — giving the **millisecond timing precision** the paradigm needs. The channel count is expandable: add valves and Spike & Hold channels for richer odour panels.

Typical uses include **single-sensillum recordings**, **insect wind-tunnel** flight and walking assays, and **single-fly chambers**.

## Wiring

- Each three-way solenoid valve to a channel on a [Spike & Hold board](../ingredients/actuators.md#spike-and-hold-board).
- Each [Spike & Hold board](../ingredients/actuators.md#spike-and-hold-board) to a mainboard data line, plus power and ground. Spike & Hold mode pairs with the 12V/24V boost converter for the overdrive pulse.
- Air lines route through the valves into the 3D-printed mixing block; the combined stream goes to the preparation.

<!-- TODO: add mixing-block + valve schematic and airflow diagram from the BeeHive repo -->

!!! note "Schematic"
    Board schematics, the mixing-block model and connector pinouts live in the [BeeHive repository](https://github.com/BeeHive-org/BeeHive).

## Code

Controlled via MicroPython. A minimal balanced-switch pulse:

```python
# TODO: pin numbers are placeholders — set to your wiring.
from machine import Pin
import time

odour_a = Pin(12, Pin.OUT)   # odour valve, channel A (Spike & Hold)
air_a   = Pin(13, Pin.OUT)   # balancing clean-air valve, channel A

def pulse_odour(ms):
    # switch odour in and clean air out together to hold flow constant
    air_a.off()
    odour_a.on()
    time.sleep_ms(ms)
    odour_a.off()
    air_a.on()

air_a.on()                   # clean air on by default
pulse_odour(50)              # 50 ms odour pulse
```

## Results / notes

The stimulator reproduces the Raiser et al. (2017) design on open hardware, delivering balanced, millisecond-precise odour pulses validated with a **PID (photoionization detector)**. Channels expand by adding valves and Spike & Hold boards.

!!! note "Source"
    Reimplements Raiser, G. et al. (2017), *A Modular Dynamic Configurable Odour Delivery Device for Insect Olfaction Experiments*. See also the [BeeHive repository](https://github.com/BeeHive-org/BeeHive).
