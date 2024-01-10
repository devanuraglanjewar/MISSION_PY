# What are docstrings?

#     Docstrings are text strings that serve as built-in documentation within Python code.
#     They are placed as the first statement within a module, function, class, or method definition.
#     Their purpose is to explain what a code element does, its usage, arguments, and return values, 
#     making code more readable and maintainable.

# Where are docstrings used?

#     Modules: Docstrings describe the module's purpose, contents, and exported objects.
#     Functions: Docstrings explain the function's purpose, arguments, return value, and potential exceptions.
#     Classes: Docstrings describe the class's purpose, attributes, and methods.
#     Methods: Docstrings explain the method's purpose, arguments, return value, and side effects.

# Structure of docstrings:

#     Docstrings typically follow a convention:
#         First line: A concise summary of the element's purpose.
#         Blank line: A separation between the summary and detailed description.
#         Detailed description: More information about usage, arguments, return values, etc.
# Example:
def greet(name):
    """Greets a person by their name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"
print(greet.__doc__)
help(greet)

# pep-8 

# PEP 8, also known as Python Enhancement Proposal 8, is a style guide for Python code that outlines best practices for formatting, 
# indentation, naming conventions, and other aspects of code style. 
# It aims to improve readability, consistency, and maintainability across Python projects.
