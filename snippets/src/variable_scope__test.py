# %%

b = 6

def f(a):
    
    # need to say that b is not a local variable but a global one
    global b
    print(a)
    print(b)
    b = 9

b = 30
f(3)
print(b)