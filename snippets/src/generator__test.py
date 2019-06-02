# %%
import decimal
import operator
from decimal import Decimal
from fractions import Fraction
from collections import Counter
import reprlib
import re

# %%

s = 'ABC'
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break


# %%
RE_WORD = re.compile('\w+')

###################
# Take 1: A sequence of words


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, pos):
        return self.words[pos]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        return SentenceIterator(self.words)

###################
# Take 2: A classic Iterator


class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError
        raise StopIteration()

        self.index += 1
        return word

    def __iter__(self):
        return self

# %%
#######################
# Take 3: A Generator Function - much simpler
# ( no need for separate Iterator class)


class SentenceGenerator:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        for w in self.words:
            yield w
# %%
#######################
# Take 4: A Lazy Generator Function


class SentenceGeneratorLazy:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()

#######################
# Take 5: A  Generator Expression


class SentenceGeneratorExpression:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        # returns generator by using a generator expression
        # it's still lazy!!
        return (match.group() for match in RE_WORD.finditer(self.text))


# %%
s = Sentence('"The time has come," the walrus said,')
print([w for w in s])

sg = SentenceGenerator('"The time has come," the walrus said,')
print([w for w in sg])

sgl = SentenceGeneratorLazy('"The time has come," the walrus said,')
print([w for w in sgl])

se = SentenceGeneratorExpression('"The time has come," the walrus said,')
print([w for w in se])
# %%


def get_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')


# first way
a = [x*3 for x in get_AB()]
print(a)

print('first way finished')

# second way via generator expression
b = (x*3 for x in get_AB())
for i in b:
    print('-->', i)


# %%
class ArithmeticProgressions:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> Infinite series

    def __iter__(self):
        # make result he same type as begin + step and initialize with `begin`
        # e.g. result = int(self.begin)
        # this is useful when using Fraction or Decimal
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None

        index = 0
        while forever or result < self.end:
            yield result
            index += 1

            result = self.begin + self.step * index


ap = ArithmeticProgressions(0, 0.5, 3)
print(list(ap))

ap_frac = ArithmeticProgressions(0, Fraction(1, 3), 3)
print(list(ap_frac))

ctx = decimal.getcontext()
ctx.prec = 2
ap_dec = ArithmeticProgressions(0, Decimal(0.2), 3)
print(list(ap_dec))
# %%

# same as above


def arithmetic_progressions_gen(begin, step, end=None):
    # make result he same type as begin + step and initialize with `begin`
    # e.g. result = int(self.begin)
    # this is useful when using Fraction or Decimal
    result = type(begin + step)(begin)
    forever = end is None

    index = 0
    while forever or result < end:
        yield result
        index += 1

        result = begin + step * index


a = arithmetic_progressions_gen(0, 1, 3)
print(list(a))

b = arithmetic_progressions_gen(0, Fraction(1, 5), 3)
print(list(b))

ctx = decimal.getcontext()
ctx.prec = 2
c = arithmetic_progressions_gen(0, Decimal(0.69), 3)
print(list(c))

# %%
print(list(enumerate('albatroz', 1)))

print(list(map(operator.mul, range(11), range(11))))


# %%
# yield from
def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i


def chain_2(*iterables):
    for it in iterables:
        yield from it


s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t)))
print(list(chain_2(s, t)))

# %%
