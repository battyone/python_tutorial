
from collections import defaultdict


def assign_fuel_cell_power(coord, serial_no):
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


def calc_square_power(grid, coord, kernel_dim):
    x, y = coord

    pl = 0
    for m in range(0, kernel_dim):
        for n in range(0, kernel_dim):
            pl += grid[(x+n, y+m)]

    return pl


def create_grid(Dim, Grid_Serial_No):
    grid = defaultdict(int)

    for y in range(1, Dim + 1):
        for x in range(1, Dim + 1):
            grid[(x, y)] = assign_fuel_cell_power((x, y), Grid_Serial_No)

    return grid


def find_max(grid, Dim, Kernel):

    max_power_level = 0
    max_power_level_coord = ()

    for y in range(1, Dim - Kernel + 1):
        for x in range(1, Dim - Kernel + 1):
            pl = calc_square_power(grid, (x, y), Kernel)

            if pl > max_power_level:
                max_power_level = pl
                max_power_level_coord = (x, y)

    return (max_power_level, max_power_level_coord)


Grid_Serial_No = 5235
Dim = 300
Kernel = 3

grid = create_grid(Dim, Grid_Serial_No)

for k in range(3, 300):
    max_power = find_max(grid, Dim, k)
    print(k, max_power)
