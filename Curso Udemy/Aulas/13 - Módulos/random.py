from random import uniform, randint, choice, shuffle
print(uniform(1, 10))
print()
print(randint(1, 10))
print()

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))
print()

cartas = ['K', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)
shuffle(cartas)
print(cartas)
