"""
Exercise 095: Enhanced Soccer Player Management System

Improve the code from Exercise 093 to allow the registration of MULTIPLE players.
The system should include:

1. Registration Loop:
   - Read Name, Number of Matches, and Goals for each match.
   - Store each player (dictionary) inside a main list (database).
   - Ask if the user wants to continue adding players (Y/N).

2. Summary Table:
   - Display a formatted table showing the Index (Code), Name, Goals List, and Total Goals for all players.

3. Data Visualization System:
   - Ask the user for a Player's Code (Index) to see details.
   - If the code is valid, show the match-by-match breakdown (e.g., "In match 1, scored 2 goals").
   - If the code is 999, stop the program.
   - Loop until the user decides to stop.
"""
players_data_base = []
player = {}
matches = []
while True:
    player['name'] = input('Player name: ').strip().title()
    counter = int(input(f'How many matches {player["name"]} played? '))
    for i in range(counter):
        goals = int(input(f'How many goals in the {i + 1}° match? '))
        matches.append(goals)
    player['matches'] = matches[:]
    players_data_base.append(player.copy())
    matches.clear()
    while True:
        menu = input('Want to continue? [Y/N] ').strip().lower()
        if menu in 'yn':
            break
        else:
            print('Please select a valid option.')
    if menu in 'n':
        break
print('-=' * 60)
print(f'{"CODE":<4} {"NAME":<15} {"GOALS":<25} {"TOTAL":<5}')
print(f'-' * 60)
for pos, p in enumerate(players_data_base):
    print(f'{pos:>3} {p["name"]:<15} {str(p["matches"]):<25} {sum(p["matches"]):<5}')
print(f'-' * 60)
while True:
    while True:
        ipl = int(input('Show the statistics for which player? [Type 999 to finish] '))
        if ipl <= (len(players_data_base) - 1):
            break
        elif ipl == 999:
            break
        else:
            print(f'\033[31m ERROR, player {ipl} does not exist. Try again.\033[m')
            print('-' * 40)
    if ipl == 999:
        print('-' * 40)
        break
    print(f'-- Player {players_data_base[ipl]["name"]} history: ')
    for pos, g in enumerate(players_data_base[ipl]["matches"]):
        print(f'In the game {pos + 1} scored {g} goals.')
    print('-' * 40)
print(f'FINISH')
