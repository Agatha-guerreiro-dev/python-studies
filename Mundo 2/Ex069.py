# ==============================================================================
# DESAFIO 069
# ------------------------------------------------------------------------------
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
# cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
# ==============================================================================
adult = man = woman = 0
while True:
    print('-='*20)
    print('Cadastre uma pessoa.')
    age = int(input('Idade: '))
    gender = str(input('Gênero: [H/M] ')).strip().upper()
    while gender not in 'HM':
        gender = str(input('Por favor, digite um gênero válido: [H/M] ')).strip().upper()
    if age >= 18:
        adult += 1
    if gender in 'H':
        man += 1
    if gender in 'M':
        if age < 20:
            woman += 1
    print('-='*20)
    command = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while command not in 'SN':
        command = str(input('Por favor, selecione uma opção válida: [S/N] ')).strip().upper()
    if command in 'N':
        break
print(f'Total de pessoas com mais de 18 anos = {adult}.\n'
      f'Ao todo temos {man} homens cadastrados.\n'
      f'No total {woman} mulheres tem menos de 20 anos.')
