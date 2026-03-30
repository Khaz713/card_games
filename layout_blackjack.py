from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel

from layout_card import CardLayout
from deck import Deck

deck = Deck()
deck.shuffle()

class Blackjack(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        layout = QVBoxLayout()

        label = QLabel("BLACKJACK")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setStyleSheet('color: white')
        layout.addWidget(label)

        self.hand = QHBoxLayout()
        layout.addLayout(self.hand)


        button_deal = QPushButton("Deal")
        button_deal.setStyleSheet("background-color:white")
        button_deal.setFixedSize(150, 50)
        button_deal.clicked.connect(self.deal_cards)
        layout.addWidget(button_deal)

        button1 = QPushButton("BACK")
        button1.setStyleSheet("background-color:white")
        button1.setFixedSize(150, 50)
        button1.clicked.connect(self.button_back)
        layout.addWidget(button1)

        layout.setAlignment(label, Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(button1, Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)


    def deal_cards(self):
        for i in range(5):
            self.hand.addWidget(CardLayout(deck.deal_card()))

    def button_back(self):
        self.parent().main_menu()