---
title: What is this about?
---


**Beehive is an open system designed to make it easier for everyone to develop scientific equipment and learn basic electronics.** 


It is similar **and** compatible with other prototyping systems (since it follow the same order for the pin connectors and we provide adapter boards for the different cables), such as [SeeedStudio's Grove](https://wiki.seeedstudio.com/Grove_System/), [Sparkfun' Qwiic](https://www.sparkfun.com/qwiic) and [Adafruit's STEMMA](https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma)



### Why did you create it if there are other existing systems?

1. To our knowledge the existing prototyping systems are not designed to work with the currents and voltages needed for scientific equipment. For instance, some applications require the use of Peltier elements using 12V and 5A as input, and there are no good breakout boards in existing systems to deal with that.

2. By creating our own ecosystem, we are in full control of what applications and daughter boards we can design. They are created to be exact what we need and perform in the exact way needed.



### System overview:

Beehive was created with modularity in mind, so that bits and parts can be recombined in many ways to create different applications and tools.

#### :material-puzzle: hardware:

- **central board** carries a microcontroller and makes all pins of the microncontroller available for connections(right now an ESP32 - but in principle one can design different central boards to take any available microcontroller)
    - Using ESP32 allows us to have an affordable microcontroller with built-in bluetooth and wifi, an that is available through many online sellers. 

- **Daughter boards** each executing one task/function. 


#### :octicons-file-code-16: software:


 - Currently the system can be driven with Micropython or C++, allowing users to decide based on previous knowledge, and application. All applications described here use Micropython as its language. 

 - The reason for using mostly Micropython is that we can use it for development but also as an introductory programming language for researchers. Given that currently Python is widely used for data analysis in many scientific fields, this allows us to essentially teach one programming to do data collection **and** data analysis.



ADD LINKS WITH EXPLANATIONS TO THE SECTIONS

Here we provide an **Assembly guide** and a **User guide**.



