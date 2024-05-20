

# Retrieved string from the database
retrieved_string = "b'\x00\x00\x00\x80\x14\xb7\xc3\xbf\x00\x00\x00\xe0\xc2\xa2\xc5?\x00\x00\x00\xe0\x0f\x93\xc3?\x00\x00\x00@h\x1c\x88?\x00\x00\x00\xc0\xb9K\xa6?\x00\x00\x00@\xe4\t'"  # This should represent the byte data b'\x68\x65\x6c\x6c\x6f'
print(f'retrieved string: {type(retrieved_string)}')
# Step 1: Remove the b' and ' parts
byte_string_content = retrieved_string[2:-1]

# Step 2: Decode using 'unicode_escape' to interpret escape sequences
original_bytes = byte_string_content.encode('latin1').decode('unicode_escape').encode('latin1')
print(f'type of original_bytes: {type(original_bytes)}')
print(original_bytes)  # Output: b'hello'

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
#             # print(encoding)
#     elif key == ord('q'):
#         break

# cv.destroyAllWindows()