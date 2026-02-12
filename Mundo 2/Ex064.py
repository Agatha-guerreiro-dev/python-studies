# ==============================================================================
# DESAFIO 064: Tratando vários valores v1.0
# ------------------------------------------------------------------------------
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada (flag).
# No final, mostre quantos números foram digitados e qual foi a soma
# entre eles (desconsiderando o flag).
# ==============================================================================
numero = 1
cont = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um número (Se quiser parar digite 999): '))
    if numero == 999:
        print(f'Você digitou um total de {cont} números, cuja soma total é {soma}')
    else:
        cont += 1
        soma += numero
