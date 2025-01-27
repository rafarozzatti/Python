lista1 = ['Geek University']
letra = 'e'
if letra in lista1:
    print(f'Encontrei a letra {letra}')
else:
    print(f'Não encontrei a letra {letra}')
print()


lista2 = range(0, 11)
num  = 17
if num in lista2:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')
print()


lista3 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista3.sort()
print(f'''Lista ordenada: {lista3}
A lista tem {len(lista3)} números
A lista tem {lista3.count(1)} números 1
A soma dos números da lista é igual a {sum(lista3)}
O número 15 está no índice {lista3.index(15)}
O maior número é o {max(lista3)}
O menor número é o {min(lista3)}''')
print()


lista4 = []
lista4.append(4)
lista4.append(1)
print(lista4)
lista4.insert(1, 7)
print(lista4)
lista4.extend([17, 42, 99])
print(lista4)
print()


lista5 = ['P', 'Y', 'T', 'H', 'O', 'N']
lista5.reverse()
print(lista5)
print()


lista5 = ['P', 'Y', 'T', 'H', 'O', 'N']
print(lista5[:: -1])
print()


lista5 = ['P', 'Y', 'T', 'H', 'O', 'N']
lista5.pop()
print(lista5)
print()


lista5 = ['P', 'Y', 'T', 'H', 'O', 'N']
lista5.pop(2)
print(lista5)
print()


lista5 = ['P', 'Y', 'T', 'H', 'O', 'N']
lista5.clear()
print(lista5)
print()


curso = 'Curso de Python'
curso = curso.split()
print(curso)
print()


lista6 = ['Programação', 'em', 'Python']
curso = ' '.join(lista6)
print(curso)
print()


soma = 0
for elemento in lista3:
    print(elemento, end=' ')
    soma += elemento
print(f'\nA soma dos elementos da lista é igual a {soma}')
print()


carrinho = []
produto = ''
while produto != 'sair':
    produto = input('Adicione um produto na lista ou digite "sair" para sair: ')
    if produto != 'sair':
        carrinho.append(produto)
print(carrinho)
for produto in carrinho:
    print(produto, end=' ')
print()
print()


cor = ['verde', 'branco', 'vermelho', 'preto']
print(cor[0])
print(cor[:2])
print(cor[2:])
print(cor[-1])
print()


lista = [1, 2, 3]
nova = lista.copy()
nova.append(4)
print(lista)
print(nova)