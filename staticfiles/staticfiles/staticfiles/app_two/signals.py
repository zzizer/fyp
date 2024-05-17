from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import cv2
import face_recognition
from .models import Student

@receiver(post_save, sender=Student)
def generate_face_encoding(sender, instance, created, **kwargs):
    if created and instance.photo:  # Only generate face encoding if a new student is created with a photo
        image_path = instance.photo.path

        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(image, scaleFactor=1.3, minNeighbors=5)

        if len(faces) == 0:
            return

        # Extract the face region
        x, y, w, h = faces[0]
        face_region = image[y:y+h, x:x+w]

        # Convert the grayscale image to RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

        # Use face_recognition to generate face encoding
        encoding = face_recognition.face_encodings(rgb_image, [(y, x + w, y + h, x)])[0]

        # Store the encoding as bytes in the database
        instance.face_encoding = encoding.tobytes()
        instance.save()

# @receiver(post_delete, sender=Student)
# def remove_face_encoding(sender, instance, **kwargs):
#     if instance.face_encoding:
#         instance.face_encoding = None
#         instance.save()