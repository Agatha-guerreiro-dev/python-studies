#Desafio 031: Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200 km.
#E R$ 0.45 para viagens mais longas.
distancia = float(input('Digite a distância da sua viagem em km: '))
if distancia > 200:
    valor1 = distancia * 0.45
    print(f'O valor da sua passagem é de R$ {valor1:.2f}.')
else:
    valor2 = distancia * 0.5
    print(f'O valor da sua passagem é de R$ {valor2:.2f}.')
