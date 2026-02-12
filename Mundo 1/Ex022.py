#Desafio 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas.
#O nome com todas as letras minúsculas.
#Quantas letras ao todo, sem considerar os espaços.
#Quantas letras tem o primeiro nome.
nome = input('Digite o seu nome completo: ').strip().title()
lnome = nome.replace(' ','')
fnome = nome.split()
print(f'Olá {nome}!\n'
      f'O seu nome tem exatamente {len(lnome)} letras!\n'
      f'Em maiúsculas: {nome.upper()}\n'
      f'Em minúsculas: {nome.lower()}\n'
      f'Já o seu primeiro nome {fnome[0]} tem {len(fnome[0])} letras!')

