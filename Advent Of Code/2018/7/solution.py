# %%
import re
from collections import defaultdict

# %%

# all tasks names. Can only be a letter from A-Z
tasks = set()

# Each task might requires other tasks to finish first
deps = defaultdict(set)
with open('7/test.txt') as fp:
    for _, x in enumerate(fp):
        a, b = re.findall(r' ([A-Z]) ', x)
        tasks |= {a, b}

        # task 'b' can only start after 'a' finishes
        deps[b].add(a)

# input = read_input('test.txt')
# print(input)

done = []
for _ in tasks:
    # find the minimal (lexicographically) task that is not yet done
    # and has all of its prerequisites satisfied; add it to the list
    done.append(min(x for x in tasks if x not in done and deps[x] <= set(done)))
print(''.join(done))

#%%
a = set([1,2,7])
b = set([1,2,3,4])
if a <= b:
    print("True")
else:
    print("False")