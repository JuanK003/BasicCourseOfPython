# An infinite loop.
'''
while True:
    print('Ejecuted')
'''

counter = 0

# Printing the numbers from 1 to 10.
'''
while counter < 10:
    counter += 1
    print(counter)
'''

# Printing the numbers from 1 to 14.
'''
while counter < 20:
    counter += 1
    # Breaking the loop when the counter is equal to 15.
    if counter == 15:
        break
    print(counter)
'''

# Printing the numbers from 1 to 20 except 15.
'''
while counter < 20:
    counter += 1
    # Skipping the number 15.
    if counter == 15:
        continue
    print(counter)
'''