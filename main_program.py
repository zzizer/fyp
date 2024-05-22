import RPi.GPIO as GPIO
import time
from LCD.display import DisplayOnLCD
from SPECIAL.main_fingerprint import main
from SPECIAL.main_facial import main1
import numpy as np

display = DisplayOnLCD()

# Set the GPIO mode and pins
GPIO.setmode(GPIO.BCM)

# Define the pins for the buttons and LEDs
button_pin_1 = 5
button_pin_2 = 22
led_pin_1 = 23
led_pin_2 = 24

# specialbutton1 = 6
specialbutton2 = 16

# Setup GPIO pins
GPIO.setup(button_pin_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin_1, GPIO.OUT)
GPIO.setup(led_pin_2, GPIO.OUT)

# Helper function to handle LED control
def control_led(led_pin, state):
    GPIO.output(led_pin, state)

# Turn off both LEDs at the beginning
control_led(led_pin_1, False)
control_led(led_pin_2, False)

# Variable to track the current mode
current_mode = None

# Function to handle button press with debounce
def button_pressed(pin):
    time.sleep(0.2)  # Debounce time
    return GPIO.input(pin) == GPIO.LOW

# Main loop
try:
    display.welcome()

    while True:
        # Check if button 1 is pressed
        if button_pressed(button_pin_1):
            if current_mode != 1:
                # Enter mode 1
                control_led(led_pin_1, True)
                control_led(led_pin_2, False)
                display.request_fingerprint()
                time.sleep(4)
                timeout_start = time.time()

                while True:
                    main()
                    time.sleep(0.9)

                    # Check if button 2 is pressed to break out of the inner loop
                    if button_pressed(button_pin_2):
                        break

                    # Check if timeout is reached (e.g., 10 seconds)
                    if time.time() - timeout_start > 10:
                        break

                control_led(led_pin_1, False)
                control_led(led_pin_2, False)
                current_mode = 1

        # Check if button 2 is pressed
        elif button_pressed(button_pin_2):
            if current_mode != 2:
                # Enter mode 2
                control_led(led_pin_1, False)
                control_led(led_pin_2, True)
                # print('Button for green pressed')
                display.request_face()
                time.sleep(4)
                timeout_start = time.time()

                while True:
                    main1()
                    time.sleep(0.9)

                    # Check if button 1 is pressed to break out of the inner loop
                    if button_pressed(button_pin_1):
                        break

                    # Check if timeout is reached (e.g., 10 seconds)
                    if time.time() - timeout_start > 10:
                        break
                display.request_face()
                current_mode = 2

except KeyboardInterrupt:
    # Clean up GPIO
    GPIO.cleanup()
