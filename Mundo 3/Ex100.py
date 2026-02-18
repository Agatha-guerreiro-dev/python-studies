"""
Exercise 100: Functions to draw and sum

Create a program that has a list called numbers and two functions called draw() and sumEven().

1. draw(): Should draw 5 random numbers and put them inside the list.
2. sumEven(): Should show the sum of all the even values drawn by the previous function.
"""
from random import sample
from time import sleep
def draw():
    # return an array with five random intergen numbers
    randnum = sample(range(1, 21), k=5)
    return randnum


def sumEven(a_list):
    even = []
    for p in a_list:
        if p % 2 == 0:
            even.append(p)
    evtot = sum(even)
    return evtot


collection = draw()
print(f'Drawing {len(collection)} random numbers: ')
for n in collection:
    sleep(0.5)
    print(f'{n} ', end='')
print('End!')
even = sumEven(collection)
print(f'The sum of all the even values from', *collection, f'is = {even}')
