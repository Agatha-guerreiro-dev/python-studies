#Desafio 62: Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termos.
primeiro_termo = int(input('Me diga o primeiro termo da pa: '))
razao = int(input('Me diga a razão da pa: '))
termo = primeiro_termo
cont = 1
ultimo_termo = 10
while ultimo_termo != 0:
    while cont <= ultimo_termo:
        print(f'{termo} ->',end='')
        termo += razao
        cont += 1
    ultimo_termo = int(input('Deseja ver mais termos?\n'
                             'Se sim, digite a quantidade que deseja ver.\n'
                             'Se não, digite [0]: '))
    if ultimo_termo != 0:
        cont = 1
    else:
        print('Adeus.')
