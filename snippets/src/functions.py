
# %%
import random
import collections
from inspect import signature
import src.function_parameters

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


# add a new attribute to function
upper_case_name.short_description = 'Customer Name'

A = collections.namedtuple('Customer', 'first_name last_name')
a = A('Katrin', 'Henning')

NAME = upper_case_name(a)
print(NAME)

print(upper_case_name.short_description)

# %%

def clip(txt, max_len=80):
    # '''Return text clipped at the last space before
    # or after max_len'''
    end = None
    if len(txt) > max_len:
        space_before = txt.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = txt.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        # no spaces were found
        end = len(txt)
    return txt[:end].rstrip()


print(clip('Hello World', 10))

print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)

#%%

sig = signature(clip)
print(str(sig))

for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)


#%%

func_params = {
    'name': 'img',
    'title': 'Sunset Boulevard',
    'src': 'sunset.jpg',
    'cls': 'framed'
}

sig = signature(tag)
bound_args = sig.bind(**func_params)
print(bound_args)


#%% 

def clip_annotated(txt: str, max_len:'int > 0'=80) -> str:
    # '''Return text clipped at the last space before
    # or after max_len'''
    end = None
    if len(txt) > max_len:
        space_before = txt.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = txt.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        # no spaces were found
        end = len(txt)
    return txt[:end].rstrip()

clip_annotated('Hello World')
