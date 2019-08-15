# %%
class Gizmo:
    def __init__(self):
        print(f"Gizmo id: {id(self)}")


a = Gizmo()

dir()


# %%
class Demo:
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


print(Demo.klassmeth())
print(Demo.klassmeth('spam'))

print(Demo.statmeth())
print(Demo.statmeth('spam'))

# %%
# Inheritance


class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value]*2)


dd = DoppelDict(one=1)
dd['two'] = 2
print(dd)

# %%
# Multiple Inheritance


class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('C.__init__')


c = C()
print(C.__mro__)


# %%
# Property example
class Person:
    def __init__(self, first_name):
        # call to Setter
        self.first_name = first_name

    # Getter
    @property
    def first_name(self):
        return self._first_name

    # Setter
    @first_name.setter
    def first_name(self, name):
        if not isinstance(name, str):
            raise TypeError('Expected a string')
        print('setting first name')
        self._first_name = name

    # Deleter
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


p = Person('Katrin')

Person.first_name.fget

# %%
# Proxy example using __setattr__ and __getattr__

class A:
    def __init__(self):
        self.x = 1

    def __str__(self):
        return f'x: {self.x}'


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        print(f'getting {name}')
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            print('setting _obj')
            super().__setattr__(name, value)
        else:
            print(f'setting {name}')
            setattr(self._obj, name, value)


a = A()
p = Proxy(a)
p.x = 2
print(a) # is now 2
print(p.x) # is now 2
