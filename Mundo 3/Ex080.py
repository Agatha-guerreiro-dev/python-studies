#Desafio 80: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os numa lista
#Já na posição correta de inserção sem usar o sort().
#No final, mostre a lista ordenada na tela.
lista = []
for c in range(5):
    num = int(input('Digite um número: '))
    if c == 0:
        lista.append(num)
        print('Adicionado ao final da lista...')
        maior = num
        menor = num
    else:
        if num >= maior:
            local = lista.index(maior)
            print(f'Adicionado na posição {local} da lista...' if local != len(lista) - 1 else 'Adicionado ao final da lista...')
            lista.insert(local + 1, num)
            maior = num
        elif num <= menor:
            local = lista.index(menor)
            print(f'Adicionado na posição {local} da lista...')
            lista.insert(local, num)
            menor = num
        elif menor < num < maior:
            local_mai = lista.index(maior)
            local_meno = lista.index(menor)
            if local_meno != 0:
                local = local_mai - local_meno
                print(f'Adicionado na posição {local} da lista...')
                lista.insert(local, num)
            else:
                local = local_mai - (local_meno + 1)
                print(f'Adicionado na posição {local} da lista...')
                lista.insert(local, num)
print(lista)
