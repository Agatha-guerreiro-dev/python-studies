"""
Exercise 101: Functions for voting

Create a program that has a function called vote(), which receives the birth year of a person as a parameter.

The function must return a literal value indicating whether a person has a status of:
- VOTING DENIED
- OPTIONAL VOTING
- MANDATORY VOTING
(Based on their age in the current year).
"""
def vote(b_year):
    from datetime import date
    year_today = date.today().year
    age = year_today - b_year
    if age < 16:
        return f'With {age} year old: Voting Denied!'
    elif  16 <= age < 18 or age >= 70:
        return f'With {age} years old: Optional Voting!'
    else:
        return f'With {age} years old: Mandatory Voting!'



birth = int(input('What is your year of birth?: '))
print(vote(birth))
