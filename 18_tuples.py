# Creating a tuple with numbers and strings.
numbers = (1, 2, 3, 4, 5)
strings = ('Juan', 'Carlos', 'Neil', 'Juan')

# Printing the tuple numbers and strings.
print(numbers)
print(type(numbers))

print(strings)
print(type(strings))

# Printing the first and last element of the tuple.
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])


# Printing the index of the element 'Carlos' in the tuple.
# Counting the number of times the string 'Juan' appears in the tuple.
print(strings)
print(strings.index('Carlos'))
print(strings.count('Juan'))

# Converting the tuple into a list.
my_list = list(strings)
print(my_list)
print(type(my_list))

# Changing the value of the second element of the list.
my_list[1] = 'Carlitos'
print(my_list)

# Converting the list into a tuple.
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))