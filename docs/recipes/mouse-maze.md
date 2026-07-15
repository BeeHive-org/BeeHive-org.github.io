---
title: Mouse maze
description: A modular, reconfigurable mouse maze with closed-loop IR tracking and servo-driven rewards.
---

# Mouse maze

A modular maze built from swappable acrylic panels, with closed-loop tracking: an IR camera and a Python state machine follow the animal and tell BeeHive when to dispense a reward.

## Ingredients

| Board | Qty | Role |
| ----- | --- | ---- |
| [ESP32 BeeHive mainboard](../ingredients/mainboards.md#esp32-mainboard) | 1× | Receives serial commands from the tracking PC and drives the reward hardware. |
| [IR sensor array](../ingredients/sensors.md#ir-sensor-array) | 1× | Local IR sensing at reward ports / beam-breaks. |

Plus (non-BeeHive parts): 50 × 50 mm acrylic maze panels (opaque in visible light, transparent in IR), Makerbeam XL posts, a 16-channel 12-bit PWM/servo driver (Adafruit PCA9685, I2C), a servo-driven 3D-printed pellet dispenser, an IR camera, and a PC running OpenCV.

## How it works

The maze is assembled from **50 × 50 mm acrylic panels** that slot vertically between **Makerbeam XL** posts, so the layout is reconfigured by hand in minutes. Panels are opaque in the visible range but transparent in IR, so an overhead **IR camera** sees straight through the walls to track the animal while the mouse sees an opaque maze. Panels are swapped for textures, gratings or reward ports as the experiment demands.

Control is **closed-loop**:

1. The IR camera feeds video to a PC.
2. **OpenCV** tracks the animal, and a **Python state machine** decides when reward is due.
3. The PC sends a **serial command** to the BeeHive mainboard.
4. The mainboard triggers the **pellet dispenser** (and any port hardware on the [IR sensor array](../ingredients/sensors.md#ir-sensor-array)).

The pellet dispenser was redesigned to use a **servo instead of a stepper**, which makes it far easier to 3D-print and share. Servos are driven through the **PCA9685** PWM driver over I2C; a single PCA9685 chain can address a large number of servos — up to **992 servos over just two data lines** when daisy-chained — so many reward ports scale without extra mainboard pins.

## Wiring

- PCA9685 to mainboard I2C (SDA/SCL data lines) + power and ground; the dispenser servo(s) connect to the PCA9685 outputs.
- [IR sensor array](../ingredients/sensors.md#ir-sensor-array) to a mainboard data line for port sensing.
- The tracking PC connects to the mainboard over USB serial.

<!-- TODO: add maze + wiring schematic figure from the BeeHive repo -->

!!! note "Schematic"
    Panel drawings, the dispenser model and board schematics live in the [BeeHive repository](https://github.com/BeeHive-org/BeeHive).

## Code

!!! note "Written in C++"
    Unlike most BeeHive recipes, the maze firmware is written in **C++ (Arduino)** rather than MicroPython. This let it reuse the **Adafruit PWM Servo Driver** library for the PCA9685 and an existing **serial-command parsing** library. It is a good example of BeeHive's language flexibility — the same mainboard runs either toolchain.

```cpp
// TODO: pins/addresses are placeholders — set to your wiring.
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40);

void setup() {
  Serial.begin(115200);
  pwm.begin();
  pwm.setPWMFreq(50);        // servo update rate
}

void dispensePellet(uint8_t ch) {
  pwm.setPWM(ch, 0, 400);    // rotate to dispense
  delay(300);
  pwm.setPWM(ch, 0, 200);    // return
}

void loop() {
  // Serial command from the OpenCV state machine, e.g. "R3\n" = reward port 3
  if (Serial.available()) {
    char cmd = Serial.read();
    if (cmd == 'R') {
      int port = Serial.parseInt();
      dispensePellet(port);
    }
  }
}
```

## Results / notes

The maze is quick to reconfigure, tracks through the walls in IR, and rewards in closed loop from a standard PC vision pipeline. Moving the dispenser to a servo makes the whole build printable and shareable. The same servo-driven pellet dispenser is reused in the [5-choice serial reaction time task](5-csrtt.md).

!!! note "Source"
    See the [BeeHive repository](https://github.com/BeeHive-org/BeeHive) and the [Adafruit PCA9685 servo driver](https://www.adafruit.com/product/815).
