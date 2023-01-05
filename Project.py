# This is a game of Rock, Paper, Scissors. The user is asked to input a choice of Rock, Paper or
# Scissors. The machine is set to Paper. If the user inputs the same as the machine, the user ties. If
# the user inputs Rock, and the machine is set to Scissors, the user wins. If the user inputs Paper,
# and the machine is set to Rock, the user wins. If the user inputs Scissors, and the machine is set
# to Paper, the user wins.

import random

options = ('Rock', 'Paper', 'Scissor')

machine_wins = 0
user_wins = 0
rounds = 1

while True:
    print('=' * 65)
    print('\t\t\tROUND # ', rounds )
    print('=' * 65)
    
    print('\nMachine wins =>', machine_wins)
    print('\nUser wins =>', user_wins)
    
    user_option = input('\nChoose => Rock, Paper or Scissor => ').capitalize()
    
    rounds += 1
    
    if not user_option in options:
        print('You chose wrong, try again')
        continue
    
    machine = random.choice(options)

    print('User option =>', user_option)
    print('\nComputer option =>', machine)

    if user_option == machine:
        print('\nYou Tied!')
            
    elif user_option == 'Rock':
        if machine == 'Scissor':
            print('\nYou Win!')
            user_wins += 1
        else:
            print('\nYou Lost!')
            machine_wins += 1
                
    elif user_option == 'Paper':
        if machine == 'Rock':
            print('\nYou Win!')
            user_wins += 1
        else:
            print('\nYou Lost!')
            machine_wins += 1
                
    elif user_option == 'Scissor':
        if machine == 'Paper':
            print('\nYou Win!')
            user_wins += 1
        else:
            print('\nYou Lost!')
            machine_wins += 1
        
    if machine_wins == 2:
        print('\n\t\t\tThe winner is => MACHINE!')  
        print('Machine wins =>', machine_wins)
        print('User wins =>', user_wins)
        
    if user_wins == 2:
        print('\n\t\t\tThe winner is => YOU!')
        print('Machine wins =>', machine_wins)
        print('User wins =>', user_wins)  
        break 