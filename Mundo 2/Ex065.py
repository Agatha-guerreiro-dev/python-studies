# ==============================================================================
# DESAFIO 065: Maior e Menor valores
# ------------------------------------------------------------------------------
# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual
# foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.
# ==============================================================================
print('Vamos calcular médias? Digite números até estar satisfeito(a) que eu vou calcular a média deles para você.')
print('-='*20)
validation = 'S'
counter = 0
total = 0
bigger = 0
lower = 0
average = 0
while validation == 'S':
    number = int(input('Digite um número: '))
    total += number
    counter += 1
    average = total / counter
    validation = input('Deseja continuar? Digite [S/N]: ').strip().upper()
    if validation != 'S' and validation != 'N':
        if counter == 1:
            bigger = number
            lower = number
            validation = input('Digite uma opção válida, deseja continuar [S/N]: ').strip().upper()
        elif number > bigger:
            bigger = number
            validation = input('Digite uma opção válida, deseja continuar [S/N]: ').strip().upper()
        elif number < lower:
            lower = number
            validation = input('Digite uma opção válida, deseja continuar [S/N]: ').strip().upper()
    elif validation == 'N':
        if counter == 1:
            bigger = number
            lower = number
        elif counter != 1:
            if number > bigger:
                bigger = number
            elif number < lower:
               lower = number
    elif counter == 1:
        bigger = number
        lower = number
    elif number > bigger:
        bigger = number
    elif number < lower:
        lower = number
print('-='*20)
print(f'O maior valor digitado foi {bigger}\n'
                  f'E o menor foi {lower}\n'
                  f'A média entre todos os valores lidos é = {average:.1f}')
