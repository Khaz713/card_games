from PyQt6.QtWidgets import QPushButton

from card import Card


class CardLayout(QPushButton):
    def __init__(self, card):
        super().__init__()
        self.card = card


        self.setText(f"{self.card.rank}\n\n"
                     f"{self.card.symbol}\n\n"
                     f"{self.card.rank}")
        self.setStyleSheet(f"background-color:white; color: {self.card.color}; font-size: 12pt; font-weight: bold")
        self.setFixedSize(60, 100)
        self.setEnabled(False)