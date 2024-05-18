import tensorflow as tf
import numpy as np
from mtcnn import MTCNN
import cv2 as cv

model = tf.saved_model.load("/home/fyp/Desktop/model")
# model = load_facenet_model(model_path)
print('model loaded')

# print(model.signatures.keys())

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

print(detections)

if detections:
    x, y, width, height = detections[0]["box"]
    face = image[y:y+height, x:x+width]
    preprocessed_face = preprocess_image(face)

    # Generate the face embedding
    # embeddings = model.predict(preprocessed_face)
    embedding = model.signatures["serving_default"](tf.constant(preprocessed_face))["embeddings"].numpy()

    print(embedding)
else:
    print("No face detected")