conjunto1 = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(conjunto1)
print()


conjunto2 = {0, 1, 17, 23}
print(conjunto2)
conjunto2.remove(17)
print(conjunto2)
print()


conjunto3 = {0, 1, 17, 23}
print(conjunto3)
conjunto3.discard(1)
print(conjunto3)
print()


estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernanda', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
unicos = estudantes_python.union(estudantes_java)
print(unicos)
ambos = estudantes_python.intersection(estudantes_java)
print(ambos)
so_python = estudantes_python.difference(estudantes_java)
print(so_python)
so_java = estudantes_java.difference(estudantes_python)
print(so_java)
