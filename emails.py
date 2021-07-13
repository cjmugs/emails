# This module is the server
import smtplib
# This module import the email
from email.message import EmailMessage
# This module creates a template
from string import Template
# This module allows file path use
from pathlib import Path

# Path to html inside of folder
html = Template(Path('C:/Gits/emails/index.html').read_text())

# Basic email layout
msg = EmailMessage()
msg['From'] = 'Tom Foolery'
msg['To'] = 'smokeym624@gmail.com'
msg['Subject'] = ('TEST EMAIL SERVER') 

# This is the body of the email

# use this way if setup in the same folder
#msg.set_content(html.substitute({'name': 'Tintin'}), 'html')
msg.set_content('WTF')

# Create a client side server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('smokeym624@gmail.com', 'force$420')
    smtp.send_message(msg)
    # Optional info
    print('Email has been sent')
