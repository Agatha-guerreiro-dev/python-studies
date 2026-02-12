#Desafio 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere 1.00 USD = 3.27 BRL
user = str(input('Digite seu nome de usuário: '))
print(f'Olá {user}, seja bem vindo(a)!')
n = float(input('Digite um valor que deseje depositar: '))
print(f'Parabéns pelo depósito, você tem R${n+12.5:.2f} de saldo.\n'
      f'Desja converter em US${(n+12.5)/3.27:.2f}?')
