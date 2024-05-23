import cv2 as cv
from picamera2 import Picamera2
import face_recognition
from LCD.display import DisplayOnLCD
import time

display = DisplayOnLCD()

def preprocess_image(image):
    # Convert image to grayscale for consistency
    gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    # Use histogram equalization to improve contrast
    equalized_image = cv.equalizeHist(gray_image)
    return equalized_image

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

    try:
        display.random_message('Camera Ready')
        time.sleep(2)
        display.random_message('Look into the camera')
        time.sleep(2)

        while True:
            im = picam2.capture_array()
            preprocessed_im = preprocess_image(im)
            
            # Use Dlib's CNN-based face detector for better accuracy
            face_locations = face_recognition.face_locations(im, model="cnn")
            
            if face_locations:
                # Assuming only one face, take the first face found
                top, right, bottom, left = face_locations[0]
                face_image = im[top:bottom, left:right]
                
                # Generate face encoding
                encodings = face_recognition.face_encodings(face_image, known_face_locations=[(top, right, bottom, left)])
                
                if encodings:
                    encoding = encodings[0]
                    encoding_bytes = encoding.tobytes()
                    
                    print(f"Scanned from camera. Face encoding (bytes): {encoding_bytes}")

                    cv.destroyAllWindows()
                    picam2.stop()
                    
                    return encoding_bytes
                else:
                    print("Face detected, but no encoding generated")
                    display.random_message('Face detected, but no encoding generated')
                    time.sleep(2)
            else:
                print("No face detected")
                display.random_message('No face detected, Please try again')
                time.sleep(2)

    except Exception as e:
        print(f"Exception occurred: {e}")

    finally:
        cv.destroyAllWindows()
        picam2.stop()

# if __name__ == "__main__":
#     facial_detection_and_recognition()

# # face_detection_and_recognition.py
# import cv2 as cv
# from picamera2 import Picamera2
# import face_recognition
# from LCD.display import DisplayOnLCD
# import time

# display = DisplayOnLCD()

# def facial_detection_and_recognition():
#     picam2 = Picamera2()
#     picam2.preview_configuration.main.size = (800, 800)
#     picam2.preview_configuration.main.format = "RGB888"
#     picam2.preview_configuration.align()
#     picam2.configure("preview")

#     try:
#         picam2.start()
#     except Exception as e:
#         print(f"Exception occurred while starting the camera: {e}")
#         return

#     try:
#         display.random_message('Camera Ready')
#         time.sleep(2)
#         display.random_message('Look into the camera')
#         time.sleep(2)

#         while True:
#             im = picam2.capture_array()
            
#             # Convert the captured frame to grayscale
#             gray_im = cv.cvtColor(im, cv.COLOR_RGB2GRAY)
                
#             # Use OpenCV for face detection
#             face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
#             faces = face_cascade.detectMultiScale(gray_im, scaleFactor=1.3, minNeighbors=5)

#             if len(faces) > 0:
#                 # Extract the face region
#                 x, y, w, h = faces[0]

#                 # Convert the original image to RGB (as required by face_recognition)
#                 rgb_image = cv.cvtColor(im, cv.COLOR_RGB2BGR)

#                 # Use face_recognition to generate face encoding
#                 encodings = face_recognition.face_encodings(rgb_image, [(y, x + w, y + h, x)])

#                 if encodings:
#                     encoding = encodings[0]
#                     encoding_bytes = encoding.tobytes()
                    
#                     print(f"Scanned from camera. Face encoding (bytes): {encoding_bytes}")

#                     cv.destroyAllWindows()
#                     picam2.stop()
                    
#                     return encoding_bytes
#                 else:
#                     print("Face detected, but no encoding generated")
#                     display.random_message('Face detected, but no encoding generated')
#                     time.sleep(2)
#             else:
#                 print("No face detected")
#                 display.random_message('No face detected, Please try again')
#                 time.sleep(2)

#     except Exception as e:
#         print(f"Exception occurred: {e}")

#     finally:
#         cv.destroyAllWindows()
#         picam2.stop()

# # if __name__ == "__main__":
# #     facial_detection_and_recognition()
