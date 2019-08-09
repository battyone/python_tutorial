
# %%
from functools import partial, lru_cache, singledispatch
from collections import abc
from operator import mul
from src.function_parameters import tag
import html
import numbers

# %%
triple = partial(mul, 3)
triple(7)

[triple(i) for i in range(3, 10)]

# %%
half_of_tag = partial(tag, 'img', cls='pic-frame')
print(half_of_tag(src='womba.jpg'))

print(half_of_tag.keywords)

# %%
# for lru_cache is used in decorators__test.py

# %%


def hmtlize(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'


print(hmtlize({1, 2, 3}))
print(hmtlize(abs))

# %%
################
# singledispatch
################


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<\br>\n')
    return f'<p>{content}</p>'


@htmlize.register(numbers.Integral)
def _(n):
    return f'<pre>{n} (0x{n:x})</pre>'


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>'+inner+'</li>\n</ul>'


print(htmlize('Hello'))
print(htmlize(42))
print(htmlize((45, 'bla bla', 7.8)))
print(htmlize([45, 'bla bla', 7.8]))

# %%


class TestClass:
    def __init__(self):
        self.some_value = 'Hello World'


@htmlize.register(TestClass)
def _(tc):
    return ('<p>'
            + 'TestClass: '
            + html.escape(tc.some_value).replace('\n', '<\br>\n') + '</p>')


tc = TestClass()
print(htmlize(tc))


# %%
# Closure
def bla(template):
    def fill_in(**kwargs):
        return template.format_map(kwargs)
    return fill_in

s = 'Hello {name} {lastname}.'
f = bla(s)
f(name='Christian', lastname='Henning')

