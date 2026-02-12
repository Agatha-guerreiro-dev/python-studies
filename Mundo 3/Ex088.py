#Desafio 88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
#E vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from time import sleep
import secrets
jogos = list()
gerador_sort = secrets.SystemRandom()
num = range(1, 61)
print('-' * 40)
print(f'{'SIMULADOR DE JOGADAS NA MEGA SENA':^40}')
print('-' * 40)
jogadas = int(input('Quantos jogos você quer que eu sorteie?: '))
print('-=' * 3, f'Sorteando {jogadas} Jogos' , '-=' * 3)
for c in range(1, jogadas + 1):
    sorteio = gerador_sort.sample(num, k=6)
    sorteio.sort()
    jogos.append(sorteio[:])
    sleep(1)
    print(f'Jogo {c}: {sorteio}')
sleep(0.5)
print('-=' * 3, 'BOA SORTE', '-=' *3)
