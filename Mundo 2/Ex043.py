#Desafio 43:A Missão: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
#e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do Peso; Entre 18.5 e 25: Peso Ideal; Entre 25 e 30: Sobrepeso;
#Entre 30 e 40: Obesidade; Acima de 40: Obesidade Mórbida
print('-='*20)
print('Vamos calcular o seu índice de Massa Corporal?')
print('-='*20)
height = float(input('Me diga sua altura em metros: ').replace(',','.'))
weight = float(input('Agora me diga o seu peso em Kg: ').replace(',','.'))
imc = weight / height**2
if imc < 18.5:
    category = 'Abaixo do Peso'
elif imc < 25:
    category = 'no Peso Ideal'
elif imc < 30:
    category = 'com \033[33mSobrepeso\033[m'
elif imc < 40:
    category = 'com \033[31mObesidade\033[m'
else:
    category = 'com \033[31mObesidade Mórbida\033[m'
print(f'O seu imc é {imc:.1f} isso significa que você está {category}.')
