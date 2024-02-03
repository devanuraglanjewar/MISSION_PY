                                                 # finally keyword in Python

# Purpose:

    # Guarantees that a block of code is always executed, regardless of whether the try block completes normally or raises an exception.
    # Useful for:
    # Resource management: Cleaning up resources like open files, network connections, database handles, etc., even if errors occur.
    # Ensuring code execution: Executing essential code like writing data to a log file, even if other parts of the try block fail.

# Syntax:

try:
    # Code that might raise exceptions
except ExceptionType1:
    # Handle exception type 1
except ExceptionType2:
    # Handle exception type 2
else:
    # Code that executes only if no exceptions occur
finally:
    # Code that always executes

# Key Points:

    # The finally block always executes, even if try has a return statement, throws an unhandled exception, or is nested within another try...except block.
    # Use finally judiciously to avoid unnecessary overhead if resource cleanup isn't critical.
    # Consider context managers (like with open()) and try...with statements for resource management, as they often simplify cleanup and enhance readability.

# Example:

try:
    with open("myfile.txt", "w") as file:
        file.write("This line will be written.")
        raise ValueError("Intentional error")  # Simulate an error
finally:
    print("File is closed (if opened at all).")

#Example

def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)


# In essence:

    # The finally block in Python offers a reliable way to ensure cleanup or essential code execution, even under exceptional circumstances.
    # Employ it carefully for effective resource management and improved error handling in your Python programs.