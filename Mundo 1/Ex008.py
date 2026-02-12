#Desafio 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Quantos metros você percorre por dia? '))
print(f'Isso equivale a {m/1000:.1f} km,\n'
      f'Isso é igual a {m*100:.0f} cm,\n'
      f'Que é igual a {m*1000:.0f} mm')
