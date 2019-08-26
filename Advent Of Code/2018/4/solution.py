# %%
from datetime import *
from collections import namedtuple
from parse import parse

Format = '%Y-%m-%d %H:%M'
Line_Pattern = '[{}] {}'

# 1. Read input
input = []
with open('4/test.txt') as fp:
    for _, line in enumerate(fp):
        s, r = parse(Line_Pattern, line)
        dt = datetime.strptime(s, Format)
        input.append((dt, r))

Nigthshift = namedtuple('Nigthshift', 'Date ID Asleep')


def Create_Nightshift(a):
    dt = (a[-1][0].month, a[-1][0].day)
    ID = parse('#{:d}', a[0][1])

    return Nigthshift(dt, ID, [])


Nigthshift_Array = []
Sheet = []
for line in sorted(input):
    if 'Guard' in line[1]:
        if(len(Nigthshift_Array) > 0):
            Sheet.append(Create_Nightshift(Nigthshift_Array))

        Nigthshift_Array.clear()
        Nigthshift_Array.append(line)
    else:
        Nigthshift_Array.append(line)

print(*Sheet, sep='\n')

# print(*(sorted(input))[:100], sep='\n')

# 2. Sort input


# s = '[1518-09-19 00:42] wakes up'
# d1 = '1518-09-19 00:42'
# d2 = '1518-08-03 00:57'


# a = []

# a.append(datetime.strptime(d1, Format))
# a.append(datetime.strptime(d2, Format))

# d = sorted(a)
# c = sorted(a, reverse=True)

# print(c)
# print(d)
