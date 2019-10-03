from collections import defaultdict
from itertools import count


state = '...#..#.#..##......###...###...........'
rules = defaultdict(str)

rules['...##'] = '#'
rules['..#..'] = '#'
rules['.#...'] = '#'
rules['.#.#.'] = '#'
rules['.#.##'] = '#'
rules['.##..'] = '#'
rules['.####'] = '#'
rules['#.#.#'] = '#'
rules['#.###'] = '#'
rules['##.#.'] = '#'
rules['##.##'] = '#'
rules['###..'] = '#'
rules['###.#'] = '#'
rules['####.'] = '#'

for i in range(2, len(state)-2):
    print(state[i-2:i+2])
