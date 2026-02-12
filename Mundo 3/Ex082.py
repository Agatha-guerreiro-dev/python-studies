# Desafio 82: Dividindo valores em várias listas
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
par = []
impar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    #if num % 2 == 0:
        #par.append(num)
    #else:
        #impar.append(num)
    while True:
        menu = str(input('Deseja continuar? [S/N] ')).strip().lower()
        if menu in 'sn':
            break
        else:
            print('Por favor, digite uma opção válida.')
    if menu == 'n':
        break
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print('-=' *20)
print(f'Os valores que você digitou são: {lista}.')
print(f'Os números {par} são pares.')
print(f'Os números {impar} são ímpares.')
