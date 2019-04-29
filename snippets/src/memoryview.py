
# %%
from array import array
from time import perf_counter as pc

t0 = pc()
# create an array of 16bit signed integers
numbers = array('h', [-2, -1, 0, 1, 2])
mem = memoryview(numbers)
print(len(mem))
print(mem[0])

# cast the array into 8bit unsigned integers (byte)
mem_oct = mem.cast('B')
print(len(mem_oct))
print(mem_oct.tolist())

# change a value
mem_oct[5] = 4

# it reflects in the original array
print(numbers)
print(pc() - t0)
