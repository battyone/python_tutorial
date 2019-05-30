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
