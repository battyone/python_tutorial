
# %%
from datetime import *
from collections import namedtuple
from parse import parse
import re

Format = '%Y-%m-%d %H:%M'
Line_Pattern = '[{}] {}'

Nigthshift = namedtuple('Nigthshift', 'Date ID Asleep')


def Create_Nightshift(a):
    dt = (a[-1][0].month, a[-1][0].day)
    ID = re.search(r'\#(\d+)', a[0][1]).group(1)

    sleep = []

    if len(a) > 1:
        i = 1
        while i < len(a):
            asleep = a[i][0].minute
            wakeup = a[i+1][0].minute
            i += 2

            sleep.extend(range(asleep, wakeup))

    return Nigthshift(dt, ID, sleep)


# %%
# 1. Read input
input = []
with open('4/test.txt') as fp:
    for _, line in enumerate(fp):
        s, r = parse(Line_Pattern, line)
        dt = datetime.strptime(s, Format)
        input.append((dt, r))

# 2. Create an Excel like sheet where each row is one day with Guard ID
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

