conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

# Imprime imprime True se todos os elementos do conjunto_a não estão presentes no conjunto_b
print(conjunto_a.isdisjoint(conjunto_b))

# Imprime imprime True se todos os elementos do conjunto_a não estão presentes no conjunto_c
print(conjunto_a.isdisjoint(conjunto_c))
