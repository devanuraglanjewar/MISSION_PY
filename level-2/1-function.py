# what is function
# --a function is a block of code that performs a specific task. 
# --It is a reusable unit of code that helps to organize and modularize your program.

# example:
# let's create a function of geometric mean
def calculategmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

a = 9
b = 10 
calculategmean(a,b)  #function calling statement

c = 5
d = 8
calculategmean(a,d)  #function calling statement

# ther are two type of function
# --built-in functions
# ---are functions that are predefined and provided by python interpreter.
# --user-defined functions
# ---are functions that are created by the user.


# rules for creating a function
# 1. use the def keyword.
# 2. provide a function name.
#     2.1 the function name should be a valid python identifier.
#         --it should start with a letter or an underscore.
#         --it should not start with a digit.
#         --it can contain letters, digits, and underscores.
#         --it can also contain dollar signs ($), but it is not recommended.
# 3. provide a parameter list in parentheses.
# 4. write the function body in indented block.
# 5. use the colon (:) to start the function body.
# 6. write the code inside the function body.
# 7. use the return keyword to return a value.
# 8. if the function doesn't return anything, it returns "None" by default.

# types of arguments in function
# --default arguments
# ---example: function_name(8,5) --> 8 and 5 are the default arguments
 
# --keyword arguments
# ---example: function_name(b=3,a=4) --> b=3 and a=4 are the keyword arguments.
# ---in the keyword arguments you dont need to worry about orders of parameters.
 
# --required argument
# ---example: def function_name(a,b,c=1) --> a amd b are the required but c already has a value 1

# --variable-length arguments
# ---There are two main types of variable-length arguments:
# ----Non-keyworded arguments: 
# -----These are denoted by a single asterisk (*) in the function parameter list. 
#      They represent a tuple containing all the extra arguments passed to the function.
# ----Keyworded arguments: 
# ----These are denoted by a double asterisk (**) in the function parameter list. 
#     They represent a dictionary containing all the keyword arguments passed to the function, where the keys are the argument names and the values are the corresponding values.
# Example:
def sum_all(*numbers):
  """
  This function calculates the sum of all the numbers passed as arguments.

  Args:
    *numbers: An arbitrary number of numbers.

  Returns:
    The sum of all the numbers.
  """
  total = 0
  for number in numbers:
    total += number
  return total

# Example usage
sum1 = sum_all(1, 2, 3)
sum2 = sum_all(10, 20, 30, 40)

print(f"Sum1: {sum1}")
print(f"Sum2: {sum2}")


# Return statement:
# --A return statement in a function serves two main purposes:
# ---1. Exiting the function:
# ----It marks the end of the function's execution and transfers control back to the caller.
#    The execution of the function stops immediately after the return statement, regardless of any code that follows it within the function body.
# ---2. Returning a value (optional):
# ----A return statement can optionally include a value to be passed back to the caller.
#     This value can be of any type supported by the programming language, including integers, strings, booleans, or even complex data structures.
#     The caller can access this returned value and use it in their code.