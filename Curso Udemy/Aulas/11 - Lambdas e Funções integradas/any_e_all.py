print(all([0, 1, 2, 3, 4, 5]))
print(all([1, 2, 3, 4, 5]))
print(all([]))
print(all((1, 2, 3, 4, 5)))
print(all({1, 2, 3, 4, 5}))
print(all('Geek'))
print()

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Daniel']
print(all([nome[0] == 'C' for nome in nomes]))
print()


print(all([num for num in [2, 4, 6, 8, 10] if num % 2 == 0]))
print(all([num for num in [2, 4, 5, 8, 10] if num % 2 == 0]))
print()


print(any([0, 1, 2, 3, 4, 5]))
print(any([0, False, {}, (), []]))
