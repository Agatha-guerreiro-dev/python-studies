#Desafio 76: Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('Coca-Cola', 9.90, 'Energético Monster', 8.99, 'Lays', 12.50, 'Doritos', 14.50, 'Nuggets Seara', 12,
            'Ketchup Heinz', 11.99, 'Barra de Chocolate Milka', 15.50)
lista = len(produtos)
print('-' * 60)
print(f'{"LISTAGEM DE PREÇOS":^60}')
print('-' * 60)
for c in range(0, lista, 2):
    nome = produtos[c]
    valor = produtos [c + 1]
    print(f'{nome:.<50}R${valor:>8.2f}')
print('-' * 60)
