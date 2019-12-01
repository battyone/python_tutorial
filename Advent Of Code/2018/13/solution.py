#%%
from operator import add
from collections import defaultdict, Counter
import os.path
from itertools import count

def read_input():
    tracks = {}

    with open('input.txt') as fp:
        for y, l in enumerate(fp):
            for x in range(0, len(l[:-1])):
                c = l[x]
                pos = (x, y)
                if c != ' ':
                    tracks[pos] = c

    return tracks


def print_track(step, t):
    x0 = min(p[0] for p in t)
    x1 = max(p[0] for p in t)
    y0 = min(p[1] for p in t)
    y1 = max(p[1] for p in t)

    with open('out.txt', 'a') as fp:
        # fp.write(f'step {i}:\n')
        
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
            fp.write(''.join(line) + '\n')
        fp.write('\n')

def delete_output():
    if os.path.isfile('out.txt'):
        os.unlink('out.txt')



tracks = read_input()
delete_output()

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
    (1, '^') : '^',
    (1, 'v') : 'v',
    (1, '>') : '>',
    (1, '<') : '<',
    (2, '^') : '>',
    (2, 'v') : '<',
    (2, '>') : 'v',
    (2, '<') : '^'
}


class Car:
    def __init__(self, ID, pos, char, intersections):
        self.ID = ID
        self.pos = pos
        self.char = char
        self.intersections = intersections
        self.intersection_counter = 0

    def __repr__(self):
        first = f"'{self.ID}: {self.char}' - {self.pos}"
        second = str(self.intersections)
        return first # + '---' + second

    def turn_at_intersection(self, next_pos):
        # depending on the modulo decide to go left, straight, or right
        a = self.intersection_counter % 3
        self.char = intersection_turn[(a, self.char)]

        # change the decision for the next intersection
        self.intersection_counter += 1

    def move(self, step, tracks):

        # if step == 7 and self.pos == (104, 61):
        #     print('something bad is going to happen')
        #     print(self)

        ca = car_actions[self.char]
        next_pos = tuple(map(add, self.pos, ca))

        if next_pos in self.intersections:
            self.turn_at_intersection(next_pos)
        elif (self.char, tracks[next_pos]) in turn_car:
            self.char = turn_car[(self.char, tracks[next_pos])]
        
        self.pos = next_pos

# Create cars
intersections = [k for k, v in tracks.items() if v == '+']
counter = count()
cars = [Car(next(counter), k, v, intersections) for k, v in tracks.items() if v in car_actions]

step = 0
try:
    while True:

        cars = sorted(cars, key=lambda x: (x.pos[1], x.pos[0]))

        with open('out.txt', 'a') as fp:
            fp.write(str(step) + ':\n')
            [fp.write(str(c.pos) + '\n') for c in cars]

        step += 1

        # Move each car one step and check for collision
        for car in cars:
            car.move(step, tracks)

            # check for crash
            c = Counter([c.pos for c in cars])
            for k, v in c.items():
                if v > 1:
                    print('crash at', k)
                    raise StopIteration
except StopIteration:
    pass
    

    # print(*cars, sep='\n')
    # print_track(i, tracks)
