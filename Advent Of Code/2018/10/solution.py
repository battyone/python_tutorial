import re
from operator import attrgetter

# things I could have done better:
# 1. the movement of points can be calculated with time step, x = p.x + p.vx * t.
#    tuples are just fine, for instance from Michael Fogleman:
# def state(points, t):
#     return [(x + vx * t, y + vy * t) for x, y, vx, vy in points]


class Point:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.vx}, {self.vy})'


def write_to_file(time, min_x, max_x, min_y, max_y, Points):
    with open('output.txt', 'a') as txt_file:
        txt_file.write(str(time) + '\n')
        txt_file.write('---------------------\n')

        for y in range(min_y, max_y + 1):
            line = ''
            for x in range(min_x, max_x + 1):
                all_points = [p for p in Points if p.y == y and p.x == x]
                if all_points:
                    line += '#'
                else:
                    line += '.'

            txt_file.write(line+'\n')
        txt_file.write('---------------------\n')
        txt_file.write('---------------------\n')


Points = []
with open('input.txt') as fp:
    Points = [Point(*map(int, re.findall('\-?\d+', l)))
              for _, l in enumerate(fp)]

for time in range(0, 11000):

    if time % 1000 == 0:
        print(time)

    min_x, max_x, min_y, max_y = (
        min(Points, key=attrgetter('x')).x,
        max(Points, key=attrgetter('x')).x,
        min(Points, key=attrgetter('y')).y,
        max(Points, key=attrgetter('y')).y)

    num_rows = max_y - min_y

    # we only care if the points are assembled within 100 lines or less
    if num_rows < 100:

        points_per_row = [0 for i in range(min_y, max_y + 1)]

        for p in Points:
            points_per_row[p.y - min_y] += 1

        # only if there are no empty lines write out points
        if points_per_row.count(0) == 0:
            write_to_file(time, min_x, max_x, min_y, max_y, Points)

    # move points
    for p in Points:
        p.x += p.vx
        p.y += p.vy
