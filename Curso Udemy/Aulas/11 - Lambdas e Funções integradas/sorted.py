numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros))
print(numeros)
print(sorted(numeros, reverse=True))
print(numeros)
print()


usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]
print(usuarios)
print(sorted(usuarios, key=lambda usuario: usuario["username"]))