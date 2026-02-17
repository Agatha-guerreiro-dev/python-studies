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
data_base = []
person = {}
age_compiler = []
while True:
    person['name'] = input('Name: ').strip().title()
    while True:
        person['gender'] = input('Gender [W/M/N]: ').strip().upper()
        if person['gender'] in 'WMN':
            break
        else:
            print('Please, select a valid option.')
    age = int(input('Age: '))
    person['age'] = age
    age_compiler.append(age)
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
mean = sum(age_compiler) / people_total
print('-=' * 20)
print(f'The group has {people_total} people.')
print(f'The average age of the group is {mean:.0f} years old')
print('List of registered women: ')
for d in data_base:
    if d['gender'] == 'W':
        print(f'-> {d["name"]}')
print(f'List of people older than the average age:')
for d in data_base:
    if d['age'] > mean:
        print(f'Name: {d["name"]}; Gender: {d["gender"]}; Age: {d["age"]}.')
print('Finish')
