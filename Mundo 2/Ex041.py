#A Missão: O programa deve ler o ano de nascimento de um atleta e mostrar sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM; Até 14 anos: INFANTIL;  Até 19 anos: JÚNIOR;  Até 25 anos: SÊNIOR; Acima de 25 anos: MASTER
from datetime import date
user_year = int(input('Olá atleta, digite o seu ano de nascimento para averiguarmos a sua categoria: '))
current_year = date.today().year
age = current_year - user_year
if age <= 9:
    categoria = 'Mirim'
elif age <= 14:
    categoria = 'Infantil'
elif age <= 19:
    categoria = 'Júnior'
elif age <= 25:
    categoria = 'Sênior'
else:
    categoria = 'Master'
print(f'Devido a sua idade de {age} anos, você se enquadra na categoria {categoria}.')
