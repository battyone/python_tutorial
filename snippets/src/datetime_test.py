#%%
from datetime import date

d = date(2012, 2, 1)
print(d.isoformat())

print(format(d, '%A, %B %d, %Y'))

print(f'The end is {d:%d %b %Y}. Goodbye!')