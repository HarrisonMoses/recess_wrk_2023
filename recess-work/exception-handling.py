#handling a specific exception
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

#handling multiple exceptions
try:
    file = open("myfile.txt", "r")
    data = file.read()
    print("File content:", data)
    file.close()
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied to open the file.")

#else and finally
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Error: Invalid input. Please enter a number.")
else:
    print("Result:", result)
finally:
    print("Exception handling complete.")

#rasing a builtin exception
def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return num1 / num2

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print("Error:", str(e))

#Creating and raising a custom exception:
class InvalidInputError(Exception):
    pass

def calculate_square_root(num):
    if num < 0:
        raise InvalidInputError("Input cannot be negative.")
    return num ** 0.5

try:
    result = calculate_square_root(-5)
except InvalidInputError as e:
    print("Error:", str(e))

