from asyncio import sleep

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QMessageBox

from layout_card import CardLayout
from deck import Deck

VALUES_BLAKJACK = {
        "A": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
    }

cards = Deck(VALUES_BLAKJACK)
cards.shuffle()

hand_player = []
hand_dealer = []

win = 0

lose = 0



class Blackjack(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        back = QHBoxLayout()
        left = QVBoxLayout()
        right = QVBoxLayout()
        layout = QVBoxLayout()
        back.addLayout(left)
        back.addLayout(layout)
        back.addLayout(right)

        self.win_lose = QLabel(f"Win: {win}\nLose: {lose}")
        self.win_lose.setStyleSheet("background-color:black; color: white; font-size: 12pt; font-weight: bold")
        self.win_lose.setFixedSize(150, 50)
        left.addWidget(self.win_lose)
        left.setAlignment(self.win_lose, Qt.AlignmentFlag.AlignBottom)

        test2 = QLabel("Test2")
        test2.setStyleSheet("background-color:black; color: black; font-size: 12pt; font-weight: bold")
        test2.setFixedSize(150, 50)
        right.addWidget(test2)
        right.setAlignment(test2, Qt.AlignmentFlag.AlignBottom)




        label = QLabel("BLACKJACK")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setStyleSheet('color: white')
        layout.addWidget(label)

        self.dealer_points = QLabel("Dealer Points: 0")
        font = self.dealer_points.font()
        font.setPointSize(20)
        self.dealer_points.setFont(font)
        self.dealer_points.setStyleSheet('color: white')
        layout.addWidget(self.dealer_points)

        self.dealer_hand = QHBoxLayout()
        self.dealer_hand.setSpacing(5)
        layout.addLayout(self.dealer_hand)


        self.button_deal = QPushButton("Deal")
        self.button_deal.setStyleSheet("background-color:white; color: black; font-size: 12pt; font-weight: bold")
        self.button_deal.setFixedSize(150, 50)
        self.button_deal.clicked.connect(self.deal_cards)
        layout.addWidget(self.button_deal)

        self.player_points = QLabel("Points: 0")
        font = self.player_points.font()
        font.setPointSize(20)
        self.player_points.setFont(font)
        self.player_points.setStyleSheet('color: white')
        layout.addWidget(self.player_points)

        self.player_hand = QHBoxLayout()
        self.player_hand.setSpacing(5)
        layout.addLayout(self.player_hand)

        player_buttons = QHBoxLayout()
        player_buttons.addStretch()

        self.button_hit = QPushButton("Hit")
        self.button_hit.setStyleSheet("background-color:white; color: black; font-size: 12pt; font-weight: bold")
        self.button_hit.setFixedSize(150, 50)
        self.button_hit.clicked.connect(self.player_hit)
        self.button_hit.hide()
        player_buttons.addWidget(self.button_hit)

        self.button_stand = QPushButton("Stand")
        self.button_stand.setStyleSheet("background-color:white; color: black; font-size: 12pt; font-weight: bold")
        self.button_stand.setFixedSize(150, 50)
        self.button_stand.clicked.connect(self.dealer_turn)
        self.button_stand.hide()
        player_buttons.addWidget(self.button_stand)
        player_buttons.addStretch()

        layout.addLayout(player_buttons)



        button_back = QPushButton("Back")
        button_back.setStyleSheet("background-color:red; color: black; font-size: 12pt; font-weight: bold")
        button_back.setFixedSize(150, 50)
        button_back.clicked.connect(self.button_back)
        layout.addWidget(button_back)


        layout.setAlignment(label, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        layout.setAlignment(self.dealer_points, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        layout.setAlignment(self.dealer_hand, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        layout.setAlignment(self.button_deal, Qt.AlignmentFlag.AlignCenter)

        layout.setAlignment(self.player_points, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        layout.setAlignment(self.player_hand, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        layout.setAlignment(player_buttons, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        layout.setAlignment(button_back, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        layout.setSpacing(5)
        self.setLayout(back)


    def deal_cards(self):
        hand_player.append(cards.deal_card())
        hand_player.append(cards.deal_card())
        hand_dealer.append(cards.deal_card())

        self.update_player_hand()
        self.update_dealer_hand()

        self.button_deal.hide()
        self.button_hit.show()
        self.button_stand.show()



    def update_player_hand(self):
        self.clear_layout(self.player_hand)
        for card in hand_player:
            temp_card = CardLayout(card)
            self.player_hand.addWidget(temp_card)
            self.player_hand.setAlignment(temp_card, Qt.AlignmentFlag.AlignHCenter)

        self.player_points.setText(f"Points: {self.count_points(hand_player)}")

    def update_dealer_hand(self):
        self.clear_layout(self.dealer_hand)
        for card in hand_dealer:
            temp_card = CardLayout(card)
            self.dealer_hand.addWidget(temp_card)
            self.dealer_hand.setAlignment(temp_card, Qt.AlignmentFlag.AlignHCenter)

        self.dealer_points.setText(f"Dealer Points: {self.count_points(hand_dealer)}")


    def player_hit(self):
        hand_player.append(cards.deal_card())
        self.update_player_hand()
        if self.count_points(hand_player) > 21:
            message = QMessageBox.critical(self, "Bust", "You lose!")
            global lose
            lose += 1
            self.reset_game()





    def dealer_turn(self):
        hand_dealer.append(cards.deal_card())
        global win
        global lose
        while self.count_points(hand_dealer) < 17:
            hand_dealer.append(cards.deal_card())
        self.update_dealer_hand()
        if self.count_points(hand_dealer) > 21:
            message = QMessageBox.information(self, "Win", "You win!")
            win += 1
        else:
            if self.count_points(hand_dealer) > self.count_points(hand_player):
                message = QMessageBox.critical(self, "Lose", "You lose!")
                lose += 1
            elif self.count_points(hand_dealer) == self.count_points(hand_player):
                message = QMessageBox.information(self, "Tie", "You tie!")
            else:
                message = QMessageBox.information(self, "Win", "You win!")
                win += 1

        self.reset_game()


    def button_back(self):
        self.parent().main_menu()

    def count_points(self, hand):
        points = 0
        for card in hand:
            if card.rank == "A":
                if points + 11 > 21:
                    points += 1
                else:
                    points += 11
            else:
                points += card.value
        return points

    def reset_game(self):
        cards = Deck(VALUES_BLAKJACK)
        cards.shuffle()
        hand_player.clear()
        hand_dealer.clear()
        self.win_lose.setText(f"Win: {win}\nLose: {lose}")
        self.button_deal.show()
        self.button_hit.hide()
        self.button_stand.hide()

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
