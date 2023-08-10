'''Exercise1 (Lists)
1. Create a list with 5 items (names of people) and write a python program to output the 2nd item.
2. Write a python program to change the value of the first item to a new value
3. Write a python program to add a sixth item to the list
4. Write a python program to add “Bathel” as the 3rd item in your list
5. Write a python program to remove the 4th item from the list
6. Use negative indexing to print the last item in your list
7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
8. Write a list of countries and make a copy of it.
9. Write a python program to loop through the list of countries
10. Write a list of animal names and sort them in both descending and ascending order.
11. Using the list above, write a python program to output only animal names with the letter ‘a’ in them
12. Write two lists, one containing your first names and the other your second names. Join the two lists.
'''
#1
people = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(people[1])

#2
people = ["Alice", "Bob", "Charlie", "David", "Eve"]
people[0] = "Alex"
print(people)

#3
people = ["Alice", "Bob", "Charlie", "David", "Eve"]
people.append("Frank")
print(people)

#4
people = ["Alice", "Bob", "Charlie", "David", "Eve"]
people.insert(2, "Bathel")
print(people)

#5
people = ["Alice", "Bob", "Charlie", "David", "Eve"]
del people[3]
print(people)

#6
people = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(people[-1])

#7
numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[2:5])

#8
countries = ["UK", "Gambia", "France", "Germany", "Australia"]
countries_copy = countries.copy()
print(countries_copy)

#9
countries = ["UK", "Gambia", "France", "Germany", "Australia"]
for country in countries:
    print(country)
    
#10
animals = ["Elephant", "Tiger", "Lion", "Giraffe", "Zebra"]
animals.sort()  # Ascending order
print(animals)
animals.sort(reverse=True)  # Descending order
print(animals)

#11
animals = ["Elephant", "Tiger", "Lion", "Giraffe", "Zebra"]
for animal in animals:
    if 'a' in animal.lower():
        print(animal)

#12
first_names = ["John", "Alice", "David"]
last_names = ["Doe", "Smith", "Johnson"]
full_names = [first + " " + last for first, last in zip(first_names, last_names)]
print(full_names)
       
#Tuples
'''1. Consider the tuple below;
x = (“samsung”, “iphone”, “tecno”, “redmi”)
Write a python program to output your favorite phone brand.
2. Use negative indexing to print the 2nd last item in your tuple.
3. Using the phones list above, write a python program to update “iphone” to “itel”
4. Write a python program to add “Huawei” to your tuple.
5. Write a python program to loop through the tuple above.
6. Write a python program to remove/delete the first item in your tuple.
7. Using the tuple() constructor, create a tuple of the cities in Uganda.
8. Write a python program to unpack your tuple.
9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
10. Write two tuples, one containing your first names and the other your second names. Join the two tuples.
11. Create a tuple of colors and multiply it by 3.
12. Return the number of times 8 appears in this tuple thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
'''
#1
x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = x[1]
print(favorite_brand)

#2
x = ("samsung", "iphone", "tecno", "redmi")
second_last_item = x[-2]
print(second_last_item)

#3
x = ("samsung", "iphone", "tecno", "redmi")
x = list(x)
x[x.index("iphone")] = "itel"
x = tuple(x)
print(x)

#4
x = ("samsung", "iphone", "tecno", "redmi")
x = list(x)
x.append("Huawei")
x = tuple(x)
print(x)

#5
x = ("samsung", "iphone", "tecno", "redmi")
for brand in x:
    print(brand)

#6
x = ("samsung", "iphone", "tecno", "redmi")
x = list(x)
del x[0]
x = tuple(x)
print(x)

#7
cities = tuple(("Kampala", "Entebbe", "Jinja", "Gulu"))
print(cities)

#8
x = ("samsung", "iphone", "tecno", "redmi")
brand1, brand2, brand3, brand4 = x
print(brand1)
print(brand2)
print(brand3)
print(brand4)

#9
cities = ("Kampala", "Entebbe", "Jinja", "Gulu")
second_third_fourth = cities[1:4]
print(second_third_fourth)

#10
first_names = ("Amanda", "Ann")
last_names = ("Kirabo")
full_names = first_names + last_names
print(full_names)

#11
colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print(multiplied_colors)

#12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print(count_8)

