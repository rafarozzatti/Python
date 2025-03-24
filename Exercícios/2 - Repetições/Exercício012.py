"""Crie um programa que solicite ao usuário para digitar números repetidamente. O programa deve somar esses números até que o usuário digite 0. Quando o número 0 for digitado, o programa deve imprimir a soma total e terminar.

Use um loop while para continuar pedindo números.

Use uma condição para verificar quando o número 0 for digitado."""

soma = 0

while True:
    num = int(input('Digite um numero: '))
    if num == 0:
        break
    soma += num
print(f'A soma dos números é igual a {soma}')
