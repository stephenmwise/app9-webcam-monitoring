import smtplib
from email.message import EmailMessage

PASSWORD = "Password123"
SENDER = test@gmail.com


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Alert: Motion Detected"
    email_message.set_content("A person has entered your room.")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)