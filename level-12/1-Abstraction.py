# abstraction is the 
# Hiding the implementation details of class and only show the essential features to the user.

class car:
    def __init__(self):
        self.brk = False       #hiding
        self.acc = False       #hiding
        self.clutch = False    #hiding

    def start(self):
        self.acc = True         #hiding
        self.clutch =True       #hiding
        print("Car  started")

car1 = car()
car1.start()

# here we are heiding information which is not important to the user such as "brk, acc, clutch"