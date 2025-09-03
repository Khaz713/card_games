from card import Card
import random


class Deck:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]
    VALUES_DEFAULT = {
        "Ace": 14,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "Jack": 11,
        "Queen": 12,
        "King": 13,
    }

    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self, values=VALUES_DEFAULT, reset=False):
        if reset:
            self.cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(Card(suit, rank, values[rank]))

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



