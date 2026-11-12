## Exercício 1

```python
numeros = {10, 20, 30, 40, 50, 10, 20}

print(numeros)
print(type(numeros))

dados = set()

print(dados)
print(type(dados))
```

## Exercício 2

```python
frutas = {"Maçã", "Banana", "Uva", "Laranja"}

print('Banana' in frutas)
print('Morango' in frutas)
print('Uva' not in frutas)
print('Abacaxi' not in frutas)
```

## Exercício 3

```python
numeros = {10, 20, 30}

numeros.add(40)
numeros.add(50)
numeros.add(20)

print(numeros)
```

## Exercício 4

```python
frutas = {"Maçã", "Banana"}

frutas.update(['Uva', 'Laranja'])
frutas.update(['Morango', 'Banana'])

print(frutas)
```

## Exercício 5

```python
numeros = {10, 20, 30, 40, 50}

numeros.remove(30)
numeros.remove(50)

print(numeros)
```

## Exercício 6

```python
cores = {"Azul", "Verde", "Vermelho", "Amarelo"}

cores.discard('Verde')
cores.discard('Preto')

print(cores)
```

## Exercício 7

```python
numeros = {10, 20, 30, 40, 50}
print(numeros)

numeros.clear()

print(numeros)
print(type(numeros))
```

## Exercício 8

```python
numeros_a = {1, 2, 3, 4}
numeros_b = {3, 4, 5, 6}

resultado = numeros_a.union(numeros_b)

print(resultado)
print(numeros_a)
print(numeros_b)
```

## Exercício 9

```python
numeros_a = {1, 2, 3, 4, 5}
numeros_b = {4, 5, 6, 7, 8}

resultado = numeros_a.intersection(numeros_b)

print(resultado)
print(numeros_a)
print(numeros_b)
```

## Exercício 10

```python
numeros_a = {1, 2, 3, 4, 5}
numeros_b = {3, 4, 5, 6, 7}

resultado_a = numeros_a.difference(numeros_b)
resultado_b = numeros_b.difference(numeros_a)

print(resultado_a)
print(resultado_b)
```
