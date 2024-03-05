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


car1 = BMW()

print(type(car1))  # <class '__main__.BMW'>
print(isinstance(car1, car))   # True
print(car1.start())