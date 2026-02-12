#Desafio 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número: '))
n3 = int(input('Digite um terceiro número: '))
numeros = [n1, n2, n3]
print(f'O maior valor é {max(numeros)}')
print(f'O menor valor é {min(numeros)}')
