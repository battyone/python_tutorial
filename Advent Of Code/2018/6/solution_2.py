# %%
import re
from collections import defaultdict, Counter
from operator import itemgetter

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


# %%
input = read_input('input.txt')

min_x = min([i[0] for i in input])
max_x = max([i[0] for i in input])
min_y = min([i[1] for i in input])
max_y = max([i[1] for i in input])

max_dist = 10000

grid = defaultdict(int)

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        key = (x, y)
        total_dist = 0

        for coord in input:
            total_dist += Manhattan_Distance(coord, (x, y))

        if total_dist < max_dist:
            grid[key] = total_dist


# print(*grid.items(), sep='\n')

solution = len(grid)
print('solution: ', solution)
