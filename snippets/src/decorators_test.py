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
