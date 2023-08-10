
#NUMBERS IN PYTHON
  #integers,floats,complex
x=10
y=10.5
z=5j
print(type(x)) 
print(type(y)) 
print(type(z)) 

#INTEGERS
   #can be positives or negatives
   #dont have decimal points
a=2
b=-5
print(type(a))   
print(type(b))  

#fLOATS
d=3.15
e=-5.76
print(type(d))
print(type(e))

#Complex
 #have real and imaginary parts
g=4+6j
j=7j
print(type(g))
print(type(j)) 

#Type conversions
k=10
l=4.67
m=4j
#converting complex to int
# new_int=int(m)
# print(new_int)
#converting int to complex
new_complex=complex(k)
print(new_complex)
#converting int to float
new_float=float(k)
print(new_float)
#converting float to complex
new_complex2=complex(l)
print(new_complex2)
#converting complex to float
# new_float2=float(m)
# print(new_float2)


#Strings in python
print("Hello")
#assigning a string to a variable
greeting="helllo ,Byte Code"
print(greeting)
#multi-line strings
 #span morethan one line ,we use triple quotes
speach="""Today will be the very day in the day of the
 junior day at amoment in the moment of a disorganised 
 lecture if the available"""
print(speach) 
#Strings as Arrays
a="Afternoon"
print(a[2])
#lenght
print(len(a))
#for loops
for character in a:
    print(character)
for characters in enumerate(a):
    print(characters)    
#slicing a string
print(a[:5])
print(a[4:5])
#modifying strings
print(a.lower())
print(a.upper())
#removing whitespace
print(a.strip())
print(a.title())
print(a.islower())
#concatenation
item="Animal"
item_instance="Cow"
print(item + " called"+ item_instance)
print(f"{item_instance} is an {item}")

#formatting strings
 #if we want to combine a string to a number
 #we use the format method
 #the method takes in the passed arguments,formats them and places them in the 
 #placeholder of {}


age=23
identity="My goat is{}"
print(identity.format(age))

#Booleans
 # True or False
print(20<34)
print(30==40)
print(30>24) 
print(bool(15))

r="Animal"
q=""
z=45
print(bool(r))
print(bool(z))
print(bool(q))
Condition="True"
if Condition:
    print("Condition is true")
    Condition="False"

#DICTIONARIES IN PYTHON
 #store data in key value pairs
 #they are ordered , changeable but dont allow duplicates
 #Can have items of any data type
dict={
    "name":"Max",
    "age":5,
    "weight":10

 }
print(dict)
#type of the dictionary
print(type(dict))
#length of the dictionary
print(len(dict))
#accessing items in a dictionary
 #we use keys or the getter 
print(dict["name"])
print(dict.get(10))
#adding new items in a dictionary
dict["year"]=2
print(dict)
#accessing the keys in a dictionary
print(dict.keys())
#accessing values in a dictionary
print(dict.values())
#deleting items in a dictionary
 #we can delete a particular item by passing its key in the pop function
 #we can delete the last item using the inbuilt function
dict.pop("year")
print(dict)
dict.popitem()
print(dict)
#Check if a key exits in a dictionary
 #we can use the mebership operator n it returns true or false
print("age" in dict.keys())
#changing dictionary items
dict["name"]="Cow"
print(dict)
#looping through a didctionary
print(dict.items())
for key,value in dict.items():
    print(key,value)

