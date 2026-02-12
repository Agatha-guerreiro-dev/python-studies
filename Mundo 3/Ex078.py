#Desafio 78: faça um programa que leia cinco valores numéricos e gurde numa lista.
#No final mostre o menor e o maior número e sua respectiva posição na lista.
num = [int(input(f'Digite um número para a posição {c}: ')) for c in range(5)]
maior_valor = max(num)
menor_valor = min(num)
maior_c = []
menor_c = []
for p, n in enumerate(num):
    if n == maior_valor:
        maior_c.append(p)
    if n == menor_valor:
        menor_c.append(p)
print(f'O maior valor da lista é : {maior_valor} e está nas posições {maior_c}\n'
      f'O menor valor da lista é : {menor_valor} e está nas posições {menor_c}')
