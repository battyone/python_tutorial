

# %%
import re
import sys
import collections
import builtins

# %%

# dict
a = {}

tt = (1, 2, (30, 40))
print(tt)
print(hash(tt))

# All Python's immutable built-in objects are hashable. List is mutable
tt = (1, 2, frozenset([30, 40]))
print(tt)
print(hash(tt))

# %%
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = {'two': 2, 'one': 1, 'three': 3}
print(a == b == c == d)


# %%

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

print(type(DIAL_CODES))
print(type(DIAL_CODES[0]))

# make a dict via a dict comprehension
country_codes = {country: code for code, country in DIAL_CODES}
print(type(country_codes))

print({code: country.upper() for country, code in country_codes.items()})

# %%

WORD_RE = re.compile(r'\w+')

index = {}

with open('zen.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            col_no = match.start() + 1
            loc = (line_no, col_no)

            # This is ugly
            # occurences = index.get(word, [])
            # occurences.append(loc)
            # index[word] = occurences

            # Better to use setdefault
            index.setdefault(word, []).append(loc)

for word in sorted(index, key=str.upper):
    print(word, index[word])

# %%

WORD_RE = re.compile(r'\w+')

# if a key is available call list() and add key with empty list
index = collections.defaultdict(list)

with open('zen.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            col_no = match.start() + 1
            loc = (line_no, col_no)

            # Better to use setdefault
            index[word].append(loc)

for word in sorted(index, key=str.upper):
    print(word, index[word])

# %%

# combine a few dictionaries into one
pylookup = collections.ChainMap(locals(), globals(), vars(builtins))
print(pylookup)

# %%

a = collections.Counter('abeabdsoandsdsasdsadsads')
print(a)
a.update('aaaaaaccccxzzz')
print(a)
print(a.most_common(2))

# %%

a = Tra


class StrKeyDict(collections.UserDict):

    # called by __getitem__ whenever a key is not found, instead of raising KeyError
    def __missing__(self, key):
        if(isinstance(key, str)):
            # this happens when key is not in the dict and key is a string
            raise KeyError(key)

        # create a str from key and call __getitem__ again which then
        # will call __missing__ again if key is available. But this time there will be
        # a KeyError
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


a = StrKeyDict()
a['hello'] = 9
print(a)
a[3] = 99
print(a)

# %%
# create a dict
charles = {'name': 'Charles L. Dodgson', 'born': 1832}

lewis = charles
print(lewis is charles)

print(id(lewis), id(charles))

lewis['balance'] = 950

# still true and charles now also has a 'balance'
print(lewis is charles)

print(charles)


alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}

print(charles == alex)  # the same content (comparing the values)
print(charles is alex)  # not the same object (comparing ids)


# %%
# check for a key
charles = {'name': 'Charles L. Dodgson', 'born': 1832}
if 'name' in charles:
    print('charles has a name')
