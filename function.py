# TypeError: multi_func() got multiple values for argument 'num1'===> 
# code is commented out to avoid error
# def multi_func(num1, num2):
#     return num1 * num2;
# print(multi_func(5, num1=10))

# Corrected function call====>
# named arguments provided for both parameters 
def multi_func(num1, num2):
    return num1 * num2;
print(multi_func(num1=5, num2=10))

# Example of *args 
# *students: automatically collect all positional arguments passed to the function into a tuple.
def my_function(*students):
  print("The tallest student is " + students[2])
my_function("James", "Ella", "Jackson")

#when the function print_info is called,
#the default value for the age parameter is overridden by the explicit argument you provide
def print_info(name, age=18):
    print(name, age)

print_info('john', 19)

# no paranthesis after return,
# as Python treats the expression after return as a single unit. It calculates the value of num1 + num2 first, 
# and then returns that final value.
# The return statement is the "finish line" for the function. 
# Once Python hits that line, the function's job is done and it stops running immediately
#Example: 1
def add_func(num1,num2):
    return num1 + num2
print ( add_func(5 , 5) )  # Output: 10

#Example: 2
#Anything written after the return line in a function is ignored
def add_func(num1, num2):
    return num1 + num2
    print("This will never print!") # This line is ignored
result = add_func(5, 10)
print(result)  # Output: 15

# Example: 3
# return multiple things
def multi_return(num1, num2):
    return num1 + num2, num1 * num2, num1 / num2 # Returns three values
result = multi_return(10, 5)
print(result)  # Output: (15, 50, 2.0)

# When you return multiple values from a function, Python bundles them into a tuple
# You can unpack these values into separate variables like this:
sum_result, product_result, division_result = multi_return(10, 5)
print(sum_result)        # Output: 15
print(product_result)    # Output: 50  
print(division_result)   # Output: 2.0

#usefulness of unpacking
# Readability: no indexing needed, so it's clearer what each value represents.
# Convenience: direct access to values without needing to reference a tuple.
# Safety: 
# if we provide two variables to unpack them, Python will raise a ValueError.
# This helps catch bugs where your function's output might have changed.
# The Underscore (_) Trick: 
# If we want only one of the returned values, 
# we can use an underscore as a placeholder for the ones you want to ignore:


# Example: 4
# parameter outside function scope
a = 0
def add_three(a):
	return a+3

result = add_three(3)
print(result)  # Output: 6


# Example: 5
# parameter outside function scope but passing global variable
a = 0
def add_three(a):
	return a+3

result = add_three(a)
print(result)  # Output: 3

# Example: 6
# boolean return
# return statement does not have a fixed data type. 
# Instead, it returns whatever object is resulting from the expression you give it.
def is_true(a): 
  return bool(a) 

result = is_true(6<3) 
print("The result is", result)  # Output: The result is False, to get '0' typecast int use int(bool(a))


# Example: 7
# return none
def add_func(num1, num2):
    print("Adding", num1, "and", num2)
    return  # Implicitly returns None

result = add_func(5, 10)
print("Result is", result)  # Output: Result is None

# Example: 8
def is_even(num):
    if num % 2 == 0:  
        return True  
print(is_even(4))  # Output: True
print(is_even(5))  # Output: None (since no return statement is executed)

# Example: 9
# greeting function with return
def greet(name):
    return "Hello, " + name + "!" + " Welcome to the Python world."
message = greet("Alice")
print(message)  # Output: Hello, Alice! Welcome to the Python world.


# list as arguments
# Example: 10
# sum function that takes a list as an argument and returns the mean
def mean_func(list1):
    return sum(list1) / len(list1)

print(mean_func([5, 2, 2, 4])) #result: 3.25

# Example: 11
# Using Python's built-in sum function with the start parameter
# start parameter allows specifying an initial value for the summation
# This is useful when you want to add a fixed offset to the sum of the list elements.
def sum_func(num_list, start=0):
    total = start
    # here count starts from 'start' value = 0
    for num in num_list:
        total += num
    return total

