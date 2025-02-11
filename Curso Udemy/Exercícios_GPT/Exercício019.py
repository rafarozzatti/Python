"""Exercício: Dado dois conjuntos:
- Encontre a interseção e a união entre eles.
- Verifique se o conjunto A é subconjunto de B."""

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f'''Interseção: {A.intersection(B)}
União: {A.union(B)}
A é subconjunto de B? {A.issubset(B)}''')