text = 'She knows programming in Python'
text2 = 'hi my name is Juan'

# IN
# Checking if the word is in the text.
print('JavaScript' in text)
print('Python' in text)

# Checking if the word 'Python' is in the text. If it is, it prints 'Very good!', if not, it prints
# 'Nooo!, it's a joke!'.
if 'Python' in text:
    print('Very good!')
else:
    print("Nooo!, it's a joke!")

# LENGTH
# Checking the length of the word 'Love' and 'Love '.
print('LENGHT => len()')
size = len('Love ')
print(size)
size2 = len('Love')
print(size2)
print('\n')

# UPPER
# Printing the text and then printing the text in uppercase.
print('UPPER => upper()')
print(text)
print(text.upper())
print('\n')

# LOWER
# Printing the text and then printing the text in lowercase.
print('LOWER => lower()')
print(text)
print(text.lower())
print('\n')

# COUNT
# Counting the number of times the letter 'm' appears in the text.
print('COUNT => count()')
print(text)
print(text.count('m'))
print('\n')

# SWAPCASE
# Printing the text and then printing the text in swapcase.
print('SWAPCASE => swapcase()')
print(text)
print(text.swapcase())
print('\n')

# STARTSWITH 
# Checking if the text starts with 'She'.
print('STARTSWITH => startswith()')
print(text)
print(text.startswith('She'))
print('\n')

# ENDSWITH
# Checking if the text ends with 'hi'.
print('ENDSWITH => endswith()')
print(text)
print(text.endswith('C++'))
print('\n')

# REPLACE
# Replacing the word 'Python' with the word 'Go'.
print('REPLACE => REPLACE()')
print(text)
print(text.replace('Python', 'Go'))
print('\n')

# CAPITALIZE
# Capitalizing the first letter of the text.
print('CAPITALIZE => capitalize()')
print(text2)
print(text2.capitalize())
print('\n')

# TITLE
# Capitalizing the first letter of each word.
print('TITLE => title()')
print(text2)
print(text2.title())
print('\n')

# ISDIGIT
# Checking if the text is a digit.
print('ISDIGIT => isdigit()')
print(text2)
print(text2.isdigit())
print('\n')