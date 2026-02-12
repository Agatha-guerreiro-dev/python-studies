#Desafio 75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final mostre: A) Quantas vezes apareceu o valor de 9, B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
valores = (int(input('Digite um número: ')), int(input('Digite um novo número: ')),
           int(input('Digite um terceiro número: ')), int(input('Digite um último número: ')))
pares = [num for num in valores if num % 2 == 0]
#Para separar o par aqui foi utilizado um for, a variável temporária num vai receber os valores da tupla,
#o if vai testar esses valores se o resto da divisão dele foi igual a zero ele vai salvar esse valor na variável.
print('-=' * 20)
print(f'O número 9 apareceu {valores.count(9)} vezes.')
print('-=' * 20)
print(f'O valor 3 apareceu na {valores.index(3) + 1} posição'
      if 3 in valores else 'Valor não encontrado')
print('-=' * 20)
print(f'O números pares são: {pares}' if len(pares) != 0 else 'Nenhum número par encontrado')
