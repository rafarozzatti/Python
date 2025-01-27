A = [1, 0, 5, -2, -5, 7]
soma = A[0] + A[1] + A[5]
print(f'A soma entre {A[0]}, {A[1]} e {A[5]} é igual a {soma}')
A[5] = 100
print(f'\nNova lista: {A}')
print()
for num in A:
    print(num)
    