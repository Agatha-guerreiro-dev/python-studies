#Desafio 79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
#Caso o número já esteja na lista ele não será adicionado. No final serão exibidos todos os valores únicos
# digitados em ordem crescente
lista = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado, não posso adicionar!')
    while True:
        menu = str(input('Deseja continuar? [S/N] ')).strip().lower()
        if menu in 'sn':
            break
        else:
            print('Digite uma opção válida.')
    if menu == 'n':
        break
lista.sort()
lista_final = tuple(lista)
print('-=' * 20)
print(f'Você digitou os valores: {lista_final}')
