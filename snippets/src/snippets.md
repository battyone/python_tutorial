```
from time import perf_counter as pc

t0 = pc()

do_something()

print(pc() - t0)
```
