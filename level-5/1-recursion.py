# Recursion is a process in which a thing is defined in terms of itself, leading to an infinite regress or circular reference.
# It's like a set of Russian dolls, where each doll contains a smaller version of itself, and so on. 
# In simpler terms, it's when something is nested within itself.

# Example
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1) #calling function into the same function.
    
print(factorial(1))

# Example no 2:
# let's create Fibonacci series using recursion.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Get the number of terms from the user
nterms = int(input("How many terms? "))

# Check for non-positive input
if nterms <= 0:
    print("Please enter a positive integer.")
else:
    # Print the first n terms of the Fibonacci series
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(fibonacci(i))
