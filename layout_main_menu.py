from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel

class MainMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("CARD GAMES")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setStyleSheet('color: white')
        layout.addWidget(label)

        button1 = QPushButton("Blackjack")
        button1.setStyleSheet("background-color:white")
        button1.setFixedSize(150, 50)
        button1.clicked.connect(self.button_blackjack)
        layout.addWidget(button1)

        button2 = QPushButton("Scoundrel")
        button2.setStyleSheet("background-color:white")
        button2.setFixedSize(150, 50)
        button2.setEnabled(False)
        layout.addWidget(button2)

        button3 = QPushButton("Exit")
        button3.setStyleSheet("background-color:red")
        button3.setFixedSize(150, 50)
        button3.clicked.connect(self.button_exit)
        layout.addWidget(button3)

        layout.setAlignment(label, Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(button1, Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(button2, Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(button3, Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def button_exit(self):
        QApplication.quit()

    def button_blackjack(self, widget):
        self.parent().blackjack()
