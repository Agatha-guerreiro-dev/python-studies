#Desafio 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salário de R$1250, calcule um aumento de 10%
#Para salários inferiores cálcule um aumento de 15%.
pay = float(input('Qual o seu salário? '))
rise = pay * 1.1 if pay >= 1250 else pay * 1.15
print(f'Parabéns, você é um colaborador muito valioso para a nossa empresa e acaba de receber um aumento!\n'
      f'Seu novo salário é de R${rise:.2f}')
