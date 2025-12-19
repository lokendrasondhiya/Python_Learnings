# tuples is a built-in data type in Python that allows you to store multiple items in a single variable.
# Tuples are similar to lists, but they are immutable, meaning that once a tuple is created, its elements cannot be changed, added, or removed.
# Tuples are defined by enclosing the elements in parentheses () and separating them with commas.

# Example: 1
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
your_tuple = "apple", "banana", "cherry"
ours_tuple = tuple([10, 20, 30]) # Using the tuple() constructor, converting a list to a tuple
print("Original Tuple:", my_tuple)
# Output: Original Tuple: (1, 2, 3, 4, 5)
print("Your Tuple:", your_tuple)
# Output: Your Tuple: ('apple', 'banana', 'cherry')
print("Ours Tuple:", ours_tuple)
# Output: Ours Tuple: (10, 20, 30)

# Example: 2
# Accessing elements in a tuple
print("First Element:", my_tuple[0])  # Accessing the first element
# Output: First Element: 1
print("Last Element:", my_tuple[-1])  # Accessing the last element
# Output: Last Element: 5

# Example: 3
# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked Values:", a, b, c, d, e)
# Output: Unpacked Values: 1 2 3 4 5

# Example: 4
# Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("Concatenated Tuple:", combined_tuple)
# Output: Concatenated Tuple: (1, 2, 3, 4, 5, 6)


# Example: 5
# Tuple methods
my_tuple = (1, 2, 3, 4, 5)
print("Count of 2:", my_tuple.count(2))  # Counting occurrences of an element
# Output: Count of 2: 1
print("Index of 4:", my_tuple.index(4))  # Finding the index of an element
# Output: Index of 4: 3


# Example: 6
# Iterating through a tuple
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print("Tuple Item:", item)
# Output:
# Tuple Item: 1
# Tuple Item: 2
# Tuple Item: 3
# Tuple Item: 4
# Tuple Item: 5


# Example: 7
# Nested tuples
nested_tuple = (1, 2, (3, 4), 5)
print("Nested Tuple:", nested_tuple)
# Output: Nested Tuple: (1, 2, (3, 4), 5)
print("Accessing Nested Element:", nested_tuple[2][1])  # Accessing element in nested tuple
# Output: Accessing Nested Element: 4


# Example: 8
# Tuple with different data types
mixed_tuple = (1, "hello", 3.14, True)
print("Mixed Tuple:", mixed_tuple)
# Output: Mixed Tuple: (1, 'hello', 3.14, True)


# Example: 9
# Slicing a tuple
my_tuple = (1, 2, 3, 4, 5)
sliced_tuple = my_tuple[1:4]
print("Sliced Tuple:", sliced_tuple)
# Output: Sliced Tuple: (2, 3, 4)

# Example: 10
# Tuple length
my_tuple = (1, 2, 3, 4, 5)
print("Length of Tuple:", len(my_tuple))
# Output: Length of Tuple: 5


# Example: 11
# Single element tuple
single_element_tuple = (42,)
print("Single Element Tuple:", single_element_tuple)
# Output: Single Element Tuple: (42,)


# Example: 12
# Tuple repetition
repeated_tuple = (1, 2, 3) * 3
print("Repeated Tuple:", repeated_tuple)
# Output: Repeated Tuple: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Example: 13
# Checking membership in a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Is 3 in Tuple?", 3 in my_tuple)
# Output: Is 3 in Tuple? True
print("Is 6 in Tuple?", 6 in my_tuple)
# Output: Is 6 in Tuple? False


# Example: 14
# Tuple comparison ??
# note: tuples are compared element by element. i.e., the first elements are compared, and if they are equal, the second elements are compared, and so on.
# and soon as a difference is found, the comparison is decided.
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print("Is tuple1 < tuple2?", tuple1 < tuple2)
# Output: Is tuple1 < tuple2? True


# Example: 15
# Using tuples as dictionary keys
my_dict = { (1, 2): "point A", (3, 4): "point B" }
print("Dictionary Value for (1, 2):", my_dict[(1, 2)])
# Output: Dictionary Value for (1, 2): point 

# Example: 16
# Swapping variables using tuples
a = 5
b = 10
a, b = b, a
print("Swapped Values: a =", a, ", b =", b)
# Output: Swapped Values: a = 10 , b = 5


