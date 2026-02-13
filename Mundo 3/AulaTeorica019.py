pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.items())
#for k, v in pessoas.items():
    #print(f'{k} = {v}')
brasil = list()
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[0]['sigla'])
estado = dict()
for c in range(0, 3):
    estado['uf'] =  str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
