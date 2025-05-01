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


**LED, Buzzer, and Button Pin Assignment**

In this section of the code, all of the physical components are assigned a particular GPIO pin. These allow the Raspberry Pi to be able to interact with them and control them for their specific funcitons.

![Screenshot 2025-04-30 202310](https://github.com/user-attachments/assets/474596a9-6aa7-4021-b2f5-fd937e4bb3e8)


**Initializing crosswalk request button and Button Press Handler with Sleep Funtion**

We then added the button press handling and a custom sleep function that reacts to crosswalk requests. The function handle_crosswalk() is a debounce event handler which runs when the button is pressed. Checks if the request is already active and sets the flag to true. The button.when_pressed = handle_crosswalk binds the button press event to the handler function so it runs when the button is pressed. Then the smart_sleep function(duration) replaces the sleep(duration) function with a responsive version of it, with 0.1 second intervals and breaks early if crosswalk_requested function becomes True.  

![Screenshot 2025-04-30 204054](https://github.com/user-attachments/assets/a1000424-bb5d-4b60-8ef6-2b096037840c)


**Main Loop**

While the program is running constantly, when the crosswalk_requested is set (True), it begins the crossing sequence and prints the crosswalk mode text. It sets the green light to yellow for 3 seconds, then displays a red and yellow blinking light with a buzzer which comes on with the coundown from 10 seconds to 1. In the final three seconds, the buzzer beeps faster to urge pedestrains to hurry and cross the intersection before the light changes. The last part resumes the normal traffic flow after the crosswalk request, it changes to the red light for two seconds before it changes to green again. 

![Screenshot 2025-04-30 210712](https://github.com/user-attachments/assets/9fdd827e-118a-46a2-a637-6117de816f25)


**Normal Traffic Light Cycle Handler**

The else block runs only if the crosswalk_requested function flag is False. It has the regular green, yellow and red, and an additional red + yellow phase which prepares the drivers to go (it is common in UK/European traffic light systems. After each phase the if crosswalk_requested: continue function is checked and ensures that the loop jumps to the crosswalk logic as soon as a request is made. 

![Screenshot 2025-04-30 211603](https://github.com/user-attachments/assets/1e0cd44a-4354-4c58-b6ea-5e92e2747b23)


**Ends Traffic Light System**
In the final section of the code a KeyboardInterrupt is raised, when Ctrl + C in the terminal is pressed, it turns off all of the LEDS to avoid leaving them on unintentionally. It also prints a final message letting the user know that the program is exited. 


![Screenshot 2025-04-30 212309](https://github.com/user-attachments/assets/5d1b4359-ffce-4c2e-8093-c5bf0ecbda76)


## Robot In Action

[https://youtube.com/shorts/dCBrhuvimsw?si=dH5ITTQ_6hYjhZf1]



