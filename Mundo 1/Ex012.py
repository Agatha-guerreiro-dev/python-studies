#Desafio 012: Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
v = float(input('Digite o valor do produto: '))
print(f'Parabéns, você ganhou 5% de desconto!\n'
       f'Deseja levar o produto pelo valor de R$ {v*0.95:.2f}?')
