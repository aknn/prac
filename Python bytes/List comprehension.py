#   generator_expression = (expression for item in iterable)
#   list_comprehension = [expression for item in iterable]

xyz = (i for i in range(50000000))
print(list(xyz)[:5])


xyz = [i for i in range(50000000)]
print(xyz[:5])