#Desafio 006: Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
print(f'Seu número é {n},\n'
      f'O dobro dele é {n*2},\n'
      f'O triplo dele é {n*3},\n'
      f'E a raíz quadrada é {n**(1/2):.2f}')
