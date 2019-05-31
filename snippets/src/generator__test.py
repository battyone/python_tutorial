# %%
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
