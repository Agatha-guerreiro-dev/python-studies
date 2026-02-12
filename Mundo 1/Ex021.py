#Desafio 021: Faça um programa que abra e reproduza um arquivo mp3.
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input('\033[35mEscutando a música... Aperte Enter para parar.\033[m')
