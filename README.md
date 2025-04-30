# Raspberry-Pi-Traffic-Light

## What is a Raspberry Pi device?
A Raspberry Pi device is a small, powerful, and inexpensive single-baord computer (SBC). It enables wireless internet & bluetooth connectivity, HDMI/USB/Audio ports, and other devices found on a typical computer. It is commonly used to teach programming and building hardware projects to home automation, robotics, and can also act as a streamer or web server. 

## Labelled Diagram of Raspberry Pi Board.

![RASPBERRY PI BOARD LABELLED](https://github.com/user-attachments/assets/19ebbb48-85b1-46ed-a9ef-0a747b50d28f)

## What can we do with a Raspberry Pi 4 Device?
Using the Raspberry Pi, the options are limitless, for the sake of my final project I decided to do a programmable traffic light robot which carries out the regular functionality of a traffic light- Green, yellow, and red in specific intervals. In addition, like some European traffic lights, I added the feature of a red and yellow static light- this allows drivers and pedestrians to know when the light is about to change. It also has the functionality of a cross-walk feature which signals flashing red and yellow LEDs at a consistent pace, then speeds up at the last three seconds of the countdown timer for crossing. During this countdown and flashing of LEDs, a buzzer feature was also integrated to make pedestrians aware, if not visually, audibly. 

## Setup of Raspberry Pi 4 Traffic Light

![IMG_4119](https://github.com/user-attachments/assets/0fc92131-b269-46e1-8721-b8e469f603fe)

The following pieces of apparatus was used in my robot:

**Physical Apparatus**

1) Raspberry Pi 4
2) Breadboard
3) 3 x 180 Ω resistors
4) 3 x LEDs (Red, Green & Blue)
5) Jumper wires
6) Horn/Buzzer
7) Button

**Coding Environment**

This is built into the Raspberry Pi Board, it comes with a few different programming languages such as C/C++, Javascript, Python (which we used to program our robot), and a couple other languages. The coding environment which was used primarily was built into the Raspberry Pi board called Thonny. All code that is full functional will be associated with a python file named "trafficlight.py" in this repository and can be accessed by anyone. 


## Python Code Analysis

**Importing Libraries**

These libraries listed below are built-in into Python and these coding environments, the functionality of these libraries vary. Let's discuss them:

 **from gpiozero** : a special library designed for interacting with the General Purpose Input/Output (GPIO) pins on a Raspberry Pi (or other compatible systems). It provides a high-level, object-oriented interface for controlling digital I/O devices connected to the GPIO pins, simplifying tasks like turning LEDs on and off, reading button presses, and working with sensors. 

 **import LED, Button, Buzzer** : Classes within gpiozero that provides methods to control an LED (like turning it on/off or blinking). It also allows us to control the input of the button, receiving when it is pressed. The buzzer class allows us to use the buzzer functionality from the gpiozero library as well.

 **from time** :  The time library provides functions for accessing and manipulating time information, including time conversions and time-related tasks.


**import sleep** : The sleep() function, found within Python's time module, serves to pause the execution of the current thread for a specified duration. 
 
![Screenshot 2025-04-29 221222](https://github.com/user-attachments/assets/07f1a4ab-b0d8-40b2-974b-7e1c28c9ea77)





## Robot In Action

[https://youtube.com/shorts/dCBrhuvimsw?si=dH5ITTQ_6hYjhZf1]



