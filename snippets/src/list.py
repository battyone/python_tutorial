
# %%
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(fruits)
print(sorted(fruits))
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))

# inplace sorting
fruits.sort()
print(fruits)

# %%
# add list to list
a = []
a.extend(range(0, 10))
print(a)
