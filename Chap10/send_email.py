# send_email.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

from smtplib import SMTP
from email.message import EmailMessage

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Install and start local server
# python -m pip install aiosmtpd
# python -m aiosmtpd -n   # Default port 8025

# SMTP server network address
host = 'localhost'
port = 8025

def send_simple_email(to_email, from_email, subject, message):
    with SMTP(host=host, port=port) as smtp:
        # smtp.sendmail(from_email, to_email, message)      # Sending simple email message
        
        # Format email message manually with headers. 
        # Header name and value are added to same line separated with a ':'
        # A blank line is required between headers and message body
        email = f'To: {to_email}\nFrom: {from_email}\nSubject: {subject}\n\n{message}'
        smtp.sendmail(from_email, to_email, email)      # Sending simple email message

def send_email(to_email, from_email, subject, message):
    email = EmailMessage()                              # Creating a object for EmailMessage
    email['From']    = from_email                       # Sender
    email['To']      = to_email                         # Receiver
    email['Subject'] = subject                          # Subject
    email.set_content(message)                          # Message
    # password = input("Enter password: ")
    # with SMTP(host='smtp.gmail.com', port=587) as smtp:
    with SMTP(host=host, port=port) as smtp:
        # smtp.starttls()                                 # Elevate connection to use TLS
        # smtp.login(from_email,password)                 # Authenticate
        smtp.send_message(email)                        # Send Message object
        print("email sent to", to_email)

def send_multipart(to_email, from_email, subject, message, fname):
    email = MIMEMultipart()                             # Creating a object for EmailMessage
    email['From']    = from_email                       # Sender
    email['To']      = to_email                         # Receiver
    email['Subject'] = subject                          # Subject

    # Add plain text part to message
    part = MIMEText(message, "plain")                   # Build text part
    email.attach(part)                                  # Attach
    
    # Attach the file as binary using the MIMEBase class
    part = MIMEBase("application", "octet-stream")      # 
    with open(fname, "rb") as file:
        part.set_payload( file.read() )                 # Read and add file content bytes
        encoders.encode_base64(part)                    # Encode as ASCII text
    part.add_header( "Content-Disposition", f"attachment; filename={fname}" )
    email.attach(part)
    
    # MIMEImage
    # MIMEMessage
    # MIMEAudio
    # MIMEApplication
    
    with SMTP(host=host, port=port) as smtp:
        smtp.send_message(email)

if __name__ == '__main__':
    # send_simple_email('thomas@yourdomain.com', 'alexander@mydomain.com', 'First Message', 
    #                   'Mr. Watson, come here; I want you.')
    # send_email('you@yourdomain.com', 'me@mydomain.com', 'Data Delivery', 'Find data attached')
    send_multipart('you@yourdomain.com', 'me@mydomain.com', 'Data Delivery', 'Find data attached', 'report.pdf')
