# what is loops 
# loop is a block of code that repeats itself until a certain condition is met.
# there are two types of loops in python: for and while loops

# for loop
# Example 1:
name = 'anurag'
for i in name:
    print(i)

# Example 2:
colors = ["Red", "blue", "green", "yellow"]
for color in colors:
    print(color)

# range function
# the range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (also default), and stops
# Example 1:
for l in range(10):
    print(l)

# Example 2:
for k in range(1,20):
    print(k)

# Example 3:
for h in range(0,21,2):      #3rd argument create a gap between numbers
    print(h) 

# while loop
# Example 1:
num = 5
while num > 0:
    print("Hello",num)
    num -= 1

# Example 2:
count = 0
while count < 6:
    print('I love Python',count)
    count += 1