#Desafio 38: Leia um programa que leia dois números inteiros e os compare mostrando na tela uma mensagem.
#O primeiro valor é maior; O segundo valor é maior; Não existe valor maior os dois são iguais
number1 = int(input('Digite um número: '))
number2 = int(input('Digite um segundo número: '))
if number1 > number2:
    print(f'O valor {number1} é maior que {number2}.')
elif number2 > number1:
    print(f'O valor {number2} é maior que {number1}.')
else:
    print('Os dois valores são iguais.')
