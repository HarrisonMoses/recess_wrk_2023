# if statement
x = 4
y = 0
if (x>y):
    print("x is larger than y")
# if-else statement
if (x>y):
    print("x is larger than y")
else:
    print("y is larger than x")
# if-elif-else statement
if (x>y):
    print("x is larger than y")
elif (x==y):
    print("x is equal to y")
else:
    print("y is larger than x")
    
#while loop
while True:
    print("Hey there!")
    break

# for loop
sequence = [1,2,3,4,5,6]
for variable in sequence:
    print(variable)

# Class declaration
class Animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("Animal eats")
# Object creation
animal = Animal("Max", 20)
animal.name
animal.eat()
#Inheritance
class Animal:
    def eat(self):
        print("Animal eats")
class Dog(Animal):
    def walk(self):
        print("Animal walks")
dog = Dog()
dog.eat()

# Polymorphism
class Animal:
    def eat(self):
        print("Animal eats")
class Dog(Animal):
    def eat(self):
        print("Dog eats")
class Goat(Animal):
    def eat(self):
        print("Goat eats")
dog = Dog()
goat = Goat()
dog.eat()
goat.eat()

