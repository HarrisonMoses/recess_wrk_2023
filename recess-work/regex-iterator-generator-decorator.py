# import re

#Regular expression
#Matching and searching
#regex re.findall(),re.match(),re.search()

#demonstrating matching first word
text="Hello ,good morning everyone .I am a programmer with 6 yrs experience"
match = re.search(r"\d+", text)
if match:
    print("Match=" ,match.group())
matches=re.search(r"$\w+", text)
if matches:
    print("Match=" ,matches.group())    
#Validating the email address or the email format
def validateEmail(email):
    pattern=r'^[\w\.-]+@[\w\.-]+\.[\w\.-]+$'
    if re.match(pattern, email):
        return True
    else:
        return False    
print(validateEmail("nanyongarahmah@gmail.com"))
print(validateEmail("__zoo.com"))        
  #GENERATORS AND ITERATORS
#generators are defined like normal functions however 
#when they need to return a value we use the yield keyword
#rather than the return keyword
def simpleGeneratorFun():
    yield 1           
    yield 2           
    yield 3           
  
# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)

#ITERATORS IN PYTHON
#In Python, an iterator is an object used to iterate over iterable objects 
#such as lists, tuples, dictionaries, and sets.
# An object is called iterable if we can get an iterator from it or loop over it.
#A Python iterator object must implement two specific methods, __iter__() or iter() and
# __next__() or next() , which are referred to collectively as the iterator protocol. 
#Python iter()

# The iter() function in Python returns an iterator for the supplied object.
#  The iter() generates a thing that can be iterated one element at a time. 
# These items are handy when combined with loops such as for loops and while loops. 

# Syntax:

# iter( object , sentinel )
# iter() function takes two parameters:

# Object: An object whose iterator needs to be created (lists, sets, tuples, etc.).
# Sentinel (optional): Special value that represents the end of the sequence.
 

# Python next()

# The next() function returns the next item from the iterator. The next() function holds the value one at a time. 

# Syntax:

# next( iterator , default )
# The next() method accepts two parameters:

# Iterator : next( ) function retrieves the next item from the iterator.
# default(optional): this value is returned if the iterator is exhausted (not tired, but no next item to retrieve).
 


# Assume we have a list of different types as given below. 

list1 = [ 25 , 78, "cooking", 'is', '<3' ]  # list of different types
#Let’s print it with the help of Iterators ( or iter() and next() ):-

# Program to print the list using Iterator protocols
X = [25, 78, 'Coding', 'is', '<3']
# Get an iterator using iter() 
a = iter(X)

# Printing the a iterator
print(a)

# next() for fetching the 1st element in the list that is 25
print(next(a))

# Fetch the 2nd element in the list that is 78
print(next(a))

# Fetching the consecutive elements
print(next(a))
print(next(a))
print(next(a) ) 


#DECORATORS IN PYTHON
#A Python decorator is a function that takes in a function and returns it by adding some functionality.
def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()  
