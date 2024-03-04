# create student class that takes name & marks of 3 subject as arguments in constructor,
# then create a methodto print the avrage

class Student:
    # constructor
    def __init__(self,name,sub1,sub2,sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    # method    
    def avrage(self):
        av = self.sub1+self.sub2+self.sub3/3
        print(f"{name}'s Average Mark is {av}")


# main program
name=input("Student name: ")
sub1 = int(input("Marks of subject 1: "))
sub2 = int(input("Marks of subject 2: "))
sub3 = int(input("Marks of subject 3: "))

# calling method and class
a = Student(name,sub1,sub2,sub3)
a.avrage()


