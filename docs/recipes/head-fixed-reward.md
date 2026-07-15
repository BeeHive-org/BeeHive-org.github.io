---
title: Head-fixed reward delivery
description: Reward delivery and lick sensing for a head-fixed mouse two-photon setup.
---

# Head-fixed reward delivery

A reward-delivery and lick-sensing module for head-fixed mice under a two-photon microscope. A servo swings a metal lick spout to the animal only during reward, a pinch valve meters the liquid, and BeeHive emits an analogue event signal for alignment with imaging.

## Ingredients

| Board | Qty | Role |
| ----- | --- | ---- |
| [ESP32 BeeHive mainboard](../ingredients/index.md#esp32-mainboard) | 1× | Runs the task, drives the servo, reads the lick sensor, and outputs the analogue event signal. |
| [Solenoid control board](../ingredients/index.md#solenoid-control-board) | 1× | Opens the normally-closed pinch valve to deliver a metered reward. |

Plus (non-BeeHive parts): a Geekservo motor, a metal lick spout, a piezo lick sensor, a 3D-printed frame holding the spout and sensor, a normally-closed solenoid pinch valve (WZ-12021-23, Spexé VapLock), and an NI DAQ for signal capture.

## How it works

The animal is head-fixed under a two-photon microscope and presented with a 10 s visual stimulus. Timing runs as follows:

- **−0.5 s** (0.5 s before the stimulus ends): the Geekservo begins swinging the metal lick spout towards the animal.
- **−0.25 s**: the mainboard triggers the [solenoid control board](../ingredients/index.md#solenoid-control-board), opening the normally-closed pinch valve for **150 ms** to deliver a metered drop of liquid.
- The mouse is given **1 s** to lick. The piezo lick sensor on the spout registers each contact.
- The spout then retracts out of reach until the next trial.

Throughout, BeeHive emits an **analogue voltage signal** to an NI DAQ. The voltage *level* encodes the event type and its *duration* encodes how long the event lasted, so every reward, spout movement and lick can be aligned post-hoc with the two-photon imaging stream on a common timebase.

!!! tip "Two-choice tasks"
    The design extends to **left/right choice tasks** by adding a second spout and a second solenoid — pair a second [solenoid control board](../ingredients/index.md#solenoid-control-board) (or a second channel) and a second servo, and mirror the timing logic per side.

## Wiring

- Servo signal line → a mainboard data line; servo power from the 5 V rail.
- Piezo lick sensor → a mainboard analogue input.
- Pinch valve → the [solenoid control board](../ingredients/index.md#solenoid-control-board) output; the board takes a data line from the mainboard.
- Analogue event output → NI DAQ analogue input channel, sharing ground with the DAQ.

<!-- TODO: add schematic figure once exported from the BeeHive repo -->

!!! note "Schematic"
    The board schematics and connector pinouts live in the [BeeHive repository](https://github.com/BeeHive-org/BeeHive).

## Code

Controlled via MicroPython. The sketch below is a minimal single-spout trial loop.

```python
# TODO: pin numbers are placeholders — set to your wiring.
from machine import Pin, PWM, ADC
import time

servo   = PWM(Pin(12), freq=50)   # Geekservo
valve   = Pin(13, Pin.OUT)        # via solenoid control board
lick    = ADC(Pin(34))            # piezo lick sensor
event   = PWM(Pin(25), freq=50)   # analogue event signal to NI DAQ

RETRACTED, PRESENTED = 40, 90      # servo duty (deg) placeholders

def set_servo(deg):
    servo.duty(int(26 + deg / 180 * 102))

def emit_event(level, ms):
    event.duty(level)              # voltage level = event type
    time.sleep_ms(ms)              # duration = event length
    event.duty(0)

def trial():
    # 10 s visual stimulus handled elsewhere; here we time the reward.
    time.sleep_ms(9500)            # up to 0.5 s before stimulus end
    set_servo(PRESENTED)           # swing spout in
    emit_event(200, 250)           # spout-move event
    time.sleep_ms(250)             # reward at -0.25 s
    valve.on()                     # open pinch valve
    emit_event(500, 150)
    time.sleep_ms(150)
    valve.off()                    # 150 ms open time
    # 1 s lick window
    t0 = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), t0) < 1000:
        if lick.read() > 2000:     # placeholder threshold
            emit_event(800, 10)    # lick event
    set_servo(RETRACTED)           # retract spout

while True:
    trial()
```

## Results / notes

The module adds closed-loop reward delivery and lick detection to an existing head-fixed two-photon rig, with events cleanly aligned to imaging via the analogue DAQ signal. The single-spout build extends to two-choice paradigms by duplicating the spout, servo and solenoid channel.

!!! note "Source"
    See the [BeeHive repository](https://github.com/BeeHive-org/BeeHive) and the BeeHive paper for the reward-delivery module.
