class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit  # string
        self.rank = rank  # string
        self.value = value  # int, different games different scoring system

    def __str__(self):
        return f"{self.rank} of {self.suit}: {self.value}"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value
