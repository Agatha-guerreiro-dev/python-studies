"""
Exercise 091: Dice Game

Create a program where 4 players throw a die (1 to 6) and have random results.
Store these results in a dictionary.
Finally, put the dictionary in order based on the highest values (ranking),
so that the winner is shown first.
Note: Use a time delay (sleep) to make the game more exciting.
"""
from random import randint
from time import sleep
from operator import itemgetter
game ={}
print(f'Lets roll the dices')
for i in range(0, 4):
    sleep(0.5)
    game[f'player {i + 1}'] = randint(1, 6)
    print(f'The player {i + 1} rolled an {game[f"player {i + 1}"]} on the dice')
print('Players Rankings')
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
for i, (name, score) in enumerate(ranking):
    print(f'{i + 1}° place: {name} with {score}')
    if i == 2:
        break
