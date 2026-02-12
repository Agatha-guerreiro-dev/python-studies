#Desafio 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
print('Vamos comparar os pesos?')
peso1 = float(input('Me diga seu peso em Kg: ').replace(',','.'))
maior_peso = peso1
menor_peso = peso1
for balanca in range(0,4):
    peso = float(input('Me diga seu peso em Kg: ').replace(',','.'))
    if peso >= maior_peso:
        maior_peso = peso
    elif peso <= menor_peso:
        menor_peso = peso
print(f'O maior peso foi: {maior_peso}Kg.\n'
      f'O menor peso foi: {menor_peso}kg.')
