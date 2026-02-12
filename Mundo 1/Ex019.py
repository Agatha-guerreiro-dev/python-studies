#Desafio 019: Um professor quer sortear um dos quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolido.
from random import choice
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
print(f'Parabéns {choice([a1, a2, a3, a4])}!\n'
      f'Você foi sorteado(a) para apagar o quadro.')