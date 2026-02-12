#Desafio 074: Crie um programa que vai gerar cinco números aleatórios e colocalos numa tupla.
#Depois disso, mostre a lista de número gerados e mostre o maior e o menor número da tupla.
from random import randint
numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print('-=' * 20)
print(numeros)
print('-=' * 20)
print(f'O maior número é: {max(numeros)}')
print('-=' * 20)
print(f'O menor número é: {min(numeros)}')
