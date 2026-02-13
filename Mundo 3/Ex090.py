"""
Exercise 090: Student's Mean and Status

Write a program that reads a student's name and average grade.
Store this information in a dictionary, along with the student's passing status.
- If the average is 7 or higher, the status is "Passed" (Aprovado).
- If the average is below 7, the status is "Failed" (Reprovado).
Finally, display the dictionary content nicely formatted on the screen.
"""
students = []
student_data = {}
grades_repository = []
while True:
    student_data['name'] = input('Name: ').strip().title()
    grade1 = float(input('Tell me the first grade: '))
    grade2 = float(input('Tell me the second grade: '))
    student_data['grade_1'] = grade1
    student_data['grade_2'] = grade2
    grades_repository.append(grade1)
    grades_repository.append(grade2)
    average = sum(grades_repository) / len(grades_repository)
    student_data['mean'] = average
    students.append(student_data.copy())
    grades_repository.clear()
    while True:
        validation = input('Do you want to continue? [Y/N] ').strip().lower()
        if validation in 'yn':
            break
        else:
            print('Please select a valid option.')
    if validation == 'n':
        break
print('-' * 20)
for student in students:
    print(f'Student name: {student["name"]}')
    print(f'Student mean: {student["mean"]:.1f}')
    print(f'Student status:\033[32m Approved\033[m' if student["mean"] >= 7 else f'Student status:\033[31m Failed\033[m')
    print('-' * 20)
