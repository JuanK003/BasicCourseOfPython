import random

options = ('Rock', 'Paper', 'Scissor')

# Asking the user to input a choice of Rock, Paper or Scissors.
user_option = input('Choose => Rock, Paper or Scissor => ').capitalize()

if not user_option in options:
    print('Invalid option')
    
machine = random.choice(options)

print('User option =>', user_option)
print('\nComputer option =>', machine)

# This is a game of Rock, Paper, Scissors. The user is asked to input a choice of Rock, Paper or
# Scissors. The machine is set to Paper. If the user inputs the same as the machine, the user ties. If
# the user inputs Rock, and the machine is set to Scissors, the user wins. If the user inputs Paper,
# and the machine is set to Rock, the user wins. If the user inputs Scissors, and the machine is set
# to Paper, the user wins.

if user_option == machine:
    print('\nYou Tied!')
    
elif user_option == 'Rock':
    if machine == 'Scissor':
        print('\nYou Win!')
    else:
        print('\nYou Lost!')
        
elif user_option == 'Paper':
    if machine == 'Rock':
        print('\nYou Win!')
    else:
        print('\nYou Lost!')
        
elif user_option == 'Scissor':
    if machine == 'Paper':
        print('\nYou Win!')
    else:
        print('\nYou Lost!')