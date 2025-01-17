## Listas (Parte 1)

#### Exemplos:

```python
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche[3] = 'Picole'
# Resultado: 'Hamburguer', 'Suco', 'Pizza', 'Picole'
```

```python
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche.append('Cookie')
# Resultado: 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Cookie'
```

```python
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche.insert(0, 'Cookie')
# Resultado: 'Cookie', 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
```

```python
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
del lanche[3]
# Resultado: 'Cookie', 'Hamburguer', 'Suco', 'Pudim'
```

```python
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche.pop()
# Resultado: 'Cookie', 'Hamburguer', 'Suco', 'Pizza'
```

```python
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche.pop(3)
# Resultado: 'Cookie', 'Hamburguer', 'Suco', 'Pudim'
```

```python
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche.remove('Pizza')
# Resultado: 'Cookie', 'Hamburguer', 'Suco', 'Pudim'
```

```python
valores = list(range(4, 11))
print(valores)
# Resultado: 4 5 6 7 8 9 10
```

```python
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores.sort())
# Resultado: 0 2 3 4 5 8 9
```

```python
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
print(valores.sort(reverse=True))
# Resultado: 9 8 5 4 3 2 0
```

```python
valores = [8, 2, 5, 4, 9, 3, 0]
print(len(valores))
# Resultado: 7
```