# %%

from collections import Counter, defaultdict

# %%
c = Counter('AABBDD')
c['a'] += 14
c

# %%
# defaultdict for 1-to-many relationships, aka dict with lists as values

d = defaultdict(list)
d['spam'].append(42)
d['spam'].append(88)
d['bla'].append('Hello')
d['bla'].append('World')
d


# %%
