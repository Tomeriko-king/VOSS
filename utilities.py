import mediapipe as mp
import cv2
from google.protobuf.json_format import MessageToDict


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
                        return False

                    if password == secret:
                        print("youre in")
                        return True

            else:
                check = True
