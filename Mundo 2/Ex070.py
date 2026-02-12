# ==============================================================================
# DESAFIO 070
# ------------------------------------------------------------------------------
# Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000.
# C) Qual é o nome do produto mais barato.
# ==============================================================================
print('-'*20)
print('Agatha Eletrônicos')
print('-'*20)
product_name = ''
total = mil = lowest = 0
while True:
    product = input('Nome do Produto: ').strip().title()
    price = float(input('Preço: R$').replace(',','.'))
    total += price
    if lowest == 0:
        lowest = price
        product_name = product
    if price < lowest:
        product_name = product
        lowest = price
    if price > 1000:
        mil += 1
    option = input('Deseja continuar? [S/N] ').strip().upper()
    while option not in 'SN':
        option = input('Deseja continuar? [S/N] ').strip().upper()
    if option == 'N':
        break
print(f'O valor total da compra foi de R${total}\n'
      f'Ao todo {mil} produtos custam mais de R$1000.00\n'
      f'O produto mais barato foi {product_name} custando R${lowest}')
