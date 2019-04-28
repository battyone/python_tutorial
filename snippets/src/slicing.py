

# %%
s = "bicycle"

# print every 3 character
print(s[::3])

# reverse
print(f"reverse: {s[::-1]}")

# seq[start:stop:step]
# seq.__getitem__(slice(start, stop, step))

# %%
# Slice Objects

# Imaging a flat file
s = '1909 Pimoroni PiBrella $17.50 3 $52.50.'
SKU = slice(0, 4)
DESCRIPTION = slice(5, 22)
print(s[SKU])
print(s[DESCRIPTION])

# %% [markdown]
# # Assigning Slices

# %%
l = list(range(10))
print(l)

# override some elements
l[2:4] = [20, 30]
print(l)

# delete some elements
del l[5:7]
print(l)

#%% [markdown]
# # Using + and * with Sequences

#%% 
l = [1,2,3]
print(l*5)
print(5*'abcd')

#%% [markdown]
# # Building Lists of Lists

#%%
board = [['_'] * 3 for i in range(3)]
print(board)

board[1][2] = 'X'
print(board)

# Incorrect -- The Outer list has three references to the same list
weird_board = [['_']*3]*3
print(weird_board)
weird_board[1][2] = '0'
print(weird_board)


