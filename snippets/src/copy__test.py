# %%
from copy import copy, deepcopy


# Copies are shallow by default
l1 = [3, [55, 44], (7, 8, 9)]
print(type(l1[2]))

l2 = list(l1)

print(l1 is l2)  # not the same list
print(l1[1] is l2[1])  # but refering to the same inner list

l3 = l1[:]  # another way

l4 = deepcopy(l1)
print(l1[1] is l4[1])

# %%


class Bus:
    # don't use passengers=[], see pg. 238
    # see default_parameter__test.py
    def __init__(self, passengers=None):
        if(passengers is None):
            self.passengers = []
        else:
            # make a copy from the original list !!
            # see pg. 239
            self.passengers = list(passengers)


b1 = Bus(['Bob', 'Katrin'])
b2 = deepcopy(b1)
b3 = copy.copy(b1)

b2.passengers.append('Sophie')

print(b1.passengers)
print(b2.passengers)
print(b3.passengers)


#%%
#tuples are not copied!

t1 = (1,2,3)
t2 = tuple(t1)
t3 = t1[:]

print(t1 is t2)
print(t1 is t3)


