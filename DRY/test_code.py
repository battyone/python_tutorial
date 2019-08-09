# %%


def func(*a, **b):
    print('pos args are: ', a)
    print('keyword args are: ', b)


func(1, 'a', x=1, y='a', z='Hello')

a = (1, 2)
b = {'x': 1, 'y': 2, 'z': 3}
# the stars mean to "explode" the tuples or dict
func(*a, **b)


# %%
# after the '*' parameters can only be passed by keyword
def func2(a, *, b=True):
    pass


#%% 
# A closure is a function which returns a function. The returning function can have some state.

def make_adder(x,y):
    def add():
        return x + y
    return add

a = make_adder(2,3)
a()

#%%
# Classes

class Spam:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def foo(self):
        pass
    
    @classmethod
    def bar(cls):
        pass
    
    @staticmethod
    def soo():
        pass

s = Spam(2,4)
s.foo()
Spam.bar()
Spam.soo()

print(s.__dict__)
print(Spam.__dict__['foo'])
















