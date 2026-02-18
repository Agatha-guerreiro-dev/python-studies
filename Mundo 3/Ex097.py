"""
Exercise 097: Special Print

Create a program that has a function called write(), which receives any text as a parameter and displays it with an adaptive border.

Example:
write('Hello World')

(Note: The border must adjust automatically to the length of the string, with some padding).
"""
def write(msg):
    size = len(msg) + 4
    print('-' * size)
    print(f'  {msg}')
    print('-' * size)


write('Hello World')
