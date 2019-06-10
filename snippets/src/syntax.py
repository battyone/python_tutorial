
def for_test():
    # else will be executed when for was run through
    for i in range(10):
        print('Hello')
    else:
        print('for was successful')

    for i in range(2):
        print('Hello again')
        if i == 1:
            break
    else:
        print('for was successful')


def while_test():
    # while else will execute
    a = True
    while a:
        print('while I\'am')
        a = False
    else:
        print('while was aborted')


def try_test():
    try:
        print('trying')
    except Exception as e:
        pass
    else:
        print('No exeption happened.')


if __name__ == "__main__":
    # for_test()
    # while_test()
    try_test()
