# Map, Filter, Reduce functions


# map() Function:

#     Purpose: Applies a function to each element in an iterable (list, tuple, etc.) and returns an iterator (or list) containing the transformed elements.
#     Syntax: map(function, iterable, *iterables)
#     function: The function to apply to each element (can be a named function or lambda).
#     iterable: The main iterable to process.
#     *iterables (optional): Additional iterables whose elements are paired with those from the main iterable during function application.

#Example:
def square(x):
    return x * x

numbers = [1, 2, 3, 4]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16]


# filter() Function:

#     Purpose: Creates an iterator (or list) containing only elements from an iterable that pass a test provided by a function.
#     Syntax: filter(function, iterable)
#     function: The function to test each element (should return True for elements to keep, False otherwise).
#     iterable: The iterable to filter.

# Example:
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6]


# reduce() Function:

#     Purpose: Reduces an iterable to a single value by applying a function cumulatively across its elements.
#     Syntax: reduce(function, iterable, initial=None)
#     function: The function to apply to pairs of elements (should take two arguments and return a single value).
#     iterable: The iterable to reduce.
#     initial (optional): The initial value for the accumulative result (if not provided, raises TypeError).

# Example:
def product(x, y):
    return x * y

numbers = [1, 2, 3, 4]
total_product = reduce(product, numbers)
print(total_product)  # Output: 24

# -----------------------------------------------------------------------------------------------------------------------------------------------------


# # MAP 

def cube(x):
  return x * x * x


print(cube(2))

l = [1, 2, 4, 6, 4, 3]    # simple approach
newl = []
for item in l:
  newl.append(cube(item))

newl = list(map(lambda x: x*x*x, l)) # using map function
print(newl)


# FILTER
def filter_function(a):
  return a>2
  
newnewl = list(filter(filter_function, l))
print(newnewl)

from functools import reduce
# List of numbers
numbers = [1, 2, 3, 4, 5] 

# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
  return x + y
  
sum = reduce(mysum, numbers)

# Print the sum
print(sum)

