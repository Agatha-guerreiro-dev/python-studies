#Desafio 87: Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
matriz = [[0] * 3 for _ in range(3)]
par = list()
soma_coluna_3 = 0
for linha in range(0,3):
    for coluna in range(0,3):
        num = int(input(f'Digite um número para a casa [{linha}/{coluna}]: '))
        matriz[linha][coluna] = num
        if num % 2 == 0:
            par.append(num)
for linha in range(0,3):
    soma_coluna_3 += matriz[linha][2]
print('-=' * 20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()
print('-=' * 20)
print(f'A soma de todos os valores pares digitados é: {sum(par)}')
print(f'A soma de todos os valores da terceira coluna é: {soma_coluna_3}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
