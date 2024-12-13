from sender import EmailSender
from datetime import datetime

current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%Y-%m-%d")
formatted_time = current_datetime.strftime("%H:%M:%S")

# Your email credentials
sender_email = 'tomerklein9@gmail.com'
sender_password = '' # TODO

# Receiver's email address
receiver_email = 'alonmergi2020@gmail.com'

king = EmailSender(sender_email, sender_password)

# Create the email content
subject = 'Hacking attempt alert'
body = f'Someone tried to hack in the app and failed to log in after 5 attempts. \n Date: {formatted_date} \n Time: {formatted_time} '

king.send_email(subject, body, [receiver_email])
