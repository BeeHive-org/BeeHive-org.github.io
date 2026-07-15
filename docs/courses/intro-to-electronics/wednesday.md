---
title: Wednesday
description: Data logging and getting data off the microcontroller.
---

# Wednesday

### Data logging

One important thing we want to accomplish with our microcontrollers is to save the data they are collecting while performing a certain task, and given the constraints imposed by the nature of microcontrollers (memory space, communication speeds, time critical events, etc), it is a good idea to give this careful thought when designing experiments/systems.

Let’s use a practical example so that we have a better understanding of the critical points to be observed: 

The ESP32 we are using has 320kb of RAM, which can accomplish a lot, but won’t be enough for recording hours of data stream. In fact, if your system is recording data from a temperature sensor, using 12 bit resolution, you would need 2 bytes (each byte “carries” 8 bits of information) for each data point. If you would like to add information about time to each data collected, plus identify from which system the data has been collected, you would need another ~5 bytes. So every data point would be 7 bytes of information. Considering most applications will have several streams of data (temperature, humidity, triggering time of events, other sensors), and that we still have to factor in the code we write and upload to the board, this can consume all the space available in no time. Therefore, we need to find ways to “unload” data from the microcontroller’s main memory. This normally means transmitting the data to an external storage space, either an SD card, or a computer.

Data transmission can be done using serial communication. We have seen a typical communication speed of 115200 bits per second [which is equivalent to 14400 bytes/sec - 14.4kb/s], so if we want to transmit data from thetemperature sensor, above together with identifiying info, we need seven bytes per data point, plus the overhead of the communication protocol being used. Therefore in one second we can theoretically transmit ~2000 data points for temperature readings (in reality this is less as the device needs to spend time opening the communication port, sending the data, sending other check bits, etc). Another thing to observe is that the microcontroller will be busy sending out data, pretty much unable to do anything else, so we also need to be careful in observing which are appropriate moments to send/receive data.

Once the data is prepared to be transmitted out of the microcontroller, we need code on the receiving side to know what kind of data to expect, where to store it, how often, etc. 	

	


### Wednesday second part

Now we take a small break from doing and working with code, to answer possible questions you might have that have not been covered during the course.
