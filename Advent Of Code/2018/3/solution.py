# %%
from collections import namedtuple, defaultdict

# https://pypi.org/project/parse/
from parse import parse

Claim = namedtuple('Claim', 'id x_off y_off width height')

Pattern = '#{:d} @ {:d},{:d}: {:d}x{:d}'

claims = []
with open('3/input.txt') as fp:
    for _, line in enumerate(fp):
        claims.append(Claim(*parse(Pattern, line)))

# print(claims)

# count all coordinates in a dict
d = defaultdict(int)

for c in claims:
    for x in range(c.x_off, c.x_off + c.width):
        for y in range(c.y_off, c.y_off + c.height):
            d[(x,y)] += 1

Overlaps = [k for k,v in d.items() if v > 1]
print(len(Overlaps))

#%%
# Part 2
for c in claims:
    has_overlap = False
    for x in range(c.x_off, c.x_off + c.width):
        if has_overlap == False:
            for y in range(c.y_off, c.y_off + c.height):
                if d[(x,y)] > 1:
                    has_overlap = True
                    break

    if has_overlap == False:
        print(c)
        break