print(sum_func([1, 2, 3, 4]))  # Output: 10
print(sum_func([1, 2, 3, 4], 10))  # Output: 20

# Example: 11
list1 = [10, 20]
# Add the list items (30) AND start the count from 100, then add them one by one
result = sum(list1, 100)
print(result) # Output: 130


# Example: 12
# Function to concatenate a list of strings with a specified separator
def concatenate_strings(str_list, separator=" "):
    result = ""
    for s in str_list:
        result += s + separator
    return result.strip(separator)  # Remove trailing separator
strings = ["Hello", "world", "from", "Python"]
print(concatenate_strings(strings))  # Output: "Hello world from Python"


# Example: 13
# Function to filter out odd numbers from a list
# note: % 2 returns 1 for odd numbers which is treated as True
def get_odd_func(numbers):
    odd_numbers = [num for num in numbers if num % 2]
    return odd_numbers

print(get_odd_func([7, 4, 5, 6, 9, 8, 12]))  # Output: [7, 5, 9]

# example: 14
# Function to increment each number in a list by 1 and print them
# note: end=' ' in print function to print in same line with space
def my_function(numbers):
  for i in numbers:
    print(i+1, end=' ')

numbers = [1, 2, 3] 
my_function(numbers)  # Output: 2 3 4

# example: 15
# Function to print each name from a list
# note: end=' ' in print function to print in same line with space
def my_function(names):
  for i in names:
    print(i, end=' ')

names = ["john", "mark", "emmy"]
my_function(names)  # Output: john mark emmy


# example: 16
# Function to filter out even numbers from a list
# note: not num % 2 returns True for even numbers
def get_even_func(numbers):
    even_numbers = [num for num in numbers if not num % 2]
    return even_numbers

get_even_func([1, 2, 3, 4, 5, 6])  # Output: [2, 4, 6]

# example: 17
# Function to double the elements of a list
# [1, 2, 3, 1, 2, 3] and not [1, 2, 3][1, 2, 3] because * with list works as repeat operator
# It takes the original list, creates a new list. 
# where it repeats the elements of the original list n times inside that new list
# 2 * [1, 2, 3] is exactly the same as doing [1, 2, 3] + [1, 2, 3].
def double_list(numbers):
  return 2 * numbers
numbers = [1, 2, 3]
print(double_list(numbers))  # Output: [1, 2, 3, 1, 2, 3]


# Example: 18
# Function to double the value of each element in a list
def double_list_values(numbers):
    # Multiply each individual element 'n' by 2
    return [n * 2 for n in numbers]

numbers = [1, 2, 3]
print(double_list_values(numbers))  
# Output: [2, 4, 6]

#===============================================================
#scopes of variables:
# Example: 19
# Local Scope
def input_number():
    result = int(input("Enter a number: ")) * 100
    return result
print(input_number())  # Output: (depends on user input)
# 'result' variable is not accessible here, as it is local to the function

# Example: 20.1
# Global Scope
result = 0  # Global variable
def input_number():
    global result  # Declare 'result' as global to modify the global variable
    result = int(input("Enter a number: ")) * 100
    return result
print(input_number())  # Output: (depends on user input)
# 'result' variable is accessible here, as it is global 
print(result)  # Output: (same as above, depends on user input), its value is retained outside the function, can be different from 0

# example: 20.2
x = 30
def my_function():
  global x
  x = 20

my_function()
print(x)
# Output: 20


# Example: 20.3
# Global Scope without using 'global' keyword
result = 0  # Global variable
def input_number():
    result = int(input("Enter a number: ")) * 100  # This 'result' is local to the function
    return result
print(input_number())  # Output: (depends on user input)
print(result)  # Output: 0, global 'result' remains unchanged

# ===============================================================

# Example: 21
# Enclosing Scope/ Nested Function Scope/ Lexical Scope/ Closure Scope/ nonlocal scope
# note1: inner_function can access outer_var
# note2: outer_function cannot access inner_var
# note3:after declaring inner_function, returning the result of inner_function call @ the end of outer_function 
def outer_function():
    outer_var = "Hello"
    def inner_function():
        inner_var = " World"
        return outer_var + inner_var  # Accessing variable from enclosing scope
    return inner_function()  # Call inner function and return its result

