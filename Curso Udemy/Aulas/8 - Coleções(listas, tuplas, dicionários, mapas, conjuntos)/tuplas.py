# Tuplas são IMUTAVEIS

tupla1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tupla1)
print()


tupla2 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(tupla2)
print()


tupla3 = tuple(range(11))
print(tupla3)
print()


tupla4 = ('Python', 'Java')
x, y = tupla4
print(x)
print(y)
print()


tupla5 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(tupla5))
print()


tupla6 = (1, 2, 3)
for n in tupla6:
    print(n)
print()


tupla7 = (1, 2, 3, 4, 5, 5, 5, 6, 7)
print(tupla7.count(5))
print()


tupla8 = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(tupla8[11])
print(tupla8.index('Janeiro'))
i = 0
while i < len(tupla8):
    print(tupla8[i])
    i += 1
print()
