# f_string is the newly introduce feature of python 3.6 
# this feature allows you to add variable into a string
# example:
letter = "hello my name is {} and i am form {}"
country = "America"
name = "Anurag"

print(letter.format(name,country))

# insted of this we just have to do

print(f"hello my name is {name} and i am form {country}")