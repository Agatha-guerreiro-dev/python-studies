#Desafio 40: Crie um programa que leia as duas notas de um aluno e calcule sua média.
#Mostrando uma mensagem final de acordo com a média. Média < 5 = reprovado; entre 5 e 6.9 = recuperação.
#nota > 7 aprovado
from time import sleep
print('Vamos cálcular sua média final?')
n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: '))
print('Calculando a média')
sleep(2)
average_grade = (n1 + n2) / 2
if average_grade < 5:
    print(f'\033[31mSinto muito sua nota média é {average_grade:.2f}\n'
          f'Por esse motivo você foi REPROVADO!\033[m')
elif (average_grade >= 5) and (average_grade < 7):
    print(f'\033[33mInfelizmente sua nota foi {average_grade:.2f}.\n'
          f'você não está apto a aprovação direta, terá que passar por recuperação\033[m')
else:
    print(f'\033[32m Parabéns! A Sua nota foi {average_grade:.2f}.\n'
          f'Você foi APROVADO!!!\033[m')
