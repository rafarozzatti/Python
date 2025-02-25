"""Peça ao usuário para digitar dez números inteiros, adicione-os a um conjunto e exiba apenas os números únicos."""

conjunto = set()
for c in range(1, 11):
    num = int(input(f'Digite o {c}º número: '))
    conjunto.add(num)
print(f'Números únicos digitados: {conjunto}')
