# A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

# A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.


class men:
    def __init__(self,n,a,o): # it is a cunstroctor
        self.name =n
        self.age = a
        self.occupation= o 

    def display(self):
        print( f"\n{self.name} is a {self.occupation} and age is {self.age}" ) 
    

a = men("Anurag","20", "software developer") # class
a.display() # method

b = men("jay","22","data analyst")      #  another object of the same class
b.display() # calling b's method, it displays attributes of b not a's



# Types of Constructors in Python
#     Parameterized Constructor
#     Default Constructor

#     Parameterized Constructor in Python
    #     When the constructor accepts arguments along with self, it is known as parameterized constructor.

    #     These arguments can be used inside the class to assign the values to the data members.

#Example:
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group
obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")

# Output:
    # Crab belongs to the Crustaceans group.



# Default Constructor in Python
    # When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.

# Example:
class Details2:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details2()

# Output:
# animal Crab belongs to Crustaceans group