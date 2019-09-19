# %%
from collections import deque


def add(d, v):
    i = d.index(v - 1)
    insert_at = i + 2

    if insert_at >= len(d):
        d.insert(insert_at - len(d), v)
    else:
        d.insert(insert_at, v)

    d.rotate(-d.index(0))

#%%

d = deque()
d.append(0)
d.append(1)

num_players = 9
player = 2

for v in range(2, 20):

    add(d, v)
    s = ' '.join(str(x) for x in d )
    s = s.replace(f' {v}', f' ({v})')
    
    print(f'[{player}] ' + s)

    player += 1
    if player > num_players:
        player = 1



