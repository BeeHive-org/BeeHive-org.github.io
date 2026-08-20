---
title: 5-choice serial reaction time task
description: An open-hardware, Python-programmable replication of the 5-CSRTT mouse paradigm.
---

# 5-choice serial reaction time task

An open-hardware replication of the **5-choice serial reaction time task (5-CSRTT)**, a classic mouse paradigm for sustained attention and impulsivity. The original relied on proprietary hardware and a custom language; here it runs on BeeHive plus Python.

## Ingredients

BeeHive boards:

| Board | Qty | Role |
| ----- | --- | ---- |
| [ESP32 BeeHive mainboard](../ingredients/mainboards.md#esp32-mainboard) | 1× | Runs the paradigm, cues the ports, times nose-pokes and triggers reward. |
| [IR sensor array](../ingredients/sensors.md#ir-sensor-array) | 1× | Five IR LED + sensor pairs for beam-break nose-poke detection. |

Other components:

| Component | Qty | Notes |
| --------- | --- | ----- |
| 3D-printed nose-poke ports | 5× | Where the animal pokes. |
| IR LED + IR sensor pairs | 5× | One per port; beam-break poke detection (wired via the IR sensor array). |
| Yellow cue LEDs | 5× | At the rear of each port; cue where to poke. |
| Servo-driven 3D-printed pellet dispenser | 1× | Food reward; shared with the mouse maze. |

## How it works

The animal faces **five nose-poke ports**. On each trial, one port's **yellow LED** at the back lights briefly; the mouse must poke that port to earn a food pellet. Each port carries an **IR LED + IR sensor** pair from the [IR sensor array](../ingredients/sensors.md#ir-sensor-array): a poke breaks the beam, detected with **microsecond precision**, which is what makes accurate reaction-time and premature-response scoring possible.

Correct pokes trigger the **pellet dispenser** — a redesigned open-source dispenser that uses a **servo instead of a stepper** and is laid flat for easy 3D-printing. The same dispenser is shared with the [mouse maze](mouse-maze.md).

Because the whole paradigm lives in **Python**, behavioural variants — cue duration, inter-trial interval, punishment for premature or incorrect responses — are changed purely in code, no rewiring. In practice, **self-directed training reaches stable performance in 7–10 days**, versus the 3–5 months typical of the traditional setup.

## Wiring

- The five IR LED + sensor pairs to the [IR sensor array](../ingredients/sensors.md#ir-sensor-array), which takes a mainboard data line.
- The five yellow cue LEDs to mainboard outputs (or a switch array if pins are tight).
- Pellet dispenser servo to a mainboard data line + 5 V power.

<!-- TODO: add port + wiring schematic and dispenser model reference from the BeeHive repo -->

!!! note "Schematic"
    Port drawings, the dispenser model and board schematics live in the [BeeHive repository](https://github.com/BeeHive-org/BeeHive).

## Code

This box has its own repository —
[BeeHive-org/5-choice-serial-reaction-time](https://github.com/BeeHive-org/5-choice-serial-reaction-time)
— with the full paradigm under
[`software/5-csrtt/`](https://github.com/BeeHive-org/5-choice-serial-reaction-time/tree/main/software/5-csrtt),
driven from a host PC using the [Belay](https://github.com/BrianPugh/belay)
library. The building blocks are small MicroPython test scripts, reproduced
below with the box's actual pin assignments.

Read the five nose-poke IR sensors — a broken beam (`value() == 0`) is a poke
([`IR_test.py`](https://github.com/BeeHive-org/5-choice-serial-reaction-time/blob/main/documentation/testcode/IR_test.py)):

```python
from machine import Pin
from time import sleep

pokes = [Pin(p, Pin.IN) for p in (15, 2, 16, 17, 19)]  # nose-poke IR receivers

while True:
    print([p.value() for p in pokes])
    sleep(1)
```

Light the yellow cue LEDs
([`Led_test.py`](https://github.com/BeeHive-org/5-choice-serial-reaction-time/blob/main/documentation/testcode/Led_test.py))
and drive the pellet-dispenser servo
([`Servo_test.py`](https://github.com/BeeHive-org/5-choice-serial-reaction-time/blob/main/documentation/testcode/Servo_test.py)):

```python
from machine import Pin, PWM
import time

cues = [Pin(p, Pin.OUT) for p in (14, 27, 25, 26, 32)]  # one per nose-poke
dispenser = PWM(Pin(18), freq=50)                        # pellet-dispenser servo

def dispense():
    dispenser.duty(23)               # 0.5 ms pulse -> one end of travel
    time.sleep(1)
    dispenser.duty(123)              # 2.4 ms pulse -> the other end
    time.sleep(1)
```

The complete trial logic — cueing, response scoring, the food magazine, and the
staged training protocol — lives in
[`outside2.py`](https://github.com/BeeHive-org/5-choice-serial-reaction-time/blob/main/software/5-csrtt/outside2.py)
and
[`serial_beehive.py`](https://github.com/BeeHive-org/5-choice-serial-reaction-time/blob/main/software/5-csrtt/serial_beehive.py).

## Results / notes

Replicating the 5-CSRTT on open hardware slashes both cost and training time: self-directed training reaches stable performance in **7–10 days** rather than **3–5 months**, and behavioural paradigms are altered entirely in Python. The servo pellet dispenser is shared with the [mouse maze](mouse-maze.md).

!!! note "Source"
    Full hardware, code and build docs:
    [BeeHive-org/5-choice-serial-reaction-time](https://github.com/BeeHive-org/5-choice-serial-reaction-time).
