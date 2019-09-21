
# %%
from collections import deque, defaultdict
from operator import itemgetter


def update_player(p, n):
    p += 1
    if p > n:
        p = 1

    return p

# %%


d = deque()
d.append(0)
d.append(2)
d.append(1)

num_players = 447
last_marble = 71510
current_player = 3
scores = defaultdict(int)

current_value = 2


for value in range(3, last_marble + 1):

    if value % 23 == 0:

        to_be_removed_index = d.index(current_value) - 7
        d.rotate(-to_be_removed_index)

        scores[current_player] += value + d[0]
        del d[0]
        current_value = d[0]

    else:
        d.rotate(-d.index(current_value))
        d.insert(2, value)
        current_value = value

    current_player = update_player(current_player, num_players)


# not really necessary
# d.rotate(-d.index(0))
# s = ' '.join(str(x) for x in d)
# print(s)
print(max(scores.items(), key=itemgetter(1)))
