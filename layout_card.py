from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QSizePolicy

from card import Card


class CardLayout(QPushButton):
    def __init__(self, card):
        super().__init__()
        self.card = card


        self.setText(f"{self.card.rank}\n"
                     f"{self.card.symbol}\n"
                     f"{self.card.rank}")
        self.setStyleSheet(f"background-color:white; color: {self.card.color}; font-size: 14pt; font-weight: bold")
        self.setFixedSize(60, 100)
        self.setEnabled(False)
        self.setContentsMargins(0, 0, 0, 0)
