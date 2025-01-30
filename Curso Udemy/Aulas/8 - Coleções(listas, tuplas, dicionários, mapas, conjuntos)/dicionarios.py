dicionario1 = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(dicionario1)
print(dicionario1['br'])
print(dicionario1.get('eua'))
print()


dicionario2 = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
pais = dicionario2.get('py', 'Não encontrado')
print(pais)
pais1 = dicionario2.get('ru', 'Não encontrado')
print(pais1)
print()


dicionario3 = {'jan': 100, 'fev': 170, 'mar': 300}
print(dicionario3)
dicionario3['abr'] = 350
print(dicionario3)
dicionario3.pop('mar')
print(dicionario3)
print()


dicionario4 = {}.fromkeys('a', 'b')
print(dicionario4)
print()


dicionario5 = {}.fromkeys(['nome', 'idade', 'peso'], 'desconhecido')
print(dicionario5)
print()
