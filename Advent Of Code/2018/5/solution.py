
# %%
from collections import defaultdict
from operator import itemgetter

# %%

# Always remove trailing newline!!
input = []
with open('5/input.txt') as fp:
    for _, line in enumerate(fp):
        input.append(line.rstrip('\n'))

# original = 'dabAcCaCBAcCcaDA'
original = input[0]
data = original

offset = ord('A') - ord('a')

#%%

def reduce(polymer):
    Reaction = True
    loop = 0
    while Reaction:
        loop = loop + 1

        Reaction = False
        for i in range(ord('a'), ord('z') + 1):
            a = polymer.replace(chr(i)+chr(i+offset), '')
            a = a.replace(chr(i+offset)+chr(i), '')

            if a != polymer:
                Reaction = True

            polymer = a

    # print(f'Loops: {loop}')
    return polymer


# %%
print(len(original))
print(len(reduce(data)))

##################
# Part 2
##################

# %%
input = []
with open('5/input.txt') as fp:
    for _, line in enumerate(fp):
        input.append(line.rstrip('\n'))

# original = 'dabAcCaCBAcCcaDA'
original = input[0]
d = defaultdict(int)

for i in range(ord('a'), ord('z') + 1):
    a = original.replace(chr(i), '')
    a = a.replace(chr(i+offset), '')
    a = reduce(a)
    
    d[chr(i)] = len(a)

print(min(d.items(), key=itemgetter(1)))
