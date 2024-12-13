import mediapipe as mp
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PIL import ImageGrab
from PIL import Image
from datetime import datetime
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




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.success_login = False
        self.utils = Utilities()
        self.setStyleSheet("background-color: darkGray;")
        self.button2 = QPushButton("PASSWORD", self)

        #Create a button
        self.button = QPushButton("TAKE  A  SCREENSHOT!", self)
        self.image_label = QLabel(self)

        # Resize the button (optional)
        self.button.resize(200, 50)
        self.image_label.resize(800, 600)

        self.button2.setStyleSheet("background-color: cyan")
        self.button.setStyleSheet("background-color: cyan")

        # Connect the button's clicked signal to a method (command)
        self.button2.clicked.connect(self.on_button_click_password)
        self.button.clicked.connect(self.on_button_click)

        # Create a layout
        layout = QVBoxLayout()

        # Add the button and label to the layout
        layout.addWidget(self.button2)
        layout.addWidget(self.button)
        layout.addWidget(self.image_label)

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        central_widget.setLayout(layout)

        # Set the central widget
        self.setCentralWidget(central_widget)

        # Set the window title and size
        self.setWindowTitle("Button Command Example")

    def on_button_click_password(self):
        self.success_login = self.utils.passi()

    # Method that will be called when the button is clicked
    def on_button_click(self):
        if self.success_login == True:
            # Change the label text when the button is clicked
            screenshot = ImageGrab.grab()
            screenshot.save("screenshot.png")
            screenshot.close()

            image = Image.open('screenshot.png')
            new_image = image.resize((1420, 880))
            new_image.save('screenshot_small.png')

            now = datetime.now()
            self.setWindowTitle(now.strftime("%d/%m/%Y %H:%M:%S"))
            tmp_image = QPixmap('screenshot_small.png')
            self.image_label.setPixmap(tmp_image)
            self.image_label.resize(800, 600)
        else:
            print("failed to log in")



if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
