#Desafio 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input('Digite um número de 0 a 9999: '))
unidade = numero%10
divisao1 = numero//10
dezena = divisao1%10
divisao2 = divisao1//10
centena = divisao2%10
divisao3 = divisao2//10
milhar = divisao3%10
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
