#Desafio 016: Crie um programa que leia um número real qualquer e mostre na tela sua porção inteira.
from math import trunc
num = float(input('Digite um número real: '))
print(f'A porção inteira de {num} é {trunc(num)}')
