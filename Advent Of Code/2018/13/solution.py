#%%
from operator import add
from collections import defaultdict

def print_track(t):
    x0 = min(p[0] for p in t)
    x1 = max(p[0] for p in t)
    y0 = min(p[1] for p in t)
    y1 = max(p[1] for p in t)

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

def read_input():
    tracks = {}

    with open('test.txt') as fp:
        for y, l in enumerate(fp):
            for x in range(0, len(l[:-1])):
                c = l[x]
                pos = (x, y)
                if c != ' ':
                    tracks[pos] = c

    return tracks

tracks = read_input()

car_actions = {
    '<': (-1, 0),  # move car over x - 1
    '>': (1, 0),  # move car over x + 1
    '^': (0, -1),
    'v': (0, 1)
}

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


# key is modulo with 3
intersection_turn = {
    (0, '^') : '<',
    (0, 'v') : '>',
    (0, '>') : '^',
    (0, '<') : 'v',
    (1, '^') : '>',
    (1, 'v') : 'v',
    (1, '>') : '>',
    (1, '<') : '<',
    (2, '^') : '^',
    (2, 'v') : '<',
    (2, '>') : 'v',
    (2, '<') : '^'
}


class Car:
    def __init__(self, pos, char):
        self.pos = pos
        self.char = char

    def __repr__(self):
        first = f"'{self.char}' - {self.pos}"
        second = str(self.intersections)
        return first + '---' + second

    def add_intersections(self, intersections):
        self.intersections = {i: 0 for i in intersections}

    def turn_at_intersection(self, next_pos):
        a = self.intersections[next_pos] % 3
        self.char = intersection_turn[(a, self.char)]


    def move(self, step, tracks):
        print(step, ':')
        
        ca = car_actions[self.char]
        next_pos = tuple(map(add, self.pos, ca))

        if next_pos in self.intersections:
            self.turn_at_intersection(next_pos)
        elif (self.char, tracks[next_pos]) in turn_car:
            print(' ' * 4, 'turning car')
            self.char = turn_car[(self.char, tracks[next_pos])]
        
        self.pos = next_pos


# find the cars on the tracks
cars = [Car(k, v) for k, v in tracks.items() if v in car_actions]

intersections = [k for k, v in tracks.items() if v == '+']

for c in cars:
    c.add_intersections(intersections)

# print(cars[0])

for i in range(6):
    for car in cars:
        car.move(i, tracks)
        print_track(tracks)



