# %%
from inspect import getgeneratorstate
from collections import namedtuple

# %%


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

        # when send(x) is called `term` will be assigned to x and returned will be `average`
        term = yield average
        total = term
        count += 1
        average = total / count


averager = average_0()
next(averager)
a = averager.send(10.0)
print(a)

# %%
# Return a result
Result = namedtuple('Result', 'count average')


def averager_2():
    total = 0
    count = 0
    average = None

    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count

    return Result(count, average)


coro_avg = averager_2()
next(coro_avg)
coro_avg.send(20)
coro_avg.send(30)
coro_avg.send(40)
try:
    coro_avg.send(None)
except StopIteration as ex:
    result = ex.value

print(result)


# %%
#################
# yield from
#################

def gen():
    yield from 'AB'
    yield from range(1, 3)


print(list(gen()))


# %%
Result = namedtuple('Result', 'count average')

# the subgenerator


def averager_3():
    total = 0
    count = 0
    average = None

    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count

    return Result(count, average)

# the delegating generator


def grouper(results, key):
    while True:
        results[key] = yield from averager_3()

# the client code, aka the caller


def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)

        for value in values:
            group.send(value)
        group.send(None)  # finish

    # print results
    report(results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print(f'{result.count} {group:5} averaging {result.average:.2f}{unit}')


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == "__main__":
    main(data)
