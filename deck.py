from card import Card
import random


class Deck:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "A",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
    ]
    VALUES_DEFAULT = {
        "A": 14,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
    }

    def __init__(self, values=None):
        self.cards = []
        self.create_deck(values)

    def create_deck(self, values=VALUES_DEFAULT, reset=False):
        if reset:
            self.cards = []
        for suit in self.SUITS:
            if suit == "Hearts" or suit[0] == "Diamonds":
                color = "red"
            else:
                color = "black"

            if suit == "Clubs":
                symbol = "♣"
            elif suit == "Spades":
                symbol = "♠"
            elif suit == "Hearts":
                symbol = "♥"
            else:
                symbol = "♦"

            for rank in self.RANKS:
                self.cards.append(Card(suit, symbol, rank, values[rank], color))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)

    def __len__(self):
        return len(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def peak_card(self):
        return self.cards[0]

    def remove_cards(self, suits=None, ranks=None):
        if suits is not None and ranks is None:
            ranks = self.RANKS
        if ranks is not None and suits is None:
            suits = self.SUITS
        cards_to_remove = []
        for i in range(self.__len__()):
            if self.cards[i].suit in suits and self.cards[i].rank in ranks:
                cards_to_remove.append(i)
        cards_to_remove = reversed(cards_to_remove)
        for index in cards_to_remove:
            self.cards.pop(index)



