# # variables - storage references for information
# # variables will receive data types from the values they store
# # data type - format of data : Brian -text, 0 - number, 0.23 -decimal
# #nameofvariable = value

# # when naming variables:
# # 1. use descriptive names that reflect the purpose of the variable
# # 2. use lowercase letters and underscores to separate words (snake_case) not spaces
# # 3. avoid using reserved keywords in Python (like if, else, while, etc.)
# # 4. variables are case sensitive - name, Name and NAME are different variables
# nameofvariable = "Brian" # string data type : value enclosed in quotes - string
# number_one = 0  # integer data type : whole number
# decimal_number = 0.23  # float data type : decimal number
# boolean_value = True  # boolean data type : True or False
# list_variable = ["Brian", 1, 2, 3, 4, 5, True]  # list data type : collection of values in square brackets
# set_variable = {"apple", "banana", "cherry"}  # set data type : collection of unique values in curly braces
# tuple_variable = ("Brian", 1, 2, 3)  # tuple data type : collection of values in parentheses
# null_variable = None  # NoneType data type : represents absence of value. none is the reference for the data types and not empty
# dictionary_variable = {"name": "Brian", "age": 30}  # dictionary data type : key-value pairs in curly braces. it is a collection of related information

# # how to output - print(specify_what_to_print) method: output will be reflected in the console/terminal
# print(nameofvariable)
# print(set_variable)
# print(dictionary_variable)

# # # how to run the file : python filename.py - terminal

# # #camelcase vs snake_case
# # # camelCaseVariable = "This is camel case"
# # #snake_case_variable = "This is snake case"  prefered in python

# # # for input taking in python via terminal/console - input() method
# # # input_variable = input("Please enter something: ")
# # # then use formatted string to output the input value
# # # print("You entered: " + input_variable)
# # user_name = input("Enter your name: ")
# # user_email = input("Enter your email: ")
# # print("Hello, " + user_name + "! Welcome to the program.")
# # print("Your email is: " + user_email)

# # #variable reassignment - changing the value of a variable
# # nameofvariable = "not taking username at the moment "  # reassigned to a new value
# # print(nameofvariable)

# # # Control Flows - decision making in code
# # #if condition:
# #     # code to execute if condition is true
# # #elif another_condition:
# #     # code to execute if another_condition is true
# # #else:
# #     # code to execute if condition is false

# # # code blocks - indented lines of code that belong together. a group of code that executes a particular output
# # age = input("Enter your age: ")
# # age = int(age)  # convert string input to integer
# # if age > 18:
# #     print("This person is a young adult.")
# # elif age == 18:
# #     print("This person is exactly 18 years old.")
# # elif age < 18 and age >= 13:
# #     print("This person is a teenager.")
# # else:
# #     print("This person is neither a teen nor a young adult.")

# # #TYPE CASTING - converting one data type to another

# # age = input("Enter your age: ") 
# # attendee_name = input("Enter your name: ")  
# # if int(age) > 18: 
# #     print(f"{attendee_name} can enter and receive a drink!!")
# # elif int(age) < 18 and int(age) >= 16:
# #     print(f"{attendee_name} can enter but receives a juice pack!!")
# # elif int(age) < 16:
# #     print(f"{attendee_name} cannot enter the event!!")

# a = 10
# b = a + 20

# f_name = "Brian"
# l_name = "Mwangi"
# print(f_name + " " + l_name)    

# c = 7
# d = 3
# e = c * d
# print(e)
# d *= 10 # shorthand for d = d * 10
# print(d)
# d %= 7 # shorthand for d = d % 7
# print(d)

# x = 10
# y = 6
# print(x == y)  # equality operator, false
# print(x != y)  # inequality operator, true
# print(x > y)   # greater than operator, true
# print(x < y)   # less than operator, false
# print(x >= y)  # greater than or equal to operator, true
# print(10 < x and x > 1 ) # logical and operator, true
# print(10 < x or x < 1 ) # logical or operator, true
# print(not(x < y))  # logical not operator, true
# # logical operators - and, or, not
# # comparison operators - ==, !=, >, <, >=, <=
# # arithmetic operators - +, -, *, /, %, //, **
# # assignment operators - =, +=, -=, *=, /=, %=, //=, **=

# # identity operators - is, is not
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x
# print(x is z)  # true, both refer to the same object
# print(x is y)  # false, different objects with same content


# # membership operators - in, not in
# fruits = ["apple", "banana", "cherry"]
# print("banana" in fruits)  # true
# print("grape" not in fruits)  # true
# print("grape" in fruits)  # false

# # bitwise operators - &, |, ^, ~, <<, >>
# # 5 & 3  # bitwise AND
# # or_op = 5 | 3  # bitwise OR
# # xor = 5 ^ 3  # bitwise XOR
# # not_op = ~5  # bitwise NOT

# # data types operations
# # in built operations/methods that enable us to manipulate data types

