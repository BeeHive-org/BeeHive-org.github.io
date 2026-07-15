---
title: Mouse-wheel speed controller
description: Motor-and-clutch speed control for the open-source KineMouse running wheel.
---

# Mouse-wheel speed controller

An add-on that gives the experimenter control over a running wheel's timing and minimum speed. It enhances the open-source **KineMouse** wheel with a motor and clutch, so a mouse can run *faster* than the motor and keep running when the motor is off — supporting the 3Rs by reducing session count and duration.

## Ingredients

BeeHive boards:

| Board | Qty | Role |
| ----- | --- | ---- |
| [ESP32 BeeHive mainboard](../ingredients/mainboards.md#esp32-mainboard) | 1× | Reads the speed potentiometer and drives the stepper motor. |

Other components:

| Component | Qty | Notes |
| --------- | --- | ----- |
| [Adafruit DRV8833](https://www.adafruit.com/product/3297) | 1× | Off-the-shelf stepper driver for the NEMA 17. |
| NEMA 17 stepper motor | 1× | Sets the wheel's minimum speed. |
| Clutch | 1× | Lets the mouse run faster than the motor, and keep running when it's off. |
| Analog potentiometer | 1× | Sets the target wheel speed. |
| KineMouse running wheel | 1× | The open-source wheel being enhanced. |

## How it works

The [KineMouse](https://github.com/G-Node/kinemouse) wheel is a lightweight open-source running wheel. This recipe couples it to a **NEMA 17 stepper** through a **clutch**:

- The **motor** sets a **minimum running speed** and controls **when** the wheel turns, so the experimenter — not the animal — decides the timing.
- The **clutch** decouples motor and wheel one way: the mouse can always run *faster* than the motor, and can keep the wheel spinning **when the motor is off**.
- Wheel speed is set live by an **analog potentiometer** read on a mainboard analogue input; the mainboard translates that into a stepper rate.

By letting the experimenter enforce running periods and a floor speed, sessions can be made shorter and fewer — aligning with the **3Rs** (replacement, reduction, refinement).

## Wiring

- Potentiometer wiper to a mainboard analogue input; ends to 3.3 V and ground.
- [Adafruit DRV8833](https://www.adafruit.com/product/3297) control inputs to mainboard data lines; motor power and ground from the appropriate rail.
- NEMA 17 stepper to the DRV8833 outputs; the stepper shaft drives the wheel through the clutch.

<!-- TODO: add wiring schematic and clutch assembly reference from the BeeHive repo -->

!!! note "Schematic"
    Board schematics and the clutch/mount model live in the [BeeHive repository](https://github.com/BeeHive-org/BeeHive).

## Code

Controlled via MicroPython. A minimal potentiometer-to-stepper loop:

```python
# TODO: pins are placeholders — set to your wiring and stepper coil order.
from machine import Pin, ADC
import time

pot   = ADC(Pin(34))                               # speed potentiometer
coils = [Pin(p, Pin.OUT) for p in (12, 13, 14, 15)]  # DRV8833 inputs
SEQ   = [(1,0,1,0), (0,1,1,0), (0,1,0,1), (1,0,0,1)]

step = 0
while True:
    speed = pot.read()                             # 0..4095
    if speed < 40:                                 # near zero = motor off
        for c in coils: c.off()                    # clutch lets wheel free-run
        time.sleep_ms(20)
        continue
    delay = 40 - int(speed / 4095 * 38)            # higher pot = faster
    step = (step + 1) % 4
    for c, v in zip(coils, SEQ[step]):
        c.value(v)
    time.sleep_ms(delay)
```

## Results / notes

Adding a motor and clutch to the KineMouse wheel hands timing and minimum-speed control to the experimenter while never restraining the animal's ability to run faster or coast. The shorter, fewer sessions it enables support the 3Rs.

!!! note "Source"
    See the [BeeHive repository](https://github.com/BeeHive-org/BeeHive), the [KineMouse wheel](https://github.com/G-Node/kinemouse), and the [Adafruit DRV8833](https://www.adafruit.com/product/3297).
