"""
Exercise 103: Player Profile

Create a program that has a function called ficha() that receives two optional parameters:
the name of a player and how many goals they scored.

The program must be able to display the player's profile, even if some data has not been
entered correctly (for example, if the name is left empty or the number of goals is not a valid number).
"""
def record(name='Unknow', goals=0):
    if name.strip() == '':
        name = 'Unknow'
    return f'The player {name} scored {goals} goals in the tournament!'


name_input = str(input('Player name: ')).strip().title()
goal_input = str(input('Total goals: ')).strip()
if goal_input.isnumeric():
    goal_input = int(goal_input)
else:
    goal_input = 0
print(record(name_input, goal_input))
