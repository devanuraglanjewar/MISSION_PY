# del keyword
# it use to delete object properties or object itself

class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("anurag")
print(s1.name)

del s1.name # this will delete name  property of s1 object
del s1 #this will delete complete object

print(s1.name)

# output :
#   NameError: name 's1' is not defined (because it is deleted)



# Private(like) attribute and methood
# private attribute & method are ment to be used only within the class and are not accessible form outside the class.

class Student:
    def __init__(self,name):
        self.__name = name # (to make private you just need to add "__" two underscore)

s1 = Student("anurag")
print(s1.name)

# now the name is private so se cannot accsess name out of class
# but we can access through _Student__
print(s1._Student__name)