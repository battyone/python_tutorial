#%%

from collections import abc


class FrozenJson:
    """ A read-only facade for navigating a JSON-like
        using attribute notation
    """

    def __init__(self, mapping):
        # makes a copy
        print('__init__')
        self.__data = dict(mapping)

    def __getattr__(self, name):
        print(f'__getattr__ for {name}')
        # check if the dict has an attribute, like keys, items
        if hasattr(self.__data, name):
            print('hasattr is true')
            return getattr(self.__data, name)
        else:
            return FrozenJson.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        print('build')
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj

a = FrozenJson({'name':'Katrin', 'age':'20'})
# a.name

# this will throw KeyError
# a.bla

#%%
b = FrozenJson({'name':'Katrin', 'address':
    {'street': 'East 110th', 'house_number': '71'}})

b.address.street

