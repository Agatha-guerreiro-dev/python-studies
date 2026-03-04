"""
Exercise 105: Analyzing and Generating Dictionaries

Create a program that has a function called notes() that can receive multiple grades
from several students and will return a dictionary with the following information:

- Total number of grades
- The highest grade
- The lowest grade
- The average grade of the class
- The situation (optional):
    - > 7: GOOD
    - >= 5: REASONABLE
    - < 5: BAD

Add docstrings to the function as well.
"""
def notes(*n,sit=False):
    """
    -> Function to analyse grades and situation of students
    :param n: one or more grades from students
    :param sit: optional value that can return the situation of the average grade from students
    :return: dictionary with valuable information of the class grade
    """
    tot = len(n)
    average = sum(n) / tot
    highest = max(n)
    lowest = min(n)
    data = {
        'total': tot,
        'highest': highest,
        'lowest': lowest,
        'average': average
    }
    if sit:
        if average > 7:
            data['situation'] = 'Good'
        elif average >= 5:
            data['situation'] = 'Reasonable'
        else:
            data['situation'] = 'Bad'
        return data
    else:
        return data

resp = notes(4, 6, 4, sit=True)
print(resp)
help(notes)