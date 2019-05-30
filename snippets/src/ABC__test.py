import abc
import random


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable."""

    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it

        This method should raise `LookupError` when the instance is empty.
        """

    def loaded(self):
        """Return `True` if there is at least 1 item, `False` otherwise"""
        return bool(self.inspect())

    def inspect(self):
        """Return a sorted Tuple with the items currently inside."""
        items = []
        while True:
            try:
                items.append(self.pick)
            except LookupError:
                break
        self.load(items)

        return Tuple(sorted(items))


class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty bingo cage')

    def __call__(self):
        self.pick()


class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            pos = random.randrange(len(self._balls))
        except IndexError:
            raise LookupError('pick from empty lottery blower')

        return self._balls.pop(pos)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))

# example of virtual subclassing
@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            pos = random.randrange(len(self))
            return self.pop(pos)
        else:
            raise LookupError('pop from empty Tombo List')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


def main(argv):
    print(issubclass(TomboList, Tombola))
    print(issubclass(TomboList, list))

    t = TomboList(range(100))
    print(isinstance(t, Tombola))


if __name__ == "__main__":
    import sys
    main(sys.argv)
