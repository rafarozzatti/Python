"""Crie um deque e adicione cinco números. Depois, remova um elemento do início (fila) e um do final (pilha). Exiba o deque atualizado."""

from collections import deque

deq = deque([1, 2, 3, 4, 5])
print(f'Deque original: {deq}')
deq.pop()
deq.popleft()
print(f'Deque atualizado: {deq}')
