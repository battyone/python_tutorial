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

