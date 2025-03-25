"""Trabalhar com a estrutura deque, que permite manipulação eficiente de elementos em ambas as extremidades da fila.

📌 Exercício:

Crie um deque com os números de 1 a 5.

Adicione o número 0 no início e 6 no final.

Remova o primeiro e o último elemento.

Exiba o deque final."""

from collections import deque

lista = deque([1, 2, 3, 4, 5])
lista.appendleft(0)
lista.append(6)
lista.popleft()
lista.pop()
print(lista)
