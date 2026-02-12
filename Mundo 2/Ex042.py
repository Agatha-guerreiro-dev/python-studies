#Desafio 42: Refaça o exercício dos triângulos acrescentado o recurso de mostrar que tipo de triãngulo será formado:
#Equilátero: todos os lados são iguais. Isósceles dois lados são iguais. Escaleno todos os lados são diferentes.
print('Vamos brincar de montar um triângulo.\n'
      'Faça um linha utilizando o simbolo (-)')
la = input('Escreva a primeira linha: ').strip()
lb = input('Escreva a segunda linha: ').strip()
lc = input('Escreva a terceira linha: ').strip()
a = len(la)
b = len(lb)
c = len(lc)
if a + b > c and b + c > a and c + a > b:
    if a != b and b != c and c != a:
        triangle = 'Escaleno'
    elif a == b and b == c:
        triangle = 'Equilátero'
    else:
        triangle = 'Isósceles'
    print(f'Parabéns! Você montou um triângulo {triangle}.')
else:
    print('Lamento, você não conseguiu formar um triângulo')
