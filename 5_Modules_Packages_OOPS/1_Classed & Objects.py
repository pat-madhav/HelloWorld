class Vehicle:
    """
    "object" = "instance" =~ car1/car2  # in our ex.
    "Constructor" => "__init__" ; It constructs the object
        > Constructor method is always run when an object/instance is created
    "Initialization" = defining __init__ at the beginning of each Class
    Params other than "self" in "__init__" = They're needed to construct an object properly
    "self" = Represents the instance itself
    "instance attributes/variables" = vehicle_make, vehicle_body, etc
        >New instance attribs/vars can be created out of class attribs/vars
            =~ car1.color = 'purple'  # in our ex.
        >XXX Never create instance attribs/vars that the class doesn't have
            =~ car1.engine = 'v6'
    "Class attribute/variable" = independent of a given instance =~ "color"  # in our ex.
        > All instances/objects of the class are automatically going to inherit these
        > These vars can be referred as they aren't inside a method =~ car1.color
        > XXX This shouldn't be changed even though Python allows (Bad practice!)
        > Should be defined immediately under the class def
        > usually meant to be STATIC
    """

    color = 'red'
    vehicle_count = 0

    # Constructor method - Gets run every time an object/instance is created
    def __init__(self, make, body_type):
        self.vehicle_make = make
        self.vehicle_body = body_type
        '''
        since this method runs every time an object is initialized
        Defining the counter here
        '''
        Vehicle.vehicle_count += 1

    # Other methods
    def get_vehicle_count(self):
        return Vehicle.vehicle_count


car1 = Vehicle('Tesla', 'Truck')
car2 = Vehicle('Toyota', 'compact')
# car1 and car 2 are objects(instances) of a Vehicle class
# 'self' keyword inside class definition is for the instances (car1 and car2 in our ex.)

print(car1.vehicle_make)
# car1 is an "Object" which is an instance of class "Vehicle"

print(car2.vehicle_body)
# car2 is an "Object" which is an instance of class "Vehicle"

print(type(car1))  # This is a class type object

# creating more objects/instances for the class Vehicle
car3 = Vehicle('BMW', 'sedan')
car4 = Vehicle('Audi', 'SUV')
car5 = Vehicle('Ducati', 'motorcycle')

# Never change class variables outside the class
###### Vehicle.color = 'green'

# New instance attribute
car1.color = 'purple'

car1.engine = 'v6'

