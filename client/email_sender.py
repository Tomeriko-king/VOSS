import smtplib
from datetime import datetime
from email.mime.text import MIMEText


class EmailSender:
    def __init__(self, sender: str, password: str):
        self.sender = sender
        self.password = password

    def send_email(self, subject: str, body: str, recipients: list[str]) -> None:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(self.sender, self.password)
            smtp_server.sendmail(self.sender, recipients, msg.as_string())


current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%Y-%m-%d")
formatted_time = current_datetime.strftime("%H:%M:%S")

# Your email credentials
sender_email = 'tomerklein9@gmail.com'
sender_password = ''  # TODO

# Receiver's email address
receiver_email = 'alonmergi2020@gmail.com'

king = EmailSender(sender_email, sender_password)

# Create the email content
subject = 'Hacking attempt alert'
body = f'Someone tried to hack in the app and failed to log in after 5 attempts. \n Date: {formatted_date} \n Time: {formatted_time} '

king.send_email(subject, body, [receiver_email])
