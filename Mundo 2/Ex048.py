#Desafio 48: Faça um programa que cálcule a soma entre todos os números ímpares que são múltiplos de 3
#e que se encontram no intervalo de 1 a 500
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print(s)