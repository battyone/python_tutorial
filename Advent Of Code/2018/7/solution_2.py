
# %%
import re
from collections import defaultdict

tasks = set()

deps = defaultdict(set)
with open('7/input.txt') as fp:
    for _, x in enumerate(fp):
        a, b = re.findall(r' ([A-Z]) ', x)
        tasks |= {a, b}

        # task 'b' can only start after 'a' finishes
        deps[b].add(a)

num_workers = 5
done = set()
seconds = 0  # total seconds elapsed

# seconds remaining for a worker to finish its current task
counts = [0] * num_workers

work = [''] * num_workers  # which task a worker is performing

while True:

    # decrement each workers remaining time
    # if a worker finishes, mark its task as completed
    for i, count in enumerate(counts):
        if count == 1:
            done.add(work[i])

        counts[i] = max(0, count - 1)

    # while there are idle workers
    while 0 in counts:
        # find an idle worker
        i = counts.index(0)

        # find a task
        candidates = [x for x in tasks if deps[x] <= done]
        if not candidates:
            # no task is available, we might still have to wait for
            # other tasks to finish
            break
        task = min(candidates)
        tasks.remove(task)

        # have the worker start the selected task
        counts[i] = ord(task) - ord('A') + 61
        work[i] = task

    if sum(counts) == 0:
        break

    # print(f'{seconds} - {counts} - {work}')
    seconds += 1

print(seconds)
