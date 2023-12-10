# Conditionals:
# Question 1:
# Write a program that asks the user for their age and then tells them what age group they are in (e.g., child, teenager, adult).
a=int(input("Enter your age: "))
if a<10:
    print("You are an child")
elif  10<=a<=24:
    print("You are an teenager")
elif a>24:
    print("You are an adult")
else:
    print("INVALID VALUE")


# Question 2:
# Write a program that asks the user for their grade on an exam and then tells them what their letter grade is.
b = int (input ("Enter you score: "))
if 90<b<=100:
    print("Your grade is A+")
elif 80<b<=90:
    print("Your grade is A")
elif 70<b<=80:
    print("Your grade is B+")
elif 60<b<=70:
    print("Your grade is B")
elif 50<b<=60:
    print("Your grade is C+")
elif 40<b<=50:
    print("Your grade is C")
elif 35<=b<=40:
    print("Your grade is D+")
elif 20<=b<=34:
    print("Your grade is D")
elif 0<=b<=19:
    print("Your grade is F")
else:
    print("Invalid credentiall")


# Question 3:
# Write a program that asks the user for two numbers and then prints the larger of the two numbers.
print("let's compair two numbers")
c = int(input("Enter First number: "))
d = int(input("Enter second number: "))
if c>d:
    print("The greatest number is: ",c)
else:
    print("The greatest number is: ",d)


# Question 4:
# Write a program that asks the user for a word and then checks if it is a palindrome (a word that reads the same backwards as forwards).
print("Let's check if the word is a palindrome!")
word = input("Enter the word: ").lower()  # convert word to lowercase

# Check if the word is the same backwards as forwards
if word == word[::-1]:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome.")


# Question 5:
# Write a program that asks the user for a password and then checks if it meets certain criteria (e.g., minimum length, uppercase letter, lowercase letter, number).
print("--Welcome to password checker--")
p = input ("Enter the password: ")
if len(p)>=8:
    print("Password has 8 character ✅")
    if any(char.isupper() for char in p):
        print("Password has uppercase letter ✅")
        if any(char.islower() for char in p):
            print("Password has lowercase letter ✅")
            if any(char.isdigit() for char in p):
                print("Password has digit ✅")
            else:
                print("Password has no digit ❌")
        else: 
            print("Password has no lowercase letter ❌")
    else:
        print("Password has no uppercase letter ❌")
else:
    print("Password has less than 8 character ❌")
