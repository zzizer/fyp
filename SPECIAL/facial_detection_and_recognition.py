import tensorflow as tf
import numpy as np
from mtcnn import MTCNN
import cv2 as cv

model_path = tf.saved_model.load("/home/fyp/Desktop/model/20180402-114759.pb")
model = load_facenet_model(model_path)

def preprocess_image(image):
    image = tf.image.resize(image, (160, 160))
    image = (image - 127.5) / 127.5
    return np.expand_dims(image, axis=0)

detector = MTCNN()

def load_image(image_path):
    image=tf.io.read_file(image_path)
    image=tf.image.decode_jpeg(image, channels=3)
    return image

image_path = "/home/fyp/Desktop/photos/2000706650.jpeg"
image = load_image(image_path)

detections = detector.detect_faces(image.numpy())

if detections:
    x, y, width, height = detections[0]["box"]
    face = image[y:y+height, x:x+width]
    preprocessed_face = preprocess_image(face)


    embeddings = model(preprocessed_face)

    print(embeddings)

else:
    print("No face detected")

# def facial_detection_and_recognition():

#     face_encoding = "detected face encoding"

#     return face_encoding

# print(facial_detection_and_recognition())


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
