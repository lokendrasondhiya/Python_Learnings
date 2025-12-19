# 3D list : created using list comprehension
# note: using loops to create 3D list
matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix[1][1][1])  # Output: 1

# 3D List : second element in the third row, first sub-list
Colors= [ [['Blue','Green','White','Black']],
          [['Green','Blue','White','Yellow']],
          [['White','Blue','Red','Green']] ]
print(Colors[2][0][2])  # Output: Red

# 3D list : created by directly specifying values
matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]],
          [[0, 1, 2], [0, 1, 2], [0, 1, 2]],
          [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
print(matrix[0][0][0])   # Output: 0
print(matrix[2][2][2])   # Output: 2

# 3D list : written in another way as below to create the same 3D list
# note: using loops to create 3D list
matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix[1][2]) # Output: [0, 1, 2]
print(matrix[1][2][1])  # Output: 1

# 2D List : third element in the second row, second sub-list
Colors = [ ['Red', 'Green', 'White', 'Black'],
          ['Green', 'Blue', 'White', 'Yellow'],
          ['White', 'Blue', 'Green', 'Red'] ]
print(Colors[1][2])   # Output: White

# New list created by copying elements from a 3D list
# note: matrix2 is now a 2D list
matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]],
          [[0, 1, 2], [0, 1, 2], [0, 1, 2]],
          [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[2][2])  # Output: 2