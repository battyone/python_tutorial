# enw8 = open("enwik8", "rb").read()
# open("enwik6", "wb").write(enw8[0:1000000])

# enwik6:        1000000 bytes (1MB)
# gzip enwik6 ->  356264 bytes


def bitgen(x):
    """ bit generator - creates an integer (0 or 1) representing each bit of x."""
    for c in x:
        for i in range(8):
            yield int((c & (0x80 >> i)) != 0)


# printing
print(bin(0x3C6D))
enw6 = open("enwik6", "rb").read()
# print(enw6[0:100])

bg = bitgen(enw6)
for i in range(16):
    print(i, next(bg))
