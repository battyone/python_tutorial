# %%
import re
from collections import defaultdict

# %%
# wikipedia has a good description:
# https://en.wikipedia.org/wiki/Topological_sorting

# all tasks names. Can only be a letter from A-Z
tasks = set()

# Each task might requires other tasks to finish first
deps = defaultdict(set)
with open('7/input.txt') as fp:
    for _, x in enumerate(fp):
        a, b = re.findall(r' ([A-Z]) ', x)
        tasks |= {a, b}

        # task 'b' can only start after 'a' finishes
        deps[b].add(a)

print(*deps.items())

# %%
done = []
for _ in tasks:
    # find the minimal (lexicographically) task that is not yet done
    # and has all of its prerequisites satisfied; add it to the list

    # Christian: Find a task which not already in `done` and all of its
    # dependency are done.
    # Also make sure to select the "smallest" task (letter) first. Hence
    # the min(...)
    done.append(
        min(x for x in tasks if x not in done and deps[x] <= set(done)))
print(''.join(done))
