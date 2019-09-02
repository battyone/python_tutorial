
# %%
from datetime import *
from operator import *
from collections import namedtuple, Counter
import re

Format = '%Y-%m-%d %H:%M'

Nigthshift = namedtuple('Nigthshift', 'Date ID Asleep')

# %%
###############
# 1. Read input
input = []
with open('4/input.txt') as fp:
    for _, line in enumerate(fp):
        # Extract datetime
        dt = datetime.strptime(re.findall(r'^\[(.*)\]', line)[0], Format)

        # Extract Guard ID if available
        ID = -1
        m = re.search(r'\#(\d+)', line)
        if m:
            ID = int(m.groups(1)[0])

        # Create object to keep all the information plus asleep or not
        input.append(Nigthshift(dt, ID, 'asleep' in line))


# print(*sorted(input)[:10], sep='\n')

# %%

########
# 2.Sort and create a time table
TimeTable = {}

Current_ID = -1
for i in sorted(input, key=lambda i: i.Date):
    if i.ID >= 0:
        Current_ID = i.ID
    else:
        key = (i.Date.month, i.Date.day, Current_ID)
        TimeTable.setdefault(key, [])
        TimeTable[key].append(i.Date.minute)

# %%
##################
# 3. Do some stats
Most_Asleep = {}
Minute_Asleep = {}

for k, v in TimeTable.items():

    # the key is (month, day, ID)
    ID = k[2]

    Most_Asleep.setdefault(ID, int())
    Minute_Asleep.setdefault(ID, Counter())
    d = Minute_Asleep[ID]

    for p in zip(v[::2], v[1::2]):
        Most_Asleep[ID] = Most_Asleep[ID] + (p[1] - p[0])
        d.update(range(p[0], p[1]))


# print(Most_Asleep)
# print(Minute_Asleep)
# %%
most_asleep_guard = max(Most_Asleep.items(), key=itemgetter(1))
most_asleep_guard_id = most_asleep_guard[0]
minute_asleep = Minute_Asleep[most_asleep_guard_id].most_common(1)[0]

print(f'Guard {most_asleep_guard_id} slept {most_asleep_guard[1]} minutes.')
print(f'He slept minute {minute_asleep[0]} {minute_asleep[1]} times.')

print(f'Possible solution: {most_asleep_guard_id * minute_asleep[0]}')

###########################
# Part 2
###########################
#%%
aa = [ (k, v.most_common(1)[0][0], v.most_common(1)[0][1]) for k,v in Minute_Asleep.items()]
bb = sorted(aa, key=itemgetter(2), reverse=True)[0]

print(f'Possible solution: {bb[0] * bb[1]}')



