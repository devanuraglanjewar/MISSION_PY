#Super method:
# super( )method  is used to call a method from the parent class

class car:
    def __init__(self,type) :
        self.type = type
        print(f"{self.type} type car is created")

    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped.")

class brands(car):
    def __init__(self,brand,type) :
        self.brand = brand
        super().__init__(type) # Accessing method from parent class using super()
        print("brand name is: ",self.brand)
        super().start() # Accessing method from parent class using super()

car1 = brands("BMW","Electric")