# Example: 17
# Converting a tuple to a list and vice versa
my_tuple = (1, 2, 3, 4, 5)
tuple_to_list = list(my_tuple)
print("Tuple to List:", tuple_to_list)
# Output: Tuple to List: [1, 2, 3, 4, 5]
list_to_tuple = tuple(tuple_to_list)
print("List to Tuple:", list_to_tuple)
# Output: List to Tuple: (1, 2, 3, 4, 5)

# Example: 18
# empty tuple
empty_tuple = ()
print("Empty Tuple:", empty_tuple)
# Output: Empty Tuple: ()


# Example: 19
# Tuple with mutable elements
mutable_tuple = (1, 2, [3, 4], 5)
print("Original Mutable Tuple:", mutable_tuple)
mutable_tuple[2][0] = 99  # Modifying the list inside the tuple
print("Modified Mutable Tuple:", mutable_tuple)
# Output: Modified Mutable Tuple: (1, 2, [99, 4], 5)

# ----------------remaining little advanced , examples (20-28) ----------------------------------
# Immutability error handling - showing TypeError when trying to modify
# zip() - combining tuples
# enumerate() - index + value iteration
# Extended unpacking with * - splitting tuple into parts
# Named tuples - structured tuple access with .x, .y attributes
# Sorting tuples - with and without key function
# Tuples as return values - unpacking multiple returns
# Performance comparison - tuple vs list memory usage


# Example: 20
# Tuple immutability - attempting to modify raises TypeError
my_tuple = (1, 2, 3, 4, 5)
try:
    my_tuple[0] = 99  # This will raise an error
except TypeError as e:
    print("Error:", e)
# Output: Error: 'tuple' object does not support item assignment


# Example: 21
# zip() function with tuples - combines multiple iterables into tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped = zip(tuple1, tuple2)
print("Zipped Tuples:", list(zipped))
# Output: Zipped Tuples: [(1, 'a'), (2, 'b'), (3, 'c')]


# Example: 22
# enumerate() with tuples - get index and value while iterating
my_tuple = ('apple', 'banana', 'cherry')
for index, value in enumerate(my_tuple):
    print(f"Index: {index}, Value: {value}")
# Output:
# Index: 0, Value: apple
# Index: 1, Value: banana
# Index: 2, Value: cherry


# Example: 23
# Extended unpacking with * operator
my_tuple = (1, 2, 3, 4, 5)
first, *middle, last = my_tuple
print("First:", first)
print("Middle:", middle)
print("Last:", last)
# Output:
# First: 1
# Middle: [2, 3, 4]
# Last: 5


# Example: 24
# Named tuples - creating structured tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print("Point:", p)
print("X coordinate:", p.x)
print("Y coordinate:", p.y)
# Output:
# Point: Point(x=10, y=20)
# X coordinate: 10
# Y coordinate: 20


# Example: 25
# Sorting tuples - sorted() returns a list
my_tuple = (5, 2, 8, 1, 9)
sorted_tuple = tuple(sorted(my_tuple))
print("Sorted Tuple:", sorted_tuple)
# Output: Sorted Tuple: (1, 2, 5, 8, 9)


# Example: 26
# Sorting tuple of tuples by specific element
students = (("Alice", 85), ("Bob", 75), ("Charlie", 90))
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted by score:", sorted_students)
# Output: Sorted by score: [('Bob', 75), ('Alice', 85), ('Charlie', 90)]


# Example: 27
# Tuple as function return values - returning multiple values
def get_coordinates():
    return (10, 20, 30)  # Returns a tuple

x, y, z = get_coordinates()
print(f"Coordinates: x={x}, y={y}, z={z}")
# Output: Coordinates: x=10, y=20, z=30


# Example: 28
# Performance comparison: tuple vs list (tuple is faster for immutable data)
import sys
my_tuple = (1, 2, 3, 4, 5)
my_list = [1, 2, 3, 4, 5]
print("Tuple size in bytes:", sys.getsizeof(my_tuple))
print("List size in bytes:", sys.getsizeof(my_list))
# Output: Tuple size in bytes: 56, List size in bytes: 64 (tuple uses less memory)








