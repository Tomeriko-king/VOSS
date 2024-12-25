import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email credentials
sender_email = "tomerklein9@gmail.com"
receiver_email = "tomerklein9@gmail.com"
password = "no"

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "try"

# Add the text content to the email
body = "Hello, this is the email text content!"
msg.attach(MIMEText(body, 'plain'))

# Path to the image file you want to attach
image_path = "captured_image.jpg"  # Specify the correct path

# Open the image file in binary mode and attach it to the email
with open(image_path, "rb") as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)  # Encode the image to base64
    part.add_header('Content-Disposition', f'attachment; filename={image_path.split("/")[-1]}')
    msg.attach(part)

# Set up the SMTP server and send the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Use your email provider's SMTP server
    server.starttls()  # Start TLS encryption
    server.login(sender_email, password)  # Log into your email account
    text = msg.as_string()  # Convert the email message to a string
    server.sendmail(sender_email, receiver_email, text)  # Send the email
    server.quit()  # Quit the server connection
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
