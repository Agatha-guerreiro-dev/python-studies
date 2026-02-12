teste = list()
teste.append('Gustavo')
teste.append(40)
#galera = list()
#galera.append(teste[:])
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#for c in galera:
    #for pos, i in enumerate(c):
        #if pos == 0:
            #print(f'Nome: {i:.<30}', end = ' ')
        #else:
            #print(f'Idade: {i}')
    #print(f'{c[0]} tem {c[1]} anos de idade.')
    #print(f'\n{c[0]:.<30}idade: {c[1]}')
for nome, idade in galera:
    print(f'Nome: {nome}, idade: {idade}')