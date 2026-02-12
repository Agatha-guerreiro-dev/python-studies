#Desafio 045: Crie um programa que faça o computador jogar pedra, papel e tesoura com você.
from time import sleep
from random import randrange
print('-='*20)
print('Vamos jogar Pedra, Papel ou Tesoura?')
print('-='*20)
player_hand = int(input('Jô, Ken, Pô: ').strip().lower().replace('pedra','1').replace('papel','2').replace('tesoura','3'))
computer_choice = randrange(1,4)
computer_hand = str(computer_choice).replace('1','pedra').replace('2','papel').replace('3','tesoura')
sleep(2)
if player_hand == computer_choice:
    result = 'Empate'
elif player_hand != 1 and computer_choice > player_hand:
    result = 'Derrota'
elif computer_choice != 1 and player_hand > computer_choice:
    result = 'Vitória'
elif player_hand == 1 and computer_choice == 2:
    result = 'Derrota'
elif player_hand == 2 and computer_choice == 1:
    result = 'Vitória'
elif player_hand == 1 and computer_choice == 3:
    result = 'Vitória'
elif player_hand == 3 and computer_choice == 1:
    result = 'Derrota'
print(f'{result}\n'
      f'O computador escolheu {computer_hand}.')
