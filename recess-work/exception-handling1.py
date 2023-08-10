#handling a specific exception
def divide_numbers(a, b):
    try:
        result = a / b
        if result.imag != 0:
            raise ComplexResultError("Complex result encountered.")
        return result.real
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ComplexResultError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

class ComplexResultError(Exception):
    pass

print(divide_numbers(10, 2))      # Output: 5.0
print(divide_numbers(5, 0))       # Output: Error: Division by zero is not allowed.
print(divide_numbers(8, 3j))      # Output: Error: Complex result encountered.
print(divide_numbers(10, '2'))    # Output: An unexpected error occurred: unsupported operand type(s) for /: 'int' and 'str'


#handling multiple exceptions
def calculate_division(a, b):
    try:
        result = a / b
        print("The result of division is:", result)
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except (TypeError, ValueError):
        print("Error: Invalid input!")
calculate_division(10, 2)       # Output: The result of division is: 5.0
calculate_division(10, 0)       # Output: Error: Division by zero!
calculate_division(10, '2')     # Output: Error: Invalid input!


#else and finally
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except (TypeError, ValueError):
        print("Error: Invalid input!")
    else:
        print("Result:", result)
    finally:
        print("Finally block executed.")
divide_numbers(10, 2)     # Output: Result: 5.0 \n Finally block executed.
divide_numbers(10, 0)     # Output: Error: Cannot divide by zero! \n Finally block executed.
divide_numbers(10, '2')   # Output: Error: Invalid input! \n Finally block executed.


#rasing a builtin exception
def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty.")

    total = sum(numbers)
    average = total / len(numbers)
    return average
try:
    numbers_list = [10, 15, 20, 25]
    average_result = calculate_average(numbers_list)
    print("Average:", average_result)

    empty_list = []
    empty_average = calculate_average(empty_list)
    print("Average:", empty_average)  # This line won't be reached
except ValueError as e:
    print("Exception raised:", str(e))

#Creating and raising a custom exception:
class CustomException(Exception):
    def __init__(self, message):
        self.message = message

class Calculator:
    def divide(self, dividend, divisor):
        if divisor == 0:
            raise CustomException("Cannot divide by zero")
        return dividend / divisor
calculator = Calculator()

# Use the divide method and handle the custom exception
try:
    result = calculator.divide(10, 0)
    print("Result:", result)
except CustomException as e:
    print("Custom Exception:", e.message)


#writing to a file
try:
    file = open("output.txt", "w")  # Open file in write mode
    file.write("Hey there, i am using whatsapp")  # Write data to the file
    print("Data written to file successfully.")
    file.close()  # Close the file
except:
    print("Error: Failed to write to file.")

#appending to a file
try:
    file = open("output.txt", "a")  # Open file in append mode
    file.write("\nHello AKA.")  # Append data to the file
    print("Data appended to file successfully.")
    file.close()  # Close the file
except:
    print("Error: Failed to append to file.")

#reading line by line
try:
    file = open("output.txt", "r")  # Open file in read mode
    lines = file.readlines()  # Read all lines of the file into a list
    print("File lines:")
    for line in lines:
        print(line.strip())  # Print each line after removing trailing newline characters
    file.close()  # Close the file
except FileNotFoundError:
    print("Error: File not found.")

#read file
try:
    file = open("output.txt", "r")
    data = file.read()
    print("File content:", data)
    file.close()
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied to open the file.")
