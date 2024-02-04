# What it does:

# - It enhances a loop by providing both the index and value of each item in an iterable (like a list, tuple, or string).
# - It returns an enumerate object, which is an iterator yielding pairs of (index, element).

# Syntax:

# enumerate(iterable, start=0)


# Arguments:

# - `iterable`: The sequence you want to enumerate (e.g., list, tuple, string).
# - `start` (optional): The starting index for the counter (default is 0).

# Example:

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Fruit at index {index} is {fruit}")

# Output:

# Fruit at index 0 is apple
# Fruit at index 1 is banana
# Fruit at index 2 is cherry


# Key points:

# - It's often used for:
#     - Accessing both index and element within loops
#     - Creating new sequences with indexes
#     - Modifying sequences based on index
# - The enumerate object is iterable, so you can use it in multiple loops or convert it to a list or tuple.
# - You can change the starting index with the `start` argument.

# Common use cases:

# - Looping through a list and performing actions based on index
# - Creating dictionaries with keys from one list and values from another
# - Formatting output with both index and value
# - Implementing algorithms that require index-based operations
