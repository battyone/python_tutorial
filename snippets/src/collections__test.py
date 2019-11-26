# %%

from collections import Counter, defaultdict

# %%
c = Counter('AABBDD')
print(c.most_common(1))

c['a'] += 14



# %%
# defaultdict for 1-to-many relationships, aka dict with lists as values

d = defaultdict(list)
d['spam'].append(42)
d['spam'].append(88)
d['bla'].append('Hello')
d['bla'].append('World')
d


# %%
