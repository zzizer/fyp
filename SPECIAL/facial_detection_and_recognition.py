import cv2 as cv
from picamera2 import Picamera2
import face_recognition
import numpy as np

def facial_detection_and_recognition():

    picam2 = Picamera2()

    picam2.preview_configuration.main.size = (800, 800)
    picam2.preview_configuration.main.format = "RGB888"
    picam2.preview_configuration.align()

    picam2.configure("preview")  
    picam2.start()

    while True:
        im = picam2.capture_array()  
        
        cv.imshow("Camera", im)
        
        key = cv.waitKey(1)
        
        if key == ord('t'):
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

                # Process the encoding (e.g., store it in the database or perform further actions)
                # print(bytes(encoding))
                # print(encoding)
                # encoding_bytes = bytes(np.array(encoding).tobytes())

                encoding_bytes = encoding.tobytes()
                
                # saved_encoding = np.frombuffer(encoding_bytes, dtype=np.float64)

                # face_distances = face_recognition.face_distance([encoding], encoding)
                # face_distances = face_recognition.face_distance([encoding], saved_encoding)

                # similarity_percentage = (1 - face_distances[0]) * 100

                # threshold = 0.85
                # is_match = face_distances[0] <= threshold
                
                # print(similarity_percentage)

                # return encoding
                return encoding_bytes
            
            else:
                print("No face detected")
                
        elif key == ord('q'):
            break

    cv.destroyAllWindows()
    picam2.stop()

# print(facial_detection_and_recognition())

# import tensorflow as tf
# import numpy as np
# from mtcnn import MTCNN
# import cv2 as cv

# model = tf.saved_model.load("/home/fyp/Desktop/model")
# # model = load_facenet_model(model_path)
# print('model loaded')

# # print(model.signatures.keys())

# def preprocess_image(image):
#     image = tf.image.resize(image, (160, 160))
#     image = (image - 127.5) / 127.5
#     return np.expand_dims(image, axis=0)

# detector = MTCNN()

# def load_image(image_path):
#     image=tf.io.read_file(image_path)
#     image=tf.image.decode_jpeg(image, channels=3)
#     return image

# image_path = "/home/fyp/Desktop/photos/2000706650.jpeg"
# image = load_image(image_path)

# detections = detector.detect_faces(image.numpy())

# print(detections)

# if detections:
#     x, y, width, height = detections[0]["box"]
#     face = image[y:y+height, x:x+width]
#     preprocessed_face = preprocess_image(face)

#     # Generate the face embedding
#     # embeddings = model.predict(preprocessed_face)
#     embedding = model.signatures["serving_default"](tf.constant(preprocessed_face))["embeddings"].numpy()

#     print(embedding)
# else:
#     print("No face detected")