#Sets
'''1. Use the set() constructor to create a set of 3 of your favorite beverages.
2. Use the correct method to add 2 more items to the beverages set.
3. Given the set below;
mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
Check if microwave is present in the set.
4. Write a python program to remove “kettle” from the set above.
5. Write a python program to loop through the set above.
6. Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
7. Write two sets, one containing your ages and the other your first names. Join the two sets.
'''
#1
favorite_beverages = set(["coffee", "tea", "juice"])

#2
favorite_beverages.add("soda")
favorite_beverages.add("water")

#3
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")

#4
mySet.remove("kettle")

#5
mySet = {"oven", "kettle", "microwave", "refrigerator"}
for item in mySet:
    print(item)

#6
mySet = {1, 2, 3, 4}  # Set of 4 items
myList = [5, 6]  # List of 2 items

# Adding elements from the list to the set
mySet.update(myList)

print(mySet)  # Output: {1, 2, 3, 4, 5, 6}

#7
ages = {25, 30, 35}  # Set of ages
first_names = {"John", "Jane", "Mike"}  # Set of first names

# Joining the two sets
combined_set = ages.union(first_names)

print(combined_set)  # Output: {25, 30, 35, 'Jane', 'Mike', 'John'}

#Strings
'''1. Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
2. Consider the example below;
txt = “ Hello, Uganda! ”
Output the string without spaces at the beginning, in the middle and at the end.
3. Write a python program to convert the value of ‘txt’ to uppercase.
4. Write a python program to replace character ‘U’ with ‘V’ in the string above.
5. Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position.
y = “I am proudly Ugandan”
6. The piece of code below will give an error when output;
x = “All “Data Scientists” are cool!”
Write a python program to correct it.
'''
#1
# Declare the variables
integer_variable = 10
string_variable = "Hello"

# Concatenate the variables
concatenated_string = str(integer_variable) + " " + string_variable
print(concatenated_string)

#2
txt = " Hello, Uganda! "

# Remove spaces at the beginning, in the middle, and at the end
trimmed_txt = txt.strip()
print(trimmed_txt)

#3
txt = "Hello, Uganda!"
uppercase_txt = txt.upper()
print(uppercase_txt)

#4
txt = "Hello, Uganda!"
modified_txt = txt.replace("U", "V")
print(modified_txt)

#5
y = "I am proudly Ugandan"
range_of_characters = y[1:4]
print(range_of_characters)

#6
#Using single quotation marks:
x = 'All "Data Scientists" are cool!'
print(x)

#Using escaped double quotation marks:
x = "All \"Data Scientists\" are cool!"
print(x)

#Dictionaries
'''1. With reference to the dictionary below, write a python program to print the value of the shoe size.
Add this dictionary to your .py file
Shoes = {
“brand” : “Nick”,
“color” : “black”,
“size” : 40
}
2. Write a python program to change the value “Nick” to “Adidas”
3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
4. Write a python program to return a list of all the keys in the dictionary above.
5. Write a python program to return a list of all the values in the dictionary above.
6. Check if the key “size” exists in the dictionary above.
7. Write a python program to loop through the dictionary above.
8. Write a python program to remove “color” from the dictionary.
9. Write a python program to empty the dictionary above.
10. Write a dictionary of your choice and make a copy of it.
11. Write a python program to show nested dictionaries
'''
#1
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

print(Shoes["size"])

#2
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

Shoes["brand"] = "Adidas"
print(Shoes)

#3
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

Shoes["type"] = "sneakers"
print(Shoes)

#4
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

keys = list(Shoes.keys())
print(keys)

#5
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

values = list(Shoes.values())
print(values)

#6
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

if "size" in Shoes:
    print("The key 'size' exists.")
else:
    print("The key 'size' does not exist.")

#7
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

for key, value in Shoes.items():
    print(key, ":", value)

    
#8
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

del Shoes["color"]
print(Shoes)

#9
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

Shoes.clear()
print(Shoes)

#10
original_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

# Method 1: Using the copy() method
copied_dict = original_dict.copy()

# Method 2: Using the dict() constructor
copied_dict = dict(original_dict)

print(copied_dict)


#11
nested_dict = {
    "person1": {
        "name": "John",
        "age": 25,
        "city": "New York"
    },
    "person2": {
        "name": "Emily",
        "age": 30,
        "city": "London"
    }
}

print(nested_dict)

