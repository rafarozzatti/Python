## Exercício 1

```python
def operacoes (a, b):
    soma = a + b
    subtracao = a - b

    return soma, subtracao

resultado_soma, resultado_subtracao = operacoes(20, 8)

print(resultado_soma)
print(resultado_subtracao)
```

## Exercício 2

```python
def dados_produto (nome, preco, quantidade):
    return nome, preco, quantidade

produto = dados_produto('Notebook', 3500, 2)

print(produto)
print(type(produto))
```

## Exercício 3

```python
def calcular_valores (preco):
    desconto_10 = preco * 0.9
    desconto_20 = preco * 0.8

    return desconto_10, desconto_20

resultado_10, resultado_20 = calcular_valores(100)

print(resultado_10)
print(resultado_20)
```

## Exercício 4

```python
def analisar_numeros (numeros):
    soma = sum(numeros)
    quantidade = len(numeros)

    return soma, quantidade

soma, quantidade = analisar_numeros([10, 20, 30, 40, 50])

print(soma)
print(quantidade)
```

## Exercício 5

```python
def avaliar_notas (nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 7:
        return media, 'Aprovado'
    else:
        return media, 'Reprovado'

media, situacao = avaliar_notas(8, 6)

print(media)
print(situacao)
```

## Exercício 6

```python
def dados_funcionario (nome, cargo, salario):
    return nome, cargo, salario

funcionario = dados_funcionario('Rafael', 'Analista de Dados', 3500)

print(funcionario)
```

## Exercício 7

```python
def estatisticas (numeros):
    menor = min(numeros)
    maior = max(numeros)
    soma = sum(numeros)

    return menor, maior, soma

menor, maior, soma = estatisticas([12, 5, 30, 8, 20])

print(menor)
print(maior)
print(soma)
```

## Exercício 8

```python
def resumo_vendas (vendas):
    total_vendido = sum(vendas)
    quantidade_vedida = len(vendas)
    media_vendas = total_vendido / quantidade_vedida

    return total_vendido, quantidade_vedida, media_vendas

total, quantidade, media = resumo_vendas([100, 200, 300, 400])

print(total)
print(quantidade)
print(media)
```

## Exercício 9

```python
def analisar_produto (produto):
    nome = produto[0]
    preco = produto[1]
    quantidade = produto[2]

    return nome, preco, quantidade

produto = ('Monitor', 1200, 15)

nome, preco, estoque = analisar_produto(produto)

print(nome)
print(preco)
print(estoque)
```

## Exercício 10

```python
def analisar_pedido (lista):
    valor_total = sum(lista)
    quantiade_produtos = len(lista)
    maior_preco = max(lista)

    return valor_total, quantiade_produtos, maior_preco

total, quantidade, maior_preco = analisar_pedido([150, 80, 200, 70, 100])

print(total)
print(quantidade)
print(maior_preco)
```
