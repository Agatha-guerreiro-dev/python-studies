# Desafio 83: Validando expressões matemáticas
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses
# abertos e fechados na ordem correta.
expressao = input('Digite a expressão: ')
lista = list(expressao)
check = 0
for c in lista:
    if c == '(':
        check += 1
    elif c == ')':
        check -= 1
    if check < 0:
        break
if check == 0:
    print('Expressão correta.')
else:
    print('A expressão está errada.')
