# %%
import re
import reprlib

from collections import Counter

RE_WORD = re.compile('\w+')


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


s = Sentence('"The time has come," the walrus said,')
print([w for w in s])

c = Counter(s)
print(c)


# %%
