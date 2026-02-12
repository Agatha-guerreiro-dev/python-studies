#Desafio 63: A Missão: Escreva um programa que leia um número [n] inteiro qualquer
# e mostre na tela os [n] primeiros elementos de uma Sequência de Fibonacci.
n = int(input('Digite a quantidade de elementos da Sequência de Fibonacci que deseja ver: '))
n1 = 0
n2 = 1
cont = 1
while cont <= n:
    print(f'{n1} -> ', end = '')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont += 1
print('FIM')
