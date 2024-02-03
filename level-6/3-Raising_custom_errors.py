# 1. Defining Custom Exceptions:
#     Create a new class that inherits from the built-in Exception class (or a more specific subclass like ValueError).

# Example:

class InvalidAgeException(Exception):
    pass

# 2. Raising the Exception:
    # Use the raise keyword followed by the exception class name and an optional error message.

# Example:
age = 15
if age < 18:
    raise InvalidAgeException("Age must be 18 or older.")


# 3. Handling the Exception:
    # Use try...except blocks to catch and handle specific exceptions.

# Example:
try:
    # Code that might raise InvalidAgeException
except InvalidAgeException as e:
    print("Error:", e)



# Key Points:

    # Error Message: Provide informative error messages for clarity.
    # Base Classes: Choose appropriate base classes for better exception handling logic.
    # Hierarchy: Create custom exception hierarchies for specific error categories.
    # Organization: Organize custom exceptions in a separate module for large projects.
# Best Practices:
    # Use meaningful exception names.
    # Avoid overly generic exceptions.
    # Raise exceptions early to prevent issues propagating.
    # Handle exceptions appropriately for proper error handling.