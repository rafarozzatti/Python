## Exercício 1

```python
numeros = [i for i in range(1, 11)]

print(numeros)
```

## Exercício 2

```python
dobros = [i * 2 for i in range(1, 11)]

print(dobros)
```

## Exercício 3

```python
pares = [i for i in range(1, 21) if i % 2 == 0]

print(pares)
```

## Exercício 4

```python
impares = [i for i in range(1, 31) if i % 2 != 0]

print(impares)
```

## Exercício 5

```python
quadrados = [i ** 2 for i in range(1, 11)]

print(quadrados)
```

## Exercício 6

```python
dobros_pares = [i * 2 for i in range(1, 21) if i % 2 == 0]

print(dobros_pares)
```

## Exercício 7

```python
classificacao = ['Par' if i % 2 == 0 else 'Ímpar' for i in range(1, 11)]

print(classificacao)
```

## Exercício 8

```python
nomes = ["carlos", "mariana", "pedro", "ana"]

nomes_maiusculos = [nome.upper() for nome in nomes]

print(nomes_maiusculos)
```

## Exercício 9

```python
nomes = ["Carlos", "Mariana", "Pedro", "Ana", "Roberto", "João"]

nomes_grandes = [nome for nome in nomes if len(nome) > 5]

print(nomes_grandes)
```

## Exercício 10

```python
vendas = [150, 80, 250, 40, 300, 120, 60, 500]

vendas_altas = [venda * 1.1 for venda in vendas if venda > 100]

print(vendas_altas)
```
