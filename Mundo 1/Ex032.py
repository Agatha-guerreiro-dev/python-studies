#Desadio 032: Faça um programa que leia um ano e mostre se ele é um ano bissexto.
year = int(input('Digite um ano: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'O ano {year} é BISSEXTO!')
else:
    print(f'O ano {year} NÃO é bissexto!')
#Errei :(
#Está salvo o jeito mais lógio