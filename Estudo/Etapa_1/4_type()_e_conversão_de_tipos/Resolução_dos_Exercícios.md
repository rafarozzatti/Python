# Exercícios de type() e conversão de tipos

## Exercício 1

Crie uma variável chamada numero com o texto "150".

Depois:
1. Exiba o tipo original da variável usando type().
2. Converta o valor para inteiro usando int() e armazene o resultado em uma variável chamada numero_inteiro.
3. Exiba o valor de numero_inteiro.
4. Exiba o tipo de numero_inteiro.

Resolução:
```python
numero = '150'
print(type(numero))

numero_interiro = int(numero)

print(numero_interiro)
print(type(numero_interiro))
```

## Exercício 2

Crie uma variável chamada `preco` com o texto `"79.90"`.

Depois:

1. Exiba o tipo original de `preco` usando `type()`.
2. Converta `preco` para decimal usando `float()` e armazene o resultado em `preco_decimal`.
3. Exiba o valor de `preco_decimal`.
4. Exiba o tipo de `preco_decimal`.

Saída esperada:

```
<class 'str'>
79.9
<class 'float'>
```

Resolução:
```python
preco = '79.90'
print(type(preco))

preco_decimal = float(preco)

print(preco_decimal)
print(type(preco_decimal))
```

## Exercício 3

Agora, vamos praticar a conversão usando `str()`.

Crie uma variável chamada `idade` com o valor inteiro `27`.

Depois:

1. Exiba o tipo original de `idade` usando `type()`.
2. Converta `idade` para texto usando `str()` e armazene o resultado em `idade_texto`.
3. Exiba o valor de `idade_texto`.
4. Exiba o tipo de `idade_texto`.

Saída esperada:

```
<class 'int'>
27
<class 'str'>
```

Resolução:
```python
idade = 27
print(type(idade))

idade_texto = str(idade)

print(idade_texto)
print(type(idade_texto))
```

## Exercício 4

Agora, vamos praticar a conversão de `float` para `int`.

Crie uma variável chamada `nota` com o valor `8.75`.

Depois:

1. Exiba o tipo original de `nota`.
2. Converta `nota` para inteiro usando `int()` e armazene o resultado em `nota_inteira`.
3. Exiba o valor de `nota_inteira`.
4. Exiba o tipo de `nota_inteira`.

Saída esperada:

```
<class 'float'>
8
<class 'int'>
```

Lembre-se: `int()` remove a parte decimal, sem arredondar.

Resolução:
```python
nota = 8.75
print(type(nota))

nota_inteira = int(nota)

print(nota_inteira)
print(type(nota_inteira))
```

## Exercício 5

Agora, vamos praticar a conversão para valores lógicos.

Crie quatro variáveis com os seguintes valores:

1. `a = 0`
2. `b = 1`
3. `c = ""` (texto vazio)
4. `d = "Python"` (texto não vazio)

Depois, utilize `bool()` para converter cada valor e exiba os resultados com `print()`, na ordem indicada.

Saída esperada:

```
False
True
False
True
```

Resolução:
```python
a = 0
b = 1
c = ""
d = "Python"

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
```

## Exercício 6

Este exercício testa uma diferença importante entre textos e valores lógicos.

Crie estas quatro variáveis:

```
a = "False"b = ""c = "0"d = 0
```

Depois, utilize `bool()` com cada variável e exiba os resultados usando `print()`, na ordem `a`, `b`, `c`, `d`.

Saída esperada:

```
True
False
True
False
```

Resolução:
```python
a = "False"
b = ""
c = "0"
d = 0

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
```

## Exercício 7

Agora, vamos combinar diferentes conversões em um único programa.

Crie estas variáveis:

```
a = "250"b = "12.5"c = 40d = 0
```

Depois, faça as seguintes conversões e armazene cada resultado em uma nova variável:

