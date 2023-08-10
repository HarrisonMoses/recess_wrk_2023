
#A program to increment employee salary
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_salary(self):
        return self._salary
    
    def set_salary(self, salary):
        self._salary = salary
    
    def give_increment(self, increment):
        self._salary += increment


# Creating an Employee object
employee = Employee("Amanda AK", 850000)

# Getting initial employee details
print("Employee Name:", employee.get_name())
print("Employee Salary:", employee.get_salary())

# Giving an increment of 1000 to the employee
employee.give_increment(150000)

# Getting updated employee details
print("Employee Name:", employee.get_name())
print("New Employee Salary:", employee.get_salary())

#A program to convert from celcius to fahrenheit
class TemperatureConverter:
    def __init__(self,celcius):
        self._celcius = celcius
    def get_celcius(self):
        return self._celcius
    def set_celcius(self, celcius):
        self._celcius = celcius
    def convert_celcius(self):
        return (self._celcius * 9/5) + 32
converter = TemperatureConverter(37)
celcius_temp = converter.get_celcius()
print("Temperature in celcius:",celcius_temp ) #prints 37
fahrenheit_temp = converter.convert_celcius()
print("Temperature in Fahrenheit:", fahrenheit_temp) #prints 98.6


    
