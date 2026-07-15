---
title: Head-fixed reward delivery
description: Reward delivery and lick sensing for a head-fixed mouse two-photon setup.
---

# Head-fixed reward delivery

A reward-delivery and lick-sensing module for head-fixed mice under a two-photon microscope. A servo swings a metal lick spout to the animal only during reward, a pinch valve meters the liquid, and BeeHive emits an analogue event signal for alignment with imaging.

## Ingredients

BeeHive boards:

| Board | Qty | Role |
| ----- | --- | ---- |
| [ESP32 BeeHive mainboard](../ingredients/mainboards.md#esp32-mainboard) | 1× | Runs the task, drives the servo, reads the lick sensor, and outputs the analogue event signal. |
| [Solenoid control board](../ingredients/actuators.md#solenoid-control-board) | 1× | Opens the normally-closed pinch valve to deliver a metered reward. |

Other components:

| Component | Qty | Notes |
| --------- | --- | ----- |
| Geekservo motor | 1× | Swings the lick spout to the animal during reward. |
| Metal lick spout | 1× | Delivers the liquid reward. |
| Piezo lick sensor | 1× | Detects licks. |
| 3D-printed frame | 1× | Holds the spout and piezo sensor. |
| Solenoid pinch valve (WZ-12021-23, Spexé VapLock) | 1× | Normally-closed; meters the liquid reward. |
| NI DAQ | 1× | Captures BeeHive's analogue event signal for imaging alignment. |

## How it works

The animal is head-fixed under a two-photon microscope and presented with a 10 s visual stimulus. Timing runs as follows:

- **−0.5 s** (0.5 s before the stimulus ends): the Geekservo begins swinging the metal lick spout towards the animal.
- **−0.25 s**: the mainboard triggers the [solenoid control board](../ingredients/actuators.md#solenoid-control-board), opening the normally-closed pinch valve for **150 ms** to deliver a metered drop of liquid.
- The mouse is given **1 s** to lick. The piezo lick sensor on the spout registers each contact.
- The spout then retracts out of reach until the next trial.

Throughout, BeeHive emits an **analogue voltage signal** to an NI DAQ. The voltage *level* encodes the event type and its *duration* encodes how long the event lasted, so every reward, spout movement and lick can be aligned post-hoc with the two-photon imaging stream on a common timebase.

!!! tip "Two-choice tasks"
    The design extends to **left/right choice tasks** by adding a second spout and a second solenoid — pair a second [solenoid control board](../ingredients/actuators.md#solenoid-control-board) (or a second channel) and a second servo, and mirror the timing logic per side.

## Wiring

- Servo signal line to a mainboard data line; servo power from the 5 V rail.
- Piezo lick sensor to a mainboard analogue input.
- Pinch valve to the [solenoid control board](../ingredients/actuators.md#solenoid-control-board) output; the board takes a data line from the mainboard.
- Analogue event output to NI DAQ analogue input channel, sharing ground with the DAQ.

<!-- TODO: add schematic figure once exported from the BeeHive repo -->

!!! note "Schematic"
    The board schematics and connector pinouts live in the [BeeHive repository](https://github.com/BeeHive-org/BeeHive).

## Code

Delivering a reward comes down to opening the solenoid control board's valve for
a fixed time — exactly the BeeHive
[solenoid driver example](https://github.com/BeeHive-org/BeeHive/blob/master/software/code_examples/solenoid_driver/example1.py)
(the pins are the board's default outputs):

```python
from machine import Pin
import time

sole1 = Pin(2, Pin.OUT, drive=Pin.DRIVE_3)   # solenoid control board output

sole1.on()
time.sleep_ms(150)     # 150 ms reward pulse
sole1.off()
```

The full task wraps this valve pulse in the timing described above: a servo
swings the spout in ~0.5 s before stimulus offset, the reward pulse follows
0.25 s later, then a 1 s lick window is read from the piezo sensor, with an
analogue event signal sent to the DAQ (level = event type, duration = event
length). That orchestration is specific to each rig; the reward pulse itself is
the repo example above.

## Results / notes

The module adds closed-loop reward delivery and lick detection to an existing head-fixed two-photon rig, with events cleanly aligned to imaging via the analogue DAQ signal. The single-spout build extends to two-choice paradigms by duplicating the spout, servo and solenoid channel.

!!! note "Source"
    See the [BeeHive repository](https://github.com/BeeHive-org/BeeHive) and the BeeHive paper for the reward-delivery module.
