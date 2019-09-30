# %%
from itertools import islice


def calc_power_level(coord, serial_no):
    x, y = coord

    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_no
    power_level *= rack_id

    if power_level < 100:
        print('bad')
        return -100  # Cannot happen

    hundred_digit = int(str(power_level)[::-1][2])
    return hundred_digit - 5


def my_sum(row, dim):
    sums = []

    for i in range(0, len(row)-dim):
        sum = 0
        for k in range(0, dim):
            sum += row[i + k]
        sums.append(sum)

    return sums


def my_sum_2(row, dim):
    sums = []

    for i in range(0, len(row)-dim):
        sums.append(sum(islice(row, i, i + dim + 1)))

    return sums


Grid_Serial_No = 5235
Dim = 30

print(calc_power_level((3, 5), 8))
print(calc_power_level((122, 79), 57))
print(calc_power_level((217, 196), 39))
print(calc_power_level((101, 153), 71))

# %%

pl = []

for y in range(1, Dim + 1):
    row = []
    for x in range(1, Dim + 1):
        row.append(calc_power_level((x, y), Grid_Serial_No))
    pl.append(row)


# %%
print(pl[0])
print(sum(pl[0], 3))
print(sum_2(pl[0], 3))

# %%
l = [1, 2, 3]
print(sum(l))


# %%
