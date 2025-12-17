# TypeError: multi_func() got multiple values for argument 'num1'===> 
# code is commented out to avoid error
# def multi_func(num1, num2):
#     return num1 * num2;
# print(multi_func(5, num1=10))

# Corrected function call====> 
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



