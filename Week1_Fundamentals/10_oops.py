# ==========================================================
#            OBJECT ORIENTED PROGRAMMING (OOP) IN PYTHON
# ==========================================================

"""
What is OOP?
------------
Object-Oriented Programming (OOP) is a programming style that organizes
code into Classes and Objects.

Class  -> Blueprint
Object -> Real-world instance created from the blueprint

Example:
Class = Car
Objects = BMW, Tesla, Audi
"""

# ==========================================================
# 1. Creating a Class and Object
# ==========================================================

class Student:
    pass

# Creating objects
student1 = Student()
student2 = Student()

print("Object 1:", student1)
print("Object 2:", student2)

print("-" * 50)


# ==========================================================
# 2. Constructor (__init__)
# ==========================================================

"""
Constructor automatically runs when an object is created.

Syntax:
def __init__(self):
"""

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Aman", 20)

print("Name:", s1.name)
print("Age:", s1.age)

print("-" * 50)


# ==========================================================
# 3. Instance Variables
# ==========================================================

"""
Variables that belong to each object.
"""

class Laptop:

    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram


l1 = Laptop("ASUS", "16GB")
l2 = Laptop("HP", "8GB")

print(l1.brand, l1.ram)
print(l2.brand, l2.ram)

print("-" * 50)


# ==========================================================
# 4. Methods
# ==========================================================

"""
Methods are functions inside a class.
"""

class Dog:

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "is barking.")


dog = Dog("Tommy")
dog.bark()

print("-" * 50)


# ==========================================================
# 5. self Keyword
# ==========================================================

"""
self refers to the current object.
"""

class Mobile:

    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("Brand:", self.brand)


m = Mobile("Samsung")
m.show()

print("-" * 50)


# ==========================================================
# 6. Class Variables
# ==========================================================

"""
Shared among all objects.
"""

class Employee:

    company = "Google"

    def __init__(self, name):
        self.name = name


e1 = Employee("Rahul")
e2 = Employee("Aman")

print(e1.name, "-", Employee.company)
print(e2.name, "-", Employee.company)

print("-" * 50)


# ==========================================================
# 7. Instance Method
# ==========================================================

class Car:

    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Car Brand:", self.brand)


c = Car("BMW")
c.display()

print("-" * 50)


# ==========================================================
# 8. Class Method
# ==========================================================

class School:

    school_name = "ABC School"

    @classmethod
    def change_name(cls, new_name):
        cls.school_name = new_name


print(School.school_name)

School.change_name("XYZ School")

print(School.school_name)

print("-" * 50)


# ==========================================================
# 9. Static Method
# ==========================================================

"""
Static methods don't use self or cls.
"""

class Math:

    @staticmethod
    def add(a, b):
        return a + b


print(Math.add(10, 20))

print("-" * 50)


# ==========================================================
# 10. Inheritance
# ==========================================================

"""
Child class inherits Parent class.
"""

class Animal:

    def speak(self):
        print("Animal speaks")


class Cat(Animal):
    pass


cat = Cat()
cat.speak()

print("-" * 50)


# ==========================================================
# 11. Method Overriding
# ==========================================================

class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Dog Barks")


d = Dog()
d.sound()

print("-" * 50)


# ==========================================================
# 12. super() Keyword
# ==========================================================

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll


s = Student("Aman", 101)

print(s.name)
print(s.roll)

print("-" * 50)


# ==========================================================
# 13. Encapsulation
# ==========================================================

"""
Private variables use __
"""

class Bank:

    def __init__(self):
        self.__balance = 5000

    def show_balance(self):
        print("Balance =", self.__balance)


b = Bank()
b.show_balance()

# print(b.__balance)   # Error

print("-" * 50)


# ==========================================================
# 14. Polymorphism
# ==========================================================

class Bird:

    def sound(self):
        print("Bird Sound")


class Sparrow(Bird):

    def sound(self):
        print("Chirp")


class Crow(Bird):

    def sound(self):
        print("Caw")


birds = [Sparrow(), Crow()]

for bird in birds:
    bird.sound()

print("-" * 50)


# ==========================================================
# 15. Abstraction
# ==========================================================

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Bike(Vehicle):

    def start(self):
        print("Bike Started")


bike = Bike()
bike.start()

print("-" * 50)


# ==========================================================
# 16. Multiple Inheritance
# ==========================================================

class Father:

    def skills1(self):
        print("Driving")


class Mother:

    def skills2(self):
        print("Cooking")


class Child(Father, Mother):
    pass


child = Child()

child.skills1()
child.skills2()

print("-" * 50)


# ==========================================================
# 17. isinstance() Function
# ==========================================================

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print("-" * 50)


# ==========================================================
# 18. Object Attributes
# ==========================================================

class Phone:

    def __init__(self, brand):
        self.brand = brand


phone = Phone("Apple")

print(phone.__dict__)

print("-" * 50)


# ==========================================================
# 19. Deleting Object Attributes
# ==========================================================

class Test:

    def __init__(self):
        self.name = "Python"


t = Test()

print(t.name)

del t.name

# print(t.name)  # Error

print("-" * 50)


# ==========================================================
# 20. Destructor
# ==========================================================

class Demo:

    def __del__(self):
        print("Object Destroyed")


d = Demo()

del d

print("-" * 50)


# ==========================================================
#                  SUMMARY
# ==========================================================

"""
OOP Concepts

1. Class
2. Object
3. Constructor (__init__)
4. self
5. Instance Variables
6. Class Variables
7. Instance Methods
8. Class Methods
9. Static Methods
10. Inheritance
11. Method Overriding
12. super()
13. Encapsulation
14. Polymorphism
15. Abstraction
16. Multiple Inheritance
17. isinstance()
18. __dict__
19. del
20. Destructor (__del__)
"""

print("End of OOP Notes")