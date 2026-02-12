#Desafio 61: Refaça o desafio 51 da progreção aritimética, só que usando while.
termo_pa = int(input('Me diga o primeiro termo da pa: '))
razao = int(input('Me diga a razão da pa: '))
ultimo_termo = termo_pa + 9 * razao
resultado = termo_pa
print(resultado)
while resultado != ultimo_termo:
      resultado += razao
      print(resultado)
