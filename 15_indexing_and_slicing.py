text = 'She knows Python'

# INDEXING
# Printing the 5th character in the string.
print(text[4])
# The above code is printing the last character of the string.
size = len(text)
print('size => ', size)
print(text[size - 1])
print(text[-1])

# SLICING
# Printing the characters from 0 to 5.
print(text[0:5])
# Printing the characters from 0 to 10.
print(text[0:10])
print(text[:10])
print(text[5:-1])
# Printing the characters from 5 to the last character.
print(text[5:])
# Printing the entire string.
print(text[:])
# Printing the characters from 5 to 10 with a step of 2.
print(text[5:10:1])
print(text[5:10:2])
# Printing the characters from 0 to the last character with a step of 2.
print(text[::2])