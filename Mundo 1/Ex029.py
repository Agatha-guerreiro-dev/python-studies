#Desafio 029: Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7.00 para cada km acima do limite.
velocidade = int(input('Qual a sua velocidade? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Infelizmente você se encontra a cima do limite de velocidade permitida (80km/h).\n'
          f'Por esse motivo o senhor(a) terá que pagar uma multa de R${multa:.2f}\n'
          f'Equivalente a R$ 7.00 por km a cima do permitido.')
else:
    print('Parabéns, você é um motorista consciente, está dirigindo defensivamente e de acordo com a legislação!')