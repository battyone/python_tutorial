
#%%
import fileinput

with fileinput.input(files=('D:/repos/python_tutorial/Advent Of Code/2018/5/input.txt')) as f:
    for line in f:
        if line[-1] == '\n':
            print('there is a trailing newline')