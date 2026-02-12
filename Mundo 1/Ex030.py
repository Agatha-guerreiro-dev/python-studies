#Desafio 030: Crie um programa que leia um número inteiro e diga se ele é par ou impar.
numero = int(input('Digite um número: '))
if numero%2 == 0:
    print(f'O seu número {numero} é par.')
else:
    print(f'O seu número {numero} é ímpar.')
