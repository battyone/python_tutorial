# %%
from random import choices, shuffle, randint

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
def dice():
    return randint(1, 6)


for i in range(10):
    print(f' {i} '.center(10, '*'))

    # stop when 6 is rolled
    roller = iter(dice, 6)
    print([r for r in roller])


# %%
