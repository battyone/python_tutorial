# %%
import random
import collections

# %%


def factorial(n):
    #"""Returns n!"""
    return 1 if n < 2 else n * factorial(n-1)


print(factorial(42))
print(factorial.__doc__)

# rename function
func = factorial

# old school
print('old: ', list(map(func, range(5))))
print('new: ', [func(i) for i in range(5)])


# %%

# sorting a list by reverse spelling
a = 'banana apple strawberry fig blueberry'
b = a.split()

[print(w[::-1]) for w in b]


def reverse(w):
    return w[::-1]


print(b)
print(sorted(b, key=reverse))

print(sorted(b, key=lambda word: word[::-1]))

# %%
print(a)

a = random.choices(range(1, 2), k=20)
if(any(a)):
    print('There are some ones!')

if(all(a)):
    print('All are ones!')

# %%
dir(factorial)
print(random.choice.__name__)
print(random.choice.__qualname__)
print(random.choice.__kwdefaults__)
print(random.choice.__globals__)

# %%


def upper_case_name(obj):
    return f'{obj.first_name} {obj.last_name}'.upper()

upper_case_name.short_description = 'Customer Name'

A = collections.namedtuple('Customer', 'first_name last_name')
a = A('Katrin', 'Henning')

NAME = upper_case_name(a)
print(NAME)

print(upper_case_name.short_description)
