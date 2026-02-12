#Desafio 51: Desenvolva um pragrama que leia um primeiro termo e a razão de uma progressão aritimética.
#No final, mostre os 10 primeiro termos dessa progressão.
a1 = int(input('Me diga o primeiro termo da pa: '))
r = int(input('Me diga a razão da pa: '))
fim = a1 + 10 * r
for c in range(a1,fim,r):
    print(c)
