dicionario1 = {'jan': 100, 'fev': 170, 'mar': 300}
for chave in dicionario1:
    print(chave)
for chave in dicionario1:
    print(dicionario1[chave])
for chave in dicionario1:
    print(f'{chave} : {dicionario1[chave]}')
print()


dicionario2 = {'jan': 100, 'fev': 170, 'mar': 300}
print(dicionario2.keys())
for chave in dicionario2.keys():
    print(dicionario2[chave])
print()


dicionario3 = {'jan': 100, 'fev': 170, 'mar': 300}
print(dicionario3.values())
for valor in dicionario2.values():
    print(valor)
print()


dicionario4 = {'jan': 100, 'fev': 170, 'mar': 300}
print(dicionario4.items())
for chave, valor in dicionario2.items():
    print(f'chave={chave} e valor={valor}')
print()


dicionario5 = {'jan': 100, 'fev': 170, 'mar': 300}
print(sum(dicionario5.values()))
print(max(dicionario5.values()))
print(min(dicionario5.values()))
print(len(dicionario5))
