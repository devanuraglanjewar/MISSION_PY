# if-else statement
# "if-else" is a basic conditional structure. 
# It allows the program to make decisions based on specific conditions.
# Example:
a = int(input("Enter your age\n"))
if(a>18):
    print("you can drive")
else:
    print("you cannot drive")

# conditional operators
# <, >, >=, <=, !=
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)

# elif
# The else clause of an if-statement may be followed by one or more elif clauses and a final else clause.
# Example:
x = int(input("Enter number between 0 - 4 \n"))
if (x == 0):
    print ("You entered 0")
elif (x == 1):
    print ("You entered 1")
elif (x == 2):
    print ("You entered 2")
elif (x == 3):
    print ("You entered 3")
elif (x == 4):
    print ("You entered 4")
else:
    print("Enter valid number")

# Nested if
# You can use nested if statements in Python as well. Here's how it works:
y = int(input("Enter number between 5 - 9 \n"))
if y>=5:
    if y<=6:
        print("You entered 5 or 6")
    elif y<=7:
        print("You entered 7")
    elif y<=8:
        print("You entered 8")
    else:
        print("You entered 9")
else:
    print("Invalid input")

# Match case statement
# Example
a = int(input("Enter the number 0 - 3\n"))
match a:
    case 0:
        print("you entered 0")
    case 1:
        print("you entered 1")
    case 2:
        print("you entered 2")
    case 3:
        print("you entered 3")
    case _ if isinstance(a, int) and (a>3 or a<0):
        print("invalid entry")