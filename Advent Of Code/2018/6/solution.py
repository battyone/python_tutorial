
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

# key: All Grid Coordinates; value: Min Distance
grid = defaultdict(list)

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        key = (x, y)
        l = grid[key]

        for coord in input:
            dist = Manhattan_Distance(coord, (x, y))
            t = (coord, dist)

            if dist == 0:
                # this is a point given by the input
                l.clear()
                l.append(t)
                break
            elif not l:
                l.append(t)
            else:
                current_min_dist = l[0][1]
                if dist < current_min_dist:
                    l.clear()
                    l.append(t)
                elif dist == current_min_dist:
                    l.append(t)


# print(min_x, min_y, max_x, max_y)
print(*grid.items(), sep='\n')
