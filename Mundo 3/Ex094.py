"""
Exercise 094: Dictionary Union & Statistical Analysis

Create a program that reads the Name, Gender Identity, and Age of several people.
Store each person's data in an individual dictionary, and all dictionaries in a list.
After registering everyone, the program must display:
A) Total number of people registered.
B) The average age of the group.
C) A list containing all the Women (W) registered.
D) A list of all people with an age above the average.
"""
from operator import itemgetter
data_base = []
person = {}
while True:
    person['name'] = input('Name: ').strip().title()
    while True:
        person['gender'] = input('Gender [W/M/N]: ').strip().upper()
        if person['gender'] in 'WMN':
            break
        else:
            print('Please, select a valid option.')
    person['age'] = int(input('Age: '))
    data_base.append(person.copy())
    while True:
        menu = input('Want to continue? [Y/N] ').strip().lower()
        if menu in 'yn':
            break
        else:
            print('Please, select a valid option.')
    if menu in 'n':
        break
people_total = len(data_base)

