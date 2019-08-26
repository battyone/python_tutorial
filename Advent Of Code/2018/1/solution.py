
# %%
freq = 0

with open('input.txt') as fp:
    for _, line in enumerate(fp):
        freq += int(line)

print(freq)

# %%

# Part 2
# We need to loop through the frequency changes at least one time
# or more. 142 times to be exact.

f = 0

s = set()
s.add(f)

input = []

# Read all values
with open('input.txt') as fp:
    for _, line in enumerate(fp):
        input.append(int(line))

index = 0
loops = 0
while True:
    f += input[index]

    if f not in s:
        s.add(f)
    else:
        print('done')
        break

    index += 1
    if index == len(input):
        index = 0
        loops += 1


print(f)
print(loops)
