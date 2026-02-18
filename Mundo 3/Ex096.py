"""
Exercise 096: Area Calculation Function

Create a program that has a function called area(), which receives the dimensions of a rectangular terrain (width and length) and displays the area of the terrain.

The program must:
1. Define a function area(width, length) that calculates the area and prints a formatted message showing the dimensions and the total area in m².
2. In the main program, read the Width (m) and Length (m) from the user.
3. Call the area() function passing the input values as parameters.
"""
def area(a, b):
    result = a * b
    print(f'The area of a terrain {a:.1f} x {b:.1f} is {result:.1f}m²')


print('-' * 50)
print(f'{"Control of Terrains":^50}')
print('-' * 50)
width = float(input('Width (m): '))
length = float(input('Length (m): '))
area(width, length)
