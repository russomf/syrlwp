# snap.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Snap a picture and save to a file with dated file name
import datetime, sys
import cv2

# Snap a picture and save to a file
def snap():
    filename = None
    result, image = cam.read()                  # Read the camera
    if result:                                  # If successful
        now = datetime.datetime.now()           # Create file name
        filename = now.strftime('%Y%m%d%H%M%S.png')
        cv2.imwrite(filename, image)            # Save the image
        print(f'Wrote {filename}')
    return filename

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)                   # Open default video stream
    if not cam.isOpened():
        print("Camera not open")
        sys.exit(1)
    
    filename = snap()                           # Snap picture
    print(f'Created {filename}')
