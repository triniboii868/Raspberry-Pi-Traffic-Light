from gpiozero import LED, Button
import time

# LED setup
red = LED(16)
yellow = LED(18)
green = LED(17)

# Crosswalk button on GPIO 20
button = Button(20)

# Flag to trigger crosswalk mode
crosswalk_requested = False

# Button handler
def handle_crosswalk():
    global crosswalk_requested
    crosswalk_requested = True
    print("Crosswalk button pressed!")

# Assign the button press handler
button.when_pressed = handle_crosswalk

while True:
    if crosswalk_requested:
        print("Handling crosswalk request...")

        # Force red light for pedestrian
        red.on()
        yellow.off()
        green.off()
        time.sleep(10)

        # Transition back to normal
        yellow.on()
        time.sleep(2)
        yellow.off()
        red.off()
        green.on()
        time.sleep(5)
        green.off()

        # Reset the flag
        crosswalk_requested = False
        continue

    # --- Green Light ---
    green.on()
    yellow.off()
    red.off()
    print("Green light")
    time.sleep(5)

    # --- Yellow Light ---
    green.off()
    yellow.on()
    print("Yellow light")
    time.sleep(2)

    # --- Red Light ---
    yellow.off()
    red.on()
    print("Red light")
    time.sleep(5)

    # --- Red + Yellow (optional for realism) ---
    yellow.on()
    time.sleep(1)

    # Back to green
    red.off()
    yellow.off()
