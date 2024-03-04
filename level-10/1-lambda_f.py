                        # Lambda Functions in Python

# What are they?

#     Anonymous functions (no name).
#     Defined using the lambda keyword.
#     Can take any number of arguments but only have one expression.
#     Often used for short, simple functions.

# Syntax:
#     lambda arguments: expression

# Examples:

#     Squaring a number: lambda x: x**2
#     Checking if a number is even: lambda x: x % 2 == 0
#     Adding two numbers: lambda x, y: x + y

# Passed as arguments to higher-order functions like map, filter, and reduce.
# Inline functions in list comprehensions and generator expressions.
# Creating quick throwaway functions for simple tasks.

# Advantages:

#     Concise syntax for small functions.
#     Improve readability in certain contexts.
#     Can be passed around easily as function objects.

# Disadvantages:

#     Limited functionality compared to regular functions.
#     Can become less readable for complex expressions.
#     Not suitable for reusable or well-documented functions.

# Best Practices:

#     Use for simple, one-line expressions.
#     Avoid for complex logic or reusable code.
#     Use descriptive variable names within the lambda.
#     Consider regular functions for readability and maintainability.

# Remember:

# Lambda functions are powerful tools, but use them judiciously.
# When in doubt, a regular function might be a better choice.

# def double(x):
#   return x*2

def appl(fx, value):
  return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(appl(lambda x: x * x , 2))