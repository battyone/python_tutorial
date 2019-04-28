
#%%
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(fruits)
print(sorted(fruits))
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))

# inplace sorting
fruits.sort()
print(fruits)
