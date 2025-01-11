import random
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
l = [n1, n2, n3, n4]
e = random.choice(l)
print(f'O aluno escolhido foi {e}')