# snap_send.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import sys, time, datetime, pathlib, sched
from smtplib import SMTP, SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import cv2

# SMTP server network address
# Start test SMTP server: python -m aiosmtpd -n
host = 'localhost'
port = 8025

# Send an email with an attached image
def send_image(to_email, from_email, subject, message, image_file):
    email = MIMEMultipart()                     # Create message object
    email['From']    = from_email               # Sender
    email['To']      = to_email                 # Receiver
    email['Subject'] = subject                  # Subject

    # Add plain text part to message
    part = MIMEText(message, "plain")           # Build text part
    email.attach(part)                          # Attach message
    
    # Attach the image file to email using the MIMEImage class
    with open(image_file, "rb") as file:        # Open image file to read binary
        name  = pathlib.Path(image_file).name   # Get base file name
        data  = file.read();                    # Read image data
        image = MIMEImage(data, name)           # Create a container object
        image.add_header('Content-Disposition', f'attachment; filename= {name}')
        email.attach(image)                     # Attach image

    with SMTP(host=host, port=port) as smtp:    # Send MIME message
        smtp.ehlo()
        smtp.send_message(email)

# Snap a picture and save to a dated file
def snap():
    filename = None
    result, image = cam.read()                  # Read the camera
    if result:                                  # If successful
        now = datetime.datetime.now()           # Create file name
        filename = now.strftime('%Y%m%d%H%M%S.png')
        cv2.imwrite(filename, image)            # Save the image
        print(f'Wrote {filename}')
    return filename

# Snap image and send file
def snap_send():
    filename = snap()
    if filename:
        to_email    = 'thomas@yourdomain.com'
        from_email  = 'alexander@mydomain.com'
        subject     = filename
        send_image(to_email, from_email, subject, '', filename)

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)                   # Open default video stream
    if not cam.isOpened():
        print("Camera not open")
        sys.exit(1)
    
    # Start scheduler with timestamp as time function
    queue = sched.scheduler(time.time, time.sleep)
    
    # Schedule a snap every hour for the next 24 hours
    now = datetime.datetime.now()               
    for hour in range(24):
        abstime = now.timestamp() + hour*60*60
        queue.enterabs(abstime, 1, snap_send)
    
    # Run until no more events schedule
    queue.run()
    