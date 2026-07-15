---
title: OpenFlexure stage controller
description: A standalone, PC-free controller for an OpenFlexure Delta Stage.
---

# OpenFlexure stage controller

A standalone controller for an **OpenFlexure Delta Stage** — part of an open two-photon microscope project. Three rotary encoders drive three stepper motors through the mainboard, with live position feedback on an LCD. No PC required.

## Ingredients

| Board | Qty | Role |
| ----- | --- | ---- |
| [ESP32 BeeHive mainboard](../ingredients/index.md#esp32-mainboard) | 1× | Reads the encoders, converts input to delta-stage coordinates and drives the motors. |
| Rotary encoder DB | 3× | One encoder per stage axis / actuator. |
| 28BYJ-48 stepper driver | 3× | Drives the three 28BYJ-48 stepper motors. |
| LCD panel (HD44780, I2C) | 1× | Live position/status feedback. |

<!-- TODO: add rotary encoder DB, 28BYJ-48 driver and HD44780 LCD to ingredients -->

Plus (non-BeeHive parts): three [rotary encoders](https://en.wikipedia.org/wiki/Rotary_encoder), three [28BYJ-48 stepper motors](https://en.wikipedia.org/wiki/Stepper_motor) with driver boards, an [HD44780 character LCD with I2C backpack](https://en.wikipedia.org/wiki/Hitachi_HD44780_LCD_controller), and an [OpenFlexure Delta Stage](https://openflexure.org/projects/deltastage/).

## How it works

The [OpenFlexure Delta Stage](https://openflexure.org/projects/deltastage/) moves its sample with three actuators in a delta geometry. Here, **three rotary encoders** act as the manual interface: turning an encoder feeds counts to the mainboard, which converts them into **delta-stage movement coordinates** and drives the **three 28BYJ-48 stepper motors** accordingly.

Position and status are shown live on an **HD44780 LCD over I2C**, so the whole controller works **without a PC** — USB serial is optional for logging or remote control. The same approach **simplifies to cartesian stages**: with a cartesian geometry the coordinate conversion collapses to one encoder per axis driving one motor.

## Wiring

- Each rotary encoder DB → a mainboard data line (A/B channels), plus power and ground.
- Each 28BYJ-48 driver → mainboard data lines for its motor; motor power from the appropriate rail.
- HD44780 LCD (I2C backpack) → the mainboard I2C data lines (SDA/SCL), plus power and ground.
- Optional USB serial to a host PC.

<!-- TODO: add wiring schematic and delta-stage mounting reference from the BeeHive repo -->

!!! note "Schematic"
    Board schematics and connector pinouts live in the [BeeHive repository](https://github.com/BeeHive-org/BeeHive).

## Code

Controlled via MicroPython. A minimal encoder-to-motor skeleton (coordinate conversion omitted):

```python
# TODO: pins/addresses are placeholders; add the delta-stage coordinate maths
#       and your stepper stepping routine.
from machine import Pin, I2C
import time

# Three encoders (A/B per axis)
enc = [(Pin(4, Pin.IN), Pin(5, Pin.IN)),
       (Pin(12, Pin.IN), Pin(13, Pin.IN)),
       (Pin(14, Pin.IN), Pin(15, Pin.IN))]

lcd_i2c = I2C(0, scl=Pin(22), sda=Pin(21))   # HD44780 via I2C backpack
pos = [0, 0, 0]

def read_delta(i):
    # TODO: quadrature decode -> +1 / -1 / 0
    return 0

def to_stage_coords(pos):
    # TODO: delta-stage geometry; for a cartesian stage this is the identity
    return pos

def drive_motors(target):
    # TODO: step each 28BYJ-48 towards target
    pass

def show(coords):
    # TODO: write coords to the HD44780 over I2C
    pass

while True:
    for i in range(3):
        pos[i] += read_delta(i)
    coords = to_stage_coords(pos)
    drive_motors(coords)
    show(coords)
    time.sleep_ms(5)
```

## Results / notes

The controller gives a self-contained, PC-free way to drive an OpenFlexure Delta Stage from three rotary encoders, with live LCD feedback. It reduces to a simple one-encoder-per-axis controller for cartesian stages.

!!! note "Source"
    See the [BeeHive repository](https://github.com/BeeHive-org/BeeHive) and the [OpenFlexure Delta Stage](https://openflexure.org/projects/deltastage/).
