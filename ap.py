from email.message import EmailMessage
from emsend2 import password
import ssl
import smtplib

email_sender = 'oredare313@gmail.com'
email_Password = password
email_receiver = 'sajoga8391@utwoko.com'
subject = 'Making an email sending app'
body = '''Currently making an email asending app'''

em = EmailMessage()
em['from'] = email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content = body

context = ssl.create_default_context

with smtplib.SMTP_SSL('smtp.gmail.com',465,context = context) as smtp:
    smtp.login(email_sender,email_Password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

