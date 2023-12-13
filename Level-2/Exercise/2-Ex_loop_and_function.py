
# --Question 1:
# --Write a program that asks the user for a sentence and then prints the sentence with each word reversed
# --(e.g., "Hello world" becomes "olleH dlrow").
def reverse_sentence(sentence):
  """
  Reverses each word in a sentence and returns the new sentence.

  Args:
    sentence: The sentence to be reversed.

  Returns:
    The sentence with each word reversed.
  """
  words = sentence.split()
  reversed_words = []
  for word in words:
    reversed_words.append(word[::-1])
  return " ".join(reversed_words)

# Get the sentence from the user
sentence = input("Enter a sentence: ")

# Reverse the sentence and print the result
reversed_sentence = reverse_sentence(sentence)
print("Reversed sentence:", reversed_sentence)


# --Question 2:
# --Write a program that prints a right triangle of asterisks using nested loops
rows = 5

for i in range(1, rows + 1):
  for j in range(1, i + 1):
    print("*", end="")
  print()


# Question 3:
# --Write a program that prints the multiplication table of all numbers from 1 to 10 using nested loops
def table_factory(j):
  for i  in range(1,11):
    print(j,"x", i, "=", j*i)

for a  in range (2,11):
  table_factory(a)
  print()


# Question 4:
# --Write a program that takes a list of numbers and prints the sum of all the even numbers

def getinput():
  nums = input("Enter space separated numbers: ")
  lst = [int(num) for num in nums.split()]
  print(lst)
  return lst
lst = getinput()
sum_even = 0
for num in lst:
  if num % 2 == 0:
    sum_even += num
print("Sum of even numbers is ", sum_even)


# Question 5:
# --Write a program to convert binary to decimal number
k = int(input("enter any binary number: "))
s=0
n=0
while(k!=0):
  d = k%10
  s=s+d*pow(2,n)
  k=k/10
  n=n+1

print("=>",s)
