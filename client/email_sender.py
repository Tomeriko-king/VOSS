import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage


class EmailSender:
    def __init__(self, sender: str, password: str):
        self.sender = sender
        self.password = password

    def send_email(self, subject: str, body: str, image_path: str, recipients: list[str]) -> None:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(self.sender, self.password)
            # msg.attach(MIMEText(body, 'plain'))
            # with open(image_path, 'rb') as img_file:
            #     img = MIMEImage(img_file.read())
            #     img.add_header('Content-ID', '<image1>')  # Optional: Use this if you want to display inline
            #     msg.attach(img)
            smtp_server.sendmail(self.sender, recipients, msg.as_string())



