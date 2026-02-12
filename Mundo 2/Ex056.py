#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.
media = 0
mulheres = 0
homem_idade = 0
homem_velho = ''
for pessoas in range(0,4):
    nome = str(input('Me diga o seu primeiro nome: ')).strip().title()
    genero = str(input('Qual o seu gênero, Homem ou Mulher: ')).strip().lower()
    idade = int(input('Qual a sua idade: '))
    media += idade
    if genero == 'mulher':
        if idade < 20:
            mulheres += 1
    elif genero == 'homem':
        if idade > homem_idade:
            homem_idade = idade
            homem_velho = nome
    else:
        print('Gênero inválido')
media_f = media / 4
print(f'A idade média do grupo é de {media_f} anos;\n'
      f'O homem mais velho é {homem_velho} com {homem_idade} anos;\n'
      f'No total {mulheres} mulheres tem menos de 20 anos.')
