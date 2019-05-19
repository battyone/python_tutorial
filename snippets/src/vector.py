# %%
from math import hypot
from array import array

class Vector:
    typecode = 'd'

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # what a developer wants to see
    def __repr__(self):
        return f"x:{self.x}; y:{self.y}"

    # what a user wants to see
    def __str__(self):
        return f'x is {self.x} and y is {self.y}'


    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
        bytes(array(self.typecode, self)))


# %%
v=Vector(23, 89)
print(v)
print(repr(v))

for e in v:
    print(e)

octets=bytes(v)
print(octets)
