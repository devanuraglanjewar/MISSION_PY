
# 1. String Manipulation:
# --Question 1:
# --Write a program that reads a text file line by line and prints each line in reverse order.
with open("Hello.txt", "r") as file: # it use for reading lines
  for line in reversed(file.readlines()):
    print(line.strip()[::-1])
file.close()



# --Write a program that asks the user for a sentence and then prints the sentence with each word reversed
# --Write a program that reads a text file and counts the number of times each word appears in the file

# 2. Nested Loops:
# --Write a program that prints a right triangle of asterisks using nested loops
# --Write a program that prints the multiplication table of all numbers from 1 to 10 using nested loops
# --Write a program that simulates a game of tic-tac-toe using nested loops

# 3. Iterating over Sequences
# --Write a program that takes a list of numbers and prints the sum of all the even numbers
# --Write a program that takes a list of strings and prints the longest string in the list
# --Write a program that takes a list of numbers and prints the average of the numbers

# 4. List Comprehensions
# --Write a program that squares all the numbers in a list using list comprehensions
# --Write a program that filters out all the odd numbers from a list using list comprehensions
# --Write a program that combines two lists into a single list using list comprehensions

# 5. Advanced Loop Techniques
# --Write a program that uses the `enumerate` function to print the index and value of each item in a list
# --Write a program that uses the `zip` function to combine two lists into a list of tuples
# --Write a program that uses the `map` function to apply a function to each item in a list

# Bonus
# --Write a program that reads a CSV file and prints the sum of all the numbers in the second column
# --Write a program that takes a string as input and checks if it is a valid email address
# --Write a program that uses recursion to calculate the factorial of a number