# # # # if-elif-else statement to categorize age groups
# # # age = input("Enter your age: ")
# # # age = int(age)  # convert string input to integer
# # # if age > 18:
# # #     print("This person is a young adult.")
# # # elif age == 18:
# # #     print("This person is exactly 18 years old.")
# # # elif age < 18 and age >= 13:
# # #     print("This person is a teenager.")
# # # else:
# # #     print("This person is neither a teen nor a young adult.")


# # # age = input("Enter your age: ") 
# # # attendee_name = input("Enter your name: ")  
# # # if int(age) > 18: 
# # #     print(f"{attendee_name} can enter and receive a drink!!")
# # # elif int(age) < 18 and int(age) >= 16:
# # #     print(f"{attendee_name} can enter but receives a juice pack!!")
# # # elif int(age) < 16:
# # #     print(f"{attendee_name} cannot enter the event!!")


# # # #match statement : used to match a variable against multiple cases
# # # day = 6
# # # match day:
# # #     case 1:
# # #         print("Monday")
# # #     case 2:     
# # #         print("Tuesday")
# # #     case 3:
# # #         print("Wednesday")
# # #     case 4:
# # #         print("Thursday")
# # #     case 5 | 6 | 7:  # multiple values for a single case
# # #         print("Lookinf forward to the weekend")
# # #     case _:  # default case
# # #         print("Invalid day")

# # # loops - programming statements that will allow you to repeat tasks
# # # while loop, for loop
# # # while loop - we can execute a block of code as long as a condition is true
# # #while loop stops when condition becomes false
# # # incrementors, decrementors - used to change the value of a variable in each iteration ++, -- , += , -=
# # # break statement - used to exit a the loop completely
# # # continue statement - used to skip the current condition and move to the next one

# # # #break statement
# # # i = 1
# # # while i <= 6:
# # #     if i == 4:
# # #         break  # exit loop when i is 4
# # #     print(i)
# # #     i += 1  # increment i by 1

# # # #continue statement
# # # i = 1
# # # while i <= 6:
# # #     i += 1  # increment i by 1
# # #     if i == 4:
# # #         continue  # skip the rest of the loop when i is 4
# # #     print(i)


# # # # for loop - used to iterate over a sequence (like a list, tuple, dictionary, set, or string)
# # x = "banana"
# # for char in x:
# #     print(char)


# # fruits = ["apple", "banana", "cherry"]
# # for fruit in fruits:
# #     x = fruit.upper()  # convert to uppercase
# #     print(x)

# # ## range() function - generates a sequence of numbers
# # #step means skipping numbers in the sequence
# # # for loop has break and continue statements
# # for i in range(2, 10):
# #     print(i)  

# # # nested loops - loop inside another loop "" for every iteration of the outer loop, the inner loop runs completely
# # colors = ["red", "green", "blue"]
# # for x in colors:
# #     for y in fruits:
# #         print(x, y)


# # password = ""
# # while password != "secret":
# #     password = input("Enter the password: ")

# # print("Access granted!")


# # python methods for looping actions
# # enumerayte() - useful when we want both the index and the value during iteration
# names = ["Alice", "Bob", "Charlie"]
# for index, name in enumerate(names):
#     print(f"Index: {index}, Name: {name}")  

# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")


# # comprehensions - list comprehensions : loop one liners
# squares = []
# for i in range(10):
#     squares.append(i)

# print(squares)

# # using list comprehension
# squares =  [x * x for x in range(10)]  # list comprehension
# print(f"squares using comprehension: {squares}")

# # using traditional for loop
# t_squares = []
# for x in range(10):
#     multiples = x * x
#     t_squares.append(multiples)

# print(f"squares using traditional loop: {t_squares}")

# functions - block of code that performs a specific task
# a function will receive input(arguments/parameters), process the input in accordance to logic in the codelock, and return an output(single value)
# define a function using def keyword
# process -> absesce of process indicate a pass (marks the codeock as empty for now )
# return -> used to send back the result from the function to the caller
# none -> special value indicating absence of a value
# to be executed, a function must be called/invoked: function_name()
def greet_function():
    pass  # placeholder for empty code block
def greet_user():
    greeting = "Hello, welcome to the Python class!"
    return greeting
print(greet_user())

def add_numbers(a, b):
    sum = a + b
    return sum
result = add_numbers(5, 7) # calling the function, 5 and 7 are arguments/parameters
print(f"The sum is: {result}")
    

# default parameters - used when no argument is provided during function call
def multiply_numbers(a, b=2):  # b has a default value of 2
    product = a * b
    return product
print(multiply_numbers(5))  # uses default value for b
print(multiply_numbers(5, 3))  # overrides default value for bS

# special functions 
# one liner functions using lambda keyword
# used for small, throwaway functions
square = lambda x: x * x
print(f"The square of 6 is: {square(6)}")

# Multiple function arguments
def math_operations(x, y):
    sum = x + y
    difference = x - y
    product = x * y
    quotient = x / y if y != 0 else None  # handle division by zero
    return sum, difference, product, quotient
results = math_operations(10, 2)
print(f"Sum: {results[0]}, Difference: {results[1]}, Product: {results[2]}, Quotient: {results[3]}")

 # python docstrings - used to document functions


"""

why use python functions
 - reusability :: write once, use multiple times
 - organization :: breaks code into smaller, manageable blocks. keeps code modular and readable
 - debugging :: easier to identify and fix issues within specific functions
 - collaboration :: multiple developers can work on different functions simultaneously without conflicts

 pro tips for functions
    - keep functions small and focused on a single task
    - name them clearly to reflect their purpose
    - avoid side effects (functions should not modify global state unless necessary)
    - use docstrings to document function purpose, parameters, and return values

"""

def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    import math
    area = math.pi * radius * radius
    return area
print(f"Area of circle with radius 5: {calculate_area(5)}")