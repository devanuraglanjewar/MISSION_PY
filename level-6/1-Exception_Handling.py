
# What are exceptions?

#     Errors that occur during program execution.
#     Examples: ZeroDivisionError, TypeError, FileNotFoundError.

# Why handle exceptions?

#     Makes code more robust and user-friendly.
#     Prevents program crashes.
#     Provides informative error messages.

# How to handle exceptions:

#     try-except block:

    #     try: Code that might raise an exception.
    #     except: Code to handle specific exceptions.

#     Raising exceptions:
    #     Use raise to manually signal an error.

# Common exception types:

#     ValueError: Raised for invalid values.
#     IndexError: Raised for accessing invalid indices.
#     KeyError: Raised for accessing non-existent keys in dictionaries.

# Additional notes:

#     Use multiple except blocks to handle different exceptions.
#     Use else clause to execute code if no exception occurs.
#     Use finally clause to execute code always, even after exceptions.

# Benefits:

#     Improved code quality and maintainability.
#     Better user experience by providing informative error messages.


# example

a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
  for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
  print("Invalid  Input!")

print("Some imp lines of code")
print("End of program")

# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
    
# except IndexError:
#   print("Index Error")