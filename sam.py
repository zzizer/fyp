from LCD.display import DisplayOnLCD
import RPi.GPIO as GPIO

# setuo GPIO mode and pin
GPIO.setmode(GPIO.BCM)
face_trigger_button_pin = 16
GPIO.setup(face_trigger_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

display = DisplayOnLCD()

while True:
    display.random_message('Press the button')

    if GPIO.input(face_trigger_button_pin) == GPIO.LOW:
        display.random_message('Button pressed')
        break

# from pyfingerprint.pyfingerprint import PyFingerprint

# try:
#     f = PyFingerprint('/dev/ttyS0', 57600, 0xFFFFFFFF, 0x00000000)
    
#     if not f.verifyPassword():
#         raise ValueError('The given fingerprint sensor password is wrong!')

#         # get_data_from_database()  # Establish a database connection within main

#         # display.random_message("Press Finger")
#     sleep(3)

#     while not f.readImage():
#         pass

#     f.convertImage(FINGERPRINT_CHARBUFFER1)
#     scanned_xtics = f.downloadCharacteristics(FINGERPRINT_CHARBUFFER1)
#     print(scanned_xtics)

# except Exception as e:
#     print('Operation failed!')
