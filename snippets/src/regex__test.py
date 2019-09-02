
# %%
import re
import reprlib

from collections import Counter

# %%

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
m = re.search(r'\#(\d+)', 'Guard #10 begins shift')
m.group(1)

# %%
# copy all matches to list
s1 = '[1518-11-01 00:00] Guard #10 begins shift'
s2 = '[1518-11-01 00:05] falls asleep'
# Pattern = r'(\[(.*)\].*?\#(\d+))|(\[(.*)\])'
Pattern = r'\[(.*)\].*?\#(\d+)'
print(re.findall(Pattern, s1))
print(re.findall(Pattern, s2))

# %%
s1 = '[1518-11-01 00:00] Guard #10 begins shift'
s2 = '[1518-11-01 00:05] falls asleep'

dt = re.findall(r'\[(.*)\]', s1)
ID = re.findall(r'\#(\d+)', s2)

print(dt, ID)

# %%
# replace
d = 'dabAcCaCBAcCcaDA'
print(re.sub('cC', '', d))
