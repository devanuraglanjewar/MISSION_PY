#
# Basics:

    # Opening: Use open(filename, mode) where mode is "r" (read), "w" (write), "a" (append), or others.
    # Closing: Use file.close() or with open(...) as file: for automatic closure.
    # Reading: Use file.read(), file.readline(), or iteration.
    # Writing: Use file.write(data).
    # writelines(lines): Writes a list of strings to the file.
    # Types: Text (human-readable) vs. binary (machine-readable).
    # append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
    # create (x): This mode creates a file and gives an error if the file already exists.
    # text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. 
                # There is no difference between r and rt or w and wt since text mode is the default. 
                # The default mode is 'r' (open for reading text, synonym of 'rt' ).
    # binary (b): used to handle binary files (images, pdfs, etc).

# Other points:

    # Absolute paths: Start from the root directory (e.g., /path/to/file.txt).
    # Relative paths: Navigate from the current working directory (e.g., data/file.txt).
    # os.chdir(): Change the working directory temporarily.
    # with statement: Ensures proper file closing even with exceptions.
    # Binary vs. text: Use appropriate mode ("rb" for reading binary).
    # Error handling: Check for exceptions like FileNotFoundError.
    # pathlib library: Offers convenient path handling and manipulation.

# Additional notes:

    # File operations can be used for data persistence, configuration, logging, etc.
    # Different modes exist for exclusive access, appending, and more.
    # Consider using context managers or exception handling for safe file operations.

f = open('D:\Programing Code\python\MISSION_PY\level-9\data\mytext.txt','r')
# print(f)
data = f.read()
print(data)
f.close()

a = open('D:\Programing Code\python\MISSION_PY\level-9\data\mytext2.txt','w')
a.write("Hi \nThis file is created by python program")
a.close()
a = open('D:\Programing Code\python\MISSION_PY\level-9\data\mytext2.txt','r')
data = a.read()
print(data)
a.close()

