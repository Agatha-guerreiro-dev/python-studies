# Desafio 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
year = date.today().year
adult = 0
minor = 0
adult_name = ''
minor_name = ''
for c in range(0,7):
    name = str(input('Qual o seu primeiro nome: ')).strip().title()
    year_b = int(input('Digite o ano do seu nascimento: '))
    age = year - year_b
    if age >= 21:
        adult += 1
        adult_name += ' ' + name
    else:
        minor += 1
        minor_name += ' ' + name
print(f'{adult_name} são maiores de idade e {minor_name} são menores de idade.\n'
      f'Contabilizando {adult} adultos e {minor} menores de idade.')
