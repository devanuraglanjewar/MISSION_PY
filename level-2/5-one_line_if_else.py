# Shortest way to write a if else in more readable way and it is also maintainable.
    # Syntax: value_if_true if condition else value_if_false
    # Evaluates the condition and returns the first value if True, otherwise the second value.
    # Example:

a = 330000
b = 3303
print("A") if a > b else print("=") if a == b else print("B")

c = 9 if a>b else 0
print(c)