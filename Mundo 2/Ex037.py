#Desafio 37: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual
#será a base da conversão: 1 para binário, 2 para octal, 3 para hexadecimal.
number = int(input('Digite um número inteiro: '))
option = int(input('Escolha as seguintes opções de converções:\n'
                   'Digite 1 para binário.\n'
                   'Digite 2 para octal.\n'
                   'Digite 3 para hexadecimal.\n'
                   ': '))
if option == 1:
    print(f'O número {number} convertido em binário é {bin(number)[2:]}')
elif option == 2:
    print(f'O número {number} convertido em octal é {oct(number)[2:]}')
elif option == 3:
    print(f'O número {number} convertido em hexadecimal é {hex(number)[2:]}')
else:
    print('\033[31mEscolha um opção válida\033[m')
