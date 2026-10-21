# Exercícios de Entrada de dados com input()

## Exercício 1

Escreva um programa que:

1. Utilize `input()` para perguntar o nome do usuário, com a mensagem `Digite seu nome: `.
2. Armazene a resposta na variável `nome`.
3. Utilize `print()` para exibir o nome digitado.
4. Utilize `print()` com `type()` para mostrar o tipo da variável `nome`.

Exemplo de execução, caso o usuário digite `Rafael`:

```
Digite seu nome: Rafael
Rafael
<class 'str'>
```

Resolução:
```python
nome = input('Digite seu nome: ')
print(nome)
print(type(nome))
```

## Exercício 2

Escreva um programa que:

1. Pergunte a idade do usuário com a mensagem `Digite sua idade: `.
2. Armazene a resposta na variável `idade`, convertendo-a para um número inteiro.
3. Imprima a idade.
4. Imprima o tipo da variável `idade`.

Exemplo de execução, caso o usuário digite `27`:

```
Digite sua idade: 27
27
<class 'int'>
```

Resolução:
```python
idade = int(input('Digite sua idade: '))
print(idade)
print(type(idade))
```

## Exercício 3

Escreva um programa que:

1. Pergunte o preço de um produto com a mensagem `Digite o preço do produto: `.
2. Armazene a resposta na variável `preco`, convertendo-a para `float`.
3. Imprima o preço.
4. Imprima o tipo da variável `preco`.

Exemplo de execução, caso o usuário digite `49.90`:

```
Digite o preço do produto: 49.90
49.9
<class 'float'>
```

Atenção: em Python, utilize o ponto (`.`) como separador decimal.

Resolução:
```python
preco = float(input('Digite o preço do produto: '))
print(preco)
print(type(preco))
```

## Exercício 4

Escreva um programa que:

1. Peça o primeiro número inteiro com a mensagem `Digite o primeiro número: `.
2. Peça o segundo número inteiro com a mensagem `Digite o segundo número: `.
3. Armazene os valores nas variáveis `numero1` e `numero2`.
4. Calcule a soma e armazene o resultado na variável `soma`.
5. Imprima o resultado da soma.

Exemplo de execução:

```
Digite o primeiro número: 10
Digite o segundo número: 5
15
```

Resolução:
```python
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

soma = numero1 + numero2
print(soma)
```

## Exercício 5

Escreva um programa que:

1. Peça a primeira nota do aluno, usando a mensagem `Digite a primeira nota: `.
2. Peça a segunda nota, usando a mensagem `Digite a segunda nota: `.
3. Converta as duas notas para `float`.
4. Calcule a média das duas notas e armazene o resultado na variável `media`.
5. Imprima a média.
6. Imprima o tipo da variável `media`.

Exemplo de execução:

```
Digite a primeira nota: 7.5
Digite a segunda nota: 8.5
8.0
<class 'float'>
```

Resolução:
```python
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
print(media)
print(type(media))
```

## Exercício 6

Agora vamos combinar `input()` com diferentes operações matemáticas.

Escreva um programa que:

1. Peça dois números inteiros ao usuário, usando as mensagens `Digite o primeiro número: ` e `Digite o segundo número: `.
2. Armazene os valores nas variáveis `numero1` e `numero2`.
3. Calcule a soma e armazene em `soma`.
4. Calcule a subtração do primeiro pelo segundo e armazene em `subtracao`.
5. Calcule a multiplicação e armazene em `multiplicacao`.
6. Imprima os três resultados, cada um em uma linha.

Exemplo de execução:

```
Digite o primeiro número: 10
Digite o segundo número: 2
12
8
20
```

Resolução:
```python
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

print(soma)
print(subtracao)
print(multiplicacao)
```

## Exercício 7

Agora vamos usar `input()` para receber um valor e realizar um cálculo.

Escreva um programa que:

1. Pergunte quantas horas a pessoa estudou, usando a mensagem `Quantas horas você estudou? `.
2. Converta o valor recebido para `float` e armazene na variável `horas`.
3. Calcule o equivalente em minutos, multiplicando `horas` por `60`, e armazene em `minutos`.
4. Imprima o valor de `minutos`.
5. Imprima o tipo da variável `minutos`.

Exemplo de execução:

```
Quantas horas você estudou? 2.5
150.0
<class 'float'>
```

Resolução:
```python
horas = float(input('Quantas horas você estudou? '))

minutos = horas * 60

print(minutos)
print(type(minutos))
```

## Exercício 8

Escreva um programa que:

1. Pergunte o preço de um produto, usando `Digite o preço do produto: `, e converta o valor para `float`.
2. Pergunte a quantidade comprada, usando `Digite a quantidade: `, e converta o valor para `int`.
3. Calcule o valor total da compra e armazene na variável `total`.
4. Imprima o nome da variável `total`? Não — imprima somente o valor armazenado nela.
5. Imprima o tipo da variável `total`.

Exemplo de execução:

```
Digite o preço do produto: 25.50
Digite a quantidade: 3
76.5
<class 'float'>
```

Resolução:
```python
preco = float(input('Digite o preço do produto: '))
quantidade = int(input('Digite a qunatidade: '))

total = preco * quantidade

print(total)
print(type(total))
```

## Exercício 9

Agora vamos combinar entrada de texto, números inteiros e números decimais.

Escreva um programa que:

1. Pergunte o nome do produto e armazene em `produto`.
2. Pergunte o preço do produto e armazene em `preco`, convertendo-o para `float`.
3. Pergunte a quantidade disponível em estoque e armazene em `estoque`, convertendo-a para `int`.
4. Imprima as três informações, uma por linha, neste formato:

```
Produto: Teclado
Preço: 120.5
Estoque: 15
```

O exemplo considera que o usuário digitou `Teclado`, `120.50` e `15`.

Resolução:
```python
produto = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto: '))
disponivel = int(input('Digite a quantidade disponível em estoque: '))

print('Produto: ', produto)
print('Preço: ', preco)
print('Estoque: ', disponivel)
```

## Exercício 10

Este é o último exercício do tópico. Vamos reunir o que você aprendeu sobre `input()`, conversão de tipos e operações matemáticas.

Escreva um programa que:

1. Pergunte o nome do produto e armazene em `produto`.
2. Pergunte o preço unitário e converta para `float`.
3. Pergunte a quantidade comprada e converta para `int`.
4. Calcule o subtotal (`preço × quantidade`) e armazene em `subtotal`.
5. Imprima o nome do produto.
6. Imprima o subtotal.
7. Imprima o tipo da variável `subtotal`.

Exemplo de execução:

```
Digite o nome do produto: Mouse
Digite o preço unitário: 49.90
Digite a quantidade comprada: 3
Produto: Mouse
Subtotal: 149.7
<class 'float'>
```

Atenção: o subtotal deve ser calculado usando as variáveis convertidas, não os textos originais recebidos pelo `input()`.

Resolução:
```python
produto = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto: '))
quantidade = int(input('Digite a quantidade comprada: '))

subtotal = preco * quantidade

print('Produto: ', produto)
print('Subtotal: ', subtotal)
print(type(subtotal))
```
