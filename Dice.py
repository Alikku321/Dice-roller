import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class DiceRoller(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Rolling The Dices Game")
        self.setGeometry(300, 300, 550, 350)
        self.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel()
        self.label.setFont(QFont("times", 250))
        self.label.setStyleSheet("color: yellow;")
        layout.addWidget(self.label)

        button = QPushButton("Roll!")
        button.clicked.connect(self.rollDices)
        button.setStyleSheet("background-color: aqua;")
        layout.addWidget(button)

        self.show()

    def rollDices(self):
        dice_dots = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        self.label.setText(f'{random.choice(dice_dots)}{random.choice(dice_dots)}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DiceRoller()
    sys.exit(app.exec())