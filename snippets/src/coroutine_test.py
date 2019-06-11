
from inspect import getgeneratorstate


def simple_coroutine():
    print('coroutine started')
    x = yield
    print(f'-> coroutine received: {x}')


try:
    x = simple_coroutine()
    next(x)
    x.send(42)
except StopIteration:
    pass

# a coroutine has to start first before sending data
# y = simple_coroutine()
# y.send(67) # too early

print(''.center(50, '*'))
print(''.center(50, '*'))
print(''.center(50, '*'))


def simple_coroutine_2(a):
    print(f'Started with {a}')
    b = yield a  # b wont be a. `a` is just a statement before yield.
    print(f'-> received: {b}')
    # c wont be `a+b`, it's just a statement before yield.
    c = yield a + b
    print(f'-> received: {c}')


try:
    z = simple_coroutine_2(34)
    print(getgeneratorstate(z))
    next(z)
    # assigns 8 to `b`, prints the second message, and runs `yield a + b`, yielding (returning) 42
    a = z.send(8)
    print(getgeneratorstate(z))
    sum = z.send(99)
except StopIteration:
    print("Stop exception received")

print(''.center(50, '*'))
print(''.center(50, '*'))
print(''.center(50, '*'))


def average_0():
    total = 0
    count = 0
    average = 0

    while True:
        term = yield average
        total = term
        count += 1
        average = total / count


averager = average_0()
next(averager)
a = averager.send(10.0)
print(a)
