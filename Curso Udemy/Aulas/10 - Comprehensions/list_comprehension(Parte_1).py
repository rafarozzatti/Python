numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)
res = [numero / 2 for numero in numeros]
print(res)
print()


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)
print()


numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)
print(numeros_dobrados)
print([numero * 2 for numero in numeros])
print()


nome = 'Geek University'
print([letra.upper() for letra in nome])
print()


def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['mario', 'julia', 'pedro', 'guilherme', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])
print()


print([numero * 3 for numero in range(1, 10)])
print()


print([bool(valor) for valor in [0, [], '', True, 1, 3, 14]])
print()


print([str(numero) for numero in [1, 2, 3, 4, 5]])
