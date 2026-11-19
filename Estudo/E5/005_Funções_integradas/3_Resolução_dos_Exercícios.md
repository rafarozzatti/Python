## Exercício 1

```python
vendas = [150, 200, 350, 100, 250]

print(len(vendas))
print(sum(vendas))
```

## Exercício 2

```python
precos = [120, 85, 250, 40, 180, 95]

print(min(precos))
print(max(precos))
```

## Exercício 3

```python
numeros = [45, 12, 89, 3, 27, 60]

ordenados = sorted(numeros)

print(numeros)
print(ordenados)
```

## Exercício 4

```python
notas = [7.5, 9.0, 6.5, 8.0, 5.5]

notas_ordenadas = sorted(notas, reverse=True)

print(notas_ordenadas)
```

## Exercício 5

```python
media = 8.67894

media_arredondada = round(media, 2)

print(media_arredondada)
```

## Exercício 6

```python
produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor']

for indice, produto in enumerate(produtos, start=1):
    print(f'{indice} - {produto}')
```

## Exercício 7

```python
nomes = ['Carlos', 'Ana', 'Pedro']
salarios = [3000, 4500, 3500]

for nome, salario in zip(nomes, salarios):
    print(f'{nome} recebe R$ {salario}')
```

## Exercício 8

```python
produtos = ['Notebook', 'Mouse', 'Teclado']
precos = [3500, 80, 150]
quantidades = [5, 20, 15]

for produto, preco, quantidade in zip(produtos, precos, quantidades):
    print(f'{produto} - R$ {preco} - Quantidade: {quantidade}')
```

## Exercício 9

```python
produtos = ['Notebook', 'Mouse', 'Teclado']
precos = [3500, 80, 150]
quantidades = [2, 5, 3]

for produto, preco, quantidade in zip(produtos, precos, quantidades):
    print(f'{produto} - Total: R$ {preco * quantidade}')
```

## Exercício 10

```python
vendas = [1200.456, 850.789, 2300.123, 1750.567, 950.234]

vendas

print(len(vendas))
print(sum(vendas))
print(min(vendas))
print(max(vendas))
print(round((sum(vendas)) / (len(vendas)), 2))
print(sorted(vendas, reverse=True))
```
