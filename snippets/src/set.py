#%%
l = ['spam', 'spam', 'eggs', 'spam']
print(set(l))

#empty is set() NOT {}. Which is empty dict

#%%
from unicodedata import name

a = {chr(i) for i in range(32,256) if 'SIGN' in name(chr(i), '')}
print(a)

#%%
from random import choices

print(choices(range(0,1000), k=10))
haystack = set(range(0,1000))
needles = set(range(20,30))
print(needles & haystack)