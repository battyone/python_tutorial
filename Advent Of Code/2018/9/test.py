# %%
from collections import deque, defaultdict

d = deque()
d.append(0)
d.append(2)
d.append(1)

for nv in range(3, 23):
    cv = nv - 1

    d.rotate(-d.index(cv))
    d.insert(2, nv)
    d.rotate(-d.index(0))

    s = ' '.join(str(x) for x in d)
    print(s)
