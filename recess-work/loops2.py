#Control Flow
# if statement:
# The if statement is used to execute a block of code only if a certain condition is true.
# It can be followed by an optional elif (short for "else if") and else clauses.
# Indentation is crucial to define the scope of the code block.
# Example:
'''if condition1:
    # code block executed if condition1 is true
elif condition2:
    # code block executed if condition2 is true and condition1 is false
else:
    # code block executed if both condition1 and condition2 are false

# for loop:
# The for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects.
# It executes a block of code for each element in the sequence.
# Example:
for item in sequence:
    # code block executed for each item in the sequence

# while loop:
# The while loop is used to repeatedly execute a block of code as long as a certain condition is true.
# It keeps executing the code block until the condition becomes false.
# Example:
while condition:
    # code block executed as long as the condition is true

# break statement:
# The break statement is used to exit the current loop prematurely, even if the loop condition is still true.
# It is commonly used to terminate a loop based on a certain condition.
# Example:
while condition:
    if some_condition:
        break
    # code block executed until some_condition is true, then the loop is terminated

# continue statement:
# The continue statement is used to skip the current iteration of a loop and move to the next iteration.
# It is useful when you want to bypass specific iterations but continue looping.
# Example:
for item in sequence:
    if some_condition:
        continue
    # code block executed unless some_condition is true, then it moves to the next iteration

# pass statement:
# The pass statement is a placeholder that does nothing.
# It is used when a statement is required syntactically but you don't want to perform any action.
# Example:


# try-except statement:
# The try-except statement is used to handle exceptions (errors) that may occur during the execution of code.
# It allows you to catch and handle specific exceptions gracefully, preventing the program from crashing.
# Example:
try:
    # code that may raise an exception
except SomeException:
    # code executed if SomeException is raised
except AnotherException:
    # code executed if AnotherException is raised
else:
    # code executed if no exceptions are raised
finally:
    # code executed regardless of whether an exception occurred or not
# if statement'''
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
  
# for loop
sequence = [1,2,3,4,5,6]
for variable in sequence:
    print(variable)

#while loop and break
while True:
    print("Hey there!")
    break

#continue statement
sequence = [1,2,3,4,5,6]
for variable in sequence:

    if variable == 3:
        continue
    print( variable)
# Exception Handling in Python:
"""

# In Python, exception handling is a mechanism to handle errors or exceptional situations that may occur during program execution.
# It allows you to catch and handle specific exceptions gracefully, preventing the program from crashing.

# The basic structure of exception handling in Python involves the following keywords:

# try:
#     The code block placed inside the 'try' block is the one where an exception might occur.
#     It is the section of code where you anticipate potential errors.

# except ExceptionType:
#     If an exception of type 'ExceptionType' occurs inside the 'try' block, the corresponding 'except' block is executed.
#     'ExceptionType' represents the specific type of exception that you want to handle.
#     You can catch and handle specific exceptions, such as ValueError, TypeError, or FileNotFoundError, or use a more general 'except' block to handle any exception.

# except ExceptionType as error:
#     You can assign the exception instance to a variable 'error' using the 'as' keyword.
#     This allows you to access the details of the exception and handle it accordingly.

# else:
#     The 'else' block is optional and executed if no exceptions occur in the 'try' block.
#     It contains code that should run only if the 'try' block does not raise any exceptions.

# finally:
#     The 'finally' block is optional and always executed, regardless of whether an exception occurred or not.
#     It is useful for performing cleanup tasks or releasing resources that should be done regardless of the outcome of the exception handling.


try:
    # Code that may raise an exception
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)

except ZeroDivisionError:
    # Handling a specific exception (division by zero)
    print("Cannot divide by zero")

except ValueError as error:
    # Handling a specific exception (invalid input)
    print("Invalid input:", str(error))

except Exception as error:
    # Handling any other exception
    print("An error occurred:", str(error))

else:
    # Code executed if no exceptions occur
    print("No exceptions occurred")

finally:
    # Code always executed
    print("Finally block")



"""


# Try-except statement
num1 = 10
num2 = 0

try:
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
    
    

# List of animals
animals = ["Goat", "Cow", "Man"]

try:
    
    index = int(input("Enter the index of the animal you want to access: "))


    animal_selection = animals[index]
    print("Animal selection:", animal_selection)

except IndexError:
    print("Invalid index! The list does not have an element at the specified index.")

except ValueError:
    print("Invalid input! Please enter a valid integer index.")

except Exception as error:
    print("An error occurred:", str(error))

finally:
    print("Exception handling completed.")    

#mentalhealth survey
emotions={
    1:"Angry",
    2:"Happy",
    3:"Distressed",
    4:"Upset",
    5:"Rage",
    6:"Disgust",
    7:"Surprised",
    8:"Excited",
    9:"Fear",
    10:"LOL",
    }
#print(emotions[3]) 
mentalHealth=int(input("How can you rate your mental Health on a scale of 1-10?"))

print(type(mentalHealth))

if mentalHealth in emotions.keys():
    print(emotions[mentalHealth])  
