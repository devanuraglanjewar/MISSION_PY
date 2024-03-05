# Inheritance
# When one class (chlid/derived) drives the properties & methods of another class(parent/base), it is called inheritance
#Example 1
class car:
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped.")
    
class BMW(car):
    def __init__(self,name):
        self.name = name


car1 = BMW("x1")

print(type(car1))  # <class '__main__.BMW'>
print(isinstance(car1, car))   # True
print(car1.start())
        

# their are 3 types of  inheritance 
# 1] Single Inheritance : when a class inherits from one parent class .
# --> Example 1 is the example of single inheritance


# 2] multi-level  inheritance : when a class inherits from more than one classes.
#  Example 2
class car:
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped.")

class brands(car):
    def __init__(self,brand) :
        self.brand = brand

class bmw(brands):
    def __init__(self,name):
        self.name = name


car1 = BMW("x1")
car1.start()



# 3] Multiple Inheritance : when a class inherits from more than two classes.
class A: # parent class
    varA = "welcome to class A"

class B: # parent class
    varB = "Welcome to class B" 

class C(A,B):# child class
    varC = "welcome to class C" 

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)