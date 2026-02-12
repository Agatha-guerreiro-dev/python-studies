# ==============================================================================
# DESAFIO 068
# ------------------------------------------------------------------------------
# Faça um programa que jogue PAR OU ÍMPAR com o computador. O jogo só será
# interrompido quando o jogador PERDER, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.
# ==============================================================================
from random import randrange
print('Vamos jogar par ou ímpar?')
counter = 0
while True:
    player_hand = int(input('Digite um número: '))
    computer_hand = randrange(1,11)
    player_choice = str(input('Escolha par ou ímpar [P/I]: ')).strip().upper()
    total = player_hand + computer_hand
    result = total % 2
    while player_choice not in 'PI':
        player_choice = str(input('Opção inválida!\n'
                                  'Escolha uma opção válida [P/I]: ')).strip().upper()
    print('-='*20)
    print(f'Você jogou {player_hand} e o computador jogou {computer_hand}.')
    print(f'Valor total foi {total}.','Deu par.' if result == 0 else 'Deu Ímpar.')
    if player_choice == 'P':
        if result == 0:
            print('Você Venceu!!! Vamos jogar novamente.')
            counter +=1
        else:
            print('Você Perdeu!!')
            break
    elif player_choice == 'I':
        if result != 0:
            print('Você Venceu!!! Vamos jogar novamente.')
            counter += 1
        else:
            print('Você Perdeu!!')
            break
print(f'Fim de jogo! Voçê venceu {counter} vezes.')
