

"""
Abstraction:
    Abstraction is the concept of hiding complex implementation details
    and showing only the essential features.

    **
        Python doesn't enforce strict abstraction like some languages,
        But you can create abstract classes using the abc module.
    **
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, shape_name):
        self.shape_name = shape_name

    @abstractmethod
    def draw(self):
        pass

"""
    Shape which would contain the blueprint for specific shapes to follow
    This class will provide the methods that are needed to be implemented 
    by its child classes for specific shapes.
"""

#child class inherit Shape
class Circle(Shape):
    def __init__(self):
        super().__init__("circle")

    def draw(self):
        print(f"Drawing a {self.shape_name}")

circle_object = Circle()
circle_object.draw()

# draw another shape, say a Triangle.
class Triangle(Shape):
    def __init__(self, shape):
        super().__init__(shape)

    def draw(self):
        print(f"Drawing a {self.shape_name}")

triangle_object = Triangle('triangle')
triangle_object.draw()

"""
    Similarly, we can create as many specific shape classes as we want,
    with the Shape class being the main abstract class.
"""

"""

Why Use Abstract Base Classes?

    Abstract classes are used to create a blueprint of our classes
    as they don't contain the method implementation. 
    This is a very useful capability, 
    especially in situations where child classes should provide their own separate implementation. 
    Also, in complex projects involving large teams and a huge codebase, 
    It is fairly difficult to remember all the class names.
    
Importance of Abstract Classes:
    The importance of using abstract classes in Python is that if our subclasses don’t follow that blueprint, 
    Python will give an error. 
    Thus we can make sure that our classes follow the structure 
    and implement all the abstract methods defined in our abstract class.
    
    ** 
        We do not define the draw() method; instead, we define a draw_circle() method,
        TypeError will shows.
    **
    
"""