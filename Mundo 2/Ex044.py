#Desafio 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento.
#à vista em dinheiro/cheque: 10% de desconto; à vista no cartão: 5% de desconto; em até 2x no cartão: valor normal sem juros; 3x ou mais no cartão: 20% de juros.
import sys
product_price = float(input('Insira o valor do produto: R$').replace(',','.'))
payment_method = int(input('Escolha qual o seu método de pagamento\n'
                           'Digite 1 para pagamentos em dinheiro à vista ou cheque.\n'
                           'Digite 2 para pagamentos à vista no cartão.\n'
                           'Digite 3 para pagamentos em até 2x no cartão.\n'
                           'Digite 4 para pagamentos em 3x ou mais no cartão.\n'
                           'Digite aqui: '))
if payment_method == 1:
    payment = product_price * 0.9
    installment = 1
elif payment_method == 2:
    payment = product_price * 0.95
    installment = 1
elif payment_method == 3:
    payment = product_price / 2
    installment = 2
elif payment_method == 4:
    installment = int(input('Em quantas vezes deseja parcelar essa compra: '))
    payment = (product_price * 1.2) / installment
else:
    print('\033[31mVocê digitou uma opção inválida\033[m')
    sys.exit()
print(f'Deu um total de {installment}x de R${payment:.2f}')
