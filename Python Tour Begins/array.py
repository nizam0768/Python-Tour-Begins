# Creating a list (array-like)
arr = [1, 2, 3, 4, 5]

# Accessing elements
print(arr[0])  # Output: 1

# Adding elements
arr.append(6)

# Removing elements
arr.remove(3)

# Iterating through list
for item in arr:
    print(item)
print("2-D array")
# 2D Array (Matrix) using a list of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements (row 1, col 2)
print(matrix[0][1])  # Output: 2

# Iterating through 2D array
for row in matrix:
    for col in row:
        print(col, end=' ')
    print()

