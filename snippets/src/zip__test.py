# %%
from itertools import zip_longest

# %%
list(zip(range(3), 'ABC'))

# %%
# 88 will be ignored
list(zip(range(3), 'ABC', [3, 6, 9, 88]))

# %%
# use a fill value in case some values are missing
list(zip_longest(range(3), 'ABC', [3, 6, 9, 88], fillvalue=-1))
