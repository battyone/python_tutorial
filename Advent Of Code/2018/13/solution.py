import operator

tracks = {}

car_actions = {
    '<': (-1, 0),  # move car over x - 1
    '>': (1, 0),  # move car over x + 1
    '^': (0, -1),
    'v': (0, 1)
}


with open('test.txt') as fp:
    for y, l in enumerate(fp):
        for x in range(0, len(l[:-1])):
            c = l[x]
            pos = (x, y)
            if c != ' ':
                tracks[pos] = c

x0 = min(p[0] for p in tracks)
x1 = max(p[0] for p in tracks)
y0 = min(p[1] for p in tracks)
y1 = max(p[1] for p in tracks)

turn_car = {
    ('>', '\\'): 'v',
    ('<', '\\'): '^',
    ('^', '\\'): '<',
    ('v', '\\'): '>',
    ('>', '/'): '^',
    ('<', '/'): 'v',
    ('^', '/'): '>',
    ('v', '/'): '<'
}


class Car:
    def __init__(self, pos, char):
        self.pos = pos
        self.char = char

    def __repr__(self):
        return f"'{self.char}' - {self.pos}"


cars = [Car(k, v) for k, v in tracks.items() if v in car_actions]


def print_track(t):
    for y in range(y0, y1 + 1):
        line = []
        for x in range(x0, x1 + 1):
            pos = (x, y)
            if pos in tracks:
                # any cars at this position?
                c = [c for c in cars if c.pos == pos]
                if len(c) > 0:
                    line.append(c[0].char)
                else:
                    line.append(tracks[pos])
            else:
                line.append(' ')
        print(''.join(line))
    print('')


print_track(0)

# time_steps = 3
# for t in range(1, time_steps):
#     print(t)

#     cars[t] = {}

#     # for all coords find car and advance by one step
#     for y in range(y0, y1 + 1):
#         for x in range(x0, x1 + 1):
#             pos = (x, y)
#             if pos in tracks:
#                 c = tracks[pos]

#                 if t == 2:
#                     pp = 9

#                 if c in cars[t-1] and cars[t-1][c] == pos:
#                     npos = tuple(map(operator.add, pos, car_actions[c]))
#                     npos_c = tracks[pos]

#                     if (c, npos_c) in turn_car:
#                         print('need to turn car')
#                         npos_c = c[(c, npos_c)]

#                     cars[t][npos_c] = npos
#     print(cars)
#     print_track(t)
