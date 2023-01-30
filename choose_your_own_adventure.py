name = input('Type your name:')
print('Welcome', name, 'to this adventure!')

answer = input('Your are on a dirt road, it has come to an end and you can go lef or right. Which way would you like to go? ').lower()

if answer == 'left':
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim. ")
    
    if answer == 'swim':
        print('You swam across and were eaten by an alligator.')
    elif answer == 'walk':
        print('You walk for many miles, ran out of water and lost the game.')
    else:
        print('Not a valid option.')


elif answer == 'right':
    answer = input('You come to a bridge, it looks wobbly, do you want to creoss it or head back? (cross/back) ').lower()
    if answer == 'back':
        print('You go back and lost.')
    elif answer == 'cross':
        anwer = input('You cross the bridge at meet a stranger. Do you talk to them(YES/NO) ').lower()

        if answer == 'yes':
            print('You talk to the stranger and they give you gold. YOU WIN!')

        elif answer == 'no':
            print('You ignored the stranger and they are offended and you lose. YOU LOSE!')
        
        else:
            print('Not a valid option.')

            
    else:
        print('Not a valid option.')

else:
    print('That is not a valid option. You lose.')

print('Thanks for playing!', name)
