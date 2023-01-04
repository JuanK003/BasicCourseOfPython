# Creating a dictionary with the name my_dictionary and it is printing the type of the variable and
# the variable itself.
my_dictionary = {
    'airplane' : 'It is a means of air transport',
    'name' : 'Juan Carlos Neil',
    'last_name' : 'Palacios Escobar',
    'age' : 19
}
print(type(my_dictionary))
print(my_dictionary)

# Printing the value of the key 'age' and the value of the key 'last_name'
print(my_dictionary['age'])
print(my_dictionary['last_name'])

# Printing the value of the key 'name' and it is printing 'None' because the key 'car' does not exist.
print(my_dictionary.get('name'))
print(my_dictionary.get('car'))

# Checking if the key 'airplane' and 'dog' are in the dictionary.
print('airplane' in my_dictionary)
print('dog' in my_dictionary)