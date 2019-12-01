# %%
import numpy as np
import timeit
# numpy is fast
my_arr = np.arange(1_000_000)

timeit.timeit('a = my_arr * 2', globals=globals())
