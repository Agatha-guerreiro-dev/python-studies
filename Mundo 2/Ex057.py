#Desafio 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores F ou M.
#Se estiver errado peça a digitação novamente até ter um valor correto.
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Seu sexo biológico é? [M/F]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Por favor, digite um sexo válido.')
print(f'Seu sexo é {sexo}.')
