
# %%

import collections
from random import shuffle


Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]




# %%
# this will fail, see below
deck = FrenchDeck()
shuffle(deck)


# %%
# Monkey Patching FrenchDeck to allow for shuffling (pg, 325)
def set_card(deck, position, card):
    deck._cards[position] = card

FrenchDeck.__setitem__ = set_card

new_deck = FrenchDeck()
shuffle(new_deck)
print(new_deck[:5])

#%%
