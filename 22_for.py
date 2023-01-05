# Printing the numbers 0-19.
'''
# Creating a list of numbers from 0 to 19.
for element in range(20):
    print(element)
'''

# Printing the elements in the list.
'''
my_list = [23, 45, 66, 11, 2, 100]
# Iterating through the list and assigning each element to the variable `element`.
for element in my_list:
    print(element)
'''

# Iterating through the tuple and assigning each element to the variable `element`.
'''
mytuple = ('juan', 'jilio', 'manolo')
for element in mytuple:
    print(element)
'''

# Iterating through the dictionary and printing the key and value of each element.
'''
product = {
    'name' : 'T-Shirt',
    'price' : 100,
    'stock' : 89
}
# First option
for element in product:
    print(element, '=>', product[element])
    
# Second option
for key, value in product.items():
    print(key, '=>', value)
'''

# Iterating through the list of dictionaries and printing the key and value of each element.
people = [
    {
        'name' : 'Juan',
        'age' : 19
    },
    {
        'name' : 'Luis',
        'age' : 22
    },
    {
        'name' : 'Peter',
        'age' : 54
    }
]
for person in people:
    print('people =>', person)
    print('name =>', person['name'])
    print('age =>', person['age'])