person = {
    'name' : 'Juan Carlos',
    'last_name' : 'Palacios',
    'langs' : ['C#', 'C', 'Python', 'Java', 'C++'],
    'age' : 19
}
print(person)

# Changing the value of the key 'name' to 'Neil'
person['name'] = 'Neil'

# Adding 10 to the value of the key 'age'
person['age'] += 10

# Adding the string 'MySQL' to the list of languages.
person['langs'].append('MySQL')

# Deleting the key 'last_name' from the dictionary.
del person['last_name']

# It deletes the key 'age' from the dictionary, is necessary to add parameters in the POP method.
person.pop('age')

print(person)

# It prints the items of the dictionary.
print('\nItems =>', person.items())

# It prints the values of the dictionary.
print('\nValues =>', person.values())