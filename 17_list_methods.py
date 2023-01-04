# CRUD -> Create, Read, Update & Delete

# The first line is creating a list of numbers. The second line is printing the second number in the
# list. The third line is changing the last number in the list to 10. The fourth line is printing the
# list.
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1])
numbers[-1] = 10
print(numbers)

# Creating a list of numbers.
crud = [1, 2, 3, 4, 5, 6]

# Printing or Reading the second number in the list.
print(crud[1])

# Adding 700 to the end of the list.
crud.append(700)
print(crud)

# Adding the string 'Hi number' to the beginning of the list and the string 'Change' to the
# fourth position in the list.
crud.insert(0, 'Hi number')
print(crud)
crud.insert(4, 'Change')
print(crud)

# Adding the list tasks to the list crud.
tasks = ['j', 'u', 'a', 'n']
new_list = crud + tasks
print(new_list)

# Finding and Update the index of the letter 'n' in the list new_list and then changing the letter
# 'n' to 'change'.
index = new_list.index('n')
new_list[index] = 'change'
print(new_list)

# Removing the letter 'j' from the list new_list.
new_list.remove('j')
print(new_list)

# Removing the last item in the list.
new_list.pop()
print(new_list)

# Removing the first item in the list.
new_list.pop(0)
print(new_list)

# Reversing the list.
new_list.reverse()
print(new_list)

# Creating a list of numbers and then sorting the list from smallest to largest.
another_numbers = [1, 4, 2, 0, 33, 10, 3]
another_numbers.sort()
print(another_numbers)

# Creating a list of strings and then sorting the list from smallest to largest.
strings = ['re', 'ab', 'fg']
strings.sort()
print(strings)