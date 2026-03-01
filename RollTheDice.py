import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap, QIcon
import random

class diceRoller(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.score_int = 0

    def initUI(self):
        self.setGeometry(230, 300, 1000, 800)
        layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        self.setWindowTitle("DiceRoller")
        self.setWindowIcon(QIcon("pfp.svg"))
        self.dice = QLabel(self)
        self.rolling_text = QLabel("Rolling...", self)
        self.score = QLabel("Score : 0", self)
        self.rolling_text.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("1.png")
        self.dice.setPixmap(pixmap)
        self.dice.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.dice)
        layout.addWidget(self.rolling_text)
        layout.addWidget(self.score)
        self.score.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)
        self.btn = QPushButton("Roll", self)
        self.btn2 = QPushButton("Reset Score", self)

        self.btn.setGeometry(500, 500, 100, 500)
        self.btn.setFixedSize(200, 80)
        self.btn2.setFixedSize(200, 80)
        layout2.addWidget(self.btn)
        layout2.addWidget(self.btn2)
        layout.addLayout(layout2)
        self.btn.clicked.connect(self.add)
        self.btn2.clicked.connect(self.reset_score)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.roll_the_dice)
        self.rolling_text.hide()
        self.setStyleSheet("background-color: grey;")
        self.btn.setStyleSheet("""
            QPushButton {
                background-color: blue;
                color: white;
                border-radius: 20px;
                border: 1px solid #2980b9;
                padding: 5px;
            }
            QPushButton:pressed {
                background-color: white;
            }
        """)
        self.btn2.setStyleSheet("""
                    QPushButton {
                        background-color: blue;
                        color: white;
                        border-radius: 20px;
                        border: 1px solid #2980b9;
                        padding: 5px;
                    }
                    QPushButton:pressed {
                        background-color: white;
                    }
                """)

    def add(self):
        self.rolling_text.show()
        self.timp_scurs = 0
        self.btn.setEnabled(False)
        self.timer.start(50)
    def reset_score(self):
        self.score_int = 0
        self.score.setText("Score : 0")
    def roll_the_dice(self):
        self.timp_scurs += 50
        x = random.randint(1,6)
        if x:
            image = f"{x}.png"
            pixmap = QPixmap(image)
            self.dice.setPixmap(pixmap)
        if self.timp_scurs >= 600:
            self.score_int += x
            self.score.setText(f"Score : {self.score_int}")
            self.rolling_text.hide()
            self.timer.stop()
            self.btn.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dice = diceRoller()
    dice.show()
    sys.exit(app.exec_())