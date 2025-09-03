from deck import Deck

def main():
    deck = Deck()
    deck.shuffle()
    print(len(deck))
    deck.remove_cards(["Hearts", "Diamonds"], ["Ace", "King", "Queen", "Jack"])
    print(len(deck))
    while len(deck) != 0:
        print(deck.deal_card())




if __name__ == "__main__":
    main()