1. Converta `a` para inteiro, armazenando em `a_inteiro`.
2. Converta `b` para decimal, armazenando em `b_decimal`.
3. Converta `c` para texto, armazenando em `c_texto`.
4. Converta `d` para valor lógico, armazenando em `d_logico`.

Por fim, exiba o valor e o tipo de cada nova variável, nessa ordem. Para cada uma, use um `print()` para o valor e outro para `type()`.

Saída esperada:

```
250
<class 'int'>
12.5
<class 'float'>
40
<class 'str'>
False
<class 'bool'>
```

Resolução:
```python
a = "250"
b = "12.5"
c = 40
d = 0

a_inteiro = int(a)
b_decimal = float(b)
c_texto = str(c)
d_logico = bool(d)

print(a_inteiro)
print(type(a_inteiro))
print(b_decimal)
print(type(b_decimal))
print(c_texto)
print(type(c_texto))
print(d_logico)
print(type(d_logico))
```

## Exercício 8

Imagine que você recebeu dados de vendas armazenados nos tipos errados e precisa convertê-los para realizar cálculos.

Comece com estas variáveis:

```
preco = "49.90"quantidade = "3"
```

Faça o seguinte:

1. Converta `preco` para `float` e armazene o resultado em `preco_convertido`.
2. Converta `quantidade` para `int` e armazene o resultado em `quantidade_convertida`.
3. Crie a variável `total`, multiplicando `preco_convertido` por `quantidade_convertida`.
4. Exiba o valor de `total`.
5. Exiba o tipo de `total` usando `type()`.

Saída esperada:

```
149.7
<class 'float'>
```

Resolução:
```python
preco = "49.90"
quantidade = "3"

preco_convertido = float(preco)
quantidade_convertida = int(quantidade)

total = preco_convertido * quantidade_convertida

print(total)
print(type(total))
```

## Exercício 9

Considere as variáveis abaixo:

```
nome = "Notebook"preco = "3500.50"estoque = "12"disponivel = 1
```

Faça o seguinte:

1. Converta `preco` para `float` e armazene em `preco_convertido`.
2. Converta `estoque` para `int` e armazene em `estoque_convertido`.
3. Converta `nome` para `bool` e armazene em `nome_logico`.
4. Converta `disponivel` para `bool` e armazene em `disponivel_logico`.
5. Imprima o valor e o tipo de cada uma das quatro novas variáveis.

Resolução:
```python
nome = "Notebook"
preco = "3500.50"
estoque = "12"
disponivel = 1

preco_convertido = float(preco)
estoque_convertido = int(estoque)
nome_logico = bool(nome)
disponivel_logico = bool(disponivel)

print(preco_convertido)
print(type(preco_convertido))
print(estoque_convertido)
print(type(estoque_convertido))
print(nome_logico)
print(type(nome_logico))
print(disponivel_logico)
print(type(disponivel_logico))
```

## Exercício 10

Este é o último exercício do tópico. Vamos combinar conversão de tipos com cálculo.

Considere as variáveis:

```
produto = "Mouse"preco = "89.90"quantidade = "4"desconto = "10"
```

Faça o seguinte:

1. Converta `preco` para `float`.
2. Converta `quantidade` para `int`.
3. Converta `desconto` para `float`.
4. Calcule o valor total sem desconto e armazene em `total`.
5. Calcule o valor do desconto e armazene em `valor_desconto`. O desconto é uma porcentagem do total.
6. Calcule o valor final, subtraindo o desconto do total, e armazene em `total_final`.
7. Imprima `produto`, `total`, `valor_desconto` e `total_final`.

Atenção: o desconto de `"10"` representa 10%, não R$ 10,00.

Resolução:
```python
produto = "Mouse"
preco = "89.90"
quantidade = "4"
desconto = "10"

preco_convertido = float(preco)
quantidade_convertida = int(quantidade)
desconto_covertido = float(desconto)

total = preco_convertido * quantidade_convertida
valor_desconto = total * desconto_covertido / 100
total_final = total - valor_desconto

print(produto)
print(total)
print(valor_desconto)
print(total_final)
```
