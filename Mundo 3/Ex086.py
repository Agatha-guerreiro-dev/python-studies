#Desafio 86: Crie um programa que faça uma matriz de dimensão 3x3
#E preencha com valores lido pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.
matriz = list()
data = list()
for c in range(9):
    num = int(input('Digite um valor para a matriz 3x3: '))
    data.append(num)
    if c == 2:
        matriz.append(data[:])
        data.clear()
    elif c == 5:
        matriz.append(data[:])
        data.clear()
    elif c == 8:
        matriz.append(data[:])
        data.clear()
print('-=' * 20)
for a, b, c in matriz:
    print(f'[{a}][{b}][{c}]')
