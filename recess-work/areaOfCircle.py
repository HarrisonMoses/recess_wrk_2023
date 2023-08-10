'''
pi = 3.14
def areaOfCircle(r):
    return pi*r*r
r = int(input("Enter radius  "))
x = areaOfCircle(r)
print(f"Area of cicle is {x}")


for i in range(1,6):
    for j in range(0,i):
        print(i, end=" ")
print('')

letters = "Amanda"
for letter in letters:
    print(letter)


greeting = 'Hello, world!'
new_greeting = 'J' + greeting[:]
print(new_greeting)
print(greeting.swapcase().isupper())
'''
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)

print(string.hexdigits) 
print(string.whitespace)
print(string.punctuation)
