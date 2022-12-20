name = 'Juan'
last_name = 'Palacios'

# Concatenating the two strings.
full_name = name + " " + last_name
print(full_name)

# Printing the string "I'm Juan Palacios"
quote = "I'm Juan Palacios"
print(quote)

# Printing the string "She said "Hello"".
quote2 = 'She said "Hello"'
print(quote2)

# Format
template = 'Hi, my name is: ' + name + ' and my last name is: ' + last_name
print('V1', template)

# Using the format method to replace the {} with the values of the variables name and last_name.
template2 = 'Hi, my name is {} and my last name is {}'.format(name, last_name)
print('V2', template2)

# Using the f-string method to format the string.
template3 = f'Hi, my name is {name} and my last name is {last_name}'
print('V3', template3)