# %%
from datetime import *
from parse import parse

Format = '%Y-%m-%d %H:%M'
Line_Pattern = '[{}] {}'

# 1. Read input
input = []
with open('4/input.txt') as fp:
    for _, line in enumerate(fp):
        s, r = parse(Line_Pattern, line)
        dt = datetime.strptime(s, Format)
        input.append((dt, r))

print(*(sorted(input))[:10], sep='\n')

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
