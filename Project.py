# Asking the user to input a choice of Rock, Paper or Scissors.
user_option = input('Choose => Rock, Paper or Scissors => ').capitalize()
machine = 'Paper'

# This is a game of Rock, Paper, Scissors. The user is asked to input a choice of Rock, Paper or
# Scissors. The machine is set to Paper. If the user inputs the same as the machine, the user ties. If
# the user inputs Rock, and the machine is set to Scissors, the user wins. If the user inputs Paper,
# and the machine is set to Rock, the user wins. If the user inputs Scissors, and the machine is set
# to Paper, the user wins.

if user_option == machine:
    print('You Tied!')
    
elif user_option == 'Rock':
    if machine == 'Scissors':
        print('You Win!')
    else:
        print('You Lost!')
        
elif user_option == 'Paper':
    if machine == 'Rock':
        print('You Win!')
    else:
        print('You Lost!')
        
elif user_option == 'Scissors':
    if machine == 'Paper':
        print('You Win!')
    else:
        print('You Lost!')