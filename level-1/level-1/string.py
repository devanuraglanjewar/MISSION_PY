# what is strings in python
# Strings are sequences of characters. 
# In Python, they can be defined using either single or double quotes and can contain any character including letters, numbers, special
# In Python, we can create a string using single or double quotes.

string1 = 'Anurag'
print(type(string1)) # type function use to print the type of data

print("Hello, " + string1)

# multiline string
# it define as triple sinle quote or double quote (''') or(""")
# example:
intro = '''Hi,
I am Anurag,
i am software developer'''
print(intro)

# In python the string is like a array of characters it starts with 0.
name = 'anurag'
print("The first character of my name is: ", name[0])
print("The second character of my name is: ", name[1])
print("The third character of my name is: ", name[2])
print("The fourth character of my name is: ", name[3])
print("The fifth character of my name is: ", name[4])
print("The sixth character of my name is: ", name[5])

# slicing of string
print("\nslicing of string")
print(name[0:4])
print(name[-4:-1])
print('My name is :', name[:6], '-', name[-1])
print('My name is :', name[:6], '-', name[-2])


# Methods in string
# len() - Returns the length of a string.
# example:
s = 'hello world'
print('\nLength of s :',len(s))

# upper() - Converts a string to uppercase.
# example:
print('\nUpper case string :',s.upper())

# lower() - Converts a string to lowercase.
# example:
print('\nLower case string :',s.lower())

# title() - Converts the first letter of each word in a string to uppercase.
# example:
print('\nTitle case string :', s.title())

# capitalize() - Converts the first letter of a string to uppercase.
# example:
print('\nCapitalized string :', s.capitalize())

# strip() - Removes whitespace from the beginning and end of a string.
# example:
print('\nStripped string :', s.strip())

# lstrip() - Removes whitespace from the beginning of a string.
# example:
print('\nLeft stripped string :', s.lstrip())

# rstrip() - Removes whitespace from the end of a string.
# example:
print('\nRight stripped string :', s.rstrip())

# find() - Finds the first occurrence of a substring in a string.
# example:
sub_str = "lo"
print('\nFirst occurrence of sub-string :', s.find(sub_str))

# rfind() - Finds the last occurrence of a substring in a string.
# example:
print('\nLast occurrence of sub-string :', s.rfind(sub_str))

# index() - Finds the first occurrence of a substring in a string and raises an exception if the substring is not found.
# example:
print('\nCount of sub-string :', s.count(sub_str))

# rindex() - Finds the last occurrence of a substring in a string and raises an exception if the substring is not found.
# example:
print('\nIndex of sub-string :', s.index(sub_str))

# replace() - Replaces all occurrences of a substring in a string with another substring.
# example:
new_str = s.replace('hello','python')
print('\nOld string is hello world and replaced string is :', new_str)

# split() - Splits a string into a list of substrings based on a delimiter.
# example:
words = s.split(" ")
print('\nSplit words are :', words)

# join() - Joins a list of substrings into a single string using a delimiter.
# example:
joined_str = "-".join(words)
print('\nJoined words are :', joined_str)

# format() - Formats a string using a format string.
# example: 
formatted_str = '{} {}'.format('Hello', 'World')
print('\nFormatted string is :', formatted_str)
