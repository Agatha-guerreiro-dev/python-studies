#Desafio 49: faça um tabuádo usando o número que o usuário escolher só que dessa vez com a ferramenta for
n = int(input('Digite um número: '))
print(f'A tabuáda de {n} é:')
print('-='*20)
for c in range(1, 11):
    tab = n * c
    print(f'{n} x {c} = {tab}')
print('-='*20)
