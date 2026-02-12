#Desafio 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
print('Vamos testar se sua frase é um palíndromo?')
print('-='*20)
frase = input('Digite uma frase: ').strip().replace(' ','').upper()
print('-='*20)
inverso = ''
#pal = frase[::-1]
#if frase == pal:
 #   print(f'A frase  é um palíndromo.')
#else:
  #  print(f'A frase não é um palíndromo.')
for letra in range(len(frase) -1, -1, -1):
    inverso += frase[letra]
if frase == inverso:
    print(f'A frase é um palíndromo!')
else:
    print(f'A frase não é um palíndromo!')
