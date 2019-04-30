# %%
import random

# choose 10 values from a range with equal probability
a = random.choices(range(0, 1000), k=10)
print(a)
