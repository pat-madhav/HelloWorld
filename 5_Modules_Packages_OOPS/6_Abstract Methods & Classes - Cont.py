from abc import ABC, abstractmethod


# defining Abstract Class
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

# CANNOT create objects
# com = Computer()  # This will throw an error
# com.process()


# Laptop is a kind of Computer
class Laptop(Computer):
    def process(self):
        print('Process running...!')


class Whiteboard:
    def text(self):
        print('Brainstorming on whiteboard.!')


class Programmer:
    def work(self, com_obj):  # com = Programmers need computer to work
        print('Solving problems...!')
        com_obj.process()


# defining objects of PARENT-CLASS and passing obj to SUB-CLASS
com1 = Laptop()
p1 = Programmer()
p1.work(com1)

com2 = Whiteboard()
p1.work(com2)  # this will fail (AttributeError); com2 is an object of Whiteboard which doesn't have process()
# To resolve above AttributeError - We can make Whiteboard a form of Computer
#   Doing this will