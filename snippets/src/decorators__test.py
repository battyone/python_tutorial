# %%
import time


# %%


def deco(func):
    def inner():
        print('running inner()')

    return inner()


@deco
def target():
    print('running target()')


# not working ???
target

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


print('*' * 40, '\ncalling snooze')
snooze(0.5)
print('*' * 40)
