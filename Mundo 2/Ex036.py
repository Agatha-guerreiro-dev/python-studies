#Desafio 036: Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou o empréstimo será negado.
from time import sleep
print('Olá, prezado usuário. Deseja calcular o financiamente do seu imóvel com a gente?')
house_value = float(input('Qual o valor do imóvel: R$'))
salary = float(input('Qual o valor do seu salário: R$'))
total_months = int(input('Em quanto anos deseja finaciar: ')) * 12
limit = salary * 0.3
installment = house_value / total_months
print('\033[33mEstamos calculando o seu financiamento!\033[m')
sleep(2)
if installment <= limit:
    print(f'\033[32mParabéns, seu financiamento foi aprovado!\033[m\n'
          f'Deseja progredir com a compra do imóvel em {total_months} parcelas de R${installment:.2f} mensais?')
else:
    print(f'\033[31mSinto muito, seu financiamento foi recusado\033[m\n'
          f'Não podemos prosseguir com a negociação, pois as parcelas de R${installment:.2f} ultrapassam 30% da sua renda mensal.')

