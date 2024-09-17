"""
Encapsulation:

    Encapsulation is a core concept in object-oriented programming (OOP)
    that involves restricting direct access to some of an object's attributes or methods
    and providing controlled access through public methods.

    This helps protect the internal state of an object and ensures
    that it is used in a controlled manner.

Access specifiers:
    In Python, encapsulation is typically achieved using access specifiers.

    ****
        Although Python does not have strict access specifiers like some other languages
        (e.g., public, private, protected in Java)
    ****

It uses conventions to indicate the intended level of access:

    Public Attributes and Methods:
        Accessible from outside the class. No special notation is used.

    Protected Attributes and Methods:
        Intended to be accessible only within the class and its subclasses.
        This is indicated by a single underscore (_).

    Private Attributes and Methods:
        Intended to be accessible only within the class itself.
        This is indicated by double underscores (__).
"""

#Example of Public Attributes and Methods:
class Person:
    def __init__(self, name):
        self.name = name # Public attribute

    def show_name(self):
        print(f"Person name is {self.name}") # Public method

person_object = Person('john')
person_object.show_name() # Accessible


# Protected Attributes and Methods:
class Person:
    def __init__(self, name):
        self._name = name # Protected attribute

    def _show_name(self):
        print(f"Person name is {self._name}") # Protected method

#usage
person_object = Person('Babu')
person_object._show_name() # Accessible
print(person_object._name) # Accessible, but should be used with caution

class Child(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        self._show_name() # Accessing protected method of the parent class
        print(f"Child age is {self.age}")

child_object = Child('rinu', 10)
child_object.display() # Accessible
child_object._show_name() # Accessible, but should be used with caution
print(child_object._name) # Accessible, but should be used with caution


#Example of Private Attributes and Methods:

class Parent:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def __show_name(self):
        print(f"Parent name is {self.__name}")  # Private method

    def reveal_name(self):
        self.__show_name()  # Public method that accesses the private method
        print(f"Parent name is {self.__name}")  # Public method that accesses the private attribute

parent_object = Parent('anu')
parent_object.reveal_name()
# parent_object.__show_name() Raises AttributeError
# print(parent_object.__name) Raises AttributeError

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age  # Public attribute

    def display(self):
        # self.__show_name()  # Raises AttributeError
        print(f"Child age is {self.age}")
        # print(self.__name)  # Raises AttributeError

child_object = Child("Alice", 10)
child_object.display()
# child_object.__show_name()  # Raises AttributeError


"""
If we dont use the access specifires it will show the error:
    # Encapsulated access to the private attribute
    AttributeError: 'Person' object has no attribute 'name'
"""