# # string operations (str) used to manipulate text data
# greeting = "Hello, "
# # common operations/methods
# print(greeting.lower())  # convert to lowercase
# print(greeting.upper())  # convert to uppercase

# # substring - slice a string and return the portion specified
# print(greeting[0:5])  # slice from index 0 to 4
# # join - join a list of strings into a single string with a specified separator
# letters = ["H", "e", "l", "l", "o"]
# # "hello"
# # .join
# joined_string = "".join(letters)
# print(joined_string)

# #isinstance - check if an object is an instance of a specified data type
# print(isinstance(greeting, str))  # true
# print(isinstance(10, int))  # true

# #collections / sequnces : grouping of related data types - immutable and mutable
# # list, set, tuple, dictionary
# # list - ordered collection of items, mutable (can be changed) and are ordered and allow duplicate values
# # ordering in lists is based on the index position starting from 0
# # size : number of items in the list - len()
# # 

list_fruits = ["apple", "banana", "cherry"]  # list - mutable

# operations/methods
print(list_fruits[0])  # access first item
print(len(list_fruits))  # length of the list
print(list_fruits[-1])  # access last item
print(list_fruits[1:3])  # slice from index 1 to 2
list_fruits.append("orange")  # add item to the end
print(list_fruits)
list_fruits.pop(0)  # remove item at index 0
print(list_fruits)
list_fruits[0] = "kiwi"  # change item at index 0
print(list_fruits)

# tuples - immutable (cannot be changed) ordered collection of items, allow duplicate values
coordinates = (5, 10, 20)  # tuple - immutable
one_item_tuple = (5,)  # single item tuple - note the comma
# operations/methods
print(len(coordinates))  # length of the tuple
# ordered based on index position starting from 0
print(coordinates[1])  # access item at index 1
print(coordinates[-1])  # access last item
print(coordinates[0:2])  # slice from index 0 to 1
# update values in a tuple (type casting ) (remove, update) tuple -> list -> tuple
changed_coordinates = list(coordinates)  # convert to list
print(changed_coordinates)
changed_coordinates.pop(0)  # remove item at index 0 - remove("value") also works
changed_coordinates[1] = 15  # change item at index 1
coordinates = tuple(changed_coordinates)  # convert back to tuple
print(coordinates)
#delete a tuple completely
del one_item_tuple

#sets - unordered, unchanged, unindexed , no duplicate values on printing
#false and 0 are the same in sets
set_fruits = {"apple", "banana", "cherry", "apple", False, 0}  # set - unordered, mutable, no duplicate values(if duplicates are added, they are ignored)
print(set_fruits)
print(len(set_fruits))  # length of the set
#accessing items in a set - cannot access by index as sets are unordered : refrence via loop or check for existence
#loops allows you to repeat actions for each item in a collection
for fruit in set_fruits:
    print(fruit)
# operations/methods
# sets cannot be changed - but we can add or remove items
set_fruits.add("orange")  # add item
print(set_fruits)
# sets will also allow addition of any colletion type inside them except another set
set_fruits.update(list_fruits)  # add multiple items from another collection
print(set_fruits)
set_fruits.remove("banana")  # remove item (raises error if item not found)
print(set_fruits)
set_fruits.discard("apple")  # remove item (does not raise error if item not found)
print(set_fruits)


# dictionaries - Storage of key-value pairs, unordered, mutable, indexed by keys, won't allow duplicate keys
my_vehicle = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "engineNo" : "AX12345",
    "ntsaReg" : False
}  
print(my_vehicle)
# operations/methods
print(len(my_vehicle))  # length of the dictionary
print(my_vehicle["model"])  # access value by key
print(my_vehicle.get("year"))  # access value by key using get() method
print(my_vehicle.keys())  # get all keys
print(my_vehicle.values())  # get all values
print(my_vehicle.items())  # get all key-value pairs
print("brand" in my_vehicle)  # check if key exists
# add or update key-value pairs
my_vehicle["color"] = "Blue"  # add new key-value pair
my_vehicle["year"] = 2021  # update existing key-value pair
print(my_vehicle)
# remove key-value pairs
my_vehicle.pop("engineNo")  # remove key-value pair by key
print(my_vehicle)
del my_vehicle["ntsaReg"]  # remove key-value pair by key using del
print(my_vehicle)


### nested collections
x = { ("apple", "banana"), "Joseph" , "Jane" , (1,90.09) , False }  # set containing tuple, strings, tuple, boolean
print(x)

# dictionaries and lists cannot be stored in sets (they are mutable)
nested_dict = {
    "fullname": "Brian Mwangi", 
    "staff_id" : 8473
}  # dictionary with nested data
print(nested_dict)

myFamily = {
    "father": {
        "name": "John",
        "age": 50
    },
    "mother": {
        "name": "Jane",
        "age": 48
    },
}
mother_name = myFamily["mother"]["name"]
print(mother_name)  # output: Jane
print(myFamily["father"]["age"])  # output: 50
print(f"the mother's name is {mother_name} and the father is {myFamily['father']['name']}")