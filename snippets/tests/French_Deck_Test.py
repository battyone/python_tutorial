import collections
from random import choice

import unittest

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


class FrenchDeck_Tests(unittest.TestCase):
    def create_deck(self):
        return FrenchDeck()

    def test_deck_len(self):
        deck = FrenchDeck()
        self.assertEqual(len(deck), 52)

    def test_index(self):
        deck = FrenchDeck()

        self.assertEqual(deck[0], Card("2", "spades"))
        self.assertEqual(deck[-1], Card("A", "hearts"))

    def test_pick_random(self):
        deck = self.create_deck()

        a = choice(deck)
        b = choice(deck)

    def test_slice(self):
        deck = self.create_deck()

        a = deck[:3]
        self.assertEqual(len(a), 3)

        # start on card 12 and skipping 13
        b = deck[12::13]

        # make sure all cards are aces
        c = [r.rank for r in b]
        self.assertEqual(c, ["A", "A", "A", "A"])
        return


if __name__ == '__main__':
    unittest.main()
