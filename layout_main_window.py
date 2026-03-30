
from PyQt6.QtWidgets import  QMainWindow

from layout_main_menu import MainMenu
from layout_blackjack import Blackjack



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Card Games")
        self.setFixedSize(1200, 600)
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color:black")
        self.widget = MainMenu(self)


        self.setCentralWidget(self.widget)

    def main_menu(self):
        self.widget = MainMenu(self)
        self.setCentralWidget(self.widget)

    def blackjack(self):
        self.widget = Blackjack(self)
        self.setCentralWidget(self.widget)