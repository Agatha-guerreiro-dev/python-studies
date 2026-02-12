#Desafio 39: Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade
#se ele ainda vai se alistar; se é hora de se alistar; se já passou do tempo de alistamento.
#O programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
user_year = int(input('Olá, deseja verificar se você tem a idade para se apresentar no alistamento militar?\n'
                      'Digite o ano do seu nascimento: '))
current_year = date.today().year
age = current_year - user_year
if age < 18:
    balance = 18 - age
    year_enlistment = current_year + balance
    print(f'Você tem apenas {age} anos de idade, ainda não está apto ao alistamento obrigatório.\n'
          f'Você terá que se apresentar ao exército brasileiro no ano de {year_enlistment}.')
elif age > 18:
    balance = age - 18
    year_enlistment = current_year - balance
    print(f'Você tem {age} anos de idade, parece que já passou da hora de cumprir com o seu dever civíl.\n'
          f'Você deveria ter se apresentado ao exército brasileiro no ano de {year_enlistment}.\n'
          f'\033[31mVá agora regularizar seu título de reservista para evitar qualquer punição!\033[m')
else:
    print(f'Você tem {age}.\n'
          f'Parabéns, esse é o ano em que você deve se alistar, evite perder prazos.')
