lista = [1, 8, 4, 99, 34, 129]
print(max(lista))
print(min(lista))
print()
tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))
print(min(tupla))
print()
conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))
print(min(conjunto))
print()
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))
print(max(dicionario.values()))
print(min(dicionario))
print(min(dicionario.values()))
print()

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print(max(n1, n2))
print(min(n1, n2))
print()


nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Olivander']
print(max(nomes))
print(min(nomes))
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))
print()

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Top old to rock in roll, too young to die", "tocou": 32}
]
print(max(musicas, key=lambda musica: musica["tocou"]))
print(min(musicas, key=lambda musica: musica["tocou"]))
print(max(musicas, key=lambda musica: musica["tocou"])["titulo"])
print(min(musicas, key=lambda musica: musica["tocou"])["titulo"])
