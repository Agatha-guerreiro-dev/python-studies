#Desafio 60: Faça um programa que leia um número qualquer e mostre o seu fatorial.
n = int(input('Digite um número para calcular o fatorial: '))
subtrator = n
fatorial = n
while subtrator != 1:
    subtrator -= 1
    fatorial *= subtrator
print(f'O resultado de {n}! é = {fatorial}')
#meu programa não funciona para o 0, dps voltar para corrigir
