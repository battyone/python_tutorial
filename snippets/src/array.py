from array import array
from random import random

# typecodes
# d float
# h short signed integer
# B unsigned char



def run_test():
    # create an array from a generator expression
    floats = array('d', (random() for n in range(10**7)))
    print(floats[-1])

    fp = open('temp/floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()

    floats2 = array('d')
    fp = open('temp/floats.bin', 'rb')
    floats2.fromfile(fp, 10**7)
    fp.close()

    print(floats2[-1])

    print(floats == floats2)

    print('sorting')
    a = array(floats2.typecode, sorted(floats2))


if __name__ == "__main__":
    run_test()
