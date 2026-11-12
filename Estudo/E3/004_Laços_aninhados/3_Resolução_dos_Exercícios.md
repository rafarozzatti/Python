# Exercícios de Laços aninhados

## Vamos praticar — Exercício 1

Crie um programa usando dois laços `for` aninhados para produzir a seguinte saída:

```
1 1 1
2 2 2
3 3 3
```

Regras:

- O laço externo deve percorrer os números de 1 a 3.
- O laço interno deve repetir 3 vezes para cada número externo.
- Cada linha deve exibir o número externo três vezes, separados por espaços.

Resolução:
```python
for i in range(1, 4):
    for j in range(3):
        print(i, end=' ')
    print()
```

## Exercício 2

Escreva um programa Python que exiba a tabuada dos números 1, 2 e 3, de 1 até 5.

A saída deve ser exatamente neste formato:

```
Tabuada do 1:
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5

Tabuada do 2:
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10

Tabuada do 3:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
```

Regras:

1. Utilize dois laços `for`, um dentro do outro.
2. O laço externo deve percorrer os números de 1 até 3.
3. O laço interno deve percorrer os números de 1 até 5.
4. Utilize `print()` para exibir os resultados.
5. Utilize `print()` vazio para separar as tabuadas.

Resolução:
```python
for i in range(1, 4):
    print(f'Tabuada do {i}:')
    for j in range(1, 6):
        print(f'{i} x {j} = {i * j}')
    print()
```

## Exercício 3

Vamos aumentar um pouco a dificuldade.

Escreva um programa utilizando dois laços `for` para produzir esta saída:

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

Regras:

1. Utilize dois laços `for` aninhados.
2. O laço externo deve controlar as linhas, de 1 até 5.
3. O laço interno deve exibir os números de 1 até o número da linha atual.
4. Utilize `end=' '` para manter os números da mesma linha.
5. Utilize `print()` vazio para pular para a próxima linha.

Resolução:
```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
```

## Exercício 4

Escreva um programa utilizando dois laços `for` para produzir esta saída:

```
* * * *
* * * *
* * * *
* * * *
```

Regras:

1. Utilize dois laços `for` aninhados.
2. O laço externo deve controlar as quatro linhas.
3. O laço interno deve repetir quatro vezes em cada linha.
4. Utilize `print('*', end=' ')` para exibir os asteriscos.
5. Utilize `print()` vazio para pular para a próxima linha.

Resolução:
```python
for i in range(4):
    for j in range(4):
        print('*', end=' ')
    print()
```

## Exercício 5

Agora vamos mudar um pouco a lógica.

Escreva um programa utilizando dois laços `for` para produzir esta saída:

```
*
* *
* * *
* * * *
* * * * *
```

Regras:

1. Utilize dois laços `for` aninhados.
2. O laço externo deve controlar cinco linhas.
3. O laço interno deve imprimir uma quantidade de asteriscos correspondente ao número da linha atual.
4. Utilize `end=' '` para manter os asteriscos na mesma linha.
5. Utilize `print()` vazio para pular para a próxima linha.

Resolução:
```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end=' ')
    print()
```

## Exercício 6

Agora vamos inverter o padrão anterior.

Escreva um programa utilizando dois laços `for` para produzir esta saída:

```
* * * * *
* * * *
* * *
* *
*
```

Regras:

1. Utilize dois laços `for` aninhados.
2. O laço externo deve controlar cinco linhas.
3. O laço interno deve começar com cinco repetições e diminuir uma repetição a cada linha.
4. Utilize `end=' '` para manter os asteriscos na mesma linha.
5. Utilize `print()` vazio para pular para a próxima linha.

Resolução:
```python
for i in range(1, 6):
    for j in range(5, i - 1, -1):
        print('*', end=' ')
    print()
```

## Exercício 7

Vamos voltar às multiplicações, mas agora com um intervalo maior.

Escreva um programa que exiba as tabuadas de 1 até 5, com multiplicadores de 1 até 10.

O início da saída deve ficar assim:

```
Tabuada do 1:
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
...
1 x 10 = 10

Tabuada do 2:
2 x 1 = 2
2 x 2 = 4
...
```

Regras:

1. Utilize dois laços `for` aninhados.
2. O laço externo deve percorrer os números de 1 até 5.
3. O laço interno deve percorrer os números de 1 até 10.
4. Utilize `f-string` para exibir as multiplicações.
5. Utilize `print()` vazio para separar as tabuadas.

Resolução:
```python
for i in range(1, 6):
    print(f'Tabuada do {i}:')
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}')
    print()
```

## Exercício 8

Agora vamos trabalhar com uma estrutura semelhante a uma matriz.

Escreva um programa que produza exatamente esta saída:

```
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
```

Regras:

1. Utilize dois laços `for` aninhados.
2. O laço externo deve controlar as quatro linhas.
3. O laço interno deve controlar as quatro colunas.
4. Utilize uma variável para armazenar o número atual, começando em 1.
5. Após exibir cada número, incremente essa variável em 1.
6. Utilize `end=' '` para manter os números na mesma linha.
7. Utilize `print()` vazio para pular para a próxima linha.

Resolução:
```python
n = 1

for i in range(4):
    for j in range(4):
        print(n, end=' ')
        n += 1
    print()
```

## Exercício 9

Agora vamos utilizar os valores dos próprios laços para construir uma matriz.

Escreva um programa que produza exatamente esta saída:

```
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
```

Regras:

1. Utilize dois laços `for` aninhados.
2. O laço externo deve controlar as quatro linhas.
3. O laço interno deve percorrer os números de 1 até 4.
4. Não utilize uma variável adicional para incrementar os números.
5. Utilize `end=' '` para manter os valores na mesma linha.
6. Utilize `print()` vazio para pular para a próxima linha.

Resolução:
```python
for i in range(4):
    for j in range(1, 5):
        print(j, end=' ')
    print()
```

## Exercício 10

Vamos fechar esta sequência com um desafio que combina o que você aprendeu.

Escreva um programa que produza exatamente esta saída:

```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

Regras:

1. Utilize dois laços `for` aninhados.
2. O laço externo deve controlar cinco linhas.
3. O laço interno deve aumentar a quantidade de números conforme a linha atual.
4. Utilize uma variável `n`, começando em 1.
5. Incremente `n` após cada número exibido.
6. Utilize `end=' '` para manter os números na mesma linha.
7. Utilize `print()` vazio para pular para a próxima linha.

Resolução:
```python
n = 1

for i in range(1, 6):
    for j in range(1, i + 1):
        print(n, end=' ')
        n += 1
    print()
```
