---
title: Welcome
---

# Welcome to BeeHive! 

In this page you will find a bit of the rationale on creating this system, how it relates to other existing systems, how it is structured and how to get started.

If something is not clear, or you would like to contribute as a developer and/or user, feel free to reach out to us on our ["issues page"](https://github.com/BeeHive-org/BeeHive/issues) or via [email](mailto:a.maia-chagas@sussex.ac.uk). We are an open community, and would love to hear from you!

## what is this all about?



**Beehive is an open system designed to make it easier for everyone to develop scientific equipment and learn basic electronics.** 


It is similar **and** compatible with other prototyping systems (since it follow the same order for the pin connectors and we provide adapter boards for the different cables), such as [SeeedStudio's Grove](https://wiki.seeedstudio.com/Grove_System/), [Sparkfun' Qwiic](https://www.sparkfun.com/qwiic) and [Adafruit's STEMMA](https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma)



### Why did you create it if there are other existing systems?

1. To our knowledge the existing prototyping systems are not designed to work with the currents and voltages needed for scientific equipment. For instance, some applications require the use of Peltier elements using 12V and 5A as input, and there are no good breakout boards in existing systems to deal with that.

2. By creating our own ecosystem, we are in full control of what applications and daughter boards we can design. They are created to be exact what we need and perform in the exact way needed.



### System overview:

Beehive was created with modularity in mind, so that bits and parts can be recombined in different ways to 

#### hardware:

:material-puzzle: A central board, which carries a microcontroller and makes all pins of the microncontroller available for connections(right now an ESP32 -  which can be programmed with micropython or C++), 

:material-puzzle: Daughter boards, each executing one task/function. 


#### software:


Here we provide an **Assembly guide** and a **User guide**.



