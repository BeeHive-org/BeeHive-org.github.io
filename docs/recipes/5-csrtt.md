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

Controlled via MicroPython. A minimal single-trial skeleton:

```python
# TODO: pins are placeholders — set to your wiring.
from machine import Pin, PWM
import time, urandom

cues   = [Pin(p, Pin.OUT) for p in (4, 5, 12, 13, 14)]   # yellow LEDs
pokes  = [Pin(p, Pin.IN)  for p in (15, 16, 17, 18, 19)]  # IR beam-break
feeder = PWM(Pin(21), freq=50)                            # pellet servo

CUE_MS, RESPONSE_MS = 1000, 5000

def dispense():
    feeder.duty(120); time.sleep_ms(300)      # rotate to drop pellet
    feeder.duty(80)                            # return

def trial():
    target = urandom.getrandbits(3) % 5
    cues[target].on()
    time.sleep_ms(CUE_MS)
    cues[target].off()
    t0 = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), t0) < RESPONSE_MS:
        for i, p in enumerate(pokes):
            if p.value() == 0:                 # beam broken = poke
                if i == target:
                    dispense()                 # correct
                return                         # incorrect / premature scored elsewhere

while True:
    trial()
    time.sleep_ms(2000)                        # inter-trial interval
```

## Results / notes

Replicating the 5-CSRTT on open hardware slashes both cost and training time: self-directed training reaches stable performance in **7–10 days** rather than **3–5 months**, and behavioural paradigms are altered entirely in Python. The servo pellet dispenser is shared with the [mouse maze](mouse-maze.md).

!!! note "Source"
    See the [BeeHive repository](https://github.com/BeeHive-org/BeeHive) and the BeeHive paper for the 5-CSRTT replication.
