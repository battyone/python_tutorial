# %%
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


Grid_Serial_No = 5235

print(calc_power_level((3, 5), 8))
print(calc_power_level((122, 79), 57))
print(calc_power_level((217, 196), 39))
print(calc_power_level((101, 153), 71))

# %%

pl = []

for y in range(1, 4):
    row = []
    for x in range(1, 4):
        row.append(calc_power_level((x, y), Grid_Serial_No))
    pl.append(row)

print(pl[0][1])