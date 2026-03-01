"""
Exercise 104: Validating Data Input in Python

Create a program that has a function called readInt(), which will work similarly
to Python's built-in input() function, but will include data validation to ensure
that only a numeric (integer) value is accepted.

If the user types something that is not a valid integer, the program should display
an error message and prompt the user to type the value again, repeating this
until a valid number is entered.

Example of usage:
n = readInt('Type a number: ')
"""
def readint(text):
    while True:
        number = input(f'{text}')
        if number.isnumeric():
            number = int(number)
            return number
        else:
            print(f'\033[31m ERROR! Type a valid number.\033[m')


n = readint('Type a number: ')
print(f'You just typed the number {n}')
