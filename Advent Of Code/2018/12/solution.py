
initial = ''
notes = []

with open('input.txt') as fp:
    initial = fp.readline()[:-1]
    empty = fp.readline()

    for n in fp.readlines():
        notes.append(n[:-1])

print(initial)
print(*notes, sep='\n')
