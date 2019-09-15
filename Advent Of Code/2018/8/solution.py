# %%
input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
# 2  - A num childs
# 3  - A num meta
# 0  - B num childs
# 3  - B num meta
# 10 - B meta 1
# 11 - B meta 2
# 12 - B meta 3
# 1  - C num childs
# 1  - C num meta
# 0  - D num childs
# 1  - D num meta
# 99 - D meta 1
# 2  - C meta 1
# 1  - A meta 1
# 1  - A meta 2
# 2  - A meta 3

# %%
with open('8/input.txt') as fp:
    input = fp.readline()

it = map(int, input.split())


def parse(it):
    num_childs, num_meta = next(it), next(it)

    childs = [parse(it) for c in range(num_childs)]
    meta = [next(it) for m in range(num_meta)]

    return (childs, meta)


root = parse(it)

# %%


def sum_meta(node):
    childs, meta = node

    # return the sum of meta plus the sum of meta
    # of all my childs
    return sum(meta) + sum(sum_meta(x) for x in childs)


print(sum_meta(root))
