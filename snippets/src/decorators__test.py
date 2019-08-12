
# %%
import time
import functools

# %%
def deco(func):
    def inner():
        print(func.__qualname__)

    return inner()


@deco
def target():
    print('running target()')


# %%

registry = []


# function is called 3 times during import time
def register(func):
    print(f'running register {func}')
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


@register
def f3():
    print('running f3()')


def main():
    print('running main')
    print('registry ->', registry)

    f1()
    f2()
    f3()


main()

# %%
def clock(func):

    # inner function which accepts any number of positional arguments
    def clocked(*args):
        t0 = time.perf_counter()

        result = func(*args)

        elapsed = time.perf_counter() - t0

        name = func.__name__
        arg_str = ','.join(repr(a) for a in args)
        print(f'{elapsed:.8f} {name}({arg_str}) -> {result}')

        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


# %%
print('*' * 40, '\ncalling snooze')
snooze(0.5)
print('*' * 40)
print('*' * 40, '\ncalling factorial')
factorial(80)
print('*' * 40)


##################
# clock decorator v2
#################

# %%
def clock_v2(func):

    # add support for keyword arguments
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0

        name = func.__name__

        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(a) for a in args))
        if kwargs:
            pairs = [f'{k}={v}' for k, v in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))

        arg_str = ', '.join(arg_lst)

        print(f'{elapsed:.8f} {name}({arg_str}) -> {result} ')

        return result
    return clocked

# %%
@clock_v2
def fibonacci_v2(n):
    if n < 2:
        return n
    return fibonacci_v2(n-2) + fibonacci_v2(n-1)


@functools.lru_cache()
@clock_v2
def fibonacci_v3(n):
    if n < 2:
        return n
    return fibonacci_v3(n-2) + fibonacci_v3(n-1)


# %%
# fibonacci(1) is called a lot of times...
print(fibonacci_v2(6))

# %%
# fibonacci(1) is called one time!
print(fibonacci_v3(6))


#%%
#  A decorator which takes parameters
from functools import wraps, partial

def debug(func=None, *, prefix=''):
    # When using the prefix, func is None.
    # This is a workaround around the problem.
    if func is None:
        return partial(debug, prefix=prefix)

    msg = prefix + func.__qualname__

    # wraps copies metadata for help(func), etc
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, *kwargs)
    return wrapper


@debug(prefix='***')
def add(x, y):
    return x + y

add(2,8)

