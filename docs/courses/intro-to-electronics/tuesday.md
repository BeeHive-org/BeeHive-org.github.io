---
title: Tuesday
description: Timers and counters on the microcontroller.
---

# Tuesday

### What is timer and what is counter?

[timers.dvi (ou.edu)](https://www.cs.ou.edu/~fagg/classes/es_general/timers.pdf)

Counters, as the name suggests, are hardware mechanisms for counting some form of event. At the heart of the counter is a special purpose register that stores the current value of the counter. Any time that a certain event occurs, the value of this counter is incremented (+1 is added to the value). The type of event that causes this increment is typically configurable through other special purpose registers. Because the counter value is stored in a special purpose register, this implies that the value can also be read from or written to by the executing code. Also, different counters will store values of different sizes. The typical sizes for 8-bit microcontrollers, such as the Atmel MegaX line, are 8 and 16 bits (1 and 2 bytes). Because of this finite size, the counter can only count to a maximum value (255 for an 8-bit counter, and 65535 for a 16-bit counter). Once the counter reaches this maximum value, and a new event occurs, the counter resets back to zero. From here, the counter continues to increment with each event

In addition to counting external events, it is possible to also count events that are internal to the processor. In particular, by using the system clock (or a derivative thereof), the counter can be incremented at regular intervals. In this form, the counter becomes a form of timer. Often, the system clock is running at some “high” frequency (e.g., in our microcontrollers, we might see clocks of 16 MHz or 20 MHz). However, it is often the case that we may want our timer to count at much slower rates. This is handled in microcontrollers through the use of hardware prescalers that divide the system clock down to some reasonable frequency. Figure 3 shows the relationship between the system clock, the prescaler and the counter value. Prescalers are implemented as counters in and of themselves. Recall that if some counter is being incremented at a regular frequency, f, then bit 0 of the counter is exhibiting a regular signal at a frequency of f/2. Furthermore, bit 1 has a frequency of f/4. By “tapping into” the prescaler counter at different bits, we can divide the system clock by a range of different divisors (where the divisor takes a form of 2<sup>i</sup> for some i).

We would now like to answer questions involving the rate at which our counter is counting or the amount of time that a certain number of counts will take. In order to talk about these ideas, we first must be able to distinguish between cycles/second of the main system clock and of the prescaled signal. Here, we have artificially defined the unit of a “tick” as a single cycle of the system clock and “tock” as a single cycle of the prescaled signal. Hence, we can express prescaler values in terms of ticks per tock, i.e, how many system clock cycles compose a single prescaled cycle. Example: assume a system clock of 16, 000, 000 ticks/sec and a prescaler of 64 ticks/tock. What is the period of a single increment of the Timer 0 counter?

The answer:



$$ {64\ \text{ticks/tock} \over 16{,}000{,}000\ \text{ticks/sec}} \times 1\ \text{tock} = 4\ \mu\text{s} $$


Example: What is the period of 250 increments of the Timer 0 counter? Answer:



$$ {64\ \text{ticks/tock} \over 16{,}000{,}000\ \text{ticks/sec}} \times 250\ \text{tocks} = 4\ \text{ms} $$


What timers are in ESP32? (optional)
