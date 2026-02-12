#Desafio 58: A Missão: Melhore o jogo onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar.
# A cada erro, o computador deve dar uma dica: se o número é maior ou menor que o palpite.
#No final, mostre quantos palpites foram necessários para vencer.
from random import randrange
from time import sleep
print('-='*20)
print('Vamos brincar de adivinhação?')
print('Eu vou pensar em um número de 0 a 10 e você tem que advinhar que número eu escolhi ;)')
print('Pronto?')
sleep(2)
print('Já pensei, qual número será que eu escolhi?')
print('-='*20)
computer_guess = randrange(11)
guess = 15
counter = 0
while guess != computer_guess:
    guess = int(input('Tente advinhar.\n'
                      'Digite um número de 0 a 10: '))
    counter += 1
    if guess != computer_guess:
        if guess > computer_guess:
            print(f'{guess} é maior do que o meu número.')
        elif guess < computer_guess:
            print(f'{guess} é menor do que o meu número.')
    else:
        print('Parabéns você acertou.')
print(f'O número que eu escolhi foi {computer_guess}.\n'
      f'foram necessárias {counter} tentativas para você vencer o jogo.')
