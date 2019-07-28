# %%
from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([10, 20, 30])
print(dq)
# first insert 10 on the left, then 20 on left, etc
dq.extendleft([10, 20, 30, 40])
print(dq)


# %%
# keep a window of the last 5 values and sum them

data = range(0, 10)
last_n = deque(maxlen=5)

for d in data:
    last_n.append(d)
    if len(last_n) == 5:
        print(last_n, sum(last_n))
