
# What are sets?

# - Sets are unordered collections of unique elements.
# - They're mutable, meaning you can add or remove elements after creation.
# - Elements must be hashable (immutable like numbers, strings, or tuples).

# Key characteristics:

# - Unordered: Elements have no specific order.
# - Unique: No duplicates are allowed.
# - Mutable: You can modify the contents of a set.
# - Unindexed: You can't access elements by index like in lists.

# Creating sets:
from sre_parse import TYPE_FLAGS


my_set = {1, 2, 3, 3}  # Output: {1, 2, 3} (duplicates removed)

# set() constructor:
my_set = set([1, 2, 2, 4])  # Output: {1, 2, 4}

# Common operations:
# - Adding elements:
my_set.add(5)  # Adds 5 to the set

# - Removing elements:
my_set.remove(2)  # Removes 2 from the set (raises an error if not found)
my_set.discard(3)  # Removes 3 if present, otherwise does nothing

# - Checking membership:
if 1 in my_set:
    print("1 is in the set")


# Set operations:
# - Union: Combines elements from two sets, removing duplicates.
set1 = {1, 2, 3}
set2 = {2, 4, 5}
union_set = set1.union(set2)  
print(union_set)# Output: {1, 2, 3, 4, 5}
set1.update(set2)
print(set1)

# - Intersection: Returns elements common to both sets.
intersection_set = set1.intersection(set2)  
print(intersection_set)# Output: {2}

# - Difference: Returns elements in set1 but not in set2.
difference_set = set1.difference(set2)  
print(difference_set)# Output: {1, 3}

# - Symmetric difference: Returns elements in either set but not in both.
symmetric_difference_set = set1.symmetric_difference(set2)  
print(symmetric_difference_set)# Output: {1, 3, 4, 5}

# - Disjoin set
print("the set is joint >")
print(set1.isdisjoint(set2))

# - issuperset
print("Is set1 a superset of set2? ", set1.issuperset(set2))

# Frozen sets:
# - Immutable versions of sets, useful for keys in dictionaries.
frozen_set = frozenset([1, 2, 3])

# Empty set:
empty_set = set()
print(type(empty_set))  

# Remove and discard
set1.discard(1)
print(set1)
set1.remove(2)
print(set1)

# del
# - it use to delete complete set
del set1
print(set1) # it will show not define error because set1 id deleted completely

# clear
# - It removes all items from the set.
set1 = {1, 2, 3}
print(set1)
set1.clear()
print(set1)


# When to use sets:

# - Removing duplicates from a collection.
# - Performing mathematical set operations (union, intersection, difference).
# - Checking for membership efficiently.
# - Using sets as keys in dictionaries (since they're hashable).
