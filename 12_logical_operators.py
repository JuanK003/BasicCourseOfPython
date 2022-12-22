# AND
print('AND')

# Printing the string 'True and True =>' and then the result of the expression True and True.
print('True and True =>', True and True) # True
print('True and False =>', True and False) # False
print('False and True =>', False and True) # False
print('False and False =>', False and False) # False

# Checking if 10 is greater than 5 and 5 is less than 10.
print(10 > 5 and 5 < 10) # True
print(10 > 5 and 5 > 10) # False

# Asking the user to input a stock number and then checking if the stock number is between 100 and 1000.
stock = input('Ingrese el numero de stock ')
stock = int(stock)
print(stock >= 100 and stock <= 1000)

# OR
print('OR')

# Printing the string 'True or True =>' and then the result of the expression True or True.
print('True or True =>', True or True) # True
print('True or False =>', True or False) # True
print('False or True =>', False or True) # True
print('False or False =>', False or False) # False

# Asking the user to input a role and then checking if the role is either admin or seller.
role = input('Digaita el rol => ')
print(role == 'admin' or role == 'seller')

# NOT 

# Printing the opposite of the boolean value.
print(not True)
print(not False)

print('NOT AND')

# Printing the string 'True and True =>' and then the result of the expression not (True and True).
print('True and True =>', not (True and True)) # False
print('True and False =>', not (True and False)) # True
print('False and True =>', not (False and True)) # True
print('False and False =>', not (False and False)) # True

# Asking the user to input a stock number and then checking if the stock number is not between 100 and 1000.
stock = input('Ingrese el numero de stock =>')
stock = int(stock)
print(not (stock >= 100 and stock <= 1000))