if True:
    print('This is greeting')

if False:
    print("This isn't greeting")

# Asking the user to input a pet. If the pet is Dog, Fish, Tiger, or Cat, then it will print
# 'Congratulations!' or 'Good luck with that!'. If the pet is not Dog, Fish, Tiger, or Cat, then it
# will print 'You don't have any pets! xD'.
pet = input('Who is your favorite pet? ')
if pet == 'Dog':
    print('Congratulations!')

elif pet == 'Fish':
    print('Congratulations!')
    
elif pet == 'Tiger':
    print('Good luck with that!!')
    
elif pet == 'Cat':
    print('Good luck with that!')
    
else :
    print("You don't have any pets! xD")
    
# Asking the user to input a number. If the number is between 100 and 1000, then it will print 'The
# stock is correct!'. If the number is not between 100 and 1000, then it will print 'The stock is incorrect!'.
stock = int(input('Type the stock ➙ '))

if stock >= 100 and stock <= 1000:
    print('The stock is correct!')
    
else:
    print('The stock is incorrect!')