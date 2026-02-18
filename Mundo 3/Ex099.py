"""
Exercise 099: Function that finds the greatest value

Create a program that has a function called greatest(), which receives several parameters with integer values.

Your program must analyze all the values and state which one of them is the greatest.
"""
def greatest(*num):
    num = list(num)
    length = len(num)
    if not num:
        num.append(0)
        length = 0
    great = max(num)
    print('-=' * 30)
    print(f'Analyzing all values...')
    print(*num, f' In total {length} values has analyzed...')
    print(f'The greatest value of the total is: {great}')



greatest(1, 2, 3, 4, 5, 23, 89, 4, 91, 12, 14)
greatest(2, 9, 4, 5, 7, 1)
greatest(4, 7, 0)
greatest(1, 2)
greatest(6)
greatest()