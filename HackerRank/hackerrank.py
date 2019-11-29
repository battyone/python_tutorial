# %%
from itertools import groupby
from collections import Counter
from itertools import combinations_with_replacement
x, y, z = 1, 1, 3
print(x, y, z)
print(x is y)
print(id(x), id(y))

x = 6
print(x, y, z)
print(x is y)
print(id(x), id(y))


# %%
# unpack a list
*a, b = [100, 200, 400]
print(a, b)

# %%
x, y, z = 2, 2, 2
n = 2

a = [[i, j, k]
     for i in range(x + 1)
     for j in range(y + 1)
     for k in range(z + 1)
     if i + j + k != n]

print(a)

# %%

line = '1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78'
a = set(map(int, line.split()))
b = set(map(int, '1 2 3 4 5'.split()))
c = set(map(int, '100 11 12'.split()))

print(a, c)
if (a >= c) == False:
    print(False)
else:
    print(True)


# %%

line = 'HACK 2'
s = list(line.split()[0])
n = int(line.split()[1])

a = combinations_with_replacement(s, n)
b = [''.join(sorted(i)) for i in a]
print('\n'.join(sorted(b)))


# %%

line = '1222311'
a = list(map(int, line))
b = [str((len(list(g)), k)) for k, g in groupby(a)]

print(' '.join(b))

# %%

X = 10
shoe_sizes = list(map(int, '2 3 4 5 6 8 7 6 5 18'.split(' ')))
N = 6

shoe_avail = Counter(shoe_sizes)
print(shoe_avail)

a = ['6 55', '6 45', '6 55', '4 40', '18 60', '10 50']

amount = 0
for p in a:
    size, price = tuple(map(int, p.split(' ')))

    if size in shoe_avail:
        if shoe_avail[size] > 0:
            amount += price
            shoe_avail[size] -= 1

print(amount)

# %%
# Not Y in this challenge
vowels = 'AEIOU
s = 'BANANA'

for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)

#%%
s = 'Hello'
d = ''.join(c.upper() if c.islower() else c.lower() for c in s)
d


#%%
s = 'this is a string'
'-'.join(s.split(' '))

#%%
s = 'AABCAAADA'
k = 3
p = len(s) // k
for p in range(0,len(s),k):
    print(s[p:p+k])
    print(''.join(set(s[p:p+k])))

