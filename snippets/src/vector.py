
# %%
from math import hypot
from array import array

# to make Vector hashable it has to immutable (see __x, etc.)


class Vector:
    typecode = 'd'  # double

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        print('hashing')
        return hash(self.x) ^ hash(self.y)

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

    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self)
        return '({} {})'.format(*components)

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))


# %%
v = Vector(23, 89)
print(v)
print(repr(v))

for e in v:
    print(e)

octets = bytes(v)
print(octets)

format(v)

a = Vector(3, 89)
b = Vector(3, 89)
print(a == b)

a.__x = 99
print(str(a))
print(a.__x)
print(a.x)

print(hash(a))
print(hash(b))

# %%
a = Vector(1.3, 2.99)
print(hash(a))
print(hash(float(33.1)))

octets = bytes(a)
print(octets)
b = Vector.frombytes(octets)
print(a)
print(b)
