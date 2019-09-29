# %%
import re
from operator import attrgetter,  itemgetter
from collections import namedtuple
from copy import copy, deepcopy


class Point:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.vx}, {self.vy})'

# %%


Points = []
Stats = []
with open('10/test.txt') as fp:
    Points = [Point(*map(int, re.findall('\-?\d+', l)))
              for _, l in enumerate(fp)]


for time in range(0, 5):

    min_x, max_x, min_y, max_y = (
        min(Points, key=attrgetter('x')).x,
        max(Points, key=attrgetter('x')).x,
        min(Points, key=attrgetter('y')).y,
        max(Points, key=attrgetter('y')).y)

    points_per_row = [0 for i in range(min_y, max_y + 1)]
    for p in Points:
        points_per_row[p.y - min_y] += 1

    Stats.append((time, len(points_per_row),
                  points_per_row.count(0), deepcopy(Points)))

    # move points
    for p in Points:
        p.x += p.vx
        p.y += p.vy


Best_Guess = min([s for s in Stats if s[2] == 0], key=itemgetter(1))

# print(*Stats, sep='\n')
#%%
print(Best_Guess)

Points = Best_Guess[3]

# print message
min_x, max_x, min_y, max_y = (
    min(Points, key=attrgetter('x')).x,
    max(Points, key=attrgetter('x')).x,
    min(Points, key=attrgetter('y')).y,
    max(Points, key=attrgetter('y')).y)

with open('10\output.txt', 'w') as txt_file:
    for y in range(min_y, max_y + 1):
        line = ''
        for x in range(min_x, max_x + 1):
            all_points = [p for p in Points if p.y == y and p.x == x]
            if all_points:
                line += '#'
            else:
                line += '.'
        
        txt_file.write(line+'\n')













