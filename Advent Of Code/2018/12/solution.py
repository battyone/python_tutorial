
from collections import Counter

# see https://en.wikipedia.org/wiki/Elementary_cellular_automaton

initial = set()
rules = {}

with open('input.txt') as fp:
    first = fp.readline()[:-1].replace('initial state: ', '')
    initial = set(i for i, x in enumerate(first) if x == '#')

    fp.readline()

    for n in fp.readlines():
        a, b = n[:-1].split(' => ')
        rules[a] = b

# indices of a pots with a plant


def step(state):
    result = set()
    # check all indexes in "view" of any active cells
    for i in range(min(state) - 2, max(state) + 3):

        # construct a window string like '#.##.'
        w = ''.join('#' if j in state else '.' for j in range(i - 2, i + 3))

        # check the rule for this window
        if rules[w] == '#':
            result.add(i)

    return result


# part 1
s = initial

# run 20 iterations
for i in range(20):
    s = step(s)

# simply sum the active indexes
print(sum(s))


print('part 2')
s = initial

p = n = 0
# run enough iterations, tracking current and previous sums
for i in range(1000):
    p = n
    s = step(s)
    n = sum(s)
# extrapolate to 50 billion
print(n, p, i)
print(p + (n - p) * (50000000000 - i))

4300000000349
