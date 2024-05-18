import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image

pb_model_dir = "/home/fyp/Downloads/facenet_keras.h5"
h5_model = "./mymodel.h5"

# Loading the Tensorflow Saved Model (PB)
model = tf.keras.models.load_model(pb_model_dir)
print(model.summary())

# Saving the Model in H5 Format
tf.keras.models.save_model(model, h5_model)