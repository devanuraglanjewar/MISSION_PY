# Understanding the else clause:

    # - It's a unique feature of Python that allows you to execute a block of code after a for loop completes normally, 
        #   meaning it iterated through all elements without encountering a `break` statement.
    # - The `else` clause executes only if the loop completes all iterations without being interrupted by a `break`.

# Syntax:
for element in iterable:
        # code to execute for each element
        if condition:
            break  # Terminates the loop prematurely
else:
        # code to execute if the loop completes normally

# Key points:

    # - The `else` clause is not mandatory for for loops.
    # - It's often used for tasks like:
    #     - Handling cases where a specific value is not found within the loop.
    #     - Signaling that a loop has exhausted all possible values.

# Example 1: Searching for a value:

numbers = [1, 4, 2, 9]

for num in numbers:
    if num == 3:
        print("Found the number 3!")
        break
else:
    print("Number 3 not found in the list.")

# Output:
    # Number 3 not found in the list.


# Example 2: Iterating through a dictionary:

person = {"name": "Alice", "age": 30, "city": "New York"}

for key in person:
    print(key, ":", person[key])
else:
    print("All keys have been iterated over.")

# Output:
    # name : Alice
    # age : 30
    # city : New York
    # All keys have been iterated over.


# Remember:

    # - The `else` clause is not executed if the loop is empty (no elements to iterate over).
    # - It's a helpful construct for handling specific scenarios and ensuring code clarity.
