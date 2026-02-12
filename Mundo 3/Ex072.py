#Desafio 72: Crie uma tupla totalmente preenchida com uma contagem por extenso de 0 té 20.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
n_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
             'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um número de 0 a 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ', end='')
print(f'O número {n} é escrito como {n_extenso[n]} por extenso.')
