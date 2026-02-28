"""
Exercise 102: Factorial Function

Create a program that has a function called factorial() that receives two parameters:
1. The number to calculate.
2. An optional logical value (e.g., show=False) indicating whether or not to show the calculation process on the screen.

The function must also include a docstring explaining its operation and parameters.
"""
def factorial(n, show = False):
    if n == 0:
        return '0 x 0 = 0'
    steps = []
    subtrator = n
    factorial = n
    steps.append(n)
    while subtrator != 1:
        subtrator -= 1
        factorial *= subtrator
        if show:
            steps.append(subtrator)
    if n != 0 and show:
        for pos, i in enumerate(steps):
            if pos == len(steps) - 1:
                print(f'{i} ', end = '')
            else:
             print(f'{i} x ', end = '')
        return f'= {factorial}'
    else:
        return factorial


num = int(input('Type a number: '))
print(factorial(num, show=True))