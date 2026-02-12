#Desafio 020: O mesmo professor que sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
deck = [a1, a2, a3 ,a4]
shuffle(deck)
print('A ordem será:')
print(*deck, sep=', ')
#O * tira os itens da caixa. O sep=', ' coloca uma vírgula entre eles.