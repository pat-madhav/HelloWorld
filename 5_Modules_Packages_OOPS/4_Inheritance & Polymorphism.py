# ------------------------------------
# Polymorphism
# ------------------------------------
class Vehicle:
    """
    A vehicle can be anything
        Plane
        Car
        Truck
        Boat
        Motorcycle
    """
    vehicle_count = 0

    # Constructor
    def __init__(self, make, body_type):
        self.vehicle_make = make
        self.vehicle_body = body_type
        Vehicle.vehicle_count += 1

    # ----------------
    # Other method 1
    def get_vehicle_count(self):
        return Vehicle.vehicle_count

    # Other method 2
    def drive(self):
        print('Vehicle driving...')


# ------------------------------------
# Demonstrating INHERITANCE
# ------------------------------------
# Creating a specific vehicle class
# this is a SUB-CLASS of Vehicle
class Truck(Vehicle):
    """
    This is a child class of Vehicle

    Since we are passing a class to Truck
    It is "inheriting" all the variables & methods of
        # == This means that all Truck instances will be a kind of Vehicle
        # All instances of "Truck" will require the params req'd by Vehicle class

    """
    # Overriding a method from a parent class
    # Polymorphism - Methods of parent class can be redefined
    def drive(self):
        print('Truck driving...')


# ------------------------------------
# Creating instances/objects of class - Truck

# Wrong object creation
# truck1 = Truck()

# Correct object creation
truck2 = Truck('Chevy', 'big rig')
truck3 = Truck('Ford', 'small rig')

print(truck3.get_vehicle_count())
print(truck2.drive())


# ------------------------------------
# Creating instances/objects of class - Motorcycle
class Motorcycle(Vehicle):
    def drive(self):
        print('Motorcycle driving fast...')


moto1 = Motorcycle('Ducati', '899')

# ------------------------------------
# Testing Polymorphism
# ------------------------------------
car = Vehicle('Tesla', 'Model Y')
truck = Truck('Tesla', 'Cybertruck')
moto = Motorcycle('Ducati', '899')

# ------------------------------------
# Ways of calling objects
# ------------------------------------
# 1
for v in [car, truck, moto]:
    v.drive()

# 2
def perform_drive(veh_obj):
    veh_obj.drive()

print('\n')
perform_drive(car)
perform_drive(truck)
perform_drive(moto)