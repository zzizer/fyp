import cv2 as cv
from picamera2 import PiCamera2
# from picamera2 import PiCamera2 

# Create a PiCamera2 object
picam2 = PiCamera2()

# Configure preview settings
picam2.preview_configuration.main.size = (800, 800)  # Corrected attribute name
picam2.preview_configuration.main.format = "RGB"  # Changed format to "RGB" (no need for 888)
picam2.preview_configuration.align = (0, 0)  # Corrected attribute name

# Start the preview
picam2.configure("preview")  # Changed method call to correct syntax
picam2.start()

while True:
    # Capture image as an array
    im = picam2.capture_array()  # Corrected method call
    
    # Display the image
    cv.imshow("Camera", im)
    
    # Wait for 'q' key to exit
    if cv.waitKey(1) == ord('q'):
        break

# Clean up
cv.destroyAllWindows()  # Corrected method call
