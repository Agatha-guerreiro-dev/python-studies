from random import randint
lista = []
for c in range(100):
    num = randint(0, 1000)
    if not lista or num > lista[-1]:
        #se eu quiser reverter a ordem da lista eu faço num < lista[-1]
        #com isso eu vou estar movendo o menor número para o final da lista
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        local = 0
        while local < len(lista):
            if num <= lista[local]:
                #aqui eu mudo num >= lista[local]
                lista.insert(local, num)
                print(f'Adicionado na posição {local} da lista...')
                break
            local += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')
