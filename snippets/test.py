# hackerrang

# %%
from itertools import product
import itertools
from itertools import groupby
lines = ['insert 0 1', 'insert 1 10', 'insert 0 6', 'remove 6', 'print']
a = []

for line in lines:
    t = line.split()
    instructions = list(map(int, [t[i] for i in range(1, len(t))]))

    if line.startswith('insert'):
        i = instructions[0]
        e = instructions[1]
        a.insert(i, e)
    elif line.startswith('remove'):
        e = instructions[0]
        a.remove(e)
    elif line.startswith('append'):
        e = instructions[0]
        a.append(e)
    elif line.startswith('sort'):
        a = sorted(a)
    elif line.startswith('pop'):
        a.pop()
    elif line.startswith('reverse'):
        a = reversed(a)
    elif line.startswith('print'):
        print(a)

    print(a)


# %%

for c, g in groupby('LLLAAGGGGG'):
    print(c, len(list(g)))

# %%
animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin',
           'shark', 'lion']

animals.sort(key=len)

for length, animals in groupby(animals, len):
    print(length, list(animals))

# %%
line = list(map(int, '1222311'))

a = []
for c, g in groupby(line):
    a.append(str((len(list(g)), c)))

print(' '.join(a))

# %%

N = 4
line = 'a a c d'
K = 2

bla = list(line.split(' '))
a = [i+1 for i, c in enumerate(bla) if c == 'a']

comb = list(itertools.combinations(range(1, N+1), K))
b = {c for c in comb for i in a if i in c}
print(f'{(len(b) / len(comb)):.4}')


# %%

K, M = map(int, '3 1000'.split(' '))
Input = ['2 5 4', '3 7 8 9', '5 5 7 8 9 10']

# ignore the first value!!!
a = [list(set(map(int, i.split(' ')[1:]))) for i in Input]
print(max(map(lambda x: sum(i**2 for i in x) % M, product(*a))))


# %%

# read first line from stdin and split into K,M
K, M = map(int, input().split(' '))

# for K rows from stdin split the numbers into a list, ignoring first number
a = [list(set(map(int, input().split(' ')[1:]))) for i in range(K)]

# 1. create a bunch of lists
print(max(map(lambda x: sum(i**2 for i in x) % M, product(*a))))


# %%

# All substrings from a string
vowels = ['a', 'e', 'i', 'o', 'u']

Stuart = 0
Kevin = 0
s = 'BANANA'
substrings = {s[i:j] for i in range(len(s)) for j in range(i+1, len(s) + 1)}

for ss in substrings:
    if ss[0] in vowels:
        Kevin += sum(1 for i in range(len(s)) if s.startswith(ss, i))
    else:
        Stuart += sum(1 for i in range(len(s)) if s.startswith(ss, i))

if Stuart > Kevin:
    print('Stuart ', Stuart)
else:
    print('Kevin ', Kevin)

# %%
s = 'BANANA'
vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    print(len(s)-i)
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)

if kevsc > stusc:
    print('Kevin', kevsc)
elif kevsc < stusc:
    print('Stuart', stusc)
else:
    print('Draw')
