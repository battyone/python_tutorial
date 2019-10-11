

tracks = {}

with open('input.txt') as fp:
    for y, l in enumerate(fp):
        for x in range(0, len(l[:-1])):
            c = l[x]
            if c != ' ':
                tracks[(x, y)] = l[x]

print(set(tracks.values()))
