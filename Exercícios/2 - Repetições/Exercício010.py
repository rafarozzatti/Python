"""Crie um programa que peça ao usuário para digitar 10 números. O programa deve contar quantos números são pares e quantos são ímpares."""

contp = conti = 0

for c in range(1, 11):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        contp += 1
    else:
        conti += 1

print(f'Foram digitados {contp} números pares e {conti} números ímpares')
