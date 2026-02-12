#Desafio 89: Crie um programa que leia o nome e duas notas de vários alunos
# e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um
#E permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista = list()
aluno = list()
nota = list()
data_a = list()
data_n = list()
while True:
    nome = str(input('Nome: ')).strip().title()
    data_a.append(nome)
    n1 = float(input('Nota 1: ').replace(',', '.'))
    n2 = float(input('Nota 2: ').replace(',', '.'))
    data_n.append(n1)
    data_n.append(n2)
    data_a.append(data_n[:])
    lista.append(data_a[:])
    data_a.clear()
    data_n.clear()
    while True:
        menu = str(input('Deseja continuar? [S/N] ')).strip().lower()
        if menu in 'sn':
            break
        else:
            print('Por favor, digite uma opção válida.')
    if menu == 'n':
        break
print('-=' * 26)
print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-' * 26)
for c in range(len(lista)):
    media = sum(lista[c][1]) / len(lista[c][1])
    print(f'{c:<4} {lista[c][0]:<10} {media:>8.1f}')
print('-' * 26)
while True:
    opt = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if opt == 999:
        print('Adeus!')
        break
    print(f'Notas de {lista[opt][0]} são: {lista[opt][1]}')
    print('-' * 26)
