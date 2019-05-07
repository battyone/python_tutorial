
# %%
from functools import partial
from operator import mul
from src.function_parameters import tag

# %%
triple = partial(mul, 3)
triple(7)

[triple(i) for i in range(3, 10)]

# %%
half_of_tag = partial(tag, 'img', cls='pic-frame')
print(half_of_tag(src='womba.jpg'))

print(half_of_tag.keywords)
