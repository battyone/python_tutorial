
# %%
import re
from collections import defaultdict, Counter
# %%


def read_input(FileName):
    result = []

    with open('6/' + FileName) as fp:
        for _, line in enumerate(fp):
            t = re.findall(r'(\d+), (\d+)', line)[0]
            result.append((int(t[0]), int(t[1])))

    return result


def Manhattan_Distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


input = read_input('test.txt')

min_x = min([i[0] for i in input])
max_x = max([i[0] for i in input])
min_y = min([i[1] for i in input])
max_y = max([i[1] for i in input])

# %%

grid = defaultdict(list)

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        for coord in input:
            grid[(x, y)].append(Manhattan_Distance(coord, (x, y)))

# clear all list which have two equal distances
for k, v in grid.items():
    c = Counter(v)

    if c.most_common(1)[0][1] > 1:
        grid[k].clear()

# print(min_x, min_y, max_x, max_y)
print(*grid.items(), sep='\n')
