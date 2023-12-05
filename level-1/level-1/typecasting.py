# Typecasting is the conversion of one datatype into other datatype.
# In Python, typecasting can be done using built-in functions like int(), float(), str() etc.

a = "1" # it's a string
b = "2" # it's a string
c = 2.36
d = 1.05
# lets convert string into int
print(int(a) + int(b)) 

# the value should be valid for typecasting
print(float(c) + float(d))
# but if we try to cast invalid values then python will raise an error

# so there are two type of typecasting in python
# 1. implicit typecasting (python does this automatically when required)
# example:
x = 4.7
y = x + 2  
print("Implicit Casting Example :", y)

# example:
x = 4
y = x / 2
z = y * 2
print("Implicit Casting Example : ", z)


# 2. explicit typecasting (using function or method) it happens by the developers
# example:
x = 7
y = 9
sum_of_numbers = x + y
print("Explict Casting Example : ", sum_of_numbers)