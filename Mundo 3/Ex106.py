"""
Exercise 106: Interactive Helping System in Python

Create a mini-system that utilizes Python's interactive help (the help() function).
The user will type a command (a function or library name) and the system will
display its documentation.

The system should stop when the user types 'QUIT'.
Additional challenge: Use colors (ANSI escape codes) to make the interface
more readable and distinct for each part of the process.
"""
def ajuda():
    while True:
        intro = 'Helping System Python'
        tam = len(intro) + 4
        print(f'\033[30:42m')
        print('~' * tam)
        print(f'  {intro}')
        print('~' * tam)
        print('\033[m')
        menu = input('Function or Library: ').strip().lower()
        if menu == 'end':
            break
        text = f'Accessing the manual of {menu} command'
        size = len(text) + 4
        print('\033[30:44m')
        print('~' * size)
        print(f'  {text}')
        print('~' * size)
        print(f'\033[m')
        print('\033[7:40m')
        help(menu)
        print('\033[m')

ajuda()
