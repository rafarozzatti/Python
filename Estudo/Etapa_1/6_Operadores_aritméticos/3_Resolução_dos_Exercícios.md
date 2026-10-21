# Exercícios de Operadores Aritméticos

## Exercício 1

Crie duas variáveis:

```
numero1 = 18
numero2 = 6
```

Depois:

1. Calcule a soma e armazene em `soma`.
2. Calcule a subtração do segundo número pelo primeiro? Não — subtraia `numero2` de `numero1` e armazene em `subtracao`.
3. Calcule a multiplicação e armazene em `multiplicacao`.
4. Imprima os três resultados, um por linha.

O resultado esperado, na ordem solicitada, é:

```
24
12
108
```

Resolução:
```python
numero1 = 18
numero2 = 6

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

print(soma)
print(subtracao)
print(multiplicacao)
```

## Exercício 2

Considere as variáveis:

```
numero1 = 17
numero2 = 5
```

Faça o seguinte:

1. Calcule a divisão comum (`/`) e armazene em `divisao`.
2. Calcule a divisão inteira (`//`) e armazene em `divisao_inteira`.
3. Calcule o resto da divisão (`%`) e armazene em `resto`.
4. Imprima os três resultados, um por linha.
5. Imprima o tipo da variável `divisao`.

Resolução:
```python
numero1 = 17
numero2 = 5

divisao = numero1 / numero2
divisao_inteira = numero1 // numero2
resto = numero1 % numero2

print(divisao)
print(type(divisao))
print(divisao_inteira)
print(resto)
```

## Exercício 3

Considere as variáveis:

```
base = 4
expoente = 3
```

Faça o seguinte:

1. Calcule `base` elevado a `expoente` e armazene o resultado na variável `potencia`.
2. Imprima o resultado.
3. Imprima o tipo da variável `potencia`.

Resultado esperado:

```
64
<class 'int'>
```

Resolução:
```python
base = 4
expoente = 3

potencia = base ** expoente

print(potencia)
print(type(potencia))
```

## Exercício 4

Considere as variáveis:

```
preco = 35
quantidade = 4
```

Escreva um programa que:

1. Calcule o valor total da compra e armazene em `total`.
2. Calcule o valor de cada parcela caso a compra seja dividida em 4 parcelas iguais, armazenando em `parcela`.
3. Imprima `total`.
4. Imprima `parcela`.

Resultado esperado:

```
140
35.0
```

Resolução:
```python
preco = 35
quantidade = 4

total = preco * quantidade
parcela = total / 4

print(total)
print(parcela)
```

## Exercício 5

Uma empresa possui `53` produtos e precisa distribuir a mesma quantidade em caixas com capacidade para `8` produtos cada.

```
produtos = 53
capacidade = 8
```

Escreva um programa que:

1. Calcule quantas caixas completas podem ser preenchidas e armazene em `caixas_completas`.
2. Calcule quantos produtos sobrarão e armazene em `sobras`.
3. Imprima os dois resultados, um por linha.

Resultado esperado:

```
6
5
```

Resolução:
```python
produtos = 53
capacidade = 8

caixas_completas = produtos // capacidade
sobras = produtos % capacidade

print(caixas_completas)
print(sobras)
```

## Exercício 6

Considere as seguintes variáveis:

```
a = 10
b = 4
c = 2
```

Escreva um programa que:

1. Calcule `a + b * c` e armazene em `resultado1`.
2. Calcule `(a + b) * c` e armazene em `resultado2`.
3. Imprima os dois resultados, um por linha.

Resultado esperado:

```
18
28
```

Resolução:
```python
a = 10
b = 4
c = 2

resultado1 = a + b * c
resultado2 = (a + b) * c

print(resultado1)
print(resultado2)
```

## Exercício 7

Uma loja vende um produto por R$ 250, e o cliente recebe um desconto de 15%.

Considere:

```
preco = 250
desconto = 15
```

Escreva um programa que:

1. Calcule o valor do desconto e armazene em `valor_desconto`.
2. Calcule o preço final após o desconto e armazene em `preco_final`.
3. Imprima `valor_desconto`.
4. Imprima `preco_final`.

Resultado esperado:

```
37.5
212.5
```

Resolução:
```python
preco = 250
desconto = 15

valor_desconto = (preco * desconto) / 100
preco_final = preco - valor_desconto

print(valor_desconto)
print(preco_final)
```

## Exercício 8

Agora vamos combinar os operadores aritméticos com o `input()` que você estudou na aula anterior.

Escreva um programa que:

1. Peça ao usuário dois números inteiros, armazenando-os em `numero1` e `numero2`.
2. Calcule e armazene em variáveis separadas:
   - A soma (`soma`).
   - A divisão inteira (`divisao_inteira`).
   - O resto da divisão (`resto`).
3. Imprima os três resultados, um por linha.

Exemplo de execução:

```
Digite o primeiro número: 17
Digite o segundo número: 5
22
3
2
```

Resolução:
```python
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

soma = numero1 + numero2
divisao_inteira = numero1 // numero2
resto = numero1 % numero2

print(soma)
print(divisao_inteira)
print(resto)
```

## Exercício 9

Uma empresa recebeu uma quantidade de produtos e precisa descobrir quantas caixas completas consegue montar e quantas caixas serão necessárias para guardar todos os produtos.

Escreva um programa que:

1. Pergunte ao usuário a quantidade de produtos, convertendo a entrada para `int` e armazenando em `produtos`.
2. Pergunte quantos produtos cabem em cada caixa, convertendo a entrada para `int` e armazenando em `capacidade`.
3. Calcule quantas caixas completas podem ser preenchidas e armazene em `caixas_completas`.
4. Calcule quantos produtos sobram e armazene em `sobras`.
5. Imprima os três resultados, um por linha, nesta ordem: `caixas_completas` e `sobras`.

Exemplo de execução:

```
Digite a quantidade de produtos: 53
Digite a capacidade de cada caixa: 8
6
5
```

Resolução:
```python
produtos = int(input('Digite a quantidade de produtos: '))
capacidade = int(input('Digite a capacidade de cada caixa: '))

caixas_completas = produtos // capacidade
sobras = produtos % capacidade

print(caixas_completas)
print(sobras)
```

## Exercício 10

Este é o último exercício do tópico. Vamos combinar entrada de dados, conversão de tipos e operadores aritméticos.

Escreva um programa que:

1. Peça o preço unitário de um produto e converta para `float`.
2. Peça a quantidade comprada e converta para `int`.
3. Calcule o subtotal e armazene em `subtotal`.
4. Calcule um desconto de 10% sobre o subtotal e armazene em `valor_desconto`.
5. Calcule o preço final após o desconto e armazene em `total_final`.
6. Calcule quantos produtos cabem em grupos de 3, usando a quantidade comprada, e armazene em `grupos_completos`.
7. Calcule quantos produtos sobram ao formar esses grupos e armazene em `sobras`.
8. Imprima os valores de `subtotal`, `valor_desconto`, `total_final`, `grupos_completos` e `sobras`, nessa ordem.

Exemplo de execução:

```
Digite o preço unitário: 25
Digite a quantidade comprada: 8
180.0
20.0
180.0
2
2
```

Resolução:
```python
preco_unitario = float(input('Digite o preço unitário: '))
quantidade = int(input('Digite a quantidade comprada: '))

subtotal = preco_unitario * quantidade
valor_desconto = subtotal * 0.1
total_final = subtotal - valor_desconto
grupos_completos = quantidade // 3
sobras = quantidade % 3

print(subtotal)
print(valor_desconto)
print(total_final)
print(grupos_completos)
print(sobras)
```
