#   generator_expression = (expression for item in iterable)
#   list_comprehension = [expression for item in iterable]
#import timeit
import timeit

# Define a function to filter values divisible by two
def div_by_two(num):
    return num % 2 == 0

# Generate the values using a generator expression
xyz = (i for i in range(50) if div_by_two(i))

# Measure the time for iterating through the generator
generator_time = timeit.timeit(lambda: [x for x in xyz], number=1)

# Generate the values using a list comprehension
input_list = [i for i in range(50) if div_by_two(i)]

# Measure the time for the list comprehension
list_time = timeit.timeit(lambda: [x for x in input_list], number=1)

# Print the results
print("Generator expression time:", generator_time)
print("List comprehension time:", list_time)

