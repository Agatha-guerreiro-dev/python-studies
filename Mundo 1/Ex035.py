#Desafio 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuários se eles podem
#ou não formar um triângulo.
print('Vamos brincar de montar um triângulo.\n'
      'Faça um linha utilizando o simbolo (-)')
la = input('Escreva a primeira linha: ').strip()
lb = input('Escreva a segunda linha: ').strip()
lc = input('Escreva a terceira linha: ').strip()
la = len(la)
lb = len(lb)
lc = len(lc)
if la + lb > lc and lb + lc > la and lc + la > lb:
    print('Parabéns, você montou um triângulo :)')
else:
    print('Lamento, você não conseguiu formar um triângulo')
