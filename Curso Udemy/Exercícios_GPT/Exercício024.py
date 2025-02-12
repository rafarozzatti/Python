"""Exercício: Utilize deque para adicionar e remover elementos de ambos os lados."""

from collections import deque
deq = deque('python')
print(f'Palavra original: {''.join(deq)}')
deq.append('s')
print(f'Palavra com uma letra adicionada na direita: {''.join(deq)}')
deq.pop()
print(f'Palavra com a ultima letra removida: {''.join(deq)}')
deq.appendleft('p')
print(f'Palavra com uma letra adicionada na esquerda: {''.join(deq)}')
deq.popleft()
print(f'Palavra com a primeira letra removida: {''.join(deq)}')