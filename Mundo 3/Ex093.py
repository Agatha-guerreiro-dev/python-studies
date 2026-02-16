"""
Exercise 093: Soccer Player Management

Create a program that manages a soccer player's performance.
The program will read the player's name and how many matches they played.
Then, it will read the number of goals scored in each match.
All this data, including the total number of goals scored during the season,
must be stored in a dictionary.
"""
player_history = {}
matches = []
player_history['name'] = input('Player name: ').strip().title()
player_history['goals'] = matches
matchs_played = int(input(f'How many matches {player_history["name"]} played? '))
for c in range(matchs_played):
    goal = int(input(f'How many goals in the {c + 1} match? '))
    matches.append(goal)
player_history['total'] = sum(matches)
print('-=' * 20)
print(player_history)
print('-=' * 20)
for k, v in player_history.items():
    print(f'- {k} is: {v}')
print('-=' * 20)
print(f'the player {player_history["name"]} played {len(matches)} matches.')
for pos,c in enumerate(matches):
    print(f'   => In the {pos + 1}° match, scored {c} goals')
