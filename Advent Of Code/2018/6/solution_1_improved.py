
# %%
import re
from collections import defaultdict

# %%

# Return a list of tuples


def read_input(FileName):
    with open('6/' + FileName) as fp:
        return [tuple(map(int, re.findall(r'\d+', x))) for _, x in enumerate(fp)]


points = read_input('input.txt')
# print(*points, sep=' ')

# find the min / max bounds of all points
x0, x1 = min(x for x, y in points), max(x for x, y in points)
y0, y1 = min(y for x, y in points), max(y for x, y in points)

# manhattan distance function


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# %%
counts = defaultdict(int)
infinite = set()
for x in range(x0, x1 + 1):
    for y in range(y0, y1 + 1):
        # sorted dist for each point
        ds = sorted((dist(x, y, px, py), i)
                    for i, (px, py) in enumerate(points))

        # if two points both have shortest dist then don't count the current coord
        if ds[0][0] != ds[1][0]:
            counts[ds[0][1]] += 1

        if x == x0 or y == y0 or x == x1 or y == y1:
            infinite.add(ds[0][1])


# discard all infinite regions
for k in infinite:
    counts.pop(k)
# print the maximal area
print(max(counts.values()))
