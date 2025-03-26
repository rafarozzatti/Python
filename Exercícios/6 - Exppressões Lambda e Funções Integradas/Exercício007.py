"""Você tem uma lista de números. Use o any() para verificar se há pelo menos um número negativo na lista e use o all() para verificar se todos os números são positivos."""

numeros = [1, -2, 3, 4, 5]

print(any(numero < 0 for numero in numeros))
print(all(numero > 0 for numero in numeros))
