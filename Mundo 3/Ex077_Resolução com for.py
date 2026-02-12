#Desafio 77: crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
words = ('Alface', 'Carro', 'Abacaxi', 'Geladeira', 'Guitarra', 'Gemini', 'Amor', 'Professor', 'Bola', 'Papel')
for palavras in words:
    print(f'\nNa palavra {palavras} temos as vogais: ', end = '')
    for letra in palavras:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end = ' ')
