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
