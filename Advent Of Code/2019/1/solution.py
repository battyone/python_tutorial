# %%
input = []
with open('input.txt', 'r') as fp:
    input = list(map(int, [l[:-1] for _, l in enumerate(fp)]))

part_1 = sum([i // 3 - 2 for i in input])
print(part_1)

# %%


def calc(i):
    s = 0
    while True:
        i = i // 3 - 2
        if i > 0:
            s += i
        else:
            return s


part_2 = sum([calc(i) for i in input])
print(part_2)
