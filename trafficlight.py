from gpiozero import LED, Button, Buzzer 
from time import sleep

# LED setup
red = LED(16)
yellow = LED(18)
green = LED(17)
buzzer = Buzzer(21)

# Crosswalk button with debounce time
button = Button(14, pull_up=True, bounce_time=1)

# Global flag
crosswalk_requested = False

# Debounced button handler
def handle_crosswalk():
    global crosswalk_requested
    if not crosswalk_requested:
        crosswalk_requested = True
        print("🚶 Crosswalk button pressed!")

button.when_pressed = handle_crosswalk

# Smart sleep that checks for crosswalk requests
def smart_sleep(duration):
    for _ in range(int(duration * 10)):  # 0.1s slices
        if crosswalk_requested:
            break
        sleep(0.1)

try:
    while True:
        if crosswalk_requested:
            print("🚨 Crosswalk requested! Preparing to stop traffic...")

            # Transition to yellow for 3 seconds
            print("Preparing to transition to crosswalk mode...")
            green.off()
            yellow.on()
            sleep(3)

            # Red + Yellow blinking for pedestrian countdown
            yellow.off()
            red.off()
            print("🚦 Red + Yellow blinking for pedestrian crossing")

            for i in range(10, 0, -1):
                print(f"🚶 Cross now: {i} seconds")
    
                beep_delay = 0.5 if i > 3 else 0.25  # Faster beeps at the end

                buzzer.on()
                red.on()
                yellow.on()
                sleep(beep_delay)

                buzzer.off()
                red.off()
                yellow.off()
                sleep(beep_delay)


            # Resume traffic
            yellow.on()
            sleep(2)
            yellow.off()
            red.off()
            green.on()
            print("Returning to normal traffic")
            sleep(5)
            green.off()

            crosswalk_requested = False

        else:
            # --- Green Light ---
            green.on()
            yellow.off()
            red.off()
            print("Green light")
            smart_sleep(5)
            if crosswalk_requested: continue

            # --- Yellow Light ---
            green.off()
            yellow.on()
            print("Yellow light")
            smart_sleep(2)
            if crosswalk_requested: continue

            # --- Red Light ---
            yellow.off()
            red.on()
            print("Red light")
            smart_sleep(5)
            if crosswalk_requested: continue

            # --- Red + Yellow (prepare to go) ---
            yellow.on()
            print("Red + Yellow")
            smart_sleep(1)
            if crosswalk_requested: continue

            # Back to green
            red.off()
            yellow.off()

except KeyboardInterrupt:
    red.off()
    yellow.off()
    green.off()
    print("Program exited.")
