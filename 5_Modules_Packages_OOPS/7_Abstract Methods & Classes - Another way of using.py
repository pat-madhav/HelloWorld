class Animal:
    def __init__(self, name):
        self.animal_name = name

    def eat(self):  # This method cannot be invoked directly by Animal Object
        raise NotImplementedError('Child class should be implementing this method')


# This won't work
#   Since we are defining an ABSTRACT CLASS, and it shouldn't/can't be instantiated
'''
my_dog = Animal('Loki')
my_dog.eat()
'''

# Instead, we need to use a SUB-CLASS and OVERRIDE eat()
class Monkey(Animal):
    def eat(self):
        print('Monkey eating bananas')

my_monkey = Monkey('JoJo')
my_monkey.eat()


class Bird(Animal):
    def eat(self):
        print('Birds eating seeds')

    def fly(self):
        print('Bird soaring high')

my_bird = Bird('Timmy')
my_bird.eat()
my_bird.fly()
