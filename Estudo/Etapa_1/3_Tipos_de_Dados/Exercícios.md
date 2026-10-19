# Exercícios de Tipos de dados

## Exercício 1

Crie quatro variáveis:

1. idade, com o valor inteiro 27.
2. salario, com o valor decimal 3500.75.
3. nome, com o texto "Rafael".
4. empregado, com o valor lógico True.
Depois, utilize print() para exibir cada variável, nessa ordem, uma por linha.

Saída esperada:

```
27
3500.75
Rafael
True
```

## Exercício 2

Agora, crie quatro variáveis com os seguintes valores:

1. `quantidade` com o valor `15`.
2. `preco` com o valor `49.99`.
3. `produto` com o texto `"Teclado"`.
4. `disponivel` com o valor lógico `False`.

Desta vez, em vez de exibir os valores, utilize `print()` com a função `type()` para mostrar o tipo de cada variável, na ordem indicada.

Saída esperada:

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

## Exercício 3

Agora, vamos verificar se você consegue identificar quando um número está armazenado como texto.

Crie estas quatro variáveis:

1. `a` com o valor `100` (sem aspas).
2. `b` com o valor `"100"` (com aspas).
3. `c` com o valor `25.5` (sem aspas).
4. `d` com o valor `"25.5"` (com aspas).

Depois, utilize `print(type(...))` para exibir o tipo de cada variável, na ordem `a`, `b`, `c`, `d`.

Saída esperada:

```
<class 'int'>
<class 'str'>
<class 'float'>
<class 'str'>
```

## Exercício 4

Agora, vamos praticar o tipo `bool`.

Crie quatro variáveis:

1. `maior_de_idade` com o valor `True`.
2. `pedido_pago` com o valor `False`.
3. `tem_estoque` com o valor `True`.
4. `mensagem` com o texto `"False"`.

Depois, utilize `print(type(...))` para exibir o tipo de cada variável, nessa ordem.

Saída esperada:

```
<class 'bool'>
<class 'bool'>
<class 'bool'>
<class 'str'>
```

## Exercício 5

Imagine que você está criando um cadastro de produtos para uma empresa.

Crie as seguintes variáveis:

1. `codigo_produto` com o valor inteiro `205`.
2. `preco` com o valor decimal `89.90`.
3. `nome_produto` com o texto `"Mouse sem fio"`.
4. `em_promocao` com o valor lógico `True`.
5. `marca` com o texto `"Logitech"`.

Depois, utilize `print(type(...))` para exibir o tipo de cada variável, exatamente nessa ordem.

Saída esperada:

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'str'>
```

## Exercício 6

Agora, vamos aumentar um pouco a dificuldade.

Crie as seguintes variáveis:

1. `nome_funcionario` com o texto `"Mariana"`.
2. `idade` com o valor inteiro `32`.
3. `salario` com o valor decimal `4200.50`.
4. `ativo` com o valor lógico `True`.

Depois, exiba o valor e o tipo de cada variável, nessa ordem. Para cada variável, use primeiro um `print()` para mostrar seu valor e depois outro `print()` com `type()` para mostrar seu tipo.

Saída esperada:

```
Mariana
<class 'str'>
32
<class 'int'>
4200.5
<class 'float'>
True
<class 'bool'>
```

## Exercício 7

Agora, vamos praticar a identificação dos tipos sem executar o código primeiro.

Crie estas seis variáveis:

```
a = 0b = -15c = 3.14d = "Python"e = Falsef = "2026"
```

Depois, utilize `print(type(...))` para mostrar o tipo de cada variável, na ordem `a`, `b`, `c`, `d`, `e`, `f`.

Saída esperada:

```
<class 'int'>
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'str'>
```

## Exercício 8

Imagine que você está trabalhando com dados de vendas de uma empresa.

Crie as seguintes variáveis:

1. `vendas_dia` com o valor inteiro `150`.
2. `valor_total` com o valor decimal `12750.80`.
3. `regiao` com o texto `"Sudeste"`.
4. `meta_atingida` com o valor lógico `True`.
5. `mes_referencia` com o texto `"Outubro"`.
6. `desconto` com o valor decimal `0.15`.

Depois, utilize `print(type(...))` para exibir o tipo de cada variável, nessa ordem.

Saída esperada:

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'str'>
<class 'float'>
```

## Exercício 9

Agora, vamos trabalhar com um código que contém erros nos tipos de dados.

Uma empresa precisa armazenar o nome de um produto, seu preço, a quantidade disponível e se ele está em promoção.

O código abaixo foi escrito por outra pessoa:

```
nome_produto = 500preco = "79.90"quantidade = "20"em_promocao = "True"
```

Sua tarefa:

Corrija as atribuições para que cada variável tenha o tipo adequado:

- `nome_produto` → `str`
- `preco` → `float`
- `quantidade` → `int`
- `em_promocao` → `bool`

Depois, utilize `print(type(...))` para exibir o tipo das quatro variáveis, nessa ordem.

Saída esperada:

```
<class 'str'>
<class 'float'>
<class 'int'>
<class 'bool'>
```

## Exercício 10

Este é o último exercício desta aula. Vamos reunir os quatro tipos de dados em um único programa.

Crie as seguintes variáveis:

1. `nome_cliente` com o texto `"Ana Souza"`.
2. `idade_cliente` com o valor inteiro `29`.
3. `valor_compra` com o valor decimal `349.90`.
4. `cliente_ativo` com o valor lógico `True`.
5. `compras_realizadas` com o valor inteiro `12`.
6. `recebe_promocoes` com o valor lógico `False`.

Depois, para cada variável, exiba primeiro seu valor e, na linha seguinte, seu tipo utilizando `type()`. Siga exatamente a ordem da lista.

Saída esperada:

```
Ana Souza
<class 'str'>
29
<class 'int'>
349.9
<class 'float'>
True
<class 'bool'>
12
<class 'int'>
False
<class 'bool'>
```
