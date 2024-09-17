

"""
Classes and Objects:

    Class : is  blueprint for creating objects.
    It defines the properties (attributes) and behaviors (methods)
    that the objects created from it will have.

    Object : is an instance of a class that holds actual data.
"""

#simple example

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving")

car_object = Car('bmw', 'x1')
car_object.drive()
#output
    #bmw x1 is driving

car_object.brand = 'benz'
car_object.model = 's1'
car_object.drive()
#output
    #benz s1 is driving

"""
Understand the built-in __init__() function:

    All classes have a function called __init__(),
    which is always executed when the class is being initiated.
"""

"""
Understand self keyword:

    The self parameter is a reference to the current instance of the class, 
    and is used to access variables that belong to the class.
    
    It does not have to be named self , you can call it whatever you like,
    but it has to be the first parameter of any function in the class:
"""
