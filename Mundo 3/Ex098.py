"""
Exercise 098: Counter Function

Create a program that has a function called counter(), which receives three parameters: start, end, and step.

The program must perform three counts using the created function:
1. From 1 to 10, in steps of 1.
2. From 10 to 0, in steps of 2.
3. A personalized count:
   The program asks the user for the Start, End, and Step values.
"""
from time import sleep
def counter (a, b, c):
    print('-=' * 30)
    print(f'Counter from {a} until {b} in steps of {c}:')
    if c == 0:
        c = 1
    if c < 0:
        c = abs(c)
    if a > b:
        c = -(c)
        b -= 1
    elif a < b:
        b += 1
    for i in range(a, b, c):
        sleep(0.5)
        print(f'{i}', end=' ')
    print('End!')


counter(1, 10, 1)
counter(10, 0, 2)
print('-=' * 30)
print('Now is your turn: ')
start = int(input('Start: '))
finish = int(input('End: '))
step = int(input('Step: '))
counter(start, finish, step)
