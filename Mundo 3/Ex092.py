"""
Exercise 092: Worker Registry

Create a program that reads name, birth year and work permit (CTPS) and registers
them (with age) in a dictionary.
If the CTPS is different from 0, the dictionary will also receive the hiring year
and the salary.
Calculate and add to the dictionary the age at which the person will retire.
For this exercise consider 35 years of working for retirement
"""
from datetime import date
register = {}
date_y = date.today().year
register['name'] = input('Name: ').strip().title()
register['age'] = date_y - int(input('Birth year: '))
register['ctps'] = int(input('Work permit (0 if none): '))
if register['ctps'] != 0:
    register['hiring'] = int(input('Hiring year: '))
    register['salary'] = float(input('Salary: '))
    register['retire'] = (35 - (date_y - register['hiring'])) + register['age']
for k, v in register.items():
    print(f'- {k.title()} is: {v}.')
