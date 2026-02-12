#Desafio 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite um frase: ').strip().lower()
print(f'A letra (a) apareceu {frase.count('a')} vezes')
print(f'A primeira letra está na posição {frase.find('a') + 1}')
print(f'A última letra está na posição {frase.rfind('a') + 1}')
