#medthod are the function which belongs to objects
class students:

    def welcome(self,collage): # method
        self.coll = collage
        print(f"welcome to {self.coll}")
    
a=students()
a.welcome("IIT Mumbai")