

"""
    polymorphism:
        The word "polymorphism" means "many forms",
        and in programming it refers to methods/functions/operators with the same name
        that can be executed on many objects or classes.
"""

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"{self.brand}-{self.model} Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"{self.brand}-{self.model} Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"{self.brand}-{self.model} Fly!")


car_object = Car("Ford", "Mustang")
boat_object = Boat("Ibiza", "Touring 20")
plane_object = Plane("Boeing", "747")



for obj in (car_object, boat_object, plane_object):
    obj.move()

"""
    Output:
        Ford-Mustang Drive!
        Ibiza-Touring 20 Sail!
        Boeing-747 Fly!
        
        Look at the for loop at the end. 
        Because of polymorphism we can execute the same method for all three classes.
        
"""

# Inheritance Class Polymorphism

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"{self.brand} {self.model} Move!")


class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
      def move(self):
        print("Fly!")

car_object = Car("Ford", "Mustang") #Create a Car object
boat_object = Boat("Ibiza", "Touring 20") #Create a Boat object
plane_object = Plane("Boeing", "747")

for x in (car_object, boat_object, plane_object):
    x.move()
    print(x.brand)
    print(x.model)

"""
    output:
        Ford Mustang Move!
        Ford
        Mustang
    
    Child classes inherits the properties and methods from the parent class.
    In the example above you can see that the Car class is empty,
    but it inherits brand, model, and move() from Vehicle.
    
    
    output :
        Sail!
        Ibiza
        Touring 20
        Fly!
        Boeing
        747
        
    The Boat and Plane classes also inherit brand, model, 
    and move() from Vehicle, but they both override the move() method.
    
    Because of polymorphism we can execute the same method for all classes.
"""