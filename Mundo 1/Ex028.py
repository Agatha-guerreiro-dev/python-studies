#Desafio 028: Escreva um programa que faça o computador digitar um número entre 0 e 5
#E peça para o usuário advinhar o número. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randrange
n = randrange(6)
user = int(input('Digite um número de 0 a 5 e tente adivinhar qual o computador escolheu: '))
if user == n:
    print('Parabéns, você venceu!')
else:
    print('Sinto muito, você perdeu!')
print(f'O número sorteado foi {n}')
