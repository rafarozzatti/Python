# Exercícios de Retorno de Múltiplos Valores

## Exercício 1

Crie uma função chamada `operacoes` que:

1. Receba dois parâmetros: `a` e `b`.
2. Calcule a soma dos dois números.
3. Calcule a subtração de `a` por `b`.
4. Retorne os dois resultados simultaneamente.

Depois:

- Chame a função passando `20` e `8`.
- Armazene os resultados em duas variáveis: `resultado_soma` e `resultado_subtracao`.
- Exiba as duas variáveis utilizando `print()`.

Saída esperada:

```
28
12
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-1)

## Exercício 2

Crie uma função chamada `dados_produto` que:

1. Receba três parâmetros: `nome`, `preco` e `quantidade`.
2. Retorne os três valores simultaneamente.

Depois:

- Chame a função passando `'Notebook'`, `3500` e `2`.
- Armazene o retorno em uma única variável chamada `produto`.
- Exiba essa variável com `print()`.
- Exiba também o tipo de dado de `produto` utilizando `type()`.

Saída esperada:

```
('Notebook', 3500, 2)
<class 'tuple'>
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-2)

## Exercício 3

Agora vamos fazer o caminho inverso.

Crie uma função chamada `calcular_valores` que:

1. Receba um parâmetro chamado `preco`.
2. Calcule o valor com 10% de desconto.
3. Calcule o valor com 20% de desconto.
4. Retorne os dois resultados simultaneamente.

Depois:

- Chame a função passando `100`.
- Receba os resultados em duas variáveis: `desconto_10` e `desconto_20`.
- Exiba as duas variáveis.

Saída esperada:

```
90.0
80.0
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-3)

## Exercício 4

Crie uma função chamada `analisar_numeros` que:

1. Receba uma lista de números como parâmetro.
2. Calcule a soma dos números.
3. Calcule a quantidade de elementos da lista.
4. Retorne os dois resultados simultaneamente.

Depois:

- Chame a função passando `[10, 20, 30, 40, 50]`.
- Armazene os resultados em `soma` e `quantidade`.
- Exiba as duas variáveis.

Saída esperada:

```
150
5
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-4)

## Exercício 5

Crie uma função chamada `avaliar_notas` que:

1. Receba duas notas: `nota1` e `nota2`.
2. Calcule a média das notas.
3. Verifique se a média é maior ou igual a 7.
4. Retorne simultaneamente a média e a situação (`'Aprovado'` ou `'Reprovado'`).

Depois:

- Chame a função passando `8` e `6`.
- Armazene os resultados em `media` e `situacao`.
- Exiba as duas variáveis.

Saída esperada:

```
7.0
Aprovado
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-5)

## Exercício 6

Crie uma função chamada `dados_funcionario` que:

1. Receba três parâmetros: `nome`, `cargo` e `salario`.
2. Retorne os três valores simultaneamente.

Depois:

- Chame a função passando `'Rafael'`, `'Analista de Dados'` e `3500`.
- Armazene os resultados em uma única variável chamada `funcionario`.
- Exiba a variável com `print()`.

Saída esperada:

```
('Rafael', 'Analista de Dados', 3500)
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-6)

## Exercício 7

Crie uma função chamada `estatisticas` que:

1. Receba uma lista de números.
2. Calcule o menor número.
3. Calcule o maior número.
4. Calcule a soma dos números.
5. Retorne os três resultados simultaneamente.

Depois:

- Chame a função passando `[12, 5, 30, 8, 20]`.
- Armazene os resultados em `menor`, `maior` e `soma`.
- Exiba as três variáveis.

Pode utilizar `min()`, `max()` e `sum()`, que já estudamos anteriormente.

Saída esperada:

```
5
30
75
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-7)

## Exercício 8

Crie uma função chamada `resumo_vendas` que:

1. Receba uma lista de valores de vendas.
2. Calcule o total vendido.
3. Calcule a quantidade de vendas.
4. Calcule a média das vendas.
5. Retorne os três resultados simultaneamente.

Depois:

- Chame a função passando `[100, 200, 300, 400]`.
- Armazene os resultados em `total`, `quantidade` e `media`.
- Exiba as três variáveis.

Pode utilizar `sum()` e `len()`.

Saída esperada:

```
1000
4
250.0
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-8)

## Exercício 9

Crie uma função chamada `analisar_produto` que:

1. Receba uma tupla contendo três informações: nome do produto, preço e quantidade em estoque.
2. Retorne essas três informações separadamente.

Depois:

- Crie a tupla `('Monitor', 1200, 15)`.
- Passe essa tupla como argumento para a função.
- Armazene os três valores retornados em `nome`, `preco` e `estoque`.
- Exiba as três variáveis.

Saída esperada:

```
Monitor
1200
15
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-9)

## Exercício 10

Crie uma função chamada `analisar_pedido` que:

1. Receba uma lista contendo os preços dos produtos de um pedido.
2. Calcule o valor total do pedido.
3. Calcule a quantidade de produtos.
4. Calcule o maior preço entre os produtos.
5. Retorne os três resultados simultaneamente.

Depois:

- Passe a lista `[150, 80, 200, 70, 100]` para a função.
- Armazene os resultados em `total`, `quantidade` e `maior_preco`.
- Exiba as três variáveis.

Pode utilizar `sum()`, `len()` e `max()`.

Saída esperada:

```
600
5
200
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-10)
