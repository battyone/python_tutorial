# %%
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
            pl += grid[y+m][x+n]

    return pl


Grid_Serial_No = 5235
Dim = 300
Kernel = 3

# Test
# print(calc_power_level((3, 5), 8))
# print(calc_power_level((122, 79), 57))
# print(calc_power_level((217, 196), 39))
# print(calc_power_level((101, 153), 71))

# %%

grid = []

for y in range(1, Dim + 1):
    row = []
    for x in range(1, Dim + 1):
        row.append(assign_fuel_cell_power((x, y), Grid_Serial_No))
    grid.append(row)

max_power_level = 0
max_power_level_coord = ()

for y in range(0, Dim - Kernel + 1):
    for x in range(0, Dim - Kernel + 1):
        pl = calc_square_power(grid, (x, y), Kernel)

        if pl > max_power_level:
            max_power_level = pl
            max_power_level_coord = (x+1, y+1)

print(max_power_level)
print(max_power_level_coord)

# for y in range(0, Dim - Kernel + 1):
#     for x in range(0, Dim - Kernel + 1):
#         indices = []
#         for m in range(0, Kernel):
#             for n in range(0, Kernel):
#                 indices.append((x + n, y + m))
#         Counter += 1
#         print(Counter, indices)
