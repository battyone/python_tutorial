import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    # "2" is 0 and "A" is 12 -- position in FrenchDeck.ranks lists
    rank_value = FrenchDeck.ranks.index(card.rank)

    # return card's value based on suit_values dict
    return rank_value * len(suit_values) + suit_values[card.suit]


def run_test():

    a = Card("7", "diamonds")
    print(a)

    deck = FrenchDeck()
    print(len(deck))

    # __getitem__
    print(deck[4])
    print(deck[-1])  # last

    # choose random card
    print(choice(deck))

    # print all acces, by starting at 12 and skip 13 cards
    print(deck[12::13])

    # sort a deck
    for card in sorted(deck, key=spades_high):
        print(card, spades_high(card))

    print(type(FrenchDeck.ranks))


if __name__ == "__main__":
    run_test()
