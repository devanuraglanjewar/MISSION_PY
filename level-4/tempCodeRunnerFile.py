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
