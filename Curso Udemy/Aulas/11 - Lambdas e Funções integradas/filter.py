import statistics
dados = [1.3, 2.7, 0.8, 4.1, 4.3, 0.1]
media = statistics.mean(dados)
print(f'Média: {media}')
res = filter(lambda valor: valor > media, dados)
print(list(res))
print()

print(list(filter(lambda valor: valor > statistics.mean(dados), dados)))
print()


paises = ['', 'Argentina', '', 'Brasil', '', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)
res = filter(None, paises)
print(list(res))
print()

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))
print()

res = filter(lambda pais: pais != '', paises)
print(list(res))
print()


usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]
print(usuarios)
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)
print()
inativos = list(filter(lambda u: not u['tweets'], usuarios))
print(inativos)
print()


nomes = ['Vanessa', 'Ana', 'Maria']
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
