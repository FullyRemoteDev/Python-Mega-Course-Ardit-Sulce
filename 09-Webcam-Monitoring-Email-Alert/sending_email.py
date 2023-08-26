import smtplib
import os
import imghdr
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

sender_email = os.getenv('APP9_USER_EMAIL')
password = os.getenv('APP9_USER_PASSWORD')

receiver_email = os.getenv('APP9_RECEIVER')


def send_email(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = "Intrusion Detected!"
    email_message.set_content("A new intrusion detected!")

    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content,
                                 maintype='image',
                                 subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender_email, password)
    gmail.sendmail(sender_email, receiver_email, email_message.as_string())
    gmail.quit()

if __name__ == '__main__':
    send_email(image_path='images/test_img.png')
