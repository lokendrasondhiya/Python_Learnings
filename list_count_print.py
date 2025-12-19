# Counting iterations in nested loops and printing values
count = 0
for x in [0, 2, 1, 3]:
    for y in [0, 4, 1, 2]:
        print('x')
        count = count + 1
        print(count, ":", x, y)
print("Total iterations:", count)   # Output: 16    