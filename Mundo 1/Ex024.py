#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade = input('Digite o nome de um cidade: ').strip().title()
if cidade:
    nome1 = cidade.split()
    objetivo = 'Santo'
    if nome1[0] == objetivo:
        print('Sua cidade começa com o nome SANTO')
    else:
        print('Sua cidade não começa com o nome SANTO :(')
else:
    print('Acho que isso não é uma cidade :(')