# example: 22
# nonlocal keyword example:
# note: nonlocal allows inner_function to modify the 'count' variable from outer_function scope
def outer_function():
    count = 0
    def inner_function():
        nonlocal count  # Tells Python to use the variable from the enclosing scope
        count += 1
        return count
    return inner_function()

print(outer_function()) # Output: 1

# Example: 23
# closure example 1:
def outer_function(msg):
    def inner_function():
        return "Message: " + msg  # Accessing variable from enclosing scope
    return inner_function  # Return the inner function itself
my_func = outer_function("Hello, World!")
print(my_func())  # Output: Message: Hello, World!  

# Example: 24
# closure example 2:
def make_multiplier(n):
    # This is the Enclosing Scope
    def multiplier(number):
        # This is the Local Scope
        # It "remembers" 'n' from the enclosing scope
        return number * n
    
    return multiplier # We return the FUNCTION itself, not the result

# Create a "Double" function
doubler = make_multiplier(2)

# Create a "Triple" function
tripler = make_multiplier(3)

print(doubler(10)) # Output: 20
print(tripler(10)) # Output: 30


# example: 25
# variable shadowing
# note: inner x (30) shadows outer x (20) within my_function scope
x = 20
def my_function():
  x = 30
  print(x, end=' ')

my_function()
print(x)
# Output: 30 20


# Example: 26
# inner function variable scope
# note: print(x) is outside my_inner_function
# def my_function():
#   def my_inner_function():
#     y = 20
#   print(y)
#   my_inner_function()

# my_function()
# Output: Error, y is not defined

# Example: 27
# def myfunc():
#   z = 20

# myfunc()
# print(z)
# Output: Error, z is not defined


#===============================================================

# example: 28
# *args example
# note: *argv collects or pack all positional arguments into a tuple named 'argv'
# note: it prints exaactly as tuple, with parentheses and commas
def my_function(*argv):
  print(argv)
  print(*argv)  # unpacking the tuple to print values without parentheses and commas

my_function('Hello', 'World!')  # Output: ('Hello', 'World!'), Hello World!


# example: 28.1
# *args example to sum all arguments - ERROR VERSION (commented out)
# note: args is a tuple of all positional arguments passed to the function
# def sum(*args):
#     for arg in args:
#         result += arg  # Error: result is not initialized
#     return result 
# print(sum(2, 3, 1))  # Error: UnboundLocalError: local variable 'result' referenced before assignment

# example: 28.1 - CORRECTED VERSION
def sum_all(*args):
    result = 0  # Initialize result to 0
    for arg in args:
        result += arg
    return result 

print(sum_all(2, 3, 1))  # Output: 6


# example: 28.2
# *args example to print first argument only
def my_function(*argv):
  print(argv[0])

my_function('Hello', 'World!')  # Output: Hello


# example: 28.3
# *args example to iterate through all arguments
def my_function(arg1, *argv): 
    print ("First argument:", arg1) 
    for arg in argv: 
        print("Next argument:", arg) 

my_function('Welcome', 'to', 'Python!')
# Output:
# First argument: Welcome
# Next argument: to
# Next argument: Python!


# example: 28.4
# *args example to find maximum value among arguments
def find_maximum(*args):
    if not args:
        return None  # Return None if no arguments are provided
    max_value = args[0]
    for num in args:
        if num > max_value:
            max_value = num
    return max_value
print(find_maximum(3, 5, 1, 8, 2))  # Output: 8


# example: 28.5
# *args example to print all arguments
def my_function(*argv):  
    for arg in argv:  
        print(arg) 

my_function('Hello', 'World!')
# Output:
# Hello
# World!



# example: 29
# **kwargs example
# note: **kwargs collects or pack all keyword arguments into a dictionary named 'kwargs'
def my_function(**kwargs):
  print(kwargs) # prints the dictionary
  for key, value in kwargs.items():
    print(f"{key}: {value}")
my_function(name="John", age=30)
# Output: {'name': 'John', 'age': 30}

