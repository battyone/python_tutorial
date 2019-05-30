# %%
from random import choices, shuffle

# %%
# choose 10 values from a range with equal probability
a = choices(range(0, 10), k=10)
print(a)

shuffle(a)
print(a)


# %%
l = list(range(10))
for _ in range(10):
    shuffle(l)
    print(l)


# %%
