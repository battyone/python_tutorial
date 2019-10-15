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

# do we need the car symbol? Maybe just position is enough?

cars = {}
cars[0] = {tracks[t]: t for t in tracks if tracks[t] in car_actions}


def print_track(t):
    for y in range(y0, y1 + 1):
        l = []
        for x in range(x0, x1 + 1):
            pos = (x, y)
            if pos in tracks:
                if pos in cars[t].values():
                    bb = [k for k, v in cars[t].items() if v == pos]
                    l.append(bb[0])
                else:
                    l.append(tracks[pos])
            else:
                l.append(' ')
        print(''.join(l))
    print('')


print_track(0)

time_steps = 3
for t in range(1, time_steps):
    print(t)

    cars[t] = {}

    # for all coords find car and advance by one step
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            pos = (x, y)
            if pos in tracks:
                c = tracks[pos]

                if t == 2:
                    pp = 9

                if c in cars[t-1] and cars[t-1][c] == pos:
                    npos = tuple(map(operator.add, pos, car_actions[c]))
                    npos_c = tracks[pos]

                    if (c, npos_c) in turn_car:
                        print('need to turn car')
                        npos_c = c[(c, npos_c)]

                    cars[t][npos_c] = npos
    print(cars)
    print_track(t)
