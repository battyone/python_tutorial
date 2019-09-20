
# %%
from collections import deque, defaultdict


def get_index(d, cv):
    i = d.index(cv)
    insert_at = i + 2

    if insert_at >= len(d):
        return insert_at - len(d)
    else:
        return insert_at


def print_dequeue(d, cv, p):
    s = ' '.join(str(x) for x in d)
    s = s.replace(f' {cv}', f' ({cv})')

    print(f'[{p}] ' + s)


def update_player(p, n):
    p += 1
    if p > n:
        p = 1

    return p

# %%


num_players = 9
player = 2

scores = defaultdict(int)

d = deque()
d.append(0)
d.append(1)

cv = 1

for v in range(2, 24):

    if v % 23 == 0:
        # do something special
        print('hello')

        scores[player] += v
        
        i = get_index(d, cv)
        to_be_removed = d[i]
        n = 'str'

    
    else:
        d.insert(get_index(d, cv), v)
        cv = v

    d.rotate(-d.index(0))

    print_dequeue(d, v, player)
    player = update_player(player, num_players)
