# Desafio 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Digite o seu nome: ').strip().title()
grupos = nome.split()
last_name = len(grupos) - 1
print(f'Olá {grupos[0]} {grupos[last_name]},\n'
      f'Seja bem vindo(a)!')
