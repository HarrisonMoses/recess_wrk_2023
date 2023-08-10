#A program that prints a shopping receipt

#Create product list with their prices
item1, item1_price = "Bread", 2500
item2, item2_price = "Sugar", 5000
item3, item3_price = "Milk", 3000
item4, item4_price = "Salt", 500
item5, item5_price = "TeaLeaves", 1000

#Create company name and address
company_name = "AKA Retail Shop"
company_address = "Wilson street, plot 27"
company_city = "Kampala, Uganda"

#declare thank you message
th_message = "Thank you for shopping with us today!."
ds_message = "Goods once sold are not returnable."

#create a top border
print("\t\tRECEIPT")
print("*" *50)

#print company name and address first using format
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address))
print("\t\t{}".format(company_city))
 
#print a line between sections
print("*"*50)
print("\t Item \t Item Price")

#print statement for each product
print("\t{}\t\t shs{}".format(item1.title(),item1_price))
print("\t{}\t\tshs{}".format(item2.title(),item2_price))
print("\t{}\t\tshs{}".format(item3.title(),item3_price))
print("\t{}\t\tshs{}".format(item4.title(),item4_price))
print("\t{}\tshs{}".format(item5.title(),item5_price))

#print a line between sections
print("="*50)

#print out header for total section
print("\t\t\t Total ")

total = item1_price + item2_price +item3_price+item4_price+item5_price
print("\t\t\tshs{}".format(total))
print("="*50)

#output thank you message
print("\n\t{}".format(th_message))
print("\n\t{}\n".format(ds_message))

#create bottom border
print("*"*50)


# #demonstrating abstraction
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def make_sound(self):
#         pass

#     def show_info(self):
#         print(f"I am {self.name}.")
#         self.make_sound()

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")

# # Creating objects
# cat = Cat("Whiskers")
# dog = Dog("Buddy")

# # Calling the methods
# cat.show_info()
# dog.show_info()

# #Demonstrating inheritance
# # Define the superclass
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print("An animal speaks.")


# # Define a subclass that inherits from Animal
# class Dog(Animal):
#     def __init__(self, name, breed):
#         # Call the superclass's initializer to set the name
#         super().__init__(name)
#         self.breed = breed

#     def speak(self):
#         print("Dog barks.")


# # Create an instance of the superclass
# animal = Animal("Generic Animal")
# animal.speak()

# # Create an instance of the subclass
# dog = Dog("Buddy", "Golden Retriever")
# print(dog.name)  # Inherits the 'name' attribute from Animal
# print(dog.breed)  # Specific to the Dog class
# dog.speak()  # Overrides the speak() method defined in Animal

# #Polymorphism can be achieved through method overriding and method overloading
# #method overriding
# class Shape:
#     def area(self):
#         pass
#     def perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width
#     def perimeter(self):
#         return 2*(self.length + self.width)

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius**2
#     def perimeter(self):
#         return 2* 3.14 * self.radius

# # Create instances
# rectangle = Rectangle(5, 10)
# circle = Circle(7)

# # Call the area and perimeter method on both objects
# print(rectangle.area())  # Output: 50
# print(rectangle.perimeter())
# print(circle.area())     # Output: 153.86
# print(circle.perimeter())

# #method overloading
# #Python does not support method overloading in the same way as some other languages,
# #but you can achieve a similar effect using default arguments or variable-length arguments.
# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c

# calculator = Calculator()
# print(calculator.add(2, 3))         # Output: TypeError: add() missing 1 required positional argument: 'c'
# print(calculator.add(2, 3, 4))      # Output: 9
# '''In this example, we define two add() methods in the Calculator class, one with two parameters and the other with three parameters.
# However, Python does not support true method overloading based on the number of arguments alone.
# When we try to call calculator.add(2, 3), it raises a TypeError because the second add() method expects three arguments.
# Only when we call calculator.add(2, 3, 4) with three arguments, it correctly executes the appropriate method.'''

