# tuples are just similar as list but the difference is string can be change and the tuple cannot. 
# how to define
tup = (1,5)
print(type(tup),tup)
# tuple is one kind of constant list 

# Characteristics:

# Ordered: Tuples maintain the order of their elements.
# Immutable: Once created, the elements of a tuple cannot be changed.
# Heterogeneous: Can store elements of different data types (integers, strings, lists, etc.) within the same tuple.
# Duplicates allowed: You can have duplicate elements in a tuple.

# Creating Tuples:

# There are two ways to create a tuple:

# 1.Using parentheses:
# Empty tuple
my_tuple = ()

# Tuple with one element
my_tuple = (1,)

# Tuple with multiple elements
my_tuple = ("apple", "banana", "cherry")

# Tuple with mixed data types
my_tuple = ("apple", 10, True)


# 2. Using the `tuple()` function:
my_tuple = tuple(["apple", "banana", "cherry"])


# Accessing Tuple Elements:
# You can access individual elements of a tuple using their index, starting from 0. Negative indexing can also be used.

# Access first element
first_element = my_tuple[0]

# Access second element
second_element = my_tuple[1]

# Access last element
last_element = my_tuple[-1]

# Tuple Operations:

# Some common operations supported by tuples include:

# Concatenation: You can combine two tuples using the `+` operator.
# Slicing: You can extract a specific sub-tuple using slice notation.
# Membership: You can check if an element exists in a tuple using the `in` operator.
# Length: You can get the number of elements in a tuple using the `len()` function.

# Tuple vs. List:

# While both tuples and lists store collections of data, they have key differences:

# | Feature              | Tuple                                     | List                             |
# |---------------------|-------------------------------------------|--------------------------------- |
# | Order              | Ordered                                   | Ordered                          |
# | Mutability        | Immutable (elements cannot be changed)    | Mutable (elements can be changed)|
# | Performance      | Generally faster than lists               | Generally slower than tuples     |
# | Use cases       | When order and immutability are important | When you need to modify elements |