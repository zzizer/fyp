from RPLCD.i2c import CharLCD
import time

class DisplayOnLCD():

    def __init__(self):
        self.lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4, dotsize=8)
        time.sleep(0.1)

    # call function from class on successul verification of a student
    def on_success(self, reg_no, student_status, seat_no):
        self.lcd.clear()
        self.lcd.cursor_pos = (0, 4)
        self.lcd.write_string(reg_no)

        self.lcd.cursor_pos = (2, 1)
        self.lcd.write_string(student_status)

        self.lcd.cursor_pos = (1, 4)
        self.lcd.write_string('Access Granted')

        self.lcd.cursor_pos = (3, 5)
        self.lcd.write_string(seat_no)
    
    def on_failure(self, reason):
        self.lcd.clear()
        self.lcd.cursor_pos = (0, 4)
        self.lcd.write_string('Access Denied')

        self.lcd.cursor_pos = (1, 0)
        self.lcd.write_string('--------------------')

        self.lcd.cursor_pos = (2, 3)
        self.lcd.write_string(reason)

    def request_fingerprint(self):
        self.lcd.clear()
        self.lcd.cursor_pos = (1, 2)
        self.lcd.write_string('Fingerprint Mode')

        self.lcd.cursor_pos = (2, 0)
        self.lcd.write_string('--------------------')
    
    def request_face(self):
        self.lcd.clear()
        self.lcd.cursor_pos = (0, 1)
        self.lcd.write_string('Facial Recognition')
        self.lcd.cursor_pos = (1, 0)
        self.lcd.write_string('---------------------------')
        self.lcd.cursor_pos = (2, 0)
        self.lcd.write_string('Look into the camera')
        self.lcd.cursor_pos = (3, 0)
        self.lcd.write_string('and press 3rd button')

    def welcome(self):
        self.lcd.clear()
        self.lcd.cursor_pos = (0, 5)
        self.lcd.write_string('ACM-SYSTEM')

        self.lcd.cursor_pos = (1, 0)
        self.lcd.write_string('--------------------')

        self.lcd.cursor_pos = (2, 1)
        self.lcd.write_string('Select Mode To Use')
    
    def processing(self):
        self.lcd.clear()
        self.lcd.cursor_pos = (0, 5)
        self.lcd.write_string('Processing')

        self.lcd.cursor_pos = (1, 0)
        self.lcd.write_string('--------------------')

        self.lcd.cursor_pos = (2, 4)
        self.lcd.write_string('Please Wait...')
    
    def random_message(self, message):
        self.lcd.clear()
        self.lcd.cursor_pos = (1, 2)
        self.lcd.write_string(message)