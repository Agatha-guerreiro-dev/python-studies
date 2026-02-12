#Desafio 46: Faça uma contagem regressiva para fogos de artifício, indo de 10 até 0, com uma pausa de 1s entre eles.
from time import sleep
print('Preparados para os FOGOS?')
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BOOOOOOM')
