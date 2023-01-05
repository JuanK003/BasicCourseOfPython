# Creating a matrix with 3 lists, each with 3 elements.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

# Printing the second element of the first list in the matrix.
print(matrix[0][1])

# Printing the matrix in a readable format.
for i in matrix:
    print('\nComplet =>',i)
    # Printing the elements of the list one by one.
    # Iterating through the elements of the list `i`.
    for j in i:
        print('one by one =>',j)