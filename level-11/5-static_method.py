# static method that dont use the self parameter (Work at class level)
# Static methods are not inherited, they belong to a class rather than an instance of a class.

class Student:
    @staticmethod  # decorator
    def college():
        print("I am in College")


# Decorator allow us to wrap another function in order to extend
# the behaviour of the wraped function, without permanently ,modifying it 