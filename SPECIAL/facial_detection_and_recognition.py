
def facial_detection_and_recognition():

    face_encoding = "detected face encoding"

    return face_encoding


# print(facial_detection_and_recognition())

# import cv2 as cv
# from picamera2 import Picamera2
# import face_recognition

# picam2 = Picamera2()

# picam2.preview_configuration.main.size = (800, 800)
# picam2.preview_configuration.main.format = "RGB888"
# picam2.preview_configuration.align()

# picam2.configure("preview")  
# picam2.start()

# while True:
#     im = picam2.capture_array()  
    
#     cv.imshow("Camera", im)
    
#     key = cv.waitKey(1)
    
#     if key == ord('t'):
#         # Convert the captured frame to grayscale
#         gray_im = cv.cvtColor(im, cv.COLOR_RGB2GRAY)
        
#         # Use OpenCV for face detection
#         face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
#         faces = face_cascade.detectMultiScale(gray_im, scaleFactor=1.3, minNeighbors=5)

#         if len(faces) > 0:
#             # Extract the face region
#             x, y, w, h = faces[0]
#             face_region = gray_im[y:y+h, x:x+w]

#             # Convert the grayscale image to RGB
#             rgb_image = cv.cvtColor(im, cv.COLOR_RGB2BGR)

#             # Use face_recognition to generate face encoding
#             encoding = face_recognition.face_encodings(rgb_image, [(y, x + w, y + h, x)])[0]

#             # Process the encoding (e.g., store it in the database or perform further actions)
#             print(bytes(encoding))
    
#     elif key == ord('q'):
#         break

# cv.destroyAllWindows()
