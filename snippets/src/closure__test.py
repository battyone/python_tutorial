# A closure is with an extended scope that encompasses
# nonglobal variables referenced in the body of a the
# function but not defined there.
#

# A closure remembers the values from its enclosing lexical scope even when the program flow is no longer in that scope.

# %%

# a class to calculate


class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))

# %%

# a higher order function to calc the average


def make_averager():

    # closure - start

    # a free variable - it's not bound in the local scope
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    # closure - end

    return averager


avg = make_averager()
print(avg(12))
print(avg(13))
print(avg(14))


# %%

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)

print(avg.__closure__)

# print the current values in 'series'
print(avg.__closure__[0].cell_contents)

# %%
# A more efficient averager


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        # assigning to non local variables is not supported
        nonlocal count, total  # flag both variables as free variables
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager()
print(avg(99))
