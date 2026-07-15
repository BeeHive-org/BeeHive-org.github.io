---
title: Flashing MicroPython
description: Get MicroPython running on your BeeHive ESP32 mainboard.
---

# Flashing MicroPython

BeeHive is driven mostly with [MicroPython](https://micropython.org/) — a
Python 3 implementation for microcontrollers. This page gets it running on your
mainboard's ESP32.

## Get your ESP32 ready

You'll need two things:

1. **[Thonny IDE](https://thonny.org/)** — a beginner-friendly Python editor
   that can flash and talk to the board. Installation is straightforward.
2. **The latest ESP32 MicroPython firmware** — download the `.bin` from the
   [ESP32 firmware page](https://micropython.org/download/ESP32_GENERIC/).

## Flash the firmware

1. Connect the ESP32 to your computer via USB.
2. In Thonny, go to **Tools > Options > Interpreter**.
3. Set the interpreter to **MicroPython (ESP32)**.
4. For the port, choose the one labelled **Silicon Labs** (the USB-serial chip).
5. Click **Install or update the firmware**.
6. Select the `.bin` file you downloaded and flash it.

A detailed walkthrough is on
[Random Nerd Tutorials](https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/).

## First program

With the firmware installed, Thonny's shell talks to the board live. A quick
blink to confirm everything works:

```python
from machine import Pin
import time

led = Pin(2, Pin.OUT)  # onboard LED on many ESP32 dev boards
while True:
    led.value(not led.value())
    time.sleep(0.5)
```

## Learn the basics

New to programming or microcontrollers? Work through the
**[Intro to electronics course](../courses/intro-to-electronics.md)** — it
covers the fundamentals and comes with the code from BeeHive's
[2022 workshop exercises](https://github.com/BeeHive-org/BeeHive/tree/master/workshops/2022_autum/code).

!!! tip "Prefer C++?"
    The ESP32 also runs Arduino/C++, which is handy when you need an existing
    library — the [mouse maze](../recipes/mouse-maze.md) recipe does this to
    reuse the Adafruit servo driver. Most recipes here use MicroPython.
