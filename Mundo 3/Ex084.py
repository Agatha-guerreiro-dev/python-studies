#Desafio 84: Faça um programa que leia o nome e peso de várias pessoas.
#Guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
data = list()
clientes = list()
peso_cli = list()
mais_peso = list()
menos_peso = list()
med_peso = list()
counter = 0
while True:
    nome = str(input('Nome: ')).strip().title()
    peso = float(input('Peso: ').replace(',', '.'))
    data.append(nome)
    data.append(peso)
    clientes.append(data[:])
    counter += 1
    data.clear()
    while True:
        menu = str(input('Deseja continuar: [S/N] ')).strip().lower()
        if menu in 'sn':
            break
        else:
            print('Por favor, escolha uma opção válida!')
    if menu == 'n':
        clientes = tuple(clientes)
        break
for _, peso in clientes:
    peso_cli.append(peso)
med_peso_total = sum(peso_cli) / counter
pessoa_mais_peso = max(peso_cli)
pessoa_menos_peso = min(peso_cli)
for nome, peso in clientes:
    if peso > med_peso_total:
        data.append(nome)
        data.append(peso)
        mais_peso.append(data[:])
        data.clear()
    elif peso == med_peso_total:
        data.append(nome)
        data.append(peso)
        med_peso.append(data[:])
        data.clear()
    else:
        data.append(nome)
        data.append(peso)
        menos_peso.append(data[:])
        data.clear()
print('-=' * 30)
print(f'No total foram cadastrados {counter} clientes.')
print('-=' * 30)
print('Os clientes mais pesados são: ')
for nome, peso in mais_peso:
    if peso == pessoa_mais_peso:
        print(f'\033[31m {nome} com {peso} kg é o(a) cliente mais pesado\033[m')
    else:
        print(f'{nome} com {peso} kg')
if len(med_peso) > 0:
    print('-=' * 30)
    print('Os clientes que se enquandram dentro da média de peso são: ')
    for nome, peso in med_peso:
        print(f'{nome} com {peso} kg')
print('-=' * 30)
print('Os clientes mais leves são: ')
for nome, peso in menos_peso:
    if peso == pessoa_menos_peso:
        print(f'\033[33m {nome} com {peso} kg é o(a) cliente mais leve\033[m ')
    else:
        print(f'{nome} com {peso} kg')
