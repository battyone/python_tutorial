def square_numbers(numbers):
    for i in numbers:
        yield (i*i)


# this will be a generator
numbers = square_numbers([1, 2, 3, 4, 5])
print(numbers)

print(next(numbers))

# this is not a generator
numbers_2 = [x*x for x in [1, 2, 3, 4, 5]]
print(numbers_2)


# this will NOT loop through all numbers since we just called numbers one time
for i in numbers:
    print(i)

# another way to create a generator via list comprehensions
numbers_generator = (x*x for x in [1, 2, 3, 4, 5])
print(numbers_generator)

# make a list from a generator
numbers_3 = list(numbers_generator)
print(numbers_3)
