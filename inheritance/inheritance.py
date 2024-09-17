
"""
Inheritance:
    Inheritance allows us to define a class that inherits all the methods and properties from another class.

    Parent class:
        is the class being inherited from, also called base class

    Child class:
        is the class that inherits from another class, also called derived class.
"""
from symtable import Class


#Prent class
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        print(f"Person full name is : {self.first_name} {self.last_name}")


person_object = Person('jhon', 'vim')
person_object.display()

#Child class
class Student(Person):
    pass

student_object = Student('Alice', 'kim')
student_object.display()


"""
    In our child class, we don't have any methods or properties,yet we are able to achieve display.
    This is an simple example of how we can use inheritance to leverage the behaviors of the parent class.
"""



"""
    When you add the __init__() function, the child class
    will no longer inherit the parent's __init__() function.
    
    Note: 
        The child's __init__() function overrides
        the inheritance of the parent's __init__() function.
"""



class Teacher(Person):
    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name)

teacher_object = Teacher('Min', 'Miny')
teacher_object.display()

"""
    To keep the inheritance of the parent's __init__() function,
    add a call to the parent's __init__() function:
    
    or 
    
    Use the super() Function:
        super() function, you do not have to use the name of the parent element,
        it will automatically inherit the methods and properties from its parent.
"""


class Teacher(Person):
    def __init__(self, first_name, last_name, year):
        super().__init__(first_name, last_name)
        self.retired = year

    def show(self):
        print(f"Mr {self.first_name} {self.last_name} was retired {self.retired}")


teacher_object = Teacher('Thomas', 'Paul', 2020)
teacher_object.display()

teacher_object.show()

"""
    Here we add another parameter (year) in the __init__() function:
"""