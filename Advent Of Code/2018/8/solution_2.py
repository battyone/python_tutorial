
# %%
input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

with open('8/input.txt') as fp:
    input = fp.readline()

it = map(int, input.split())

counter = 0


def parse(it):
    global counter

    num_childs, num_meta = next(it), next(it)

    name = chr(ord('A') + counter)
    counter += 1

    childs = [parse(it) for c in range(num_childs)]
    meta = [next(it) for m in range(num_meta)]

    return (name, childs, meta)


root = parse(it)
# print(root)

# %%
# only leaf nodes (no childs) sum their meta data
# if a node has childs use the meta as references
# to the childs


def node_value(node):
    name, childs, meta = node

    if childs:
        return sum(node_value(childs[i-1])
                   for i in meta if 1 <= i <= len(childs))
    else:
        return sum(meta)


print(node_value(root))

# %%

a = 0

a = 1
if 1 <= a <= 10:
    print('possible')
