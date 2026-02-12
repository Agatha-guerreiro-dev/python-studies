#Desafio 81: Extraindo dados de uma Lista
#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    #if not lista or num < lista[-1]:
        #lista.append(num)
    #else:
        #local = 0
        #while local < len(lista):
            #if num >= lista[local]:
                #lista.insert(local, num)
                #break
            #local += 1
    #Coloquei o scaner aqui para mostrar onde eu encaixaria se eu optasse por ele nessa resolução
    #Como o professor não falou nada sobre .sort() eu optei por ele.
    while True:
        menu = str(input('Deseja continuar? [S/N] ')).strip().lower()
        if menu in 'sn':
            break
        else:
            print('Por favor, digite uma opção válida.')
    if menu == 'n':
        break
lista.sort(reverse = True)
print('-=' * 20)
print(f'Você digitou {len(lista)} valores.')
print(f'Os valores em ordem decrescente são: {lista}')
print(f'O valor 5 faz parte da lista' if 5 in lista else 'O valor 5 não faz parte desta lista.')
