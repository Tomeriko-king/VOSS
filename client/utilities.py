import mediapipe as mp
import cv2
from email_sender import EmailSender
from security_picture import security_picture
from datetime import datetime
from google.protobuf.json_format import MessageToDict
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_the_email():
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    formatted_time = current_datetime.strftime("%H:%M:%S")

#    security_picture()
    image_path = 'security_image.jpg'

    # Your email credentials
    sender_email = 'tomerklein9@gmail.com'
    sender_password = ''  # TODO

    # Receiver's email address
    receiver_email = 'tomerklein9@gmail.com'
    king = EmailSender(sender_email, sender_password)

    # Create the email content
    subject = 'Hacking attempt alert'
    body = f'Someone tried to hack in the app and failed to log in after 3 attempts. \n Date: {formatted_date} \n Time: {formatted_time}'
    king.send_email(subject, body, image_path, [receiver_email])


class Utilities:
    def passi(self):
        # Initializing the Model
        mpHands = mp.solutions.hands
        hands = mpHands.Hands(
            static_image_mode=False,
            model_complexity=1,
            min_detection_confidence=0.75,
            min_tracking_confidence=0.75,
            max_num_hands=2)

        # Start capturing video from webcam
        cap = cv2.VideoCapture(0)

        password = []
        secret = ['Right', 'Right', 'Left']
        c = 0
        test = 0

        check = True

        while True:
            # Read video frame by frame
            success, img = cap.read()

            # Flip the image(frame)
            img = cv2.flip(img, 1)

            # Convert BGR image to RGB image
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Process the RGB image
            results = hands.process(imgRGB)

            # If hands are present in image(frame)
            if results.multi_hand_landmarks:
                if check:
                    check = False
                    for i in results.multi_handedness:
                        # Return whether it is Right or Left Hand
                        label = MessageToDict(i)['classification'][0]['label']

                    password.insert(c, label)
                    c = c + 1
                    print(password)
                    print(password[0:c] != secret[0:c])

                    if password[0:c] != secret[0:c]:
                        print(test)

                        test = test + 1
                        c = 0
                        password = []

                    if test == 3:
                        send_the_email()
                        return False

                    if password == secret:
                        print("youre in")
                        return True

            else:
                check = True
