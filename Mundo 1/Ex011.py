#Desafio 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
#a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2m^2
pb = float(input('Digite a largura da sua parede em metros: '))
pl = float(input('Digite a altura da sua parede em metros: '))
a = pb*pl
print(f'Você precisará de {a/2:.1f} l de tinta para pintar a parede')
