# ==============================================================================
# DESAFIO 071
# ------------------------------------------------------------------------------
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
# ==============================================================================
print('-='*20)
print('JAVA CORPORATION BANK')
print('-='*20)
while True:
    withdraw = int(input('Bem Vindo(a) ao JCB.\n'
                'Qual valor deseja sacar: R$'))
    fifty_banknote = int(withdraw / 50)
    calculator = withdraw - (fifty_banknote * 50)
    twenty_banknote = int(calculator / 20)
    if fifty_banknote >= 1:
        print(f'Total de {fifty_banknote} notas de R$50.00')
    calculator = calculator - (twenty_banknote * 20)
    ten_banknote = int(calculator / 10)
    if twenty_banknote >= 1:
        print(f'Total de {twenty_banknote} notas de R$20.00')
    calculator = calculator - (ten_banknote * 10)
    one_banknote = int(calculator / 1)
    if ten_banknote >= 1:
        print(f'Total de {ten_banknote} notas de R$10.00')
    if one_banknote >= 1:
        print(f'Total de {one_banknote} notas de R$1.00')
    break
