"""Implemente uma função fibonacci(n) que retorna o n-ésimo termo da sequência de Fibonacci usando recursão."""

def fibonacci(n):
    if n <= 0:
        return "Entrada inválida. O número deve ser maior ou igual a 1."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Exemplo de uso:
n = int(input("Digite um número: "))
print(f"O {n}-ésimo termo da sequência de Fibonacci é {fibonacci(n)}")
