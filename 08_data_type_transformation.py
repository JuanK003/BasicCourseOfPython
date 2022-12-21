# Defining the variable name and then printing the type of the variable.
name = 'Juan'
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

age = 19
# Concatenating the string "I'm " with the variable age, which is an integer, so it needs to be
# converted to a string. Then it is concatenating the string ' years old' to the end of the string.
print("I'm " + str(age) + ' years old')
# Using the f-string method to print the string and the variable age.
print(f"I'm {age} years old")

# Asking the user to input their age and then it is printing the type of the variable.
# Then it is converting the variable to an integer and printing the string and the variable.
age2 = input ('How old are you => ')
print(type(age2))
int_age = int(age2)
print(f"You're {int_age} years old")