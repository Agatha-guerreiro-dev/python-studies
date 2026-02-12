#Desafio 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome.
nome = input('Digite seu nome: ').title().strip()
print(nome.find('Silva') != -1)
