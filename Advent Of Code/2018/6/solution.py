
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


input = read_input('input.txt')

min_x = min([i[0] for i in input])
max_x = max([i[0] for i in input])
min_y = min([i[1] for i in input])
max_y = max([i[1] for i in input])

print(min_x, min_y, max_x, max_y)


# %%

# key: All Grid Coordinates; value: (Input, Min Distance)
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
                # no distance is added yet
                l.append(t)
            else:
                current_min_dist = l[0][1]
                if dist < current_min_dist:
                    l.clear()
                    l.append(t)
                elif dist == current_min_dist:
                    l.append(t)

# print(*grid.items(), sep='\n')

# %%
# ignore the points where two or more inputs have the same min dist
updated_grid = defaultdict(tuple)
for k, v in grid.items():
    if len(v) == 1:
        updated_grid[k] = v[0]

# print(*updated_grid.items(), sep='\n')
# %%

infinite = set()
for k, v in updated_grid.items():
    x = k[0]
    y = k[1]
    if x == min_x or x == max_x or y == min_y or y == max_y:
        infinite.add(v[0])

area = defaultdict(int)
for k, v in updated_grid.items():
    key = v[0]
    if key not in infinite:
        area[key] = area[key] + 1


# print(*area.items(), sep='\n')
# print(*sorted(infinite), sep='\n')

solution = max(area.items(), key=itemgetter(1))
print('solution: ', solution[1])
