import cv2 as cv
from picamera2 import Picamera2
import face_recognition
import numpy as np
from LCD.display import DisplayOnLCD
import RPi.GPIO as GPIO

# setuo GPIO mode and pin
GPIO.setmode(GPIO.BCM)
face_trigger_button_pin = 6
GPIO.setup(face_trigger_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

display = DisplayOnLCD()

def facial_detection_and_recognition():

    picam2 = Picamera2()

    picam2.preview_configuration.main.size = (800, 800)
    picam2.preview_configuration.main.format = "RGB888"
    picam2.preview_configuration.align()

    picam2.configure("preview")
    
    try:  
        picam2.start()
    except Exception as e:
        print(f"Exception occurred while starting the camera: {e}")
        return
    
    while True:
        try:
            im = picam2.capture_array()  
            
            # cv.imshow("Camera", im)
            
            key = cv.waitKey(1)
            
            # if key == ord('t'):
            if GPIO.input(face_trigger_button_pin) == GPIO.LOW:
                # Convert the captured frame to grayscale
                gray_im = cv.cvtColor(im, cv.COLOR_RGB2GRAY)
                
                # Use OpenCV for face detection
                face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
                faces = face_cascade.detectMultiScale(gray_im, scaleFactor=1.3, minNeighbors=5)

                if len(faces) > 0:
                    # Extract the face region
                    x, y, w, h = faces[0]
                    face_region = gray_im[y:y+h, x:x+w]

                    # Convert the grayscale image to RGB
                    rgb_image = cv.cvtColor(im, cv.COLOR_RGB2BGR)

                    # Use face_recognition to generate face encoding
                    encoding = face_recognition.face_encodings(rgb_image, [(y, x + w, y + h, x)])[0]

                    

                    encoding_bytes = encoding.tobytes()
                    
                
                    print(f"scanned from camera Face encoding(bytes): {encoding_bytes}")

                    cv.destroyAllWindows()
                    picam2.stop()
                    
                    return encoding_bytes
                
                else:
                    print("No face detected")
                    display.random_message('No face detected, Try Again')

                    
            elif key == ord('q'):
                break
        
        except Exception as e:
            print(f"Exception occurred: {e}")
            break

    cv.destroyAllWindows()
    picam2.stop()