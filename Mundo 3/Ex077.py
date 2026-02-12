#Desafio 77: crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
words = ('Alface', 'Carro', 'Abacaxi', 'Geladeira', 'Guitarra', 'Gemini', 'Amor', 'Professor', 'Bola', 'Papel')
final = len(words)
vowal = ''
for c in range(0, final):
    palavra = words[c].lower()
    if 'a' in palavra:
        counter = palavra.count('a')
        vowal += 'a ' * counter
    if 'e' in palavra:
        counter = palavra.count('e')
        vowal += 'e ' * counter
    if 'i' in palavra:
        counter = palavra.count('i')
        vowal += 'i ' * counter
    if 'o' in palavra:
        counter = palavra.count('o')
        vowal += 'o ' * counter
    if 'u' in palavra:
        counter = palavra.count('u')
        vowal += 'u ' * counter
    print(f'Na palavra {palavra.upper()} temos as vogais: {vowal}')
    vowal = ''
