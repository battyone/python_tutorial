# %%
import struct

# little endian;two sequences of 3 bytes;two 16-bit integers
fmt = '<3s3sHH'
with open('some.gif', 'rb') as fp:
    img = memoryview(fp.read())

    header = img[:10]
    print(bytes(header))

    print(struct.unpack(fmt, header))

    # delete references tp release the memory associated with the memoryview
    # instances
    del header
    del img
