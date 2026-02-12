#Desafio 85: Crie um programa onde o usuário possa digitar 7 valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores
# pares e ímpares em ordem crescente.
lista = [[], []]
for c in range(7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print('-=' * 20)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
