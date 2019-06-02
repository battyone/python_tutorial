
# %%
import itertools
import operator

gen = itertools.count(0, 99)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# %%
# take a generator and but stop at a given predicate
gen = itertools.takewhile(lambda n: n < 30, itertools.count(0, 5))
print(list(gen))

# %%
# second version
# has no yield but it returns a generator which makes this function a
# generator factory


def arithmetic_progressions_gen_fac(begin, step, end=None):
    # make result he same type as begin + step and initialize with `begin`
    # e.g. result = int(self.begin)
    # this is useful when using Fraction or Decimal
    first = type(begin + step)(begin)
    ap_gen = itertools.count(begin, step)

    if end is not None:
        ap_gen = itertools.takewhile(lambda x: x < end, ap_gen)

    return ap_gen


a = arithmetic_progressions_gen_fac(0, 1, 3)
print(list(a))

b = arithmetic_progressions_gen_fac(0, Fraction(1, 5), 3)
print(list(b))

ctx = decimal.getcontext()
ctx.prec = 2
c = arithmetic_progressions_gen_fac(0, Decimal(0.69), 3)
print(list(c))


# %%
i = itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1, 0, 1))
print(list(i))

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(list(itertools.accumulate(sample)))

print(list(itertools.accumulate(sample, min)))
print(list(itertools.accumulate(sample, max)))

print(list(itertools.accumulate(sample, operator.mul)))

print(list(itertools.chain('AA', 'BB', range(4))))

print(list(itertools.product('ABC', range(3))))

# %%
# all combinations of length 4
print(list(itertools.combinations('ABCDEF', 4)))

# all combinations with repetitions of length 2
print(list(itertools.combinations_with_replacement('ABCDEF', 2)))

# %%
print(list(itertools.combinations('ABC', 2)))
print()
print(list(itertools.permutations('ABC', 2)))


# %%
print(list(itertools.product('ABC', repeat=4)))


# %%

# groupby yields by (key, group_generator)

for c, g in itertools.groupby('LLLAAGGGGG'):
    print(c, len(list(g)))
# %%
animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin',
           'shark', 'lion']

animals.sort(key=len)

for length, animals in itertools.groupby(animals, len):
    print(length, list(animals))

# %%
