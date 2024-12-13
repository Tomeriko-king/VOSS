from utilities import Utilities

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PIL import ImageGrab
from PIL import Image
from datetime import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.success_login = False
        self.utils = Utilities()
        self.setStyleSheet("background-color: darkGray;")
        self.button2 = QPushButton("PASSWORD", self)

        # Create a button
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


def start_gui():
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
