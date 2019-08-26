
# %%
from collections import Counter

doubles = 0
triples = 0

with open('2/input.txt') as fp:
    for _, line in enumerate(fp):
        c = Counter(line)
        d = [k for k, v in c.items() if v == 2]
        t = [k for k, v in c.items() if v == 3]

        if len(d) > 0:
            doubles += 1

        if len(t) > 0:
            triples += 1

print(doubles)
print(triples)
print(doubles * triples)

# Part 2
# Find the two lines which only differ by one character.
# There is only one instance which is the solution.

# %%


def similar(a, b):
    num_diff = 0

    for i in range(0, len(a)):
        if a[i] != b[i]:
            num_diff += 1

        if num_diff > 1:
            return False

    return True


a = []
with open('2/input.txt') as fp:
    for _, line in enumerate(fp):
        a.append(line)

s1 = ''
s2 = ''
for s in a:
    for t in a:
        if s is not t:
            if similar(s, t):
                s1 = s
                s2 = t
                break

solution = ''
for i in range(0, len(s) - 1):
    if s1[i] == s2[i]:
        solution += s1[i]

print(s1)
print(s2)
print(solution)
