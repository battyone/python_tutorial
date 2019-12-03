
#%%
input = []
with open('input.txt', 'r') as fp:
    line = fp.read()[:-1]
    input = [int(n) for n in line.split(sep=',')]

input[1] = 12
input[2] = 2

def do_operation(input, pos):
    op = input[pos]
    v1 = input[input[pos+1]]
    v2 = input[input[pos+2]]
    re_pos = input[pos+3]

    if op == 1:
        input[re_pos] = v1 + v2
    elif op == 2:
        input[re_pos] = v1 * v2
    elif op == 99:
        return False
    else:
        print(pos)
        raise NotImplementedError()

    # continue
    return True

def do_operation(input, pos, address1, address2):
    op = input[pos]
    v1 = input[input[address1]]
    v2 = input[input[address2]]
    re_pos = input[pos+3]

    if op == 1:
        input[re_pos] = v1 + v2
    elif op == 2:
        input[re_pos] = v1 * v2
    elif op == 99:
        return False
    else:
        print(pos)
        raise NotImplementedError()

    # continue
    return True

# part 1
# pos = 0
# while True:
#     if not do_operation(input, pos):
#         break
#     pos += 4

# print(input[0])

# part 2


try:
    for noun in range(0, 100):
        for verb in range(0, 100):
            pos = 0
            a = list(input)

            print(len(a))

            while True:
                if not do_operation(a, pos, noun, verb):
                    # print(noun, verb, a[0], 'Done')
                    break
                if a[0] == 19690720:
                    print(noun, verb)
                    raise StopIteration()

                pos += 4
except StopIteration:
    print('Found part 2')

