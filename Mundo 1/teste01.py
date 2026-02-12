#Refazendo exercício que me deixou com trauma de tirar foto.
print('-='*20)
casas = int(input('Me diga a quantidade de casas da sequencia de fibonacci que você deseja ver: '))
counter = 0
trauma_1 = 0
trauma_2 = 1
trauma_3 = 0
while counter < casas:
    print(f'{trauma_1} -> ', end = '')
    counter += 1
    trauma_3 = trauma_1 + trauma_2
    trauma_1 = trauma_2
    trauma_2 = trauma_3
print('FIM')
