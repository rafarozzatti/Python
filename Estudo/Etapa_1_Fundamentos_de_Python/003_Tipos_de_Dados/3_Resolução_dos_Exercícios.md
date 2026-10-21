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

Resolução:
``` python
idade = 27
salario = 3500.75
nome = 'Rafael'
empregado = True

print(idade)
print(salario)
print(nome)
print(empregado)
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

Resolução:
``` python
quantidade = 15
preco = 49.99
produto = 'Teclado'
disponivel = False

print(type(quantidade))
print(type(preco))
print(type(produto))
print(type(disponivel))
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

Resolução:
``` python
a = 100
b = '100'
c = 25.5
d = '25.5'

print(type(a))
print(type(b))
print(type(c))
print(type(d))
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

Resolução:
``` python
maior_de_idade = True
pedido_pago = False
tem_estoque = True
mensagem = 'False'

print(type(maior_de_idade))
print(type(pedido_pago))
print(type(tem_estoque))
print(type(mensagem))
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

Resolução:
``` python
codigo_produto = 205
preco = 89.90
nome_produto = 'Mouse sem fio'
em_promocao = True
marca = 'Logitech'

print(type(codigo_produto))
print(type(preco))
print(type(nome_produto))
print(type(em_promocao))
print(type(marca))
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

Resolução:
``` python
nome_funcionario = 'Mariana'
idade = 32
salario = 4200.50
ativo = True

print(nome_funcionario)
print(type(nome_funcionario))
print(idade)
print(type(idade))
print(salario)
print(type(salario))
print(ativo)
print(type(ativo))
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

Resolução:
``` python
a = 0
b = -15
c = 3.14
d = "Python"
e = False
f = "2026"

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
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

Resolução:
``` python
vendas_dia = 150
valor_total = 12750.80
regiao = 'Sudeste'
meta_atingida = True
mes_referencia = 'Outubro'
desconto = 0.15

print(type(vendas_dia))
print(type(valor_total))
print(type(regiao))
print(type(meta_atingida))
print(type(mes_referencia))
print(type(desconto))
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

Resolução:
``` python
nome_produto = '500'
preco = 79.90
quantidade = 20
em_promocao = True

print(type(nome_produto))
print(type(preco))
print(type(quantidade))
print(type(em_promocao))
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

Resolução:
``` python
nome_cliente = 'Ana Souza'
idade_cliente = 29
valor_compra = 349.90
cliente_ativo = True
compras_realizadas = 12
recebe_promocoes = False

print(nome_cliente)
print(type(nome_cliente))
print(idade_cliente)
print(type(idade_cliente))
print(valor_compra)
print(type(valor_compra))
print(cliente_ativo)
print(type(cliente_ativo))
print(compras_realizadas)
print(type(compras_realizadas))
print(recebe_promocoes)
print(type(recebe_promocoes))
```
