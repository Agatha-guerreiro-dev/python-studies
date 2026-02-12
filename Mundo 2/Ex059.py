#Desafio 59: Crie um programa que leia dois valores e mostre um menu na tela:
#[1] SOMAR
#[2] MULTIPLICAR
#[3] MAIOR
#[4] NOVOS NÚMEROS
#[5] SAIR DO PROGRAMA
#Seu programa deverá realizar cada ação solicitada.
user_number_1 = int(input('Digite um número: '))
user_number_2 = int(input('Digite um segundo número: '))
menu = 0
while menu != 5:
    menu = int(input('Digite um número para escolher as seguintes opções:\n'
                     '[1] Somar \n'
                     '[2] Multiplicar \n'
                     '[3] Maior \n'
                     '[4] Novos números \n'
                     '[5] Sair do programa \n'
                     'Opção: '))
    if menu == 1:
        soma = user_number_1 + user_number_2
        print(f'A soma de {user_number_1} e {user_number_2} é {soma}')
    elif menu == 2:
        multi = user_number_1 * user_number_2
        print(f'O resultado da multiplicação de {user_number_1} e {user_number_2} é {multi}')
    elif menu == 3:
        if user_number_1 > user_number_2:
            print(f'O número {user_number_1} é maior que {user_number_2}')
        elif user_number_2 > user_number_1:
            print(f'O número {user_number_2} é maior que {user_number_1}')
        else:
            print('Os dois números tem valores iguais.')
    elif menu == 4:
        print('Escolha novos números.')
        user_number_1 = int(input('Digite um número: '))
        user_number_2 = int(input('Digite um segundo número: '))
    elif menu == 5:
        print('Foi um prazer te ajudar. Até a próxima.')
    else:
        print('\033[31mPor favor, escolha uma opção válida\033[m')
