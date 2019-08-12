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

class C(A,B):
    def __init__(self):
        super().__init__()
        print('C.__init__')

c = C()
print(C.__mro__)


#%%

class Person:
    def __init__(self, first_name):
        #call to Setter
        self.first_name = first_name

    #Getter
    @property
    def first_name(self):
        return self._first_name

    #Setter
    @first_name.setter
    def first_name(self, name):
        if not isinstance(name, str):
            raise TypeError ('Expected a string')
        print('setting first name')
        self._first_name = name
    
    #Deleter 
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


p = Person('Katrin')


