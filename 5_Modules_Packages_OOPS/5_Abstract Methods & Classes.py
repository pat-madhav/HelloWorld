from abc import ABC, abstractmethod


# defining Abstract Class
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

# CANNOT create objects
# com = Computer()  # This will throw an error
# com.process()


# We can create SUB-CLASS of an Abstract Class
class Laptop(Computer):
    def process(self):
        print('Process running...!')

# Objects can be defined from SUB-CLASSes of Abstract Class
#   Only when an NON-ABSTRACT method is defined in it
com1 = Laptop()
com1.process()
