# %%

from collections import abc
import keyword


class FrozenJson:
    """ A read-only facade for navigating a JSON-like
        using attribute notation
    """

    def __init__(self, mapping):
        print('__init__')

        self.__data = {}
        for k, v in mapping.items():
            if keyword.iskeyword(k):
                k += '_'

            # 2be would be an incorrect key
            if k.isidentifier() == False:
                raise RuntimeError(f'Cannot create key from "{k}".')

            self.__data[k] = v

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


class FrozenJson2:
    """ A read-only facade for navigating a JSON-like
        using attribute notation
    """

    def __new__(cls, arg):
        print('__new__')

        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        print('__init__')

        self.__data = {}
        for k, v in mapping.items():
            if keyword.iskeyword(k):
                k += '_'

            # 2be would be an incorrect key name
            if k.isidentifier() == False:
                raise RuntimeError(f'Cannot create key from "{k}".')

            self.__data[k] = v

    def __getattr__(self, name):
        print(f'__getattr__ for {name}')

        # check if the dict has an attribute, like keys, items
        if hasattr(self.__data, name):
            print('hasattr is true')
            return getattr(self.__data, name)
        else:
            return FrozenJson(self.__data[name])


# %%
a = FrozenJson({'name': 'Katrin', 'age': '20'})
# a.name

# this will throw KeyError
# a.bla


b = FrozenJson({'name': 'Katrin', 'address':
                {'street': 'East 110th', 'house_number': '71'}, 'class': 55, '2be': 66})

b.address.street
b.class_

# %%
