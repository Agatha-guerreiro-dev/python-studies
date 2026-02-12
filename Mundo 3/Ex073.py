#Desafio 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol.
#Na ordem de colocação, depois mostre: A) apenas os 5 primeiros colocados. B) os 4 últimos colocados da tabela.
#C) uma lista com os times em ordem alfabética, D) em que posição da tabela está o time Chapecoense.
camp_brasileiro = ('Botafogo', 'Chapecoense', 'Vitória', 'Fluminense', 'Mirassol', 'Bahia', 'São Paulo', 'Athletico-PR',
                   'Bragantino', 'Palmeiras', 'Atlético-MG', 'Flamengo', 'Grêmio', 'Corinthians', 'Vasco da Gama', 'Coritiba',
                   'Internacional', 'Santos', 'Remo', 'Cruzeiro')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {camp_brasileiro}')
print('-=' * 20)
print(f'Os cinco primeiros colocados da tabela são: {camp_brasileiro[:5]}')
print('-=' * 20)
print(f'Os quatro últimos colocados são: {camp_brasileiro[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(camp_brasileiro)}')
print('-=' * 20)
print(f'O time Chapecoense está na {camp_brasileiro.index('Chapecoense') + 1}ª posição')
print('-=' * 20)
