

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck():
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for v in range(1, 14):
                self.cards.append(Card(s, v))
    def show(self):
        for c in self.cards:
            c.show
            deck = Deck()
            deck.show()


class Player():
    def __init__(self) -> None:
        pass


# card = Card("Card", 6)
# card.show